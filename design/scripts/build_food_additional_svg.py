"""Build four additional observed Food states; only public logos/maps are raster.

The two list viewports are discrete observed samples, not a complete venue list.
"""
from base64 import b64encode
from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape
from PIL import Image, ImageCms
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'design/polyulife';EV=ROOT/'evidence/2026-09-28-full-audit';AS=OUT/'assets'

def crop(source,box,name):
    im=Image.open(EV/source)
    if im.info.get('icc_profile'):
        im=ImageCms.profileToProfile(im,ImageCms.ImageCmsProfile(BytesIO(im.info['icc_profile'])),ImageCms.createProfile('sRGB'),outputMode='RGB')
    else: im=im.convert('RGB')
    im.crop(box).save(AS/name)

for source,box,name in [
 ('food-165435-list-sheet-expanded.png',(0,100,576,115),'food-expanded-map-strip.png'),
 ('food-165435-list-sheet-expanded.png',(29,725,92,788),'food-thumb-sakura-full.png'),
 ('food-165435-list-sheet-expanded.png',(29,912,92,956),'food-thumb-fifth-partial.png'),
 ('food-165444-list-scrolled-h-cafe.png',(29,155,92,218),'food-thumb-communal.png'),
 ('food-165444-list-scrolled-h-cafe.png',(29,372,92,435),'food-thumb-gourmet.png'),
 ('food-165444-list-scrolled-h-cafe.png',(29,588,92,651),'food-thumb-hcafe.png')]:crop(source,box,name)

def text(x,y,value,size=22,weight=400,color='#161616',anchor=None):
    a=f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="sans-serif" font-size="{size}" font-weight="{weight}"{a}>{escape(value)}</text>'
def rect(x,y,w,h,fill='#FFFFFF',rx=0,stroke=None):
    s=f' stroke="{stroke}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'
def image(name,x,y,w,h,gid):
    d=b64encode((AS/name).read_bytes()).decode()
    return f'<g id="{gid}"><image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" xlink:href="data:image/png;base64,{d}"/></g>'
def header():
    return '<g id="Header">'+rect(.5,.5,575,99,stroke='#E1E1E1')+'<g id="Back"><path d="M34.5 57.5L27 65L34.5 72.5" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>'+text(288,75.5,'Food',27,anchor='middle')+'</g>'
def icon(x,y,gid):
    return f'<g id="{gid}" transform="translate({x},{y})"><path d="M2 2L17 17M17 2L2 17M1 5L5 1M4 8L8 4M7 11L11 7" stroke="#818481" stroke-width="2.8" stroke-linecap="round"/><path d="M18 0L12 7L16 10L21 4" fill="#818481"/></g>'
def dots(y,gid):
    return f'<g id="{gid}">'+''.join(f'<circle cx="{x}" cy="{y}" r="2.7" fill="#9FB2BE"/>' for x in (532,540,548))+'</g>'
def tags(y,labels,gid):
    s=f'<g id="{gid}" clip-path="url(#TagsClip)">';x=119
    for i,(v,w) in enumerate(labels):
        s+=f'<g id="{gid}-{i}">'+rect(x,y,w,27,'#EFEFEF',13)+text(x+8,y+20,'#'+v,18,color='#555555')+'</g>';x+=w+4
    return s+'</g>'
def badge(y,opened,gid,up=False):
    s=f'<g id="{gid}">'+rect(119,y,123 if opened else 95,30,'#E8F5DB' if opened else '#F7DEDE',15)+f'<circle cx="133" cy="{y+15}" r="6" fill="'+('#7EAD54' if opened else '#CC5146')+'"/>'
    s+=text(147,y+22,'Open Now' if opened else 'Closed',18)
    s+=text(247 if opened else 219,y+22,'Close at 23:59' if opened else 'Further information',17,color='#555555')
    x=370 if opened else 382
    s+=f'<path d="M{x} {y+(17 if up else 12)}L{x+6} {y+(10 if up else 19)}L{x+12} {y+(17 if up else 12)}Z" fill="#878787"/></g>'
    return s

def frame(body):
    return image('food-expanded-map-strip.png',0,100,576,15,'MapStrip')+'<g id="VenueListPanel"><path d="M0 142Q0 114 22 114H554Q576 114 576 142V970H0Z" fill="#FFFFFF"/><g id="PanelHandle">'+rect(238.5,130,100,7.5,'#31917D',2)+'</g>'+body+'</g>'+header()
def write(name,title,body,desc):
    defs='<defs><clipPath id="TagsClip"><rect x="0" y="0" width="508" height="970"/></clipPath></defs>'
    (OUT/name).write_text('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="970" viewBox="0 0 576 970" fill="none"><title>'+escape(title)+'</title><desc>'+escape(desc)+'</desc>'+defs+rect(0,0,576,970)+body+'</svg>')

# Expanded list viewport. Positions and visible truncation follow native evidence.
s=''
for i,y,asset in [(1,172,'food-thumb-soup.png'),(2,399,'food-thumb-taobin.png'),(3,536,'food-thumb-freshup.png'),(4,724,'food-thumb-sakura-full.png'),(5,911,'food-thumb-fifth-partial.png')]:
    s+=f'<g id="VenueCard{i}">'+rect(28,y,64,64,rx=8,stroke='#E5E5E5')+image(asset,29,y+1,63,44 if i==5 else 63,f'VenueLogo{i}')+text(119,y+21,'VA210 Vending Machine',22,700)
    s+=icon(122,y+35,f'VenueType{i}')+text(151,y+51,'P/F, Block VA · Vending Machine',20.5,color='#484848')
    if i<5:s+=badge(y+68,True,f'OpeningHours{i}',up=i==1)+dots(y+(86 if i==1 else 65),f'VenueMenu{i}')
    if i==1:
        s+='<g id="ExpandedVAHours"><circle cx="131" cy="295" r="9" stroke="#8A8A8A" stroke-width="2.5"/><path d="M131 289V295L136 298" stroke="#8A8A8A" stroke-width="2"/>'+text(151,299,'Mon - Sun, public holiday:   00:00 - 23:59',14,color='#646464')+'</g>'+tags(326,[('Chinese Soup',137),('Snacks',84),('Bottled Herbal Tea',187)],'VATags')
    elif i==3:s+=tags(651,[('Halal Certified Snacks',203)],'FreshTags')
    elif i==4:s+=tags(839,[('Chicken Breast',146),('Japanese Snacks',169),('Desserts',110)],'SakuraTags')
    s+='</g>'
s+='<path d="M0 375H576M0 512H576M0 699H576M0 887H576" stroke="#DADADA" stroke-width="1.4"/>'
write('food-sheet-expanded.svg','Food — Expanded list viewport',frame(s),'Observed S-FOOD-SHEET-EXPANDED from food-165435-list-sheet-expanded.png. Native editable labels, shapes and controls; genuine public logo crops and 15px map strip only are raster, converted to sRGB. Pointer/hover omitted. Fifth card and clipped tags match visible bounds. This is not the entire venue list or proof of continuous scrolling. Fonts/icons approximate.')

for expanded in (False,True):
    s=''
    for i,y,name,asset,loc,sub in [(1,155,'Communal Student Restaurant','food-thumb-communal.png','4/F, Communal Building','· Chinese Restaurant'),(2,372,'Gourmet Shop','food-thumb-gourmet.png','P/F, Shaw Amenities Building','· Take-away shop'),(3,588,'H Café','food-thumb-hcafe.png','P/F, Block FGHJ Courtyard · Cafe',None)]:
        s+=f'<g id="VenueCard{i}">'+rect(28,y,64,64,rx=8,stroke='#E5E5E5')+image(asset,29,y,63,63,f'VenueLogo{i}')+text(119,y+21,name,22,700)+icon(122,y+35,f'VenueType{i}')+text(151,y+51,loc,20.5,color='#484848')
        if sub:s+=text(109,y+79,sub,20.5,color='#484848')
        by=y+(96 if sub else 67);s+=badge(by,False,'HCAFEHours' if i==3 else f'OpeningHours{i}',up=expanded and i==3)
        s+=dots(y+(129 if i==3 and expanded else 94 if i==3 else 111),f'VenueMenu{i}')
        if i==1:s+=tags(299,[('Restaurant',113),('Asian Cuisine',137),('Cantonese Cuisine',189)],'CommunalTags')
        elif i==2:s+=tags(515,[('Cafe / Kiosk',125),('Western Cuisine',160),('Baked Rice',125)],'GourmetTags')
        else:
            if expanded:
                s+='<g id="HCAFEHoursExpanded"><circle cx="131" cy="708" r="9" stroke="#8A8A8A" stroke-width="2.5"/><path d="M131 702V708L136 711" stroke="#8A8A8A" stroke-width="2"/>'
                for yy,day,hours in [(706,'Mon - Fri:','08:00 - 22:00'),(727,'Sat:','08:00 - 18:00'),(748,'Sun, public holiday:','10:00 - 18:00')]:s+=text(151,yy,day,14,color='#555555')+text(329,yy,hours,14,color='#555555')
                s+='</g>'
            s+=tags(771 if expanded else 701,[('Cafe / Kiosk',125),('American Cuisine',168),('Western Cuisine',162)],'HCAFETags')
            oy=812 if expanded else 743
            s+='<g id="OnlineOrder">'+rect(119,oy,217,50,rx=25,stroke='#D3D3D3')+f'<g transform="translate(144,{oy+15})"><path d="M8 9L14 3C20 -3 27 4 21 10L15 16M13 11L7 17C1 23 -6 16 0 10L6 4" stroke="#58AF9C" stroke-width="3" stroke-linecap="round"/><path d="M7 10L14 3" stroke="#58AF9C" stroke-width="3"/></g>'+text(176,oy+33,'Online Order',20,color='#494949')+f'<path d="M296 {oy+31}L304 {oy+21}M295 {oy+21}H304V{oy+30}" stroke="#7D7D7D" stroke-width="2.5"/></g>'
        s+='</g>'
    hy=902 if expanded else 832
    s+='<g id="HomantinPartial">'+rect(26,hy,69,69,'#DEDEDE',12)+text(60,hy+48,'H',35,anchor='middle')+text(119,hy+21,'Homantin Hall Canteen',22,700)+icon(122,hy+35,'HomantinType')+text(151,hy+51,'G/F, Student Residence Halls · Cafe',20.5,color='#484848')
    if not expanded:s+=badge(hy+68,False,'HomantinHours')+dots(hy+67,'HomantinMenu')
    s+='</g><path d="M0 347H576M0 563H576M0 '+str(880 if expanded else 810)+'H576" stroke="#DADADA" stroke-width="1.4"/>'
    body=frame(s)
    source='food-165455-h-cafe-hours-expanded.png' if expanded else 'food-165444-list-scrolled-h-cafe.png'
    desc=f'Observed H Cafe viewport from {source}. Native editable venue labels, statuses, hours, tags and controls. Public logo crops and map strip are raster only. Cursor/hover omitted. Visible partial Homantin card retained, no unseen venues invented. Closed/hours are captured labels, not live business data. Fonts/icons approximate.'
    write('food-hcafe-hours.svg' if expanded else 'food-hcafe-list.svg','Food — H Café hours' if expanded else 'Food — H Café list',body,desc)
    if expanded:
        prompt='<g id="PromptDim">'+rect(72,361,433,304,'#000000')+'</g>'
        for name,x,y,w,h in [('DismissTop',0,0,576,361),('DismissBottom',0,665,576,305),('DismissLeft',0,361,72,304),('DismissRight',505,361,71,304)]:
            prompt+='<g id="'+name+'">'+rect(x,y,w,h,'#000000')+'</g>'
        prompt=prompt.replace('fill="#000000"','fill="#000000" fill-opacity="0.4"')
        prompt+='<g id="OrderPrompt">'+rect(72,361,433,304,rx=16)+text(130,415,'This will take you to a third-party',21)+text(130,442,'website URL:',21)+text(130,498,'https://odoui1.azurewebsites.net/',21)+text(130,525,'shop?poiId=795&se...',21)
        prompt+='<g id="OpenExternalUnobserved">'+rect(103,574,371,60,'#258BD6',3)+text(288,614,'Open',28,700,'#FFFFFF',anchor='middle')+'</g></g>'
        write('food-order-prompt.svg','Food — Online Order external link prompt',body+prompt,desc+' Prompt overlay from food-165505-online-order-external-link-prompt.png. Visible truncated public URL copied as displayed. Open is intentionally unwired: external destination not observed and no ordering performed. Outside-mask dismissal was observed. This full-screen state preserves the exact H Cafe background.')
print('Built four Food states and six public raster crops.')
