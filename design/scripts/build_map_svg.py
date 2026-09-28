"""Reconstruct editable map controls around public, raster map imagery.

Reads only reviewed public evidence. Map geography/labels/pins remain image crops;
this does not implement live maps, geolocation, arbitrary pan/zoom or search.
"""
from PIL import Image
from build_study_svg import ROOT, OUT, ASSETS, EVIDENCE, text, rect, group, line, bitmap, screen, header

DATA = [
 ('initial', 'map-173526-initial-campus.png', [], False, None),
 ('initial-right', 'map-173526-initial-campus.png', [], True, None),
 ('toilets', 'map-173539-toilets-selected.png', ['Toilets'], False, 'Toilets'),
 ('combined', 'map-173659-toilets-and-water-selected.png', ['Toilets','Water Stations'], False, 'Toilets'),
 ('water', 'map-173714-water-only.png', ['Water Stations'], False, 'Water Stations'),
 ('water-scrolled', 'map-173741-water-list-scrolled.png', ['Water Stations'], False, 'ScrolledWater'),
 ('clinics', 'map-173810-clinics.png', ['Clinics'], False, 'Clinics'),
 ('banks', 'map-173839-banks.png', ['Banks'], True, 'Banks'),
 ('aeds', 'map-173906-aeds.png', ['AEDs'], True, 'AEDs'),
 ('bookstores', 'map-173929-bookstores.png', ['Bookstores'], True, 'Bookstores'),
]
ROWS = {
 'Toilets':[('Toilet (Core C)','Core C','Core C'),('Toilet (Core E)','Core E','Core E'),('Toilet (Core H)','Core H','Core H')],
 'Water Stations':[('Water Station (Core C)','Podium Level, Core C','Core C'),('Water Station (Core D)','Podium Level, Core D','Core D'),('Water Station (Core E)','Podium Level, Core E','Core E')],
 'ScrolledWater':[('Water Station (Core R)','Podium Level, Core R','Core R'),('Water Station (Core T)','Podium Level, Core T','Core T')],
 'Clinics':[('Dental Clinic','Room GH020, G/F, Wing GH (Core H)','Core H'),('Integrative Health Clinic','Room AG057, G/F, Wing AG (Core A)','Core A (G/F)')],
 'Banks':[('Bank','Block VA','Block VA')],
 'AEDs':[('AED (Block X)','Block X - G/F, Sports Centre service counter','Block X (G/F)'),('AED (Block Z)','Block Z - 2/F, service counter next to Rm Z208','Block Z')],
 'Bookstores':[('Bookshop','Podium Level, Shaw Amenities Building','Block VA')],
}

def icon(name,x,y,color):
    if name=='Toilets':
        return rect(x,y,20,24,'#71849B',3)+text(x+10,y+17,'WC',9,700,'white','middle')
    if name=='Water Stations':
        return f'<path d="M{x+2} {y+11}H{x+19}V{y+18}M{x+8} {y+11}V{y+4}H{x+19}M{x+12} {y+1}V{y+6}" stroke="{color}" stroke-width="2.5"/>'
    if name=='Clinics':
        return f'<path d="M{x+3} {y+2}V{y+11}Q{x+11} {y+24} {x+18} {y+11}V{y+2}M{x+11} {y+18}V{y+24}Q{x+25} {y+28} {x+24} {y+17}" stroke="{color}" stroke-width="1.7"/><circle cx="{x+24}" cy="{y+15}" r="3" stroke="{color}"/>'
    if name=='Banks':
        return f'<path d="M{x} {y+8}L{x+12} {y}L{x+24} {y+8}ZM{x+4} {y+11}V{y+23}M{x+12} {y+11}V{y+23}M{x+20} {y+11}V{y+23}M{x} {y+25}H{x+24}" stroke="{color}" stroke-width="2"/>'
    if name=='AEDs': return rect(x,y,21,23,'#505050',2)+text(x+10,y+18,'A',19,400,'white','middle')
    return f'<path d="M{x} {y+2}Q{x+6} {y} {x+12} {y+3}Q{x+18} {y} {x+24} {y+2}V{y+23}Q{x+18} {y+20} {x+12} {y+24}Q{x+6} {y+20} {x} {y+23}ZM{x+12} {y+3}V{y+24}" stroke="{color}" stroke-width="1.6"/>'

def chips(selected,right):
    # A clean neutral band replaces hidden map fragments behind native chips.
    b=rect(0,100,576,55,'#DDE3E3')
    configs=[('Clinics',-3,126),('Banks',133,122),('AEDs',265,110),('Bookstores',385,170)] if right else [('Toilets',22,126),('Water Stations',158,204),('Clinics',373,127),('Banks',510,123)]
    for name,x,w in configs:
        c='white' if name in selected else '#4B4B4B';fill='#539B8B' if name in selected else 'white'
        b+=group('Filter'+name.replace(' ',''),rect(x,114,w,39,fill,20)+icon(name,x+13,121,c)+text(x+42,140,name,22,color=c))
    return group('CategoryStrip',b)

def result_sheet(category):
    top=620 if category=='Clinics' else 612
    b=rect(0,top,576,400,'white',36)+rect(238,top+16,100,7,'#549582',3)
    if category=='ScrolledWater':
        b+=text(31,674,'Core Q',20,color='#454545');start=698
    else:
        b+=rect(0,top+40,576,44,'#EFEFF0')+icon(category,31,top+48,'#576575')+text(75,top+73,category,28,700,'#555555');start=top+84
    for i,row in enumerate(ROWS[category]):
        y=start+i*121
        r=line(0,y,576,y,'#E5E5E5')+text(31,y+42,row[0],22,700)+text(31,y+70,row[1],20,color='#424242')+text(31,y+97,row[2],20,color='#424242')
        r+=group('Facility'+str(i+1)+'Detail',rect(512,y+32,54,54,'white').replace('fill="white"','fill="white" fill-opacity="0.001"')+''.join(f'<circle cx="{534+7*k}" cy="{y+58}" r="2.5" fill="#95A6B8"/>' for k in range(3)))
        b+=group('FacilityRow'+str(i+1),r)
    return group('ResultsList',b)

def crop(name,src,box):
    ASSETS.mkdir(exist_ok=True)
    Image.open(EVIDENCE/src).crop(box).save(ASSETS/name)
    return name

for name,src,selected,right,cat in DATA:
    stop=620 if cat=='Clinics' else 612 if cat else 970
    asset=crop('mainmap-'+name+'-geography.png',src,(0,154,576,stop))
    b=bitmap(asset,0,154,576,stop-154,'PublicMapGeography')+chips(selected,right)
    if cat:b+=result_sheet(cat)
    extra='Geography, map labels and markers are raster evidence, not editable/live map objects. The strip background is neutral rather than reconstructed hidden map pixels; icons/fonts approximate native appearance. Only sampled facility rows are included; no all-list claim. '
    if name=='initial-right':extra+='Rightmost unselected category strip was directly observed by native horizontal drag on 2026-09-28; map body reuses the identical initial geographic view. '
    screen('mainmap-'+name+'.svg','Map — '+name,src,b+header('Map'),extra)

src='map-173546-toilet-core-c-detail.png'
asset=crop('mainmap-detail-geography.png',src,(34,289,542,596))
b=rect(18,100,540,870,'white',stroke='#D8DCDE')+text(34,145,'Toilet (Core C)',29,700)+text(34,185,'Core C',21,700,'#539882')+text(34,225,'Core C',22)+line(34,252,542,252,'#E1E1E1')+bitmap(asset,34,289,508,307,'PublicDetailMap')
b+=group('ExpandMap',rect(447,525,70,64,'white',5)+'<path d="M464 553L487 535M477 535H487V545M477 556L464 570M464 559V570H475" stroke="#222" stroke-width="3"/>')
screen('mainmap-detail.svg','Toilet (Core C) — Detail',src,b+header('Toilet (Core C)'),'Only the detail map is a raster crop. The expand control and all page text are editable.')
src='map-173556-toilet-core-c-full-map.png';asset=crop('mainmap-full-geography.png',src,(0,100,576,970))
screen('mainmap-full.svg','Toilet (Core C) — Expanded map',src,bitmap(asset,0,100,576,870,'PublicExpandedMap')+header('Toilet (Core C)'),'Expanded geography, labels, marker and underlying Google controls are raster reference only. Pan, zoom, My location and Google handoff remain unimplemented/unverified. Back is editable.')
print('Built 12 editable Map SVGs with public geographic crops.')
