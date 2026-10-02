"""Build source-derived fixed filter states, preserving applied caller background."""
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as E,json,hashlib
D=Path(__file__).resolve().parents[1]/'polyulife';ns='http://www.w3.org/2000/svg';E.register_namespace('',ns);E.register_namespace('xlink','http://www.w3.org/1999/xlink');tag=lambda n:'{'+ns+'}'+n
applied=E.parse(D/'calendar-sep28.svg').getroot();applied.find(tag('desc')).text+=' Global caller variant; native return/source combinations not completely observed.'
E.ElementTree(applied).write(D/'calendar-global-acad.svg',encoding='unicode')
records=[]
for mode,bg,out,eid in [('all','default','calendar-global-all-default.svg','E-CALENDAR-FILTER-ALL'),('none','default','calendar-global-none-default.svg','E-CALENDAR-FILTER-NONE'),('acad','default','calendar-global-acad-default.svg','E-CALENDAR-FILTER-ACAD'),('acad','acad','calendar-global-acad-applied.svg','E-CALENDAR-FILTER-PERSIST'),('all','acad','calendar-global-all-applied.svg','E-CALENDAR-FILTER-ALL')]:
 base=E.parse(D/('calendar-default-demo.svg' if bg=='default' else 'calendar-global-acad.svg')).getroot()
 panel=E.parse(D/f'calendar-filter-{mode}.svg').getroot();overlay=next(x for x in panel if x.attrib.get('id')=='FilterOverlay');base.append(deepcopy(overlay))
 base.find(tag('title')).text=f'Calendar filter {mode}; applied {bg} background'
 base.find(tag('desc')).text=f'Finite reconstruction of recorded filter panel ({eid}) over the retained applied {bg} background. Private event values/patterns synthetic or omitted. Panel and geometry approximate; backdrop composited. No dirty-draft Apply None or independent Class/Exam/Payment result invented. Global caller retention is a Figma implementation.'
 path=D/out;E.ElementTree(base).write(path,encoding='unicode');records.append({'file':out,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'draft':mode,'applied_background':bg,'source_evidence_ids':[eid],'limits':['Fixed observed drafts; other categories and Apply None unimplemented.','Synthetic private background; not a full native pixel reproduction.']})
(D/'calendar-global-filter-sources.json').write_text(json.dumps({'sources':records},ensure_ascii=False,indent=2)+'\n')
