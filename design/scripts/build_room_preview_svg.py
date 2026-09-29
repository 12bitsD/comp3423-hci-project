"""Editable Room Preview reconstruction. Public sources are recorded in room-preview-assets.json.
The web body covers only the native observed range; unseen lower tables are not a claimed native observation.
"""
from pathlib import Path
from base64 import b64encode
from xml.sax.saxutils import escape
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';A=D/'assets'
def t(x,y,s,n=24,w=400,c='#101010',anchor=None):
 return f'<text x="{x}" y="{y}" font-family="Arial" font-size="{n}" font-weight="{w}" fill="{c}"'+(f' text-anchor="{anchor}"' if anchor else '')+'>'+escape(s)+'</text>'
def rect(x,y,w,h,c='#FFFFFF',rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}"/>'
def im(name,x,y,w,h,gid):return f'<g id="{gid}"><image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" xlink:href="data:image/png;base64,{b64encode((A/name).read_bytes()).decode()}"/></g>'
def group(name,s):return f'<g id="{name}">{s}</g>'
def write(name,title,s,w=576,h=970):
 (D/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{escape(title)}</title><desc>Observed Room Preview viewport reconstruction. Editable text and vector controls; public photographs and wordmarks are raster. Native source screenshots define layout. Fonts/icons approximate; cursor omitted. Continuous-body extent is limited to observed photographs, not the complete official webpage. Configure scrolling and carousel component in Figma UI.</desc>{s}</svg>')
def chrome(loading=False):
 s=group('UnderlyingRoomHeader',rect(0,0,576,100)+t(288,75,'Room Finder',27,anchor='middle')+'<path d="M34 57L27 65L34 72" fill="none" stroke="#222" stroke-width="7" stroke-linecap="round"/>')
 s+=group('WebTop',rect(8,76,561,76,'#F7F9F7',24)+rect(8,110,561,42,'#F7F9F7')+rect(8,141,561,11,'#DFDFDF')+group('ClosePreview',rect(17,88,50,49,'#F7F9F7')+'<path d="M32 104L52 124M52 104L32 124" fill="none" stroke="#303330" stroke-width="3.5" stroke-linecap="round"/>')+(t(288,123,'Room Search',23,anchor='middle') if not loading else '')+group('MoreMenu',rect(500,88,53,47,'#F7F9F7')+''.join(f'<circle cx="{x}" cy="113" r="4.2" fill="#333"/>' for x in [515,528,541])))
 s+=group('BrowserToolbar',rect(0,879,576,91,'#F7F9F7',25)+rect(0,879,576,42,'#F7F9F7')+'<path d="M8 878.5H570" stroke="#BBB"/>'+group('BrowserBackUnobserved','<path d="M55 910L42 924L55 938" stroke="#B3B5B3" stroke-width="4" stroke-linecap="round" fill="none"/>')+group('BrowserForwardUnobserved','<path d="M111 910L124 924L111 938" stroke="#B3B5B3" stroke-width="4" stroke-linecap="round" fill="none"/>')+'<rect x="151" y="895" width="388" height="60" rx="13" fill="#FFFFFF" stroke="#9D9D9D"/>'+group('Address',t(200,934,'www.polyu.edu.hk/learn...',22,c='#777')+'<rect x="175" y="923" width="13" height="10" rx="1.5" fill="#202020"/><path d="M178 923V920a4 4 0 0 1 8 0v3" transform="translate(0,0)" fill="none" stroke="#202020" stroke-width="2"/>')+group('ReloadUnobserved','<path d="M524 925A12 12 0 1 1 510 916M510 910L518 916L511 922" stroke="#222" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'))
 return s
PARA=['Computers and audio-visual equipment are','provided in the general teaching classrooms','(GT) and lecture theatres (LT) in support of a','modern interactive teaching technology','environment. You can teach face-to-face as','well as remotely at the same time using the','facilities in GT/LT. Your lecture can be recorded','also using the software / VC tools in classroom','desktop computer. You can check the AV/IT','facilities available in classrooms and lecture','theatres via the AV/IT Facilities Search Engine','below. Request for support can be directed to','the hotline at ']
def photo(which):
 s=im('room-preview-photo-'+('one' if which==1 else 'two')+'.png',0,0,526,394.5,'ClassroomPhoto')
 s+=group('PreviousUnobserved','<path d="M46 180L30 197L46 214" fill="none" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="3"/>')
 s+=group('NextPhoto' if which==1 else 'NextUnobserved','<rect x="448" y="165" width="60" height="65" fill="#FFF" fill-opacity=".001"/><path d="M478 180L494 197L478 214" fill="none" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="3"/>')
 return s
# Full visible body is deliberately bounded at the last native photograph viewport.
body=rect(8,152,561,1809)
body+=rect(8,152,561,44)+ '<path d="M383 152H569V196H340Z" fill="#A31D3C"/>'+im('room-preview-wordmark.png',398,160,146,28.5,'SiteWordmark')
body+=group('SiteTitle',rect(8,196,561,94)+t(26,241,'Information Technology Services',22,700,c='#383838')+t(26,264,'Office',22,700,c='#383838'))
body+='<defs><clipPath id="BannerCrop"><rect x="8" y="290" width="561" height="370"/></clipPath></defs><g clip-path="url(#BannerCrop)">'+im('room-preview-banner.png',-698.1667,290,1973.3334,370,'BannerPhoto')+'</g>'
body+=group('SectionHeader',rect(8,660,561,60)+ '<path d="M330 660L360 690L355 660M373 660Q374 700 399 711H569V674L535 711H424Q403 691 410 660Z" fill="#F0F0F0"/>'+t(26,759,'Learning and Teaching',37,c='#A50032')+t(26,815,'Technology Support',37,c='#A50032')+'<path d="M26 841H552" stroke="#A50032" stroke-width="2.5"/>')
for i,line in enumerate(PARA):body+=t(26,877+44*i,line,24 if i in (6,7) else 25)
body+=t(188,877+44*12,'2766 6302.',25,700)
body+=group('RoomHeading',t(26,1465,'Room : AG206',37,c='#A50032')+'<path d="M26 1489H552" stroke="#A50032" stroke-width="2.5"/>')
body+=group('CarouselPlaceholder','<g transform="translate(26,1541)">'+photo(1)+'</g>')
base=rect(0,0,576,970)+group('WebScrollContent',body)+chrome()
write('room-preview-top.svg','Room Preview — continuous observed body',base)
# Menu uses the observed top viewport behind an opaque modal mask.
menu=group('MenuDim','<rect width="576" height="970" fill="#000" fill-opacity=".70"/>')
menu+=group('WebMenu',rect(18,640,540,258,'#FFF',20)+'<path d="M18 726H558M18 812H558" stroke="#E6E6E6"/>'+t(288,693,'Open in system browser',28,anchor='middle')+t(288,779,'Share via...',28,anchor='middle')+t(288,865,'Copy link',28,anchor='middle'))
menu+=group('CancelMenu',rect(18,910,540,85,'#FFF',20)+t(288,963,'Cancel',28,c='#FF0800',anchor='middle'))
write('room-preview-menu.svg','Room Preview — browser menu',menu)
load=rect(0,0,576,970)+rect(8,152,561,44)+'<path d="M527 152H569V196H486Z" fill="#A31D3C"/>'+rect(8,196,561,94)+t(26,241,'Information Technology Services',22,700,c='#383838')+t(26,264,'Office',22,700,c='#383838')+rect(8,294,561,32,'#A31D3C')+t(26,425,'Learning and Teaching',37,c='#A50032')+t(26,481,'Technology Support',37,c='#A50032')+'<path d="M26 507H552" stroke="#A50032" stroke-width="2.5"/>'
for i,line in enumerate(PARA):load+=t(26,543+44*i,line,24 if i in (6,7) else 25)
load+=im('room-preview-loading-mark.png',265,538,49,46,'LoadingMark')+chrome(True)
write('room-preview-loading.svg','Room Preview — loading sample',load)
for n in [1,2]:write(f'room-preview-photo-{n}.svg',f'Room Preview photograph {n}',photo(n),526,394.5)
print('Wrote 3 Room Preview screens and 2 carousel component sources.')
