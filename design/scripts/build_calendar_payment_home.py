"""Build a finite DEMO Home caller from the observed Oct3 Payment roundtrip.

Personal body data are inherited synthetic examples, not native records.
This source does not imply continuous scroll or universal Calendar persistence.
"""
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
source=ET.parse(ROOT/'design/polyulife/home-demo-scrolled.svg').getroot()
source.set('height','1024');source.set('viewBox','0 0 576 1024')
source.find(f'{{{NS}}}title').text='Home — DEMO My Exam — retained Payment Calendar caller'
source.find(f'{{{NS}}}desc').text='Editable finite source for S-NATIVE-OCT3-HOME-CALLER, E-NATIVE-OCT3-PAYMENT-06. Public icon positions adjusted to observed normalized fullscreen viewport576x1024. Private greeting, count, exam dates/time/course/room and bottom sheet content are wholly synthetic DEMO. Home Calendar reentry is observed only for October/month/Oct2/Payment. No universal Calendar target, continuous scroll, card interaction or other feature behavior asserted.'
byid=lambda root,id:next(e for e in root.iter() if e.get('id')==id)
byid(source,'ViewportClip')[0].set('height','1024');byid(source,'HomeContentClip')[0].set('height','820')
body=next(e for e in source.iter() if e.get('clip-path')=='url(#HomeContentClip)')
body.remove(byid(source,'DemoClassCard'))
for e in list(body):
 if e.get('id')=='Features':e.set('transform','translate(0,-162)')
 elif e.get('id')=='DemoExamCards':e.set('transform','translate(0,-170)')
 elif e.tag in [f'{{{NS}}}text',f'{{{NS}}}rect']:e.set('transform','translate(0,-170)')
byid(source,'BottomSheet').set('transform','translate(0,10)')
preview=byid(source,'PublicNewsPreview')
for e in list(preview):preview.remove(e)
ET.SubElement(preview,f'{{{NS}}}text',{'x':'44','y':'911','font-family':'sans-serif','font-size':'16','fill':'#929D96'}).text='DEMO public content preview'
view=next(e for e in source.iter() if e.get('clip-path')=='url(#ViewportClip)')
for e in list(view):
 if e.tag==f'{{{NS}}}rect' and e.get('height')=='970':e.set('height','1024')
oldnav=byid(source,'BottomNavigation');view.remove(oldnav)
nav=deepcopy(byid(ET.parse(ROOT/'design/polyulife/calendar-oct3-payment.svg').getroot(),'BottomNavigation'))
cal=byid(nav,'NavCalendar')
for e in list(cal):
 if e.tag==f'{{{NS}}}circle':cal.remove(e)
 elif e.get('stroke'):e.set('stroke','#9FB0BA')
home=byid(nav,'NavHome');home.insert(0,ET.Element(f'{{{NS}}}circle',{'cx':'58','cy':'946','r':'22','fill':'#F2F9B4'}))
for e in home:
 if e.get('stroke'):e.set('stroke','#414141')
 if e.tag==f'{{{NS}}}text':e.set('fill','#414141')
for id,x in [('NavHome','0'),('NavCalendar','115')]:
 byid(nav,id).insert(0,ET.Element(f'{{{NS}}}rect',{'x':x,'y':'920','width':'115','height':'104','fill':'#FFFFFF','fill-opacity':'0'}))
view.append(nav)
ET.ElementTree(source).write(ROOT/'design/polyulife/calendar-oct3-payment-home-demo.svg',encoding='unicode',xml_declaration=True)
