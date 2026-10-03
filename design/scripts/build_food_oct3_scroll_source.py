"""Serialize the corrected BlockY scroll layout; Figma setup is recorded separately.

Does not operate Figma or claim that SVG itself implements prototype scrolling.
The imported original source and its historical renders remain unchanged.
"""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as E
from build_calendar_class_exam_oct2 import tag

R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
def main():
    original=D/'food-oct3-blocky-detail.svg';r=E.parse(original).getroot()
    cp=r.find('.//'+tag('clipPath'));cp.set('id','DetailViewportClip')
    viewport=next(n for n in r.iter() if n.get('id')=='DetailViewport')
    viewport.set('clip-path','url(#DetailViewportClip)')
    content=next(n for n in r.iter() if n.get('id')=='DetailContent')
    backgrounds=[n for n in content if n.tag==tag('rect') and n.get('height')=='1013']
    assert len(backgrounds)==2
    for n in backgrounds:n.set('height','992')
    r.find(tag('title')).text='BlockY detail — corrected finite scroll layout'
    r.find(tag('desc')).text='Serialized layout after actual Figma UI correction: viewport949:65 at0,100 size576x924, content949:66 height992, Left/Top constraints, Vertical overflow. Header remains outside scrolling frame. Only two background vectors shortened; text/logo/map positions preserved. SVG is a layout source, not a scrolling runtime. Native full boundaries and other controls unverified. Original import source and prior local renders retained.'
    target=D/'food-oct3-blocky-scroll.svg';E.ElementTree(r).write(target,encoding='unicode',xml_declaration=True)
    ids=[n.get('id') for n in r.iter() if n.get('id')];assert len(ids)==len(set(ids))
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    record={'file':target.name,'sha256':sha(target),'original_import_source':original.name,'original_import_source_sha256':sha(original),'figma_root_node_id':'949:63','viewport_node_id':'949:65','content_node_id':'949:66','viewport_position':[0,100],'viewport_dimensions':[576,924],'content_height':992,'inferred_range':[0,68],'native_complete_extent_verified':False,'child_constraints':{'horizontal':'Left','vertical':'Top'},'overflow':'Vertical','source_evidence_ids':['E-FOOD-MENU-01','E-FOOD-MENU-10','E-FOOD-MENU-15'],'limits':'Serialized finite layout; actual scroll proof lives in Present evidence. Header/text/vectors approximate; public map/logo raster. No navigation controls configured.'}
    (D/'food-oct3-blocky-scroll-layout.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'source_file':target.name,'inferred_scroll_range':68,'figma_input_performed':False}))
if __name__=='__main__':main()
