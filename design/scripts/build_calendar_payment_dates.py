"""Editable finite Payment date/month samples from actual native Oct3 evidence.

Calendar day structure follows observed October/November grids. Only recorded
transitions will be wired in Figma; generated cells do not imply working dates.
"""
from pathlib import Path
from copy import deepcopy
import calendar,json,hashlib
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2];S=R/'design/polyulife';NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
base=ET.parse(S/'calendar-oct3-payment.svg').getroot();byid=lambda root,id:next(e for e in root.iter() if e.get('id')==id)
specs=[(10,3,'S-NATIVE-OCT3-PAYMENT-DAY3','calendar-payment-oct3.svg','E-NATIVE-PAYMENT-DATES-01'),(10,4,'S-NATIVE-OCT3-PAYMENT-DAY4','calendar-payment-oct4.svg','E-NATIVE-PAYMENT-DATES-02'),(11,1,'S-NATIVE-OCT3-PAYMENT-NOV','calendar-payment-nov1.svg','E-NATIVE-PAYMENT-DATES-04'),(10,1,'S-NATIVE-OCT3-PAYMENT-OCT1','calendar-payment-oct1.svg','E-NATIVE-PAYMENT-DATES-05')]
metadata_path=S/'calendar-payment-dates-sources.json'
old_records={v['state_id']:v for v in json.loads(metadata_path.read_text()).get('sources',[])} if metadata_path.exists() else {}
records=[]
for month,day,state,file,eid in specs:
 root=deepcopy(base);root.find(f'{{{NS}}}title').text=f'Calendar Payment — {calendar.month_name[month]}{day} observed empty date';root.find(f'{{{NS}}}desc').text=f'Editable vectors derived from {eid}, state{state}. Fixed actual2026 date and Payment/No event sample. Geometry/font/icon approximate, private markers omitted. Only observed finite cycle controls will be connected; other days/filters/modes/Home contexts not implemented by this SVG.'
 byid(root,'MonthHeader').find(f'{{{NS}}}text').text=calendar.month_name[month]
 grid=byid(root,'CalendarGrid');outline=grid[0];week=byid(root,'WeekdayHeader');grid[:]=[outline,week];weeks=calendar.Calendar(0).monthdatescalendar(2026,month);rows=len(weeks);outline.set('height',str(55+57.2*rows));byid(root,'CalendarViewport')[0].set('height',str(55+57.2*rows))
 for row,dates in enumerate(weeks):
  for col,date in enumerate(dates):
   idx=row*7+col;x=68+73.5*col;y=215+57.2*row;is_month=date.month==month;g=ET.SubElement(grid,f'{{{NS}}}g',{'id':f'Day{date.day}' if is_month else f'AdjacentDay{idx}'});ET.SubElement(g,f'{{{NS}}}rect',{'x':str(x-36.5),'y':str(y-41),'width':'73','height':'57','fill':'#FFFFFF','fill-opacity':'0'})
   selected=is_month and date.day==day
   if selected:ET.SubElement(g,f'{{{NS}}}rect',{'x':str(x-23.5),'y':str(y-39),'width':'47','height':'47','rx':'16','fill':'#31917D'})
   ET.SubElement(g,f'{{{NS}}}text',{'x':str(x),'y':str(y),'fill':'#FFFFFF' if selected else '#4A4A4A' if is_month else '#D9DEE2','font-family':'sans-serif','font-size':'24','font-weight':'500' if selected else '400','text-anchor':'middle'}).text=str(date.day)
 import datetime
 byid(root,'SelectedDay').find(f'{{{NS}}}text').text=datetime.date(2026,month,day).strftime('%A, %B ')+str(day)
 if rows>5:
  byid(root,'SelectedDay').set('transform','translate(0,57.2)');byid(root,'NoEvent').set('transform','translate(0,57.2)')
 # Larger arrow hotspots use only observed controls; available source-cell areas are editable.
 for id,x in [('PreviousMonth',85),('NextMonth',457)]:byid(root,id).insert(0,ET.Element(f'{{{NS}}}rect',{'x':str(x),'y':'40','width':'38','height':'60','fill':'#FFFFFF','fill-opacity':'0'}))
 p=S/file;ET.ElementTree(root).write(p,encoding='unicode',xml_declaration=True);records.append({'file':file,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'state_id':state,'dimensions':[576,1024],'source_evidence_ids':[eid,eid+'-AX'],'status':'prepared_not_imported_not_replayed','limits':['Finite observed Payment dates/month cycle; other controls and full app/fidelity not_verified.','Editable vectors approximate geometry/font/glyph; private markers omitted.']})
for index,record in enumerate(records):
 prior=old_records.get(record['state_id'])
 if prior and prior.get('sha256')==record['sha256']:
  records[index]={**record,**prior}
metadata_path.write_text(json.dumps({'sources':records},ensure_ascii=False,indent=2)+'\n')
