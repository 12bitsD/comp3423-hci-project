"""Record the finite Western query layout configured in actual Figma UI.

The original imported SVG remains frozen. This source reflects recorded
grouping/viewport edits; generating it performs no application/browser input.
"""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as E
from build_calendar_class_exam_oct2 import node,tag,group,rect
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
def main():
 src=D/'food-oct3-tag-western.svg';r=E.parse(src).getroot()
 rows=[g for g in r if g.get('id','').startswith('Result-')];assert len(rows)==11
 r.find(tag('desc')).text='Finite October3 Western Cuisine query reconstruction. Recorded actual UI grouping: viewport0,200 size576x824; content18,7 size540x840 Left/Top. Header and search input remain outside viewport. Eleven fixed public results; fonts/icons/spacing approximate. Inferred23px range is prototype geometry, not verified native bounds. Back, caller, rows and arbitrary query unconfigured. Source reflects UI edits; generator does not configure Figma.'
 defs=node('defs');cp=node('clipPath',id='WesternResultsClip',clipPathUnits='userSpaceOnUse');rect(cp,0,0,576,824,'#FFFFFF');defs.append(cp);r.insert(0,defs)
 vp=group(r,'WesternResultsViewport');vp.set('transform','translate(0 200)');vp.set('clip-path','url(#WesternResultsClip)')
 content=group(vp,'WesternResultsContent');content.set('transform','translate(18 7)');coords=group(content,'OriginalResultCoordinates');coords.set('transform','translate(-18 -207)')
 for g in rows:r.remove(g);coords.append(g)
 f=D/'food-oct3-western-scroll.svg';E.ElementTree(r).write(f,encoding='unicode',xml_declaration=True)
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 meta={'file':f.name,'sha256':sha(f),'original_source':src.name,'original_source_sha256':sha(src),'state_id':'S-FOOD-OCT3-WESTERN','source_evidence_ids':['E-FOOD-TAGS-16','E-FOOD-TAGS-04'],'dimensions':[576,1024],'figma':{'root_node_id':'954:59','viewport_node_id':'957:20','content_node_id':'957:19','root_canvas_position':[700,92000],'viewport_position':[0,200],'viewport_dimensions':[576,824],'content_position':[18,7],'content_dimensions':[540,840],'content_extent_height':847,'inferred_scroll_range':[0,23],'clip_content':True,'overflow':'Vertical','child_constraints':{'horizontal':'Left','vertical':'Top'}},'status':'prepared_source_reflecting_recorded_UI_edits','native_full_geometry_verified':False,'limits':['Original source unchanged; this XML reflects actual UI edits, not a Figma export.','Eleven observed public results, fixed query; no arbitrary search, row/caller/Back navigation.','Rows/icons/fonts approximate; finite prototype bounds do not establish native extent.']}
 p=D/'food-oct3-western-scroll-layout.json'
 if p.exists():
  old=json.loads(p.read_text())
  if old['sha256']==meta['sha256']:
   for k in ['status','editor_evidence_ids','prototype_run_ids','flow']:
    if k in old:meta[k]=old[k]
 p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'rows':len(rows),'scroll_range':23,'figma_input':False}))
if __name__=='__main__':main()
