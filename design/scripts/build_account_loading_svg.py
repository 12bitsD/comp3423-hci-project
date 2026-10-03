"""Reconstruct privacy-safe native Study/Courses/QR loading viewports."""
from pathlib import Path
import xml.etree.ElementTree as E
import base64,copy,json,hashlib
from PIL import Image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';N=R/'evidence/2026-09-28-full-audit';S='http://www.w3.org/2000/svg';X='http://www.w3.org/1999/xlink';ns={'s':S};E.register_namespace('',S);E.register_namespace('xlink',X)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();records=[]
for slug,state,eid,source,base,qr in [('study','S-STUDY-LOADING','E-STUDY-LOADING','study-173055-loading.png','study-completed-demo.svg',False),('courses','S-COURSES-LOADING','E-COURSES-LOADING','courses-173334-loading.png','courses-canvas-demo.svg',False),('qr','S-QR-LOADING','E-QR-LOADING','qr-174007-loading.png','qr-demo.svg',True)]:
 t=E.parse(D/base).getroot();root=E.Element(f'{{{S}}}svg',{'width':'576','height':'970','viewBox':'0 0 576 970','fill':'none'});E.SubElement(root,f'{{{S}}}title').text=slug.title()+' — observed loading';E.SubElement(root,f'{{{S}}}desc').text=f'Privacy-safe generic loading viewport reconstructed from {eid}. No private body or functional QR. Editable public chrome/overlay/card; static raster native mark, no measured duration. Approximate font/icons, cursor omitted.'
 E.SubElement(root,f'{{{S}}}rect',{'id':'ScreenBackground','width':'576','height':'970','fill':'white'})
 header=copy.deepcopy(t.find('.//s:g[@id="Header"]',ns));demo=header.find('s:g[@id="DemoNotice"]',ns);header.remove(demo);root.append(header)
 if qr:root.append(copy.deepcopy(t.find('.//s:g[@id="BottomNavigation"]',ns)))
 overlay=E.SubElement(root,f'{{{S}}}g',{'id':'LoadingOverlay'});E.SubElement(overlay,f'{{{S}}}rect',{'width':'576','height':'970','fill':'#000000','fill-opacity':'0.4'});E.SubElement(overlay,f'{{{S}}}rect',{'x':'192','y':'455','width':'193','height':'116','rx':'16','fill':'white'})
 crop=(258,484,319,543);p=D/'assets'/f'{slug}-loading-mark.png';Image.open(N/source).convert('RGB').crop(crop).save(p);E.SubElement(overlay,f'{{{S}}}image',{'x':'258','y':'484','width':'61','height':'59',f'{{{X}}}href':'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()});out=D/f'{slug}-loading.svg';E.ElementTree(root).write(out,encoding='unicode')
 records.append({'state_id':state,'source_evidence_ids':[eid],'native_path':'../../evidence/2026-09-28-full-audit/'+source,'native_sha256':h(N/source),'base_svg':base,'base_sha256':h(D/base),'output':out.name,'output_sha256':h(out),'loading_mark':{'file':'assets/'+p.name,'sha256':h(p),'dimensions':[61,59],'crop_xyxy':crop}})
(D/'account-loading-assets.json').write_text(json.dumps({'records':records,'frame_size':[576,970],'limits':['Static native loading marks, approximate typography/geometry.','No private coursework or active QR.','Early cancellation and native latency unverified.']},ensure_ascii=False,indent=2)+'\n')
