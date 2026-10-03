"""Prepare full observed strips for the remaining September30 contexts.

Sources remain fixed historical observations. Import only the strip through
Figma UI and configure clipping/constraints/scrolling there. Does not update
coverage or mutate Figma. Existing original sources remain unchanged.
"""
from pathlib import Path
import copy,json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
def q(t):return '{'+NS+'}'+t
sources=json.loads((D/'room-dates-sources.json').read_text());output=[]
metadata=D/'room-date-context-strip-sources.json';prior={v['label']:v for v in json.loads(metadata.read_text()).get('contexts',[])} if metadata.exists() else {}
for s in sources['frames'][:9]:
 root=ET.parse(D/('room-dates-'+s['label']+'.svg')).getroot();dates=root.find(".//*[@id='DatesObserved20260930']");assert dates is not None
 dates.attrib.pop('clip-path');dates.set('id','DatesHorizontalContent');shift=s['date_strip_offset']
 for child in dates:
  for n in child:
   if 'x' in n.attrib:n.set('x',str(float(n.get('x'))-30-shift))
   if 'y' in n.attrib:n.set('y',str(float(n.get('y'))-100))
 strip=ET.Element(q('svg'),{'width':'658','height':'84','viewBox':'0 0 658 84'})
 ET.SubElement(strip,q('title')).text='Room observed seven-day strip — '+s['label']
 ET.SubElement(strip,q('desc')).text='Historical30Sep–6Oct. Full658px strip, intended516px clipped horizontal Figma viewport; initial offset configured in UI. No live data.'
 ET.SubElement(strip,q('rect'),{'width':'658','height':'84','fill':'#FFFFFF'});strip.append(copy.deepcopy(dates));p=D/('room-dates-'+s['label']+'-strip.svg');ET.ElementTree(strip).write(p,encoding='unicode')
 dates.set('transform','translate(30,100)');dates.set('clip-path','url(#FullDateViewportLocal)');g=ET.Element(q('g'),{'id':'ObservedInitialHorizontalOffset','transform':f'translate({shift},0)'})
 for n in list(dates):dates.remove(n);g.append(n)
 dates.append(g);cp=ET.SubElement(root.find(q('defs')),q('clipPath'),{'id':'FullDateViewportLocal'});ET.SubElement(cp,q('rect'),{'width':'516','height':'84'});root.find(q('desc')).text+=' Full date-strip source for horizontal viewport; UI must configure actual scrolling.';f=D/('room-dates-'+s['label']+'-horizontal.svg');ET.ElementTree(root).write(f,encoding='unicode')
 output.append({'label':s['label'],'root_node_id':s['figma_node_id'],'strip_file':p.name,'strip_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'full_source_file':f.name,'full_source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'initial_offset':-shift,'source_evidence_ids':s['source_evidence_ids'],'status':prior.get(s['label'],{}).get('status','prepared_not_imported'),'actual_edit':prior.get(s['label'],{}).get('actual_edit')})
(D/'room-date-context-strip-sources.json').write_text(json.dumps({'contexts':output,'scope_completion':'not_verified'},ensure_ascii=False,indent=2)+'\n');print('Prepared nine contexts; no Figma completion claimed.')
