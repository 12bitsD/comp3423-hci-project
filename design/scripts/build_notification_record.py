"""Editable first institutional Notification sample from public native evidence.

File generation only; preserves imported metadata if generated SHA is unchanged.
"""
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as E
import json,hashlib
from PIL import Image
from build_calendar_class_exam_oct2 import new_root,header,group,rect,label,path,hit,image,notice,find,tag,node
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-10-03-notification-record-native';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
TITLE='Upcoming IT Workshops...'

def detail_header(r):
 header(r);g=find(r,'DetailHeader');g.find(tag('text')).text=TITLE;g.find(tag('text')).set('x','288');g.find(tag('text')).set('text-anchor','middle');g.find(tag('text')).set('font-weight','400');g.remove(g.findall(tag('text'))[-1])

def list_view(unread):
 r=new_root('Notification — first public notice '+('unread' if unread else 'read'))
 rect(r,0,0,576,1024,'#F2F2F2');h=group(r,'NotificationHeader');rect(h,0,0,576,100,'#FFFFFF',stroke='#DDDDDD');label(h,288,73,'My Notification',26,'#080808',font_weight='700',text_anchor='middle')
 menu=group(h,'MenuUnverified');hit(menu,12,25,62,65);path(menu,'M25 51H58M25 64H58M25 77H58','#080808',3.5)
 search=group(h,'SearchUnverified');hit(search,491,25,67,65);search.append(node('circle',cx=526,cy=62,r=13,fill='none',stroke='#080808',stroke_width=3.5));path(search,'M536 72L543 80','#080808',3.5)
 rect(r,0,100,576,40,'#F6F6F6');label(r,16,128,'Yesterday',19,'#555555')
 card=group(r,'FirstNoticeCard');rect(card,0,140,576,123,'#FFFFFF');hit(card,14,144,545,117)
 if unread:card.append(node('circle',cx=38,cy=173,r=8.5,fill='#D6EE4E'))
 label(card,61,181,'Upcoming IT Workshops - October',23,'#000000',font_weight='700');label(card,61,209,'16 hours ago',20,'#444444');path(card,'M542 165L548 172L542 179','#DDDDDD',4.5,stroke_linecap='round')
 nav=deepcopy(find(E.parse(D/'calendar-oct3-payment.svg').getroot(),'BottomNavigation'));cal=find(nav,'NavCalendar');cal.remove(cal.find(tag('circle')))
 for n in cal:
  if n.get('stroke'):n.set('stroke','#9FB0BA')
 notif=find(nav,'NavNotification');notif.insert(0,node('circle',cx=395,cy=942,r=18,fill='#F2F9B4'))
 for n in notif:
  if n.get('stroke'):n.set('stroke','#414141')
 if unread:notif.append(node('circle',cx=422,cy=932,r=9,fill='#FF9B9B'))
 hit(cal,145,922,59,74);r.append(nav);return r

def detail(loaded):
 r=new_root('Notification detail — '+('banner loaded' if loaded else 'initial no banner'));detail_header(r);rect(r,18,100,540,924,'#FFFFFF',rx=30,stroke='#C5D0D5')
 off=168 if loaded else 0
 if loaded:
  image(group(r,'BannerRaster'),D/'assets/notification-workshop-banner.png',18,100,540,181)
  expand=group(r,'ExpandBanner');hit(expand,468,203,61,61);expand.append(node('circle',cx=500,cy=235,r=27,fill='#FFFFFF'));path(expand,'M488 226V220H495M505 220H512V226M512 244V250H505M495 250H488V244','#31917D',3)
 label(r,35,152+off,'Upcoming IT Workshops - October',26,'#242424',font_weight='700');label(r,35,197+off,'Posted by ITS on Oct 2nd, 2026',21,'#555555')
 rect(r,35,225+off,506,123,'#F5FBFF');r.append(node('circle',cx=54,cy=246+off,r=9,fill='none',stroke='#9FAFB9',stroke_width=2));label(r,54,251+off,'?',13,'#9FAFB9',text_anchor='middle')
 for j,t in enumerate(['A list of workshops on IT skills for Future of','Work / Research is now ready for students\'','enrolment. Find out more details below.']):label(r,73,254+off+j*27,t,21,'#555555')
 path(r,f'M73 {333+off}H483','#DDDDDD',1)
 rm=group(r,'ReadMore');rect(rm,35,357+off,200,51,'#FFFFFF',rx=26,stroke='#DDDDDD',stroke_width=1.6);path(rm,f'M73 {379+off}L64 {387+off}Q60 {393+off} 65 {395+off}Q70 {396+off} 76 {389+off}M76 {387+off}L83 {380+off}Q87 {374+off} 81 {374+off}Q77 {374+off} 73 {379+off}','#55B4A6',3.2,stroke_linecap='round');label(rm,91,391+off,'Read more',21,'#666666');path(rm,f'M205 {378+off}H215V{388+off}M205 {388+off}L215 {378+off}','#888888',2.5)
 return r

def main():
 banner=D/'assets/notification-workshop-banner.png';Image.open(P/'13-notification-image-expanded.png').crop((0,415,576,609)).save(banner)
 logo=D/'assets/notification-web-loading-mark.png';Image.open(P/'21-loaded-record-read-more.png').crop((258,532,319,594)).save(logo)
 specs=[]
 for unread,eid in [(True,'04'),(False,'15')]:specs.append(('notification-record-list-'+('unread' if unread else 'read')+'.svg','LIST-'+('UNREAD' if unread else 'READ'),[eid],list_view(unread)))
 specs += [('notification-record-detail-initial.svg','DETAIL-NOIMAGE',['05'],detail(False)),('notification-record-detail-loaded.svg','DETAIL-LOADED',['12','16','20','24'],detail(True))]
 r=new_root('Notification banner — expanded');rect(r,0,0,576,1024,'#FFFFFF');image(group(r,'ExpandedBannerRaster'),banner,0,415,576,194);g=group(r,'CloseImage');hit(g,496,121,62,60);path(g,'M513 133L533 153M533 133L513 153','#000000',4.5);specs.append(('notification-record-image-expanded.svg','IMAGE',['13'],r))
 for kind,state,eids in [('loading','WEB-LOADING',['21']),('blank','WEB-BLANK',['07','10','22']),('menu','WEB-MENU',['08'])]:
  r=notice(kind,logo);g=find(r,'DetailHeader');g.find(tag('text')).text=TITLE;g.find(tag('text')).set('x','288');g.find(tag('text')).set('text-anchor','middle');g.find(tag('text')).set('font-weight','400');g.remove(g.findall(tag('text'))[-1])
  for n in r.iter():
   if n.get('id')=='CloseNotice':n.set('id','CloseWeb')
   if n.get('id')=='NoticeMore':n.set('id','WebMore')
   if n.get('id')=='CancelNoticeMenu':n.set('id','CancelWebMenu')
   if n.tag==tag('text') and n.text=='www.polyu.edu.hk/ar/do...':n.text='t.edm.polyu.edu.hk/act...'
  if kind!='loading':label(find(r,'NoticeWebview'),288,123,'Upcoming IT Workshops for Stud...',20,'#202020',text_anchor='middle')
  specs.append(('notification-record-web-'+kind+'.svg',state,eids,r))
 r=E.parse(D/'calendar-oct3-payment.svg').getroot();specs.append(('notification-record-calendar-read.svg','PAYMENT-READ',['18'],r))
 record_path=D/'notification-record-sources.json';old={v['file']:v for v in json.loads(record_path.read_text()).get('sources',[])} if record_path.exists() else {};records=[]
 for file,state,eids,r in specs:
  r.find(tag('title')).text='Notification first institutional notice — '+state;r.find(tag('desc')).text='Finite native notification record reconstruction from2026-10-03 Computer Use. Public institutional text retained; no identity or complete tracking URL. Fonts/icons/geometry approximate; banner and static loading mark raster. Loading and banner transition timing are demo proxies, not measured latency. Blank browser body capture is not service failure proof; AX content differs. Other notices, search/menu/device behavior and complete app not_verified.'
  E.ElementTree(r).write(D/file,encoding='unicode',xml_declaration=True);record={'file':file,'state_id':'S-NATIVE-OCT3-PAYMENT' if state=='PAYMENT-READ' else 'S-NATIVE-NOTICE-'+state,'source_evidence_ids':['E-NATIVE-NOTICE-'+e for e in eids],'sha256':sha(D/file),'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed'}
  if state=='PAYMENT-READ':record['context_variant']='20261003-payment-after-notice-read'
  if file in old and old[file]['sha256']==record['sha256']:record.update(old[file])
  records.append(record)
 assets=[{'file':'assets/notification-workshop-banner.png','sha256':sha(banner),'source_evidence_id':'E-NATIVE-NOTICE-13','crop_xyxy':[0,415,576,609],'dimensions':[576,194],'limits':'Raster institutional illustration; editable control added separately. No private photo/identity.'},{'file':'assets/notification-web-loading-mark.png','sha256':sha(logo),'source_evidence_id':'E-NATIVE-NOTICE-21','crop_xyxy':[258,532,319,594],'dimensions':[61,62],'limits':'Static sampled mark, not rotating native animation.'}]
 record_path.write_text(json.dumps({'sources':records,'assets':assets,'limits':['One notification and finite read-state roundtrip; no arbitrary feed or queries.','No-image to loaded detail and web loading timings are illustrative proxies.','Payment after-read clone initially has only sampled Notification return; other date/mode/home controls not copied or claimed.']},ensure_ascii=False,indent=2)+'\n');print(json.dumps({'prepared_sources':len(records),'figma_mutations':0,'native_executions':0}))
if __name__=='__main__':main()
