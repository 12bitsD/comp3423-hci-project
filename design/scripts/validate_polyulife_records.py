"""Validate evidence references, hashes and current Figma mapping structure.

This check does not establish native/full-application coverage or visual fidelity.
Run from any directory: python3 design/scripts/validate_polyulife_records.py
"""
import json,hashlib,re,struct,xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter
root=Path(__file__).resolve().parents[2];b=root/'docs/polyulife';d=json.loads((b/'coverage.json').read_text());f=d['figma'];errors=[]
refs={k:{v['id'] for v in d[k]} for k in ['sessions','states','actions','evidence','findings','closure_reviews','discovery_queue','entry_points']}
for k,v in refs.items():
 if len(v)!=len(d[k]):errors.append(('duplicate',k))
def walk(o):
 if isinstance(o,dict):
  for k,v in o.items():
   target=None
   if k.endswith('evidence_ids'):target=refs['evidence']
   elif k=='state_ids' or k.endswith('_state_ids'):target=refs['states']
   elif k=='action_ids' or k.endswith('_action_ids'):target=refs['actions']
   if target is not None:
    for x in v:
     if x not in target:errors.append((k,x))
   if k in ['state_id','from_state_id','target_state_id','source_state_id','starting_state_id','eventual_state_id'] and v and v not in refs['states']:errors.append((k,v))
   if k=='action_id' and v and v not in refs['actions']:errors.append((k,v))
   if k=='session_id' and v and v not in refs['sessions']:errors.append((k,v))
   walk(v)
 elif isinstance(o,list):
  for x in o:walk(x)
walk(d)
def hashfile(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for e in d['evidence']:
 p=b/e['path']
 if not p.exists():errors.append(('missing evidence',e['id'],e['path']));continue
 if e.get('sha256') and hashfile(p)!=e['sha256']:errors.append(('evidence hash',e['id']))
 if p.suffix=='.png' and e.get('dimensions'):
  dims=list(struct.unpack('>II',p.read_bytes()[16:24]))
  if dims!=e['dimensions']:errors.append(('evidence dimensions',e['id'],dims))
manifest=json.loads((root/'evidence/2026-09-28-full-audit/manifest.json').read_text())
if len(manifest)!=len({v['file'] for v in manifest}):errors.append(('duplicate manifest filename',))
for m in manifest:
 p=root/'evidence/2026-09-28-full-audit'/m['file']
 if not p.exists():errors.append(('missing manifest image',m['file']));continue
 if hashfile(p)!=m['sha256']:errors.append(('manifest hash',m['file']))
 if list(struct.unpack('>II',p.read_bytes()[16:24]))!=m['dimensions']:errors.append(('manifest dimensions',m['file']))

additional_public_files=0
for extra_manifest in sorted((root/'evidence').glob('*/manifest.json')):
 if extra_manifest.parent.name=='2026-09-28-full-audit':continue
 em=json.loads(extra_manifest.read_text())
 items=em['images']+[em['contact_sheet']]
 if len({v['file'] for v in items})!=len(items):errors.append(('duplicate additional public file',str(extra_manifest)))
 additional_public_files+=len(items)
 for e in items:
  p=extra_manifest.parent/e['file']
  if not p.exists():errors.append(('missing replay image',e['file']));continue
  if hashfile(p)!=e['sha256']:errors.append(('replay hash',e['file']))
  if list(struct.unpack('>II',p.read_bytes()[16:24]))!=e['dimensions']:errors.append(('replay dimensions',e['file']))

nodes={m['node_id'] for m in f['state_node_mappings']};runs={r['id'] for r in f['prototype_runs']};deviations={v['id'] for v in f['reconstruction_deviations']}
if len(nodes)!=len(f['state_node_mappings']):errors.append(('duplicate current node',))
# Dated/focused frames may represent the same native state without inventing observations.
variant_keys={(m['state_id'],m.get('context_variant','base')) for m in f['state_node_mappings']}
if len(variant_keys)!=len(nodes):errors.append(('duplicate mapped state/context variant',))
counts=Counter(m['state_id'] for m in f['state_node_mappings'])
for m in f['state_node_mappings']:
 if m.get('context_variant'):
  if not isinstance(m['context_variant'],str) or not m['context_variant'].strip():errors.append(('empty context variant',m['node_id']))
  native_sources=[e for e in d['evidence'] if e['id'] in m.get('source_evidence_ids',[]) and e.get('session_id') in refs['sessions']]
  if not native_sources:errors.append(('context variant missing native evidence',m['node_id']))
  # Historical evidence may declare the association on the state instead of the screenshot.
  native_state=next((v for v in d['states'] if v['id']==m['state_id']),{})
  state_source_ids=set(native_state.get('screenshot_evidence_ids',[])+native_state.get('ax_evidence_ids',[]))
  if not any(m['state_id'] in e.get('state_ids',[]) or e['id'] in state_source_ids for e in native_sources):errors.append(('context variant native state mismatch',m['node_id']))
 if counts[m['state_id']]>1 and 'context_variant' not in m:
  # One historical base mapping is allowed; each additional view needs a named context.
  if sum(1 for v in f['state_node_mappings'] if v['state_id']==m['state_id'] and 'context_variant' not in v)>1:errors.append(('ambiguous base mapping',m['state_id']))
for m in f['state_node_mappings']:
 p=b/m['design_source_path']
 if hashfile(p)!=m['design_source_sha256']:errors.append(('source hash',m['state_id']))
 try:ET.parse(p)
 except Exception as e:errors.append(('SVG XML',m['state_id'],str(e)))
for m in f['action_connection_mappings']:
 for k in ['source_node_id','target_node_id']:
  if m.get(k) and m[k] not in nodes:errors.append((k,m[k]))
 for v in m.get('tested_target_node_ids',[]):
  if v not in nodes:errors.append(('tested back node',v))
 for v in m.get('prototype_run_ids',[]):
  if v not in runs:errors.append(('prototype run',v))
 for v in m.get('deviation_ids',[]):
  if v not in deviations:errors.append(('deviation',v))
for p in b.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if target.startswith(('https:','http:','#')):continue
  if not (b/target.split('#')[0]).exists():errors.append(('markdown link',p.name,target))
assert d['scope']['completion_status']=='not_verified'
assert next(r['status'] for r in f['prototype_runs'] if r['id']=='PROTO-VA-V2-001')=='failed'
assert next(r['status'] for r in f['prototype_runs'] if r['id']=='PROTO-FOOD-V2-001')=='failed'
assert f['archive_page_name']=='00 · Archive — initial AI draft'
assert f['archive_flow_name']=='Archive · Initial AI draft — not validated'
assert 'E-FIGMA-EDITOR-FINAL' in refs['evidence']
print(json.dumps({'errors':errors,'native':{k:len(d[k]) for k in ['sessions','entry_points','states','actions','findings','evidence','discovery_queue','closure_reviews']},'action_statuses':dict(Counter(a['status'] for a in d['actions'])),'figma':{'mapped_frames':len(nodes),'current_connections':len(f['action_connection_mappings']),'prototype_runs':len(runs)},'public_manifest_files':len(manifest)+additional_public_files,'scope_completion_status':d['scope']['completion_status']},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
