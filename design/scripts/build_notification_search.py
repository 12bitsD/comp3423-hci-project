"""Prepare current Notification caller Search states from archived native evidence.

File generation only. Arbitrary input and unobserved detail controls remain open.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import json,hashlib
from PIL import Image
from build_calendar_class_exam_oct2 import group,rect,label,path,hit,image,find,tag,node
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-10-03-notification-search-native';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def search(query='',noresult=False):
 r=E.parse(D/('search-weather-no-results.svg' if noresult else 'search-empty.svg')).getroot();r.set('height','1024');r.set('viewBox','0 0 576 1024');find(r,'ScreenBackground').set('height','1024')
 inp=find(r,'SearchInput');inp.find(tag('text')).text=query or 'Search';inp.find(tag('text')).set('fill','#141414' if query else '#8D9AA4')
 if query and not noresult:
  g=group(r,'ClearSearch');hit(g,502,115,60,71);g.append(node('circle',cx=532.5,cy=149.5,r=13,fill='#575757'));path(g,'M528 145L537 154M537 145L528 154','#FFFFFF',3.2)
 if noresult:
  hit(find(r,'ClearSearch'),502,115,60,71)
  for n in find(r,'DecorativeWaves'):n.set('d',n.get('d').replace('V970','V1024'))
 if query=='workshop':
  g=group(r,'VenueResult');hit(g,14,203,548,66);label(g,31,247,'VA210 Vending Machine',23,'#555555');path(g,'M549 231L556 238L549 246','#888888',5,stroke_linecap='round',stroke_linejoin='round')
 hit(find(r,'Back'),10,28,55,61);hit(inp,64,115,430,72)
 return r

def detail():
 r=E.parse(D/'food-detail.svg').getroot();r.set('height','1024');r.set('viewBox','0 0 576 1024');find(r,'ScreenBackground').set('height','1024');content=find(r,'PageContent')
 for n in content.findall(tag('rect')):
  if n.get('height')=='870':n.set('height','924')
 hero=find(r,'VenueHero');hero.remove(hero.find(tag('image')));image(hero,D/'assets/notice-search-va210-hero.png',207,100,223,240)
 mapg=find(r,'PublicMap');mapg.remove(mapg.find(tag('image')));image(mapg,D/'assets/notice-search-va210-map.png',35,670,507,310)
 content.remove(find(r,'MapCallout'));hit(find(r,'Back'),10,28,55,61)
 return r

def main():
 im=Image.open(P/'12-va210-entry-followup.png');assert im.size==(576,1024)
 assets=[]
 for name,crop in [('notice-search-va210-hero.png',(207,100,430,340)),('notice-search-va210-map.png',(35,670,542,980))]:
  file=D/'assets'/name;im.crop(crop).save(file);assets.append({'file':'assets/'+name,'sha256':sha(file),'source_evidence_id':'E-NOTICE-SEARCH-12','crop_xyxy':list(crop),'dimensions':list(Image.open(file).size),'limits':'Public illustration/geographic map crop; attribution retained; geography labels/pins raster'})
 specs=[('empty','S-NOTIFICATION-SEARCH-EMPTY',['02','27'],search()),('workshop','S-NOTICE-SEARCH-WORKSHOP',['09','14','21'],search('workshop')),('negative','S-NOTICE-SEARCH-NEGATIVE',['18'],search('zzhci2026',True)),('title','S-NOTICE-SEARCH-TITLE-NONE',['23'],search('Upcoming IT Workshops',True)),('detail','S-FOOD-DETAIL',['12'],detail())]
 out=[];recpath=D/'notification-search-sources.json';old={x['file']:x for x in json.loads(recpath.read_text())['sources']} if recpath.exists() else {}
 for name,state,eids,r in specs:
  filename='notification-search-'+name+'.svg';r.find(tag('title')).text='Notification caller Search — '+name;r.find(tag('desc')).text='Reconstruction from2026-10-03 native Computer Use public Search/VA210 samples.576x1024 editable chrome approximate; fixed query keyboard proxies not arbitrary text input. Public illustration/map raster. Cursor/halo and bottom rounded capture artifact omitted; its origin unknown. Native index scope, Return submission semantics and full app not_verified.'
  for n in r.iter():
   if n.get('stroke') and n.get('fill') is None:n.set('fill','none')
  E.ElementTree(r).write(D/filename,encoding='unicode',xml_declaration=True);record={'file':filename,'state_id':state,'source_evidence_ids':['E-NOTICE-SEARCH-'+e for e in eids],'sha256':sha(D/filename),'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed'}
  if name in ['empty','detail']:record['context_variant']='20261003-notification-search-'+name
  if filename in old and old[filename]['sha256']==record['sha256']:record.update(old[filename])
  out.append(record)
 recpath.write_text(json.dumps({'sources':out,'assets':assets,'limits':['Three sampled queries; native index scope and arbitrary input not established.','Fixed keyboard proxies are a Figma limitation; not native key bindings.','Existing970px callers retained. New1024px detail caller Back preserves workshop. Call/image/map/detail navigation not configured in this batch.']},ensure_ascii=False,indent=2)+'\n');print(json.dumps({'sources':len(out),'assets':len(assets),'figma_mutations':0}))
if __name__=='__main__':main()
