"""Record five query-header position edits performed in actual Figma UI.

Original import sources stay frozen. Only query text and the two magnifier
vectors change. Western retains its existing finite scroll source structure.
"""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as E
from build_calendar_class_exam_oct2 import tag

R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    meta=D/'food-oct3-query-alignment-sources.json'
    previous=json.loads(meta.read_text()) if meta.exists() else {}
    old={s['file']:s for s in previous.get('sources',[])}
    originals=json.loads((D/'food-oct3-remaining-tags-sources.json').read_text())['sources']
    sources=[]
    for s in originals:
        slug=s['file'].removeprefix('food-oct3-tag-').removesuffix('.svg')
        src=D/('food-oct3-western-scroll.svg' if slug=='western' else s['file'])
        root=E.parse(src).getroot()
        g=next(n for n in root.iter() if n.get('id')=='SearchInput')
        circle=g.find(tag('circle'));text=g.find(tag('text'))
        handle=next(n for n in g if n.tag==tag('path') and n.get('d')=='M40 154L49 163')
        assert circle.get('cx')=='32' and text.get('x')=='58'
        circle.set('cx','36');text.set('x','76');handle.set('d','M44 154L53 163')
        file=D/('food-oct3-'+slug+'-query-aligned.svg')
        E.ElementTree(root).write(file,encoding='unicode',xml_declaration=True)
        rec=dict(file=file.name,sha256=sha(file),original_source_file=src.name,
                 original_source_sha256=sha(src),state_id=s['state_id'],query=s['query'],
                 result_names=s['result_names'],source_evidence_ids=s['source_evidence_ids'],
                 dimensions=[576,1024],node_id=s['node_id'],node_name=s['node_name'],
                 status='prepared_source_reflecting_actual_UI_alignment',
                 query_text_x=76,magnifier_circle_center_x=36,magnifier_handle_start_x=44,
                 native_exact_font_and_geometry_verified=False)
        if old.get(file.name,{}).get('sha256')==rec['sha256']:
            rec.update(old[file.name])
        sources.append(rec)
    result=dict(sources=sources,limits=[
        'Only SearchInput query x58->76 and magnifier two vectors+4px; other visual source structure unchanged.',
        'Coordinates align to archived normalized screenshots; exact native font/geometry remains unknown.',
        'Original five tag SVGs and Western finite-scroll source remain unchanged as history.',
        'Fixed public query/result samples only; Back, caller, result navigation and arbitrary entry unconfigured.',
        'Generator performs no application/browser input and is not a Figma export.'
    ])
    for key in ['verification_limits','prototype_run_ids','editor_evidence_ids']:
        if key in previous:result[key]=previous[key]
    meta.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(sources=5,figma_mutations=0)))

if __name__=='__main__':main()
