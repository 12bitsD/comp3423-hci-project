"""Publish redacted Computer Use captures from the Oct 2 resume; never publish raw AX.

Run with Python + Pillow. Input is the ignored capture directory. This is a dated
archive operation, not a tool for operating the application or proving completeness.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, hashlib, re
R = Path(__file__).resolve().parents[2]
RAW = R/'evidence/raw/2026-10-02-native-resume'
PUB = R/'evidence/2026-10-02-native-calendar-resume'
DOC = R/'docs/polyulife'
SID = 'SESSION-20261002-CALENDAR-RESUME'
steps = json.loads((RAW/'steps.json').read_text())
assert len(steps) == 26, 'Inspect changed capture set before republishing this archive'
coverage=json.loads((DOC/'coverage.json').read_text())
assert not any(x['id']==SID for x in coverage['sessions']), 'Already archived; inspect current ledger instead of rerunning'
PUB.mkdir(exist_ok=True)
state_labels = {
 'room-resumed':'ROOM-MIXED-DATE', 'home-after-room-back':'HOME-RETAINED',
 'calendar-current-default':'ALL', 'filter-all-current':'DRAFT-ALL-ALL',
 'filter-none-draft':'DRAFT-NONE-ALL', 'filter-x-none-dismissed':'ALL',
 'filter-reopen-after-x':'DRAFT-ALL-ALL', 'filter-none-before-apply':'DRAFT-NONE-ALL',
 'calendar-none-applied':'NONE', 'filter-none-reopened':'DRAFT-NONE-NONE',
 'filter-class-only-draft':'DRAFT-CLASS-NONE', 'calendar-class-only-applied':'CLASS',
 'class-ellipsis-detail':'CLASS-DETAIL', 'class-notice-open':'NOTICE-LOADING',
 'class-notice-loaded':'NOTICE-BLANK', 'class-notice-more-menu':'NOTICE-MENU',
 'class-notice-menu-cancelled':'NOTICE-BLANK', 'class-notice-closed':'CLASS-DETAIL',
 'calendar-after-class-detail-back':'CLASS', 'filter-class-reopened':'DRAFT-CLASS-CLASS',
 'filter-class-cleared':'DRAFT-NONE-CLASS', 'filter-exam-only-draft':'DRAFT-EXAM-CLASS',
 'calendar-exam-only-applied':'EXAM', 'filter-exam-reopened':'DRAFT-EXAM-EXAM',
 'filter-exam-cleared':'DRAFT-NONE-EXAM', 'filter-payment-only-draft':'DRAFT-PAYMENT-EXAM',
}
state_id = lambda label: 'S-NATIVE-OCT2-'+state_labels[label]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = {'kind':'native_computer_use_calendar_resume','session_id':SID,'images':[]}
ax_records=[]
# The crop is measured from the saved fullscreen screenshot; no unrelated desktop is retained.
for i,s in enumerate(steps,1):
 im=Image.open(RAW/s['image_path']).convert('RGB')
 crop=(954,46,1998,1898) if i==1 else (978,0,2046,1898)
 im=im.crop(crop).resize((576,1024),Image.Resampling.LANCZOS)
 masks=[]
 def mask(box,fill):
  ImageDraw.Draw(im).rectangle((box[0],box[1],box[2]-1,box[3]-1),fill=fill)
  masks.append({'xyxy':list(box),'fill':fill})
 if i==2:
  mask((70,30,510,85),'#242424'); mask((14,98,570,620),'#242424')
 if i in [3,6,12,19]:
  mask((140,622,506,707),'#242424')
 # Remove private per-date event marker patterns. This is a visible redaction band,
 # including any part of a selection background it crosses, not recreated pixels.
 if i in [3,4,5,6,7,8,12,19,20,21,22]:
  fill='#999999' if i in [4,5,7,8,20,21,22] else '#FFFFFF'
  for y in [178,235,292,349,406]: mask((31,y,546,y+15),fill)
 if i in [13,18]:
  for b in [(60,24,535,90),(30,115,545,200),(30,249,550,282),(78,480,495,550)]: mask(b,'#242424')
 if i in [14,15,16,17]: mask((60,22,535,77),'#242424')
 filename=f'{i:02d}-{s["label"]}.png'; out=PUB/filename;im.save(out)
 manifest['images'].append({'file':filename,'sha256':sha(out),'dimensions':list(im.size),
  'captured_at_utc':s['timestamp'],'source':'Actual native PolyULife Computer Use screenshot bytes',
  'description':s['label'],'state_id':state_id(s['label']),
  'redaction':{'crop_xyxy':list(crop),'resize':[576,1024],'opaque_masks':masks},
  'raw_sha256':sha(RAW/s['image_path'])})
 ax=(RAW/s['ax_path']).read_text()
 # Deliberately publish a derived safe subset, not regex-sanitised private trees.
 safe=[]
 for l in ax.splitlines():
  if re.search(r'Value: checkbox|undefined\.day_2026-|slider Description:.*October|element Cancel|element Description: (Open in system browser|Share via|Copy link|Class Notice)|button Description: Apply|text Description: No event|version: 3\.0\.0',l):
   if 'version: 3.0.0' in l and 'text Description:' not in l: continue
   safe.append(l.strip())
  elif re.search(r'button.*Description:.*( Home| Calendar| Notification| More), Secondary',l):safe.append(l.strip())
 af=PUB/f'{i:02d}-safe-ax.txt'
 af.write_text(('Derived safe AX subset; identity, timetable values and hidden drawer excluded.\n'+ '\n'.join(safe)).rstrip()+'\n')
 ax_records.append({'index':i,'file':af.name,'sha256':sha(af),'state_id':state_id(s['label']),
  'captured_at':s['timestamp'],'source':'Derived safe subset of recorded native AX; not a complete accessibility tree',
  'raw_sha256':sha(RAW/s['ax_path'])})
W,H=288,552; sheet=Image.new('RGB',(W*6,H*5),'#E4E4E4'); draw=ImageDraw.Draw(sheet)
for i,m in enumerate(manifest['images']):
 thumb=Image.open(PUB/m['file']);thumb.thumbnail((270,500)); x=(i%6)*W;y=(i//6)*H
 sheet.paste(thumb,(x+9,y+25));draw.text((x+7,y+5),m['file'][:38],fill='#111111')
sheet.save(PUB/'contact-sheet.png')
manifest['contact_sheet']={'file':'contact-sheet.png','sha256':sha(PUB/'contact-sheet.png'),'dimensions':list(sheet.size),'source':'Contact sheet of the redacted native captures'}
manifest['safe_ax']=ax_records
manifest['uncertain_attempts']=[{'control':'Payment-only Apply','method':'AX click requested on index14',
 'input_execution_verified':False,'target_state_id':None,'result':'Mac locked; the combined click/capture call failed before a saved outcome. Do not infer Apply success or current app state.'}]
(PUB/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
coverage['sessions'].append({'id':SID,'started_at':steps[0]['timestamp'],'timezone':'Asia/Shanghai',
 'environment':{'platform':'macOS','runtime':'Installed iPhone app observed through Computer Use, fullscreen screenshot',
  'app_name':'PolyULife / polyuLife','app_version_last_known':'3.0.0','app_version_reverified_in_this_record':True,
  'login_state':'Existing signed-in session retained; private content only in ignored raw files',
  'capture_recovery':'Fresh bundle ambiguity resolved with current Wrapper path; actual Room window obtained. Mac later relocked during Payment Apply request.'},
 'starting_state_id':state_id(steps[0]['label']),'evidence_ids':[],'documented_through':steps[-1]['timestamp']})
session=coverage['sessions'][-1]
for i,s in enumerate(steps,1):
 st=state_id(s['label']); eid=f'E-NATIVE-OCT2-{i:02d}'; aeid=eid+'-AX'; aid=f'A-NATIVE-OCT2-{i:02d}' if s['action'] else None
 m=manifest['images'][i-1]; am=ax_records[i-1]
 coverage['evidence'].append({'id':eid,'type':'screenshot','path':'../../evidence/2026-10-02-native-calendar-resume/'+m['file'],
  'session_id':SID,'captured_at':s['timestamp'],'sha256':m['sha256'],'dimensions':m['dimensions'],
  'state_ids':[st],'action_ids':[aid] if aid else [],'redaction':m['redaction'],'source':m['source']})
 coverage['evidence'].append({'id':aeid,'type':'ax_snapshot','path':'../../evidence/2026-10-02-native-calendar-resume/'+am['file'],
  'session_id':SID,'captured_at':s['timestamp'],'sha256':am['sha256'],'state_ids':[st],
  'action_ids':[aid] if aid else [],'redaction':'Safe subset excludes personal values and hidden drawer; full tree kept only in ignored raw files','source':am['source']})
 session['evidence_ids'] += [eid,aeid]
 found=next((v for v in coverage['states'] if v['id']==st),None)
 if found is None:
  found={'id':st,'session_id':SID,'title':s['label'],'description':'Dated native Oct2 sample; private content masked. See resume walkthrough for observed facts and limits.',
   'visible_scope':'Redacted fullscreen native sample normalized to576x1024; safe AX subset',
   'preconditions':'Existing signed-in session, retained Calendar/application state',
   'screenshot_evidence_ids':[],'ax_evidence_ids':[],'action_ids':[],'discovery_checked':False,
   'remaining_uncertainties':['Complete application, data bounds, phone behavior and long-term state retention remain unverified.']}
  coverage['states'].append(found)
 found['screenshot_evidence_ids'].append(eid);found['ax_evidence_ids'].append(aeid)
 if aid:
  prev=state_id(steps[i-2]['label'])
  result='Recorded target state and screenshot; see dated trace for distinctions from load/cancel/failure.'
  action={'id':aid,'from_state_id':prev,'control':s['action']['control'],'input_summary':s['action'],
   'status':'observed','executions':[{'at':s['timestamp'],'session_id':SID,'from_state_id':prev,
    'observed_feedback':result,'target_state_id':st,'evidence_ids':[eid,aeid]}],
   'target_state_id':st,'evidence_ids':[eid,aeid],'return_path':None,
   'authorization':'Reversible navigation/filter inspection; no business submission, credentials, sharing or account setting changes.','blockers':[]}
  coverage['actions'].append(action)
  next(v for v in coverage['states'] if v['id']==prev)['action_ids'].append(aid)
# Update the generic empty-filter action with a dated execution, without rewriting historical evidence.
a=next(a for a in coverage['actions'] if a['id']=='A-CALENDAR-APPLY-NONE')
a['status']='observed';a['target_state_id']='S-NATIVE-OCT2-NONE';a['pending_reason']='Oct2 all-off result observed. Other dates/callers and complete filter combinations remain unverified.'
a['executions'].append({'at':steps[8]['timestamp'],'session_id':SID,'from_state_id':'S-NATIVE-OCT2-DRAFT-NONE-ALL',
 'target_state_id':'S-NATIVE-OCT2-NONE','observed_feedback':'No Selected Event, No event, no date event markers; reopened dialog remains all unchecked.',
 'evidence_ids':['E-NATIVE-OCT2-09','E-NATIVE-OCT2-09-AX','E-NATIVE-OCT2-10','E-NATIVE-OCT2-10-AX']})
a['evidence_ids'] += ['E-NATIVE-OCT2-09','E-NATIVE-OCT2-09-AX','E-NATIVE-OCT2-10','E-NATIVE-OCT2-10-AX']
coverage['actions'].append({'id':'A-NATIVE-OCT2-PAYMENT-APPLY','from_state_id':'S-NATIVE-OCT2-DRAFT-PAYMENT-EXAM',
 'control':'Payment-only Apply','input_summary':'AX click requested on index14; combined command/capture failed when Mac locked.',
 'status':'attempted_unverified','executions':[],'target_state_id':None,'evidence_ids':[],
 'return_path':None,'authorization':'Ordinary reversible Calendar filtering','blockers':['Mac locked before an outcome could be recorded'],
 'pending_reason':'Input execution and result are both unknown; re-read the current window before repeating.'})
for a in coverage['actions']:
 if a['id']=='A-CALENDAR-DEFAULT-CLASS-MORE':a['pending_reason']='Oct2 Class-only ellipsis now enters observed detail; all-category ellipsis remains unobserved. Do not transfer the source-context claim.'
 if a['id']=='A-CALENDAR-FILTER-X':a['pending_reason']='Oct2 none-draft X cancels to all and reopens all checked; this historical Acad-draft X context still unobserved.'
 if a['id']=='A-CALENDAR-OTHER-CATEGORIES':a['pending_reason']='Oct2 Class and Exam Apply/reopen observed; Payment draft observed, Apply unknown due relock. Other combinations/dates remain pending.'
for q in coverage['discovery_queue']:
 if q['id']=='Q-CALENDAR-REMAINING':
  q['reason']='Oct2 native none Apply/reopen, none X cancellation, Class/Exam Apply/reopen, class detail and Notice container now recorded. Payment Apply outcome unknown; historical Acad X, all-category ellipsis, complete combinations, history reverse/bounds, other weeks/dates remain open.'
  q['resolution_refs'] += ['E-NATIVE-OCT2-09','E-NATIVE-OCT2-13','E-NATIVE-OCT2-23','E-NATIVE-OCT2-26']
# The empty-filter execution belongs to the existing generic action too; keep a
# single action record instead of counting the same operation under two IDs.
old='A-NATIVE-OCT2-09';new='A-CALENDAR-APPLY-NONE'
coverage['actions']=[a for a in coverage['actions'] if a['id']!=old]
for collection in ['states','evidence']:
 for row in coverage[collection]:
  if 'action_ids' in row:row['action_ids']=[new if a==old else a for a in row['action_ids']]
(DOC/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'captures':len(steps),'new_native_states':len(set(state_labels.values())),'new_native_actions':sum(bool(s['action']) for s in steps),'status':'native_archive_only; Figma changes not yet recorded'},ensure_ascii=False))
