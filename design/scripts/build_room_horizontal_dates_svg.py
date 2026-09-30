"""Prepare the full observed date strip for Figma horizontal scrolling.
UI must configure its516px viewport and Tuesday initial scroll position.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
def q(s):return '{'+NS+'}'+s
for label,selected,initial in [('tuesday','Tue',-142),('tuesday-reversed','Tue',0)]:
 source=D/('room-dates-'+('tuesday-available' if label=='tuesday' else 'tuesday-reversed')+'.svg');root=ET.parse(source).getroot();dates=root.find(".//*[@id='DatesObserved20260930']");dates.attrib.pop('clip-path');dates.set('id','DatesHorizontalContent')
 # Normalise every date to full strip coordinates: DateToday rect0,y12.
 oldshift=-142 if label=='tuesday' else 0
 for child in dates:
  for n in child:
   if 'x' in n.attrib:n.set('x',str(float(n.get('x'))-30-oldshift))
   if 'y' in n.attrib:n.set('y',str(float(n.get('y'))-100))
 strip=ET.Element(q('svg'),{'width':'658','height':'84','viewBox':'0 0 658 84'});title=ET.SubElement(strip,q('title'));title.text='Room seven observed dates — Tuesday selected';desc=ET.SubElement(strip,q('desc'));desc.text='All seven observed September30 date labels. Import658x84 frame, then set516px clipped horizontal viewport; contentLeft/Top constraints. Tuesday initial offset must be configured via Figma UI. Not a live rolling week.';ET.SubElement(strip,q('rect'),{'width':'658','height':'84','fill':'#FFFFFF'});strip.append(ET.fromstring(ET.tostring(dates)));ET.ElementTree(strip).write(D/'room-dates-tuesday-strip.svg',encoding='unicode')
 dates.set('transform',f'translate(30,100)');dates.set('clip-path','url(#FullDateViewportLocal)');content=ET.Element(q('g'),{'id':'ObservedInitialHorizontalOffset','transform':f'translate({initial},0)'})
 for n in list(dates):dates.remove(n);content.append(n)
 dates.append(content);cp=ET.SubElement(root.find(q('defs')),q('clipPath'),{'id':'FullDateViewportLocal'});ET.SubElement(cp,q('rect'),{'width':'516','height':'84'})
 root.find(q('desc')).text+=' Full date strip provided for true horizontal viewport; initial offset only describes the observed snapshot, actual scroll initialization configured separately in Figma.'
 ET.ElementTree(root).write(D/('room-dates-'+label+'-horizontal.svg'),encoding='unicode')
print('Prepared full date strip and two current-state source snapshots.')
