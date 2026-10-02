"""Editable finite Payment Month/Events/Week reconstruction from Oct3 Computer Use.

Private history/class values remain synthetic DEMO; mode controls only follow
observed context. This does not implement arbitrary records or global state rules.
"""
from pathlib import Path
from copy import deepcopy
import json,hashlib,xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[2];S=R/'design/polyulife';N='http://www.w3.org/2000/svg';E.register_namespace('',N);tag=lambda n:f'{{{N}}}{n}'
base=E.parse(S/'calendar-oct3-payment.svg').getroot();find=lambda r,id:next(v for v in r.iter() if v.get('id')==id)
def el(parent,kind,**attrs):return E.SubElement(parent,tag(kind),{k.replace('_','-'):str(v) for k,v in attrs.items()})
def text(parent,value,x,y,size=18,fill='#494949',weight=400,anchor='start'):
 v=el(parent,'text',x=x,y=y,fill=fill,font_family='sans-serif',font_size=size,font_weight=weight,text_anchor=anchor);v.text=value;return v
specs=[]
for history in [False,True]:
 root=E.Element(tag('svg'),{'width':'576','height':'1024','viewBox':'0 0 576 1024','fill':'none'});E.SubElement(root,tag('title')).text='Payment Events — '+('synthetic history DEMO' if history else 'observed empty state');E.SubElement(root,tag('desc')).text='From native E-NATIVE-PAYMODE-'+('03' if history else '02')+'. Editable approximate geometry/font/icons. Only observed mode and history transitions connected. Private financial records/dates replaced by wholly synthetic DEMO; no actual transaction content.';el(root,'rect',id='Background',width=576,height=1024,fill='#FFFFFF')
 head=el(root,'g',id='HistoryToggle');el(head,'rect',x=185,y=35,width=200,height=76,fill='#FFFFFF',fill_opacity=0);text(head,'Events',275,73,29,'#141414',700,'middle');el(head,'path',d='M328 63L335 55L342 63Z' if history else 'M328 58L335 66L342 58Z',fill='#555555');text(head,'Hide History' if history else 'Show History',288,102,18,'#555555',600,'middle');el(root,'path',d='M0 118H576',stroke='#D6D6D6')
 mode=el(root,'g',id='ViewMode');el(mode,'path',d='M511 46H576V99H511Q500 99 500 88V57Q500 46 511 46Z',fill='#E59B7B');el(mode,'rect',x=513,y=58,width=24,height=23,stroke='#FFFFFF',stroke_width=3);el(mode,'path',d='M513 64H537M519 67V73M525 67V73',stroke='#FFFFFF',stroke_width=2);el(mode,'circle',cx=534,cy=78,r=9,fill='#E59B7B',stroke='#FFFFFF',stroke_width=3);el(mode,'path',d='M534 72V78L539 81',stroke='#FFFFFF',stroke_width=2)
 cat=deepcopy(find(base,'CalendarCategory'));cat.set('transform','translate(-7,-393)');root.append(cat);f=el(root,'g',id='Filter');el(f,'rect',x=516,y=134,width=44,height=44,rx=9,stroke='#E59B7B',stroke_width=1.5);el(f,'path',d='M527 142H548L541 152V164L535 161V152Z',fill='#E59B7B')
 if not history:
  body=deepcopy(find(base,'NoEvent'));body.set('transform','translate(0,-246)');body.remove(body[-1]);root.append(body);el(root,'path',d='M0 689H49C108 689 128 740 193 720C239 710 267 738 325 726C380 715 402 750 447 750C489 750 549 724 576 688V920H0Z',fill='#EBF8FF')
 else:
  rows=el(root,'g',id='DemoHistoryRows')
  for i in range(6):
   y=190+130.5*i;el(rows,'rect',x=0,y=y,width=576,height=38,fill='#F5F5F5');text(rows,f'Example month {i+1}, 2030 · DEMO',16,y+25,17);text(rows,['Mon','Tue','Wed','Thu','Fri','Sat'][i],58,y+66,17,anchor='middle');text(rows,f'{i+1:02}',58,y+107,27,anchor='middle');el(rows,'rect',x=115,y=y+45,width=434,height=77,rx=9,fill='#F8DEDC');text(rows,f'Example record {chr(65+i)} · DEMO',139,y+92,18,'#141414',600);el(rows,'circle',cx=512,cy=y+82,r=2.5,fill='#A6B7C0');el(rows,'circle',cx=520,cy=y+82,r=2.5,fill='#A6B7C0');el(rows,'circle',cx=528,cy=y+82,r=2.5,fill='#A6B7C0')
  # The cropped sixth row is just synthetic visible structure; no record menu/scroll invented.
  el(root,'g',id='DemoNotice');notice=find(root,'DemoNotice');el(notice,'rect',x=445,y=6,width=116,height=24,rx=5,fill='#FFF0CF');text(notice,'DEMO DATA',503,24,13,'#775313',700,'middle')
 root.append(deepcopy(find(base,'BottomNavigation')));file='calendar-payment-events-'+('history-demo' if history else 'empty')+'.svg';E.ElementTree(root).write(S/file,encoding='unicode',xml_declaration=True);specs.append((file,'S-NATIVE-PAYMENT-HISTORY' if history else 'S-NATIVE-PAYMENT-EVENTS','E-NATIVE-PAYMODE-03' if history else 'E-NATIVE-PAYMODE-02'))
week=E.parse(S/'calendar-week-demo.svg').getroot();week.set('height','1024');week.set('viewBox','0 0 576 1024');week.find(tag('title')).text='Week5 — synthetic DEMO from Payment mode cycle';week.find(tag('desc')).text='From E-NATIVE-PAYMODE-05. Editable Week5 template, synthetic class fields/count/positions retained. Source viewport enlarged970→1024; navigation from observed October2 Payment cycle. Full week grid/scroll/selector/class interactions unimplemented; no universal filter semantics.';find(week,'ViewportClip')[0].set('height','1024');old_nav=find(week,'BottomNavigation');parent=next(v for v in week.iter() if old_nav in list(v));parent.remove(old_nav);parent.append(deepcopy(find(base,'BottomNavigation')));file='calendar-payment-week-demo.svg';E.ElementTree(week).write(S/file,encoding='unicode',xml_declaration=True);specs.append((file,'S-NATIVE-PAYMENT-MODE-WEEK','E-NATIVE-PAYMODE-05'))
p=S/'calendar-payment-modes-sources.json';old={v['state_id']:v for v in json.loads(p.read_text()).get('sources',[])} if p.exists() else {};records=[]
for file,state,eid in specs:
 v={'file':file,'sha256':hashlib.sha256((S/file).read_bytes()).hexdigest(),'state_id':state,'source_evidence_ids':[eid,eid+'-AX'],'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed','limits':['Finite observed Payment mode/history cycle only; complete app/fidelity not_verified.','Private history/class data wholly synthetic DEMO; icons/fonts/geometry approximate, record menus and scroll not implemented.']}
 if state in old and old[state]['sha256']==v['sha256']:v.update(old[state])
 records.append(v)
p.write_text(json.dumps({'sources':records},ensure_ascii=False,indent=2)+'\n')
