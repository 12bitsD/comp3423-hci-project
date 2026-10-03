"""Finite editable Payment detail/Portal samples; all financial values synthetic.

No UI operations or coverage claims. Safe illustration crop must be inspected
before upload; the initial pre-image detail layout is not modeled in this batch.
"""
from pathlib import Path
import json
import hashlib
import xml.etree.ElementTree as E
from PIL import Image
from build_calendar_class_exam_oct2 import (
    new_root, header, group, rect, label, path, hit, image, notice, find, tag)

R = Path(__file__).resolve().parents[2]
D = R / 'design/polyulife'
P = R / 'evidence/2026-10-03-payment-record-native'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def demo_header(r):
    header(r)
    find(r, 'DetailHeader').find(tag('text')).text = 'Example record A · DEMO'


def detail(shown):
    r = new_root('Payment record — synthetic DEMO ' + ('shown' if shown else 'hidden'))
    demo_header(r)
    rect(r, 18, 100, 540, 924, '#FFFFFF', rx=30, stroke='#C5D0D5')
    image(group(r, 'IllustrationRaster'), D/'assets/payment-record-illustration.png', 20, 100, 536, 240)
    label(r, 35, 387, 'Example record A · DEMO', 27, '#242424', font_weight='700')
    label(r, 35, 428, 'Issued on 01-Jan-2030 · DEMO', 20, '#888888')
    label(r, 35, 475, 'The debit note can be settled via the Student', 20)
    label(r, 35, 505, 'Account Portal (SAP) through various', 20)
    label(r, 35, 535, 'payment methods.', 20)
    fields = [('Debit Note No.', 'DEMO-0001'), ('Payment Deadline', '15-Jan-2030 · DEMO'),
              ('Outstanding Amount', 'HKD 123.45 · DEMO' if shown else 'HKD ******'),
              ('Last Updated', '02-Jan-2030 · DEMO')]
    for i, (name, value) in enumerate(fields):
        y = 583 + i*68
        label(r, 35, y, name, 19, '#888888')
        label(r, 35, y+31, value, 23, '#343434', font_weight='600')
    eye = group(r, 'AmountEye')
    hit(eye, 485, 707, 57, 54)
    path(eye, 'M493 732Q509 713 527 732Q509 751 493 732Z', '#777777', 2.5)
    eye.append(E.Element(tag('circle'), {'cx':'510','cy':'732','r':'5','fill':'#777777'}))
    if not shown:
        path(eye, 'M491 716L529 749', '#777777', 3)
    portal = group(r, 'StudentAccountPortal')
    rect(portal, 35, 875, 505, 61, '#FFFFFF', rx=20, stroke='#D7D7D7')
    label(portal, 65, 914, 'Student Account Portal', 22)
    path(portal, 'M502 890H513V901M501 903L513 891', '#888888', 2.5)
    r.find(tag('desc')).text = ('Native loaded-image detail sample from E-NATIVE-PAYREC-05/07; '
        'all financial values/title/dates/identifiers are wholly synthetic DEMO. '
        'Editable approximate geometry/icons/type. Generic public illustration is a raster crop. '
        'Initial pre-image layout, expand image, shown-state exits and arbitrary records unimplemented.')
    return r


def main():
    logo = D/'assets/payment-portal-loading-mark.png'
    Image.open(P/'08-portal-entry-attempt.png').crop((260,532,319,592)).save(logo)
    specs = []
    for shown in (False, True):
        specs.append(('calendar-payment-record-'+('shown' if shown else 'hidden')+'-demo.svg',
                      'S-NATIVE-PAYMENT-RECORD-'+('AMOUNT' if shown else 'DETAIL'),
                      ['E-NATIVE-PAYREC-04'] if shown else ['E-NATIVE-PAYREC-05','E-NATIVE-PAYREC-07'],
                      detail(shown)))
    for kind, state, eid in [('loading','LOADING','08'),('blank','BLANK','09'),('menu','MENU','10')]:
        r = notice(kind, logo)
        find(r,'DetailHeader').find(tag('text')).text = 'Example record A · DEMO'
        for n in r.iter():
            if n.get('id') == 'CloseNotice': n.set('id','ClosePortal')
            if n.get('id') == 'NoticeMore': n.set('id','PortalMore')
            if n.get('id') == 'CancelNoticeMenu': n.set('id','CancelPortalMenu')
            if n.tag == tag('text') and n.text == 'www.polyu.edu.hk/ar/do...':
                n.text = 'www40.polyu.edu.hk/fos...'
        if kind != 'loading':
            label(find(r,'NoticeWebview'),288,123,'Student Account Portal',20,'#202020',text_anchor='middle')
        r.find(tag('title')).text = 'Payment Portal — observed '+kind
        r.find(tag('desc')).text = ('From E-NATIVE-PAYREC-'+eid+'. Synthetic underlying financial title. '
            'Editable approximate browser chrome; blank does not establish service/login success or failure. '
            'Loading transition timing is a demo proxy. External browser/share/copy/refresh not executed or wired.')
        specs.append(('calendar-payment-portal-'+kind+'.svg','S-NATIVE-PAYMENT-PORTAL-'+state,
                      ['E-NATIVE-PAYREC-'+eid],r))
    records=[]
    p=D/'calendar-payment-record-sources.json'
    old={s['state_id']:s for s in json.loads(p.read_text()).get('sources',[])} if p.exists() else {}
    for file,state,eids,r in specs:
        E.ElementTree(r).write(D/file,encoding='unicode',xml_declaration=True)
        item={'file':file,'sha256':sha(D/file),'state_id':state,'source_evidence_ids':eids,
              'dimensions':[576,1024],'status':'prepared_not_imported_not_replayed'}
        if state in old and old[state]['sha256']==item['sha256']: item.update(old[state])
        records.append(item)
    assets=[{'file':'assets/payment-record-illustration.png','sha256':sha(D/'assets/payment-record-illustration.png'),
             'dimensions':[536,240],'source_evidence_id':'E-NATIVE-PAYREC-04',
             'source_kind':'Safe crop from ignored raw native screenshot, before whole-body public masking',
             'normalization_crop_from_raw':[977,0,2047,1898],'normalized_dimensions':[576,1024],
             'crop_in_normalized_xyxy':[20,100,556,340],
             'limits':'Generic photo only; bottom 2px deliberately excluded to avoid adjacent financial text. Raster includes native expand icon; expansion not implemented.'},
            {'file':'assets/payment-portal-loading-mark.png','sha256':sha(logo),'dimensions':[59,60],
             'source_evidence_id':'E-NATIVE-PAYREC-08','source_sha256':sha(P/'08-portal-entry-attempt.png'),
             'crop_xyxy':[260,532,319,592],'source_kind':'Crop from already redacted public native screenshot'}]
    p.write_text(json.dumps({'sources':records,'assets':assets,
        'limits':['First observed record only; finite state sample, complete app not_verified.',
                  'Private financial data wholly synthetic. No business action or login implemented.',
                  'Asynchronous initial image appearance is not modeled; loaded-image reference only.',
                  'Actual public detail body masked; screenshot equality cannot prove body fidelity.']},indent=2)+'\n')
    print(json.dumps({'prepared_sources':len(records),'figma_mutations':0,'native_executions':0}))


if __name__ == '__main__': main()
