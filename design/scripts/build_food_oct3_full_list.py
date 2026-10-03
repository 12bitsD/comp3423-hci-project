"""Reconstruct the current 28-row public Food list from archived native evidence.

Labels, statuses, tags and affordances remain independent SVG objects. Only
public logos and the 14px map strip are raster. Figma scrolling requires actual
UI configuration and replay; this generator does not operate the application.
"""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as E
from PIL import Image,ImageDraw,ImageFont
from build_calendar_class_exam_oct2 import node,tag,group,rect,label,path,hit,image
from build_food_oct3_details import header
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-10-03-food-reverse-controls';AS=D/'assets';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
# Public logo coordinates verified against the original native viewports.
CROPS={1:('21-food-reverse-top.png',171),2:('21-food-reverse-top.png',389),3:('21-food-reverse-top.png',604),4:('21-food-reverse-top.png',791),5:('07-food-list-next.png',311),8:('10-food-list-middle.png',239),9:('10-food-list-middle.png',427),10:('10-food-list-middle.png',591),11:('10-food-list-middle.png',838),12:('11-food-list-middle2.png',359),13:('11-food-list-middle2.png',574),14:('11-food-list-middle2.png',761),15:('12-food-list-middle3.png',281),16:('12-food-list-middle3.png',497),17:('12-food-list-middle3.png',685),18:('13-food-list-va210.png',177),19:('13-food-list-va210.png',364),20:('13-food-list-va210.png',551),21:('13-food-list-va210.png',739),22:('16-food-list-machines.png',181),23:('16-food-list-machines.png',369),24:('16-food-list-machines.png',555),25:('16-food-list-machines.png',744),26:('17-food-list-last.png',378),27:('17-food-list-last.png',593),28:('17-food-list-last.png',758)}
LOCS=[['P/F, Block Y · Canteen'],['4/F, Communal Building','· Chinese Restaurant'],['3/F, Communal Building · Fast Food'],['4/F, Communal Building','· Chinese Restaurant'],['P/F, Block FGHJ Courtyard · Cafe'],['G/F, Student Residence Halls · Cafe'],['P/F, Pao Yue-kong Library · Cafe'],['G/F, Chung Sze Yuen Building · Cafe'],['1/F, Student Halls (Hung Hom)','· Fast Food'],['P/F, CD Wing & DE Wing · Fast Food'],['P/F, Jockey Club Innovation Tower','· Cafe'],['VA215, P/F, Shaw Amenities Building','· Cafe'],['P/F, Block VA · Take-away kiosk'],['G/F, Shaw Amenities Building','· Fast Food'],['G/F, Shaw Amenities Building','· Fast Food'],['P/F, Block W · Italian Food'],['P/F, Block X · Cafe'],['2/F, Block Z · Fast Food'],['2/F, Block Z · Cafe'],*([['P/F, Block VA · Vending Machine']]*5),['QT201, Wong Man and Tang Kit Wah','Global Student Hub','· Vending Machine'],['Podium Level, Block R','· Vending Machine'],['Podium Level, Block R','· Vending Machine'],['P/F, Shaw Amenities Building','· Take-away shop']]
HEIGHTS=[218,216,187,216,247,187,187,187,165,247,216,216,187,216,216,187,187,187,187,187,136,187,187,187,225,216,165,216]
FOOTER=73 # Native17/18: last separator949/950; white rows951..1023.
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
def restaurant(parent,x,y):
 g=group(parent,parent.get('id')+'-VenueType');g.set('transform',f'translate({x} {y})');path(g,'M2 2L17 17M17 2L2 17M1 5L5 1M4 8L8 4M7 11L11 7','#818481',2.8,stroke_linecap='round');g.append(node('path',d='M18 0L12 7L16 10L21 4',fill='#818481'))
def crop(source,box,name,records):
 f=AS/name;Image.open(P/source).crop(box).save(f);records.append({'file':'assets/'+name,'source_file':'../../evidence/'+P.name+'/'+source,'source_evidence_id':'E-FOOD-REV-'+source[:2],'source_sha256':sha(P/source),'crop_xyxy':list(box),'sha256':sha(f),'dimensions':list(Image.open(f).size),'limits':'Public brand/logo or narrow campus map strip; raster only. No private identity or full card screenshot.'});return f
def main(global_clips=False):
 records=[];layout=[];cat=json.loads((P/'venue-catalogue.json').read_text());assert len(cat['rows'])==28 and len(LOCS)==len(HEIGHTS)==28
 r=node('svg',width=576,height=1024,viewBox='0 0 576 1024');t=node('title');t.text='October3 Food — current28-row expanded list';r.append(t);t=node('desc');t.text='Editable reconstruction of the archived current public Food list. Research row IDs distinguish duplicate titles, not backend identity. Fixed header/map strip/handle; list content is tall, viewport147..1024. Geometry/fonts/icons approximate. Only public logos/map strip raster. No row/hours/tag/order/back actions configured; SVG does not implement scrolling. Actual Figma setup/replay recorded separately.';r.append(t)
 defs=node('defs')
 if global_clips:
  cp=node('clipPath',id='FoodOct3ListClip');rect(cp,0,147,576,877,'#FFFFFF');defs.append(cp)
 r.append(defs);rect(r,0,0,576,1024,'#FFFFFF',id='ScreenBackground')
 strip=crop('21-food-reverse-top.png',(0,100,576,114),'food-oct3-list-map-strip.png',records);image(group(r,'PublicMapStrip'),strip,0,100,576,14)
 panel=group(r,'ListSheet');panel.append(node('path',d='M0 140Q0 114 24 114H552Q576 114 576 140V1024H0Z',fill='#FFFFFF'));rect(group(panel,'PanelHandle'),238.5,130,100,7.5,'#31917D',rx=2)
 vp=group(r,'VenueListViewport')
 if global_clips:vp.set('clip-path','url(#FoodOct3ListClip)')
 content=group(vp,'VenueListContent');rect(content,0,147,576,sum(HEIGHTS)+FOOTER,'#FFFFFF',id='ListContentBackground');top=147
 for i,(record,locs,height) in enumerate(zip(cat['rows'],LOCS,HEIGHTS),1):
  y=top if global_clips else 0;g=group(content,'VenueRow%02d'%i)
  if not global_clips:g.set('transform',f'translate(0 {top})')
  rect(g,0,y,576,height,'#FFFFFF',id='RowBackground%02d'%i)
  if i in CROPS:
   source,cy=CROPS[i];f=crop(source,(28,cy,91,cy+63),'food-oct3-list-logo-%02d.png'%i,records);image(group(g,'Logo%02d'%i),f,28,y+24,63,63)
  else:
   a=group(g,'EditableAvatar%02d'%i);rect(a,28,y+24,63,63,'#DEDEDE',rx=10);label(a,59.5,y+68,'H' if i==6 else 'L',35,'#202020',text_anchor='middle')
  titlelines=['Block Y Outlet - Grove & Tai Tai','Foodtopia'] if i==1 else ['Wong Man and Tang Kit Wah Global','Student Hub Vending Machine'] if i==25 else [record['visible_name']]
  for n,title in enumerate(titlelines):label(g,119,y+44+n*30,title,22,'#101010',font_weight='700')
  extra=(len(titlelines)-1)*30;restaurant(g,122,y+52+extra)
  for n,loc in enumerate(locs):label(g,109 if loc.startswith('·') else 151,y+74+extra+n*29,loc,20,'#484848')
  extra+=(len(locs)-1)*29;by=y+91+extra;opened=i!=28;badge=group(g,'OpeningHours%02d'%i);rect(badge,119,by,123 if opened else 95,30,'#E8F5DB' if opened else '#F7DEDE',rx=15);badge.append(node('circle',cx=133,cy=by+15,r=6,fill='#7EAD54' if opened else '#CC5146'));label(badge,147,by+22,'Open Now' if opened else 'Closed',18,'#101010')
  desc=record['public_ax_description'];timing=desc.split('Open Now ',1)[1].split(' #',1)[0].replace(' Online Order','') if opened else 'Further information';tx=247 if opened else 219;label(badge,tx,by+22,timing,17,'#555555');ax=tx+font.getlength(timing)*17/18+5;badge.append(node('path',d=f'M{ax} {by+12}L{ax+6} {by+19}L{ax+12} {by+12}Z',fill='#878787'));hit(badge,119,by,ax+12-119,30)
  menu=group(g,'VenueMenu%02d'%i);my=y+89+extra/2;hit(menu,516,my-23,48,46)
  for cx in [532,540,548]:menu.append(node('circle',cx=cx,cy=my,r=2.7,fill='#9FB2BE'))
  tags=desc.split(' #')[1:];tags=[t.replace(' Online Order','') for t in tags];ty=y+138+extra
  if tags:
   cp=node('clipPath',id='FoodTagClip%02d'%i,clipPathUnits='userSpaceOnUse');rect(cp,119,ty,388,27,'#FFFFFF');defs.append(cp);tg=group(g,'TagsViewport%02d'%i);tg.set('clip-path','url(#FoodTagClip%02d)'%i);x=119
   for n,txt in enumerate(tags,1):
    w=font.getlength('#'+txt)+16;pill=group(tg,'Tag%02d-%02d'%(i,n));rect(pill,x,ty,w,27,'#EFEFEF',rx=14);label(pill,x+8,ty+20,'#'+txt,18,'#555555');x+=w+4
  if record['online_order_visible_or_in_public_leaf']:
   oy=ty+42;order=group(g,'OnlineOrder%02d'%i);rect(order,119,oy,217,50,'#FFFFFF',stroke='#D3D3D3',rx=25);path(order,f'M143 {oy+24}L155 {oy+12}M148 {oy+29}L160 {oy+17}M145 {oy+12}C139 {oy+8} 132 {oy+15} 137 {oy+21}M157 {oy+20}C162 {oy+26} 169 {oy+19} 164 {oy+13}','#58AF9C',3,stroke_linecap='round');label(order,176,oy+33,'Online Order',20,'#494949');path(order,f'M296 {oy+31}L304 {oy+21}M295 {oy+21}H304V{oy+30}','#7D7D7D',2.5);hit(order,119,oy,217,50)
  path(g,f'M0 {y+height}H576','#DADADA',1.4);layout.append({'catalogue_id':record['catalogue_id'],'name':record['visible_name'],'group':'VenueRow%02d'%i,'source_evidence_ids':record['visible_screenshot_evidence_ids'],'top_in_content':top-147,'height':height,'title_lines':titlelines,'location_lines':locs,'tags_from_public_ax':tags,'tags_visibility_limit':'Only visible prefix/clipped edge verified; offscreen tag gestures not observed','online_order_visible':record['online_order_visible_or_in_public_leaf']});top+=height
 stem='food-oct3-full-list-global-corrected' if global_clips else 'food-oct3-full-list-local';header(r,'Food');f=D/(stem+'.svg');E.ElementTree(r).write(f,encoding='unicode',xml_declaration=True)
 ids=[n.get('id') for n in r.iter() if n.get('id')];assert len(ids)==len(set(ids)),[i for i in ids if ids.count(i)>1]
 meta=D/(stem+'-layout.json');v={'file':f.name,'sha256':sha(f),'clip_coordinate_mode':'global-nested-mask' if global_clips else 'row-local-no-outer-mask','status':'prepared_not_imported_not_replayed','dimensions':[576,1024],'viewport_position':[0,147],'viewport_dimensions':[576,877],'content_height':sum(HEIGHTS)+FOOTER,'observed_footer':{'height':FOOTER,'source_evidence_ids':['E-FOOD-REV-17','E-FOOD-REV-18'],'source_pixel_rows':[951,1024],'scope':'Blank tail after last native separator; reconstructed row heights still approximate'},'inferred_scroll_range':[0,sum(HEIGHTS)+FOOTER-877],'native_complete_geometry_verified':False,'source_catalogue':'../../evidence/'+P.name+'/venue-catalogue.json','source_catalogue_sha256':sha(P/'venue-catalogue.json'),'rows':layout,'assets':records,'limits':['28 observed rows in their current archived order; no backend identity or sorting rules inferred.','Native top/bottom/reverse samples observed; reconstructed row heights and total scroll extent approximate.','SVG clip semantics must be verified after actual Figma import, not assumed from rendering.','No row/menu/hours/tag/order/Back wiring; no native app input or Figma changes by generator.','Logo/map strip raster; other labels/vectors editable source only. Full fidelity not_verified.']}
 if meta.exists():
  old=json.loads(meta.read_text())
  if old['sha256']==v['sha256']:
   for k in ['status','figma','editor_evidence_ids','prototype_run_ids']:
    if k in old:v[k]=old[k]
 meta.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
 contact=Image.new('RGB',(700,400),'white');dr=ImageDraw.Draw(contact)
 for n,rec in enumerate(records):
  if 'logo-' not in rec['file']:continue
  i=int(Path(rec['file']).stem[-2:]);x=(i-1)%7*100;y=(i-1)//7*100;im=Image.open(D/rec['file']);contact.paste(im,(x+18,y+25));dr.text((x+5,y+5),'row%02d'%i,fill='black')
 contact.save('/tmp/polyu-food-oct3-logo-contact.png');print(json.dumps({'rows':28,'content_height':sum(HEIGHTS)+FOOTER,'observed_footer':{'height':FOOTER,'source_evidence_ids':['E-FOOD-REV-17','E-FOOD-REV-18'],'source_pixel_rows':[951,1024],'scope':'Blank tail after last native separator; reconstructed row heights still approximate'},'raster_assets':len(records),'figma_input':False}))
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--global-clips',action='store_true',help='Generate a separate corrected global-coordinate comparison source; never overwrite archived failure SVGs')
 main(p.parse_args().global_clips)
