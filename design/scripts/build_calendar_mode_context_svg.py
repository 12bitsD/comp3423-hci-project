"""Copy public observed mode sources for a caller-preserving overlay cycle."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

R = Path(__file__).resolve().parents[2]
D = R / 'design/polyulife'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
records = []
for mode, source, evidence in [
    ('month', 'calendar-sep26.svg', 'E-CALENDAR-MONTH-RETURN'),
    ('events', 'calendar-events-upcoming.svg', 'E-CALENDAR-EVENTS'),
    ('history', 'calendar-events-history.svg', 'E-CALENDAR-HISTORY'),
]:
    root = ET.parse(D / source).getroot()
    root.find(f'{{{NS}}}desc').text += (
        ' Caller-preserving prototype context copy. The September26 selection and public event list '
        'are fixed historical samples, not live data. Overlay-mode navigation configured in Figma '
        'separately. This source does not implement date/filter/event-detail/list-scroll branches.')
    output = D / f'calendar-mode-{mode}-context.svg'
    ET.ElementTree(root).write(output, encoding='unicode')
    records.append({'mode': mode, 'source_svg': source,
                    'source_sha256': hashlib.sha256((D / source).read_bytes()).hexdigest(),
                    'source_evidence_id': evidence, 'output': output.name,
                    'output_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                    'scope': 'Public native sample source, editable text/vector approximation; fixed date/filter.'})
(D / 'calendar-mode-context-assets.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
