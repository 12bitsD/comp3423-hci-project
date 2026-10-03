"""Reconstruct two observed public Food loading states; requires Pillow."""
from pathlib import Path
import xml.etree.ElementTree as E
import json,hashlib,base64,copy
from PIL import Image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';N=R/'evidence/2026-09-28-full-audit';S='http://www.w3.org/2000/svg';X='http://www.w3.org/1999/xlink';ns={'s':S};E.register_namespace('',S);E.register_namespace('xlink',X)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
def g(root,name):return root.find(f'.//s:g[@id="{name}"]',ns)
def mark(root,source,crop,file,x,y):
 p=D/'assets'/file;Image.open(N/source).convert('RGB').crop(crop).save(p)
 E.SubElement(root,f'{{{S}}}image',{'x':str(x),'y':str(y),'width':str(crop[2]-crop[0]),'height':str(crop[3]-crop[1]),f'{{{X}}}href':'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()})
 return {'file':'assets/'+file,'sha256':h(p),'dimensions':[crop[2]-crop[0],crop[3]-crop[1]],'source':source,'source_sha256':h(N/source),'crop_xyxy':crop}
base=D/'food-detail.svg';r=E.parse(base).getroot();page=g(r,'PageContent');page.remove(g(r,'PublicMap'));page.remove(g(r,'MapCallout'));g(r,'ExpandMap').set('transform','translate(0 -241)')
logo=mark(page,'food-160725-vending-detail-map-loading.png',(257,671,319,730),'food-detail-loading-mark.png',257,671)
# Move loading mark before editable expand group (no overlap).
r.find('s:title',ns).text='VA210 detail — embedded map loading';r.find('s:desc',ns).text='Editable reconstruction of E-FOOD-DETAIL-LOADING using existing public detail source. Loaded map/callout removed; loading mark and expand control match observed upper map area. Static logo, duration unknown; cursor omitted; fonts/icons approximate.'
out=D/'food-detail-loading.svg';E.ElementTree(r).write(out,encoding='unicode');records.append({'state_id':'S-FOOD-DETAIL-LOADING','source_evidence_ids':['E-FOOD-DETAIL-LOADING'],'native_path':'../../evidence/2026-09-28-full-audit/food-160725-vending-detail-map-loading.png','base_svg':base.name,'base_sha256':h(base),'output':out.name,'output_sha256':h(out),'loading_mark':logo})
base=D/'food-map.svg';r=E.parse(base).getroot();viewport=g(r,'MapViewport');viewport.clear();viewport.set('id','MapViewport');E.SubElement(viewport,f'{{{S}}}rect',{'x':'0','y':'100','width':'576','height':'870','fill':'#F2F2F2'})
logo=mark(viewport,'food-161013-full-map-loading.png',(261,101,317,153),'food-map-loading-mark.png',261,101)
r.find('s:title',ns).text='VA210 full map — loading';r.find('s:desc',ns).text='Editable header and gray blank full-map body based on E-FOOD-MAP-LOADING. Static public loading mark near top; no map geography/locate controls shown before tiles load. Duration unknown; cursor omitted; fonts/icons approximate.'
out=D/'food-map-loading.svg';E.ElementTree(r).write(out,encoding='unicode');records.append({'state_id':'S-FOOD-MAP-LOADING','source_evidence_ids':['E-FOOD-MAP-LOADING'],'native_path':'../../evidence/2026-09-28-full-audit/food-161013-full-map-loading.png','base_svg':base.name,'base_sha256':h(base),'output':out.name,'output_sha256':h(out),'loading_mark':logo})
(D/'food-loading-assets.json').write_text(json.dumps({'records':records,'frame_size':[576,970],'limits':['Static captured loading marks, not live animation.','Approximate fonts/icons; no measured native loading duration.','Early exits/expand controls while loading not natively verified.']},ensure_ascii=False,indent=2)+'\n')
