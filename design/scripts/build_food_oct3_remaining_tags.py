"""Build finite editable tag-result sources from public native screenshots.

No app/Figma input. Initial transition captures remain evidence; these sources
use the later stable query samples. No arbitrary search or working navigation.
"""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as E
from build_food_oct3_details import root,header
from build_calendar_class_exam_oct2 import node,tag,group,rect,label,path,hit
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
SPECS=[
 ('asian','Asian Cuisine',['Communal Student Restaurant','V Café','Z Canteen','X Café','U Garden (Student Canteen)','Block Y Outlet - Grove & Tai Tai Foodtopia'],'14'),
 ('western','Western Cuisine',['H Café','LibCafé','VA Kiosk','W Kiosk','Gourmet Shop','V Café','Z Canteen','X Café','U Garden (Student Canteen)','Block Y Outlet - Grove & Tai Tai Foodtopia','VA Café'],'16'),
 ('taiwanese','Taiwanese Cuisine',['Block Y Outlet - Grove & Tai Tai Foodtopia'],'18'),
 ('cake','Cake / Dessert',['LibCafé','Gourmet Shop','X Café','Theatre Lounge','Block Y Outlet - Grove & Tai Tai Foodtopia','VA Café'],'20'),
 ('salad','Salad',['LibCafé','VA Kiosk','W Kiosk','Gourmet Shop','X Café','Block Y Outlet - Grove & Tai Tai Foodtopia','VA Café'],'22')]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 meta=D/'food-oct3-remaining-tags-sources.json';prev={s['file']:s for s in json.loads(meta.read_text())['sources']} if meta.exists() else {};sources=[]
 for slug,q,names,eid in SPECS:
  r=root(q+' from Block Y — stable finite query');r.find(tag('desc')).text='Editable approximation of the stable October3 public tag query. Independent text/Back/result groups. Fixed sample only; no arbitrary search, navigation or scroll configured by this generator. Initial transition captures remain separate evidence.'
  header(r,'Search');g=group(r,'SearchInput');rect(g,12,112,552,74,'#F0F0F0',rx=13);g.append(node('circle',cx=32,cy=145,r=10,fill='none',stroke='#555555',stroke_width=4));path(g,'M40 154L49 163','#555555',4);label(g,58,158,q,23,'#141414');hit(g,54,112,498,74);path(r,'M0 200H576','#D8D8D8',1.2)
  for i,name in enumerate(names):
   y=247+i*77;g=group(r,'Result-'+str(i+1));hit(g,18,y-40,540,70);label(g,30,y,name,22,'#555555');path(g,f'M550 {y-16}L556 {y-9}L550 {y-2}','#888888',4,stroke_linecap='round')
  f=D/('food-oct3-tag-'+slug+'.svg');E.ElementTree(r).write(f,encoding='unicode',xml_declaration=True)
  rec={'file':f.name,'state_id':'S-FOOD-OCT3-'+slug.upper(),'query':q,'result_names':names,'source_evidence_ids':['E-FOOD-TAGS-'+eid]+(['E-FOOD-TAGS-04'] if slug=='western' else []),'sha256':sha(f),'dimensions':[576,1024],'status':'prepared_not_imported_not_connected_not_replayed'}
  if f.name in prev and prev[f.name]['sha256']==rec['sha256']:rec.update(prev[f.name])
  sources.append(rec)
 meta.write_text(json.dumps({'sources':sources,'limits':['Fonts/icons/geometry approximate; native transitions not substituted for stable states.','Five fixed query snapshots, independent editable public text. No functional query field, row navigation or complete search index.','Western initial and scrolled native samples preserved; this source is its stable finite visible list, not a verified scroll boundary.','Generator does not operate Figma; actual import/readback/evidence must be recorded separately.']},ensure_ascii=False,indent=2)+'\n');print(json.dumps({'sources':len(sources),'figma_mutations':0}))
if __name__=='__main__':main()
