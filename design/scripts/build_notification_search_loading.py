"""Reconstruct the observed Notification/Search VA210 map-loading viewport.

File generation only. The eventual map transition timing is a prototype proxy.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import hashlib,json
from PIL import Image
from build_calendar_class_exam_oct2 import find,tag,image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=R/'evidence/2026-10-03-search-detail-observation/12-result-chevron-check.png'
    im=Image.open(source);assert im.size==(576,1024)
    asset=D/'assets/notification-search-map-loading-mark.png';crop=(257,667,319,731)
    im.crop(crop).save(asset)
    r=E.parse(D/'notification-search-detail.svg').getroot();content=find(r,'PageContent')
    content.remove(find(r,'PublicMap'));find(r,'ExpandMap').set('transform','translate(0 -243)')
    image(content,asset,257,667,62,64)
    r.find(tag('title')).text='VA210 — Notification Search observed map loading'
    r.find(tag('desc')).text='Observed native public Search detail viewport E-SEARCH-OBS-12. Editable chrome approximate, illustration and loading mark raster. Map expansion/image/tags/call not configured. Prototype delay is demonstrative; native loading duration and eventual same-visit outcome unverified.'
    file=D/'notification-search-detail-loading.svg';E.ElementTree(r).write(file,encoding='unicode',xml_declaration=True)
    out={'file':file.name,'sha256':sha(file),'state_id':'S-FOOD-DETAIL-LOADING','context_variant':'20261003-notification-search-detail-loading','source_evidence_ids':['E-SEARCH-OBS-12','E-SEARCH-OBS-12-AX'],'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed','assets':[{'file':'assets/'+asset.name,'sha256':sha(asset),'source_evidence_id':'E-SEARCH-OBS-12','crop_xyxy':list(crop),'dimensions':[62,64]},{'file':'assets/notice-search-va210-hero.png','sha256':sha(D/'assets/notice-search-va210-hero.png'),'source_evidence_id':'E-NOTICE-SEARCH-12','dimensions':[223,240]}],'limits':['Current input attempts failed to open detail; prior saved native sample supports loading viewport only.','Loading-to-settled transition in this caller is a prototype generalization;800ms does not measure native latency.','Map/image/tag/call controls remain unconfigured; full app/fidelity not_verified.']}
    p=D/'notification-search-loading-sources.json'
    if p.exists():
        old=json.loads(p.read_text())
        if old['sha256']==out['sha256']:
            for k in ['node_id','node_name','prototype_run_ids','status']: 
                if k in old:out[k]=old[k]
    p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'source':file.name,'figma_mutations':0}))
if __name__=='__main__':main()
