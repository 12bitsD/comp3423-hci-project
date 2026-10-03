"""Prepare editable Food detail sources from archived native evidence only.

No app/Figma input. Screenshot maps/logos are raster; labels and chrome editable.
Initial/lower detail are finite viewport samples, not a configured scroll region.
"""
from pathlib import Path
import json, hashlib, xml.etree.ElementTree as E
from PIL import Image
from build_calendar_class_exam_oct2 import node, tag, group, rect, label, path, hit, image

R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-10-03-food-menu-details'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
AS=D/'assets';records=[];sources=[]

def asset(name,source,box):
    file=AS/name;Image.open(P/source).crop(box).save(file)
    records.append({'file':'assets/'+name,'source_file':source,'source_evidence_id':'E-FOOD-MENU-'+source[:2],'crop_xyxy':list(box),'sha256':sha(file),'dimensions':list(Image.open(file).size),'limits':'Public logo/map crop only; raster geography/callouts/attribution retained. Cursor may remain in map crops.'})
    return file

def root(title):
    r=node('svg',width=576,height=1024,viewBox='0 0 576 1024')
    for name,value in [('title',title),('desc','Local editable reconstruction of finite2026-10-03 native Food samples. Fonts/icons approximate. Public maps/logos raster; no live data, arbitrary search, location or full scrolling implementation. Not imported/connected/replayed in Figma.')]:
        n=node(name);n.text=value;r.append(n)
    rect(r,0,0,576,1024,'#FFFFFF',id='ScreenBackground');return r

def header(r,title):
    g=group(r,'Header');rect(g,0,0,576,100,'#FFFFFF',stroke='#D0D0D0')
    b=group(g,'Back');hit(b,8,25,52,60);path(b,'M35 54L26 64L35 74','#242424',7,stroke_linecap='round')
    label(g,288,74,title,27,'#242424',text_anchor='middle')

def expand(g,x,y,ident):
    b=group(g,ident);hit(b,x-10,y-10,50,50)
    path(b,f'M{x} {y+10}V{y}H{x+10}M{x+20} {y}H{x+30}V{y+10}M{x+30} {y+20}V{y+30}H{x+20}M{x+10} {y+30}H{x}V{y+20}','#35917E',4)

def tags(g,rows):
    for y,items in rows:
        x=35
        for txt,w in items:
            t=group(g,'Tag-'+txt.replace(' / ','-').replace(' ','-'));rect(t,x,y,w,27,'#EFEFEF',rx=14);label(t,x+7,y+20,'#'+txt,19,'#555555');hit(t,x,y,w,27);x+=w+4

def detail(title,location,lib=False,lower=False):
    r=root(title+' detail'+(' lower' if lower else ''));defs=node('defs');cp=node('clipPath',id='DetailViewport');rect(cp,0,100,576,924,'#FFFFFF');defs.append(cp);r.append(defs)
    clip=group(r,'DetailViewport');clip.set('clip-path','url(#DetailViewport)');g=group(clip,'DetailContent');delta=-68 if lower else 0;g.set('transform',f'translate(0 {delta})')
    rect(g,0,100,576,1013,'#F7F9F6');rect(g,18,100,539,1013,'#FFFFFF',stroke='#CAD0D0')
    if not lib:
        image(group(g,'PublicHero'),blockhero,151,100,278,226);expand(g,487,285,'ExpandImage')
    y=134 if lib else 377
    label(g,35,y,title,22,'#151515',font_weight='700');label(g,35,y+30,location,22,'#4B4B4B')
    by=y+45;badge=group(g,'OpenStatus');rect(badge,35,by,139,34,'#E8F5DB',rx=17);badge.append(node('circle',cx=49,cy=by+17,r=6,fill='#7EAD54'));label(badge,64,by+25,'Open Now',21,'#151515');label(g,178,by+25,'Last order 22:30' if lib else 'Close at 18:00',20,'#555555')
    hours=[('Mon - Sat:','08:00 - 23:00'),('Sun:','12:00 - 22:00'),('Public holiday:','Closed')] if lib else [('Mon - Fri:','08:00 - 20:00'),('Sat:','09:00 - 18:00'),('Sun, public holiday:','Closed')]
    for i,(day,time) in enumerate(hours):label(g,35,by+65+i*28,day,21,'#555555');label(g,288,by+65+i*28,time,21,'#555555')
    sep=by+149;path(g,f'M35 {sep}H541','#DADADA',1.4)
    if lib:
        tags(g,[(363,[('Cafe / Kiosk',143),('Western Cuisine',178),('Cake / Dessert',173)]),(395,[('Coffee',91),('Salad',81),('Sandwich',126),('Savory',90)])]);my=488;bottom=452;mapfile=libinline
    else:
        tags(g,[(606,[('Asian Cuisine',158),('Western Cuisine',178)]),(638,[('Taiwanese Cuisine',200),('Cake / Dessert',177),('Coffee',91)]),(670,[('Salad',81),('Sandwich',126)])]);my=762;bottom=726;mapfile=blockinline
    path(g,f'M35 {bottom}H541','#DADADA',1.4);image(group(g,'PublicInlineMap'),mapfile,35,my,507,309)
    # The public map crop includes its native black expansion graphic. Keep one
    # graphic and an editable selection target instead of drawing a second icon.
    hit(group(g,'ExpandMap'),447,my+236,76,73)
    header(r,'LibCafé' if lib else 'Block Y Outlet - Grove &...');return r

def search(query,names):
    r=root(query+' tag search');header(r,'Search');g=group(r,'SearchInput');rect(g,12,113,552,74,'#F0F0F0',rx=13);g.append(node('circle',cx=36,cy=145,r=10,fill='none',stroke='#555555',stroke_width=4));path(g,'M44 154L53 163','#555555',4);label(g,76,158,query,23,'#141414');hit(g,64,113,485,74)
    for i,name in enumerate(names):
        y=247+i*78;g=group(r,'Result-'+str(i+1));hit(g,18,y-40,540,70);label(g,30,y,name,23,'#555555');path(g,f'M525 {y-16}L531 {y-9}L525 {y-2}','#888888',5,stroke_linecap='round')
    return r

def maps(name,file):
    r=root(name);image(group(r,'PublicMapGeography'),file,0,100,576,924);header(r,'LibCafé' if name=='LibCafe map' else 'Block Y Outlet - Grove &...');return r

def write(name,r,state,eids):
    file=D/('food-oct3-'+name+'.svg');E.ElementTree(r).write(file,encoding='unicode',xml_declaration=True)
    sources.append({'file':file.name,'state_id':state,'source_evidence_ids':['E-FOOD-MENU-'+i for i in eids],'sha256':sha(file),'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed'})

def main():
    global blockhero,blockinline,libinline
    blockhero=asset('food-oct3-blocky-hero.png','01-block-y-menu.png',(151,100,429,326))
    blockinline=asset('food-oct3-blocky-inline-map.png','10-block-y-detail-lower.png',(35,693,542,1002))
    libinline=asset('food-oct3-libcafe-inline-map.png','05-lib-cafe-detail.png',(35,488,542,795))
    expanded=asset('food-oct3-blocky-expanded-hero.png','02-block-y-image.png',(133,360,441,621))
    write('blocky-detail',detail('Block Y Outlet - Grove & Tai Tai Foodtopia','P/F, Block Y'),'S-FOOD-OCT3-BLOCKY-DETAIL',['01','03','09','17','19'])
    write('blocky-lower',detail('Block Y Outlet - Grove & Tai Tai Foodtopia','P/F, Block Y',lower=True),'S-FOOD-OCT3-BLOCKY-LOWER',['10','15'])
    write('libcafe-detail',detail('LibCafé','P/F, Pao Yue-kong Library',lib=True),'S-FOOD-OCT3-LIBCAFE-DETAIL',['05','07'])
    r=root('BlockY expanded image');image(group(r,'PublicExpandedHero'),expanded,133,360,308,261);g=group(r,'CloseImage');hit(g,495,110,62,62);path(g,'M513 133L535 155M535 133L513 155','#000000',4);write('blocky-image',r,'S-FOOD-OCT3-BLOCKY-IMAGE',['02'])
    for q,names,eid in [('Coffee',['LibCafé','Homantin Hall Canteen','Gourmet Shop','X Café','Theatre Lounge','U Garden (Student Canteen)','Block Y Outlet - Grove & Tai Tai Foodtopia','VA Café'],'04'),('Sandwich',['H Café','LibCafé','VA Kiosk','Homantin Hall Canteen','Gourmet Shop','X Café','Block Y Outlet - Grove & Tai Tai Foodtopia','VA Café'],'16')]:write(q.lower(),search(q,names),'S-FOOD-OCT3-'+q.upper(),[eid])
    for name,src,state,title in [('libcafe-map','06-lib-cafe-map.png','LIBCAFE-MAP','LibCafe map'),('blocky-map','12-block-y-map-settled.png','BLOCKY-MAP','BlockY map'),('blocky-map-zoom','13-block-y-map-zoom.png','BLOCKY-MAP-ZOOM','BlockY map zoom'),('blocky-map-out','14-block-y-map-out.png','BLOCKY-MAP-OUT','BlockY map out')]:
        f=asset('food-oct3-'+name+'.png',src,(0,100,576,1024));write(name,maps(title,f),'S-FOOD-OCT3-'+state,[src[:2]])
    loading=asset('food-oct3-blocky-map-loading.png','11-block-y-map.png',(265,100,315,151));r=root('BlockY map loading');rect(r,0,100,576,924,'#F2F2F2');image(group(r,'LoadingMark'),loading,265,100,50,51);header(r,'Block Y Outlet - Grove &...');write('blocky-map-loading',r,'S-FOOD-OCT3-BLOCKY-MAP-LOADING',['11'])
    (D/'food-oct3-detail-sources.json').write_text(json.dumps({'sources':sources,'assets':records,'limits':['Local sources only; no Figma mutations or mappings.','Two detail viewports approximate finite observed positions; continuous scroll still needs configuration and replay.','Map/button graphics within geography crops are raster. Location/Google handoff unconfigured.','Tags other than Coffee/Sandwich unobserved; same-name rows not conflated.']},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'svg_sources':len(sources),'raster_assets':len(records),'figma_mutations':0}))

if __name__=='__main__':main()
