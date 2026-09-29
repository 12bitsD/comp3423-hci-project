"""Reconstruct only the observed Room date and Sunday result range.
Figma UI must configure the date/list viewports and prototype connections.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife'
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
def q(t):return '{'+NS+'}'+t
def node(t,**kw):return ET.Element(q(t),{k.replace('_','-'):str(v) for k,v in kw.items()})
def rect(x,y,w,h,fill,**kw):return node('rect',x=x,y=y,width=w,height=h,fill=fill,**kw)
def text(x,y,s,size=17,color='#404040',weight=400,anchor='middle'):
 t=node('text',x=x,y=y,fill=color,font_family='sans-serif',font_size=size,font_weight=weight,text_anchor=anchor);t.text=s;return t
def dates(selected='Tue',shift=0,strip=False):
 g=node('g',id='DatesHorizontal' if strip else 'DatesShifted')
 if strip:g.append(rect(0,0,658,84,'#FFFFFF'))
 days=[('Today','28-Sep',40),('Tue','29-Sep',136),('Wed','30-Sep',230),('Thu','01-Oct',323),('Fri','02-Oct',416),('Sat','03-Oct',510),('Sun','04-Oct',603)]
 for day,date,x in days:
  x+=shift;row=node('g',id='Date-'+day);row.append(rect(x-40,12,80,67,'#54B39F' if day==selected else '#FFFFFF',rx=9));color='#FFFFFF' if day==selected else '#404040'
  row.extend([text(x,40,day,color=color,weight=600 if day==selected else 400),text(x,63,date,color=color,weight=600 if day==selected else 400)]);g.append(row)
 return g
base=ET.parse(D/'room-available.svg').getroot()
def clean(root,title,description):
 root.find(q('title')).text=title;root.find(q('desc')).text=description
 root.attrib['fill']='none'
def write(root,name):ET.ElementTree(root).write(D/name,encoding='unicode',xml_declaration=False)
# Standalone asset for replacing the old clipped date group in existing Available.
strip=node('svg',width=658,height=84,viewBox='0 0 658 84');strip.append(dates(strip=True));write(strip,'room-date-strip.svg')
for mode in ['transition','empty','all']:
 root=ET.fromstring(ET.tostring(base));old=root.find(".//*[@id='Dates']");idx=list(root).index(old);root.remove(old)
 dateGroup=dates('Sun',shift=-142);dateGroup.set('transform','translate(30,100)');dateGroup.set('clip-path','url(#SundayDatesClip)')
 # Clip is in local coordinates; partial Tuesday and full Sunday reproduce observed shifted strip.
 defs=root.find(q('defs'));cp=node('clipPath',id='SundayDatesClip');cp.append(rect(0,0,516,84,'#FFF'));defs.append(cp);root.insert(idx,dateGroup)
 if mode!='transition':root.find(".//*[@id='ResultDate']/"+q('text')).text='04-Oct (Sun)'
 results=root.find(".//*[@id='Results']");slots=root.find(".//*[@id='Slots']")
 if mode!='transition':results.remove(slots)
 if mode=='empty':
  g=node('g',id='NoAvailableRoom');g.append(node('path',d='M269 674L308 713M308 674L269 713',stroke='#319987',stroke_width=10,stroke_linecap='round'))
  g.extend([text(288,768,'No available room',24,'#555555',700),text(288,800,'Please search another room.',21,'#A1B2BA',500)]);results.append(g)
 if mode=='all':
  fa=root.find(".//*[@id='Filter-All']");fa.find(q('rect')).set('fill','#54B39F');fa.find(q('text')).set('fill','#FFFFFF');fa.find(q('text')).set('font-weight','600')
  fv=root.find(".//*[@id='Filter-Available']");fv.find(q('rect')).set('fill','#FFFFFF');fv.find(q('rect')).set('stroke','#DCDCDC');fv.find(q('rect')).set('stroke-width','1.5');fv.find(q('text')).set('fill','#090909');fv.find(q('text')).set('font-weight','400')
  g=node('g',id='SlotsScrollContent');g.append(rect(26,426,524,940,'#FFFFFF'))
  for i in range(26):
   minutes=510+i*30;end=minutes+30;label=f'{minutes//60:02d}:{minutes%60:02d}-{end//60:02d}:{end%60:02d}';x=27 if i%2==0 else 295;y=434+(i//2)*70
   slot=node('g',id='UnavailableSlot-'+label.replace(':',''));slot.append(rect(x,y,255,55,'#FFD0D2',rx=8,stroke='#DDDFDC',stroke_width=1.5));slot.append(node('circle',cx=x+67,cy=y+27.5,r=4.7,fill='#BA3D24'));slot.append(text(x+83,y+34,label,17,'#080808',anchor='start'));g.append(slot)
  # Only the top 22px of the next row was visible; no unseen labels are invented.
  g.extend([rect(27,1344,255,22,'#FFD0D2',rx=8),rect(295,1344,255,22,'#FFD0D2',rx=8)]);results.append(g)
 clean(root,'Room — Sunday '+mode,'Editable reconstruction from native Sunday screenshots. Fixed observed date/data; cursor omitted. Fonts/icons approximate. List content ends at last observed partial row, not verified native end. Transition delay is configured separately as demonstration timing.')
 write(root,'room-sunday-'+mode+'.svg')
# Source matching existing Available after replacing Dates with an interactive horizontal viewport.
root=ET.fromstring(ET.tostring(base));old=root.find(".//*[@id='Dates']");idx=list(root).index(old);root.remove(old);g=dates(strip=True);g.set('transform','translate(30,100)');root.insert(idx,g)
clean(root,'Room — Available with observed date strip','Editable original Available plus seven observed dates. In Figma configure DatesHorizontal as 516x84 clipped horizontal frame at (30,100); content width658. Native full date bounds unverified.')
write(root,'room-available-scroll.svg')
print('Wrote date strip, Available scroll source, and three Sunday frames.')
