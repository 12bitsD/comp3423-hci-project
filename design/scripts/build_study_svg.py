"""Build editable Study, My Courses, QR and synthetic Home design sources.

Uses public screenshot evidence and synthetic private content. Never reads raw
screenshots, application data, credentials or the network. Run with Python 3;
Pillow is only needed to recreate the public decorative Home image crop.
"""
from base64 import b64encode
from pathlib import Path
from shutil import copyfile
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "design/polyulife"
ASSETS = OUT / "assets"
EVIDENCE = ROOT / "evidence/2026-09-28-full-audit"


def text(x, y, value, size=22, weight=400, color="#171717", anchor=None):
    align = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="sans-serif" font-size="{size}" font-weight="{weight}"{align}>{escape(value)}</text>'


def rect(x, y, w, h, fill, rx=0, stroke=None, sw=1):
    border = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{border}/>'


def group(gid, body):
    return f'<g id="{gid}">{body}</g>'


def line(x1, y1, x2, y2, color="#D2D3D8", sw=1.5):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{sw}"/>'


def chevron(x, y, down=False, up=False, color="#515965"):
    if down or up:
        points = f'{x-7},{y-4} {x+7},{y-4} {x},{y+4}' if down else f'{x-7},{y+4} {x+7},{y+4} {x},{y-4}'
        return f'<polygon points="{points}" fill="{color}"/>'
    return f'<path d="M{x-5} {y-9}L{x+6} {y}L{x-5} {y+9}" stroke="{color}" stroke-width="2.2" fill="none"/>'


def bitmap(name, x, y, width, height, gid):
    data = b64encode((ASSETS / name).read_bytes()).decode()
    return group(gid, f'<image x="{x}" y="{y}" width="{width}" height="{height}" preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/>')


def screen(filename, title, source, body, extra='', demo=False):
    desc = (f'Editable interface reconstruction from {source}. Viewport 576x970. '
            'Visible interface text and ordinary controls are editable SVG text and vectors. '
            'Fonts and icons approximate the observed native geometry; pointer shadows are omitted. '
            'SVG import provides no navigation, scrolling, text input, authentication or backend behavior. ')
    if demo:
        desc += ('DEMO: personal names, subject identifiers, coursework, counts, schedules and identity content '
                 'are wholly synthetic examples. No real private body text or image is embedded. '
                 'Personal-page geometry was inspected locally, while shared evidence is intentionally cropped or masked. '
                 'These examples are not evidence of any student record or an observed public page body. ')
    desc += extra
    content = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="970" viewBox="0 0 576 970" fill="none">'
    content += f'<title>{escape(title)}</title><desc>{escape(desc)}</desc>'
    content += '<defs><clipPath id="ViewportClip"><rect width="576" height="970"/></clipPath><clipPath id="HomeContentClip"><rect y="100" width="576" height="820"/></clipPath></defs>'
    content += '<g clip-path="url(#ViewportClip)">' + rect(0, 0, 576, 970, '#FFFFFF') + body + '</g></svg>'
    (OUT / filename).write_text(content)


def demo_badge():
    return group('DemoNotice', rect(444, 7, 116, 25, '#FFF0CF', 6) + text(502, 25, 'DEMO DATA', 14, 700, '#775313', 'middle'))


def header(title, demo=False, menu=False):
    body = rect(.5, .5, 575, 99, '#FFFFFF', stroke='#D1D1D1')
    if menu:
        body += group('Menu', '<path d="M25 53H58M25 65H58M25 77H58" stroke="#151515" stroke-width="3.4" stroke-linecap="round"/>')
        body += group('Search', '<circle cx="526" cy="63" r="13" stroke="#131313" stroke-width="3.5"/><path d="M535 73L542 80" stroke="#131313" stroke-width="3.5" stroke-linecap="round"/>')
    else:
        body += group('Back', '<path d="M35 56L27 65L35 73" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    body += text(288, 75, title, 25 if menu else 27, 700 if menu else 400, anchor='middle')
    if demo:
        body += demo_badge()
    return group('Header', body)


def segment(first, second, selected):
    body = rect(49, 124, 479, 67, '#E5F562', 34)
    body += rect(55 if selected == 0 else 288, 130, 233, 55, '#FFFFFF', 28)
    for index, (label, x) in enumerate([(first,171), (second,405)]):
        body += group('Tab'+label.replace(' ', ''), rect(52+237*index,124,237,67,'#FFFFFF',34).replace('fill="#FFFFFF"','fill="#FFFFFF" fill-opacity="0.001"') + text(x,167,label,25,700 if selected==index else 400,anchor='middle'))
    return group('TabSelector',body)


def info_strip(lines, y=222, height=58):
    body = rect(0,y,576,height,'#F3F3F5')
    for i,s in enumerate(lines): body += text(16,y+35+i*25,s,19,color='#83868C')
    return group('ListInfo',body)


def subject_row(y, code, title, credits='3', expanded=False, gid='Subject', arrow=True):
    lines = title if isinstance(title,list) else [title]
    height = 129+(len(lines)-1)*27
    body = line(41,y,576,y) + text(41,y+49,code,25,700)
    body += rect(41,y+64,126,36,'#E1F2E2',18) + text(104,y+89,credits+' CREDITS',21,anchor='middle')
    for i,s in enumerate(lines): body += text(179,y+87+i*27,s,21,color='#434C5C')
    if arrow: body += group(gid+'NameToggle',rect(514,y+62,35,44,'#FFFFFF').replace('fill="#FFFFFF"','fill="#FFFFFF" fill-opacity="0.001"')+chevron(531,y+78,down=not expanded,up=expanded))
    return group(gid,body),height


def build_study():
    for expanded in [False,True]:
        body = segment('Completed','Requirements',0)+info_strip(['Subject Completed as of 29-Sep-2026'])
        subjects = [
            ('EXM1001','INTRODUCTION TO DESIGN','4',False),
            ('EXM1002',['FOUNDATIONS OF CREATIVE','RESEARCH AND PRACTICE'] if expanded else 'FOUNDATIONS OF CREATIVE...','4',True),
            ('EXM1003','EXPLORING COMMUNITIES','4',False),
            ('EXM1004','SCIENCE AND THE EVERYDAY...','4',True),
            ('EXM1005','COMMUNICATION PRACTICE','4',False),
            ('EXM1006','DEMONSTRATION SUBJECT','4',False),
        ]
        y=280
        for i,(code,title,credits,arrow) in enumerate(subjects):
            row,h=subject_row(y,code,title,credits,expanded=expanded and i==1,gid=f'CompletedSubject{i+1}',arrow=arrow)
            body+=row;y+=h
        body+=rect(559,225,14,156,'#FFFFFF',7,'#EAEAEA',1.5)+header('Study progress',True)
        screen('study-completed-demo'+('-expanded' if expanded else '')+'.svg','Study progress — Completed — DEMO'+(' — Expanded' if expanded else ''),'study-173108-completed-header-only.png; native expand/collapse observation at 17:31:19–17:31:25 UTC',body,'Second synthetic subject reproduces the observed long-name toggle geometry. All codes, titles and credit values are synthetic; there are no grades or actual completion claims.',True)

    body=segment('Completed','Requirements',1)+info_strip(['CAR, Service-Learning and GUR AIDA/IE Subject Options in','2026/27 Semester 1'],height=83)
    categories=[('RequirementCARA',['Ug-CAR-A Human Nature, Relations &','Development']),('RequirementCARD',['Ug-CAR-D Science, Technology &','Environment']),('RequirementCARM',['Ug-CAR-M Chinese History and Culture']),('RequirementCARN',['Ug-CAR-N Cultures, Organisations,','Societies and Globalisation']),('RequirementServiceLearning',['Ug Service-Learning'])]
    for i,(gid,lines_) in enumerate(categories):
        y=305+i*129;row=line(41,y,576,y)
        start=y+56 if len(lines_)==2 else y+73
        for j,s in enumerate(lines_): row+=text(41,start+35*j,s,24,700)
        row+=chevron(540,y+64,color='#151515')
        body+=group(gid,row)
    screen('study-requirements.svg','Study progress — Requirements','study-173133-requirements-categories.png',body+header('Study progress'),'Only the visible public category list is reconstructed. Other categories and destinations are unobserved.')

    body=group('InnerBack','<path d="M41 141L30 150L41 160" stroke="#252525" stroke-width="2"/>')
    body+=group('SubjectSearch',rect(74,124,478,53,'#ECECEC',17)+'<circle cx="102" cy="147" r="7.5" stroke="#777D85" stroke-width="2"/><path d="M108 153L115 160" stroke="#777D85" stroke-width="2"/>'+text(128,160,'Search Ug CAR-A Human Nature,...',26,color='#AFB0B2'))
    body+=info_strip(['Subjects on Offer in 2026/27 Semester 1 as of 29-Sep-2026','01:31'],y=201,height=82)
    subjects=[('APSS111','INTRODUCTION TO...',True),('APSS112','INTRODUCTION TO SOCIOLOGY',False),('APSS1A03','MEN AND MASCULINITY IN...',True),('APSS1A04','UNDERSTANDING ETHICS IN...',True),('APSS1A06','HUMANITY, FEAR AND...',True),('APSS1A07','',False)]
    for i,(code,title,arrow) in enumerate(subjects):
        row,_=subject_row(283+i*129,code,title,gid=f'PublicSubject{i+1}',arrow=arrow);body+=row
    body+=rect(559,200,14,259,'#FFFFFF',7,'#EAEAEA',1.5)
    screen('study-subjects-public.svg','Study progress — Public Subjects on Offer','study-173235-car-a-public-subject-offerings.png',body+header('Study progress'),'These are public catalogue entries, not a personal course list. Truncations are preserved. Search behavior and expanded course names are not invented.')
    screen('study-blank-unresolved.svg','Study progress — Blank Content — Outcome Unresolved','study-173300-empty-content.png',header('Study progress')+'<ellipse cx="288" cy="965" rx="273" ry="7" fill="#444444"/>','The observed body was blank after an attempted search. Input reception, submission and cause were not verified. Do not label this no-results, success or an application error. The bottom gray shape approximates the visible viewport edge.')


def open_button(y,gid):
    return group(gid,rect(433,y,100,37,'#E1F2E2',19)+'<g transform="translate(447,'+str(y+11)+')" stroke="#293132" stroke-width="1.6"><path d="M0 2V15H14V7M5 0H16V10M7 9L16 0"/></g>'+text(470,y+27,'Open',21))


def course_row(y,code,title,gid,expanded=False,arrow=True):
    lines=title if isinstance(title,list) else [title]
    body=line(41,y,576,y)+text(41,y+49,code,24,700)+open_button(y+23,gid+'Open')
    for i,s in enumerate(lines):body+=text(41,y+89+27*i,s,21,color='#434C5C')
    if arrow:body+=group(gid+'NameToggle',rect(514,y+69,35,38,'#FFFFFF').replace('fill="#FFFFFF"','fill="#FFFFFF" fill-opacity="0.001"')+chevron(531,y+91,down=not expanded,up=expanded))
    return group(gid,body),129+(len(lines)-1)*27


def build_courses():
    for expanded in [False,True]:
        body=segment('Canvas','Blackboard',0);y=223
        rows=[('EXM2001_DEMO_A',['EXM2001 CREATIVE RESEARCH','AND PRACTICE (DEMO)'] if expanded else 'EXM2001 CREATIVE RESEARCH...',True),('EXM2002_DEMO_A','EXM2002 VISUAL COMMUNICATION...',True),('EXM2003_DEMO_A','EXM2003 DESIGN AND SOCIETY...',True),('EXM2004_DEMO_A','EXM2004 TEAM DESIGN PROJECT',False),('EXM2005_DEMO_A','EXM2005 EVERYDAY SYSTEMS',False),('EXM2006_DEMO_A','EXM2006 PRACTICE STUDIO...',True)]
        for i,(code,title,arrow) in enumerate(rows):
            row,h=course_row(y,code,title,f'CanvasCourse{i+1}',expanded and i==0,arrow);body+=row;y+=h
        screen('courses-canvas-demo'+('-expanded' if expanded else '')+'.svg','My Courses — Canvas — DEMO'+(' — Expanded' if expanded else ''),'courses-173348-canvas-header-only.png; native name toggle observation at 17:33:56–17:34:05 UTC',body+header('My Courses',True),'First synthetic course reproduces the observed long-name toggle. Open controls do not have observed Canvas destinations in this batch.',True)
    body=segment('Canvas','Blackboard',1)
    row,_=course_row(223,'EXM3001_DEMO_01','EXM3001 Example subject...', 'BlackboardCourse1')
    screen('courses-blackboard-demo.svg','My Courses — Blackboard — DEMO','courses-173415-blackboard-header-only.png',body+row+header('My Courses',True),'The native Blackboard tab contained a course with Open; it was not an empty state. This one-row course body is wholly synthetic. The observed Open reached the empty official login page.',True)

    body=bitmap('courses-polyu-wordmark.png',38,161,385,77,'PublicUniversityWordmark')
    body+=text(38,360,'Sign in with your NetID and NetPassword',20.5)
    body+=group('NetIDField',rect(36,411,505,50,'#FFFFFF',1,'#91CBF4',5)+rect(39,414,499,45,'#FFFFFF',stroke='#949494',sw=1.2)+text(44,443,'NetID',17,color='#A5A5A5'))
    body+=group('NetPasswordField',rect(39,472,499,45,'#FFFFFF',stroke='#ADADAD',sw=1.2)+text(44,501,'NetPassword',17,color='#A5A5A5'))
    body+=group('LoginButton',rect(40,584,97,42,'#BE0000')+text(88,611,'登录',20,700,'#FFFFFF','middle'))
    body+=group('ForgotPassword',text(38,715,'Forgot Your NetPassword?',21,color='#2669D3'))
    body+=group('GuestAccess',text(38,774,'Blackboard Guest Access',21,color='#2669D3'))
    screen('courses-blackboard-login.svg','My Courses — Blackboard Login — Empty Fields','courses-173508-blackboard-login-empty-fields.png',body+header('My Courses'),'The two login fields were empty; NetID focus ring is preserved. No credentials or attempted authentication are included. Public university wordmark reuses the existing clean policy branding crop. Back was observed returning Home, not necessarily the course list; link and login actions remain untested.')


def bottom_nav(selected='Home'):
    body=rect(0,920,576,50,'#FFFFFF')
    color='#313A39' if selected=='Home' else '#9FB0B9'
    if selected=='Home':body+='<circle cx="51" cy="948" r="21" fill="#EEF3A8"/>'
    body+=group('NavHome',f'<path d="M40 947L53 935L68 947V962H57V951H49V962H40Z" stroke="{color}" stroke-width="3.5" stroke-linejoin="round"/>')
    body+=group('NavCalendar','<rect x="161" y="937" width="23" height="27" rx="1" stroke="#9FB0B9" stroke-width="4"/><path d="M166 932V941M179 932V941M164 944H182M166 951H179M166 957H179" stroke="#9FB0B9" stroke-width="3"/>')
    qr='<circle cx="288" cy="949" r="49" fill="#58B1A2"/>'
    # Tiny generic navigation glyph only; the campus code itself is never drawn.
    for x,y in [(273,932),(294,932),(273,952)]:qr+=rect(x,y,11,11,'none',stroke='#FFFFFF',sw=3)
    qr+='<path d="M294 952H300V958H306V964H294V959H288" stroke="#FFFFFF" stroke-width="3"/>'
    body+=group('NavQR',qr)
    body+=group('NavNotification','<path d="M391 937H417V956H402L395 963V956H391Z" stroke="#9FB0B9" stroke-width="4" stroke-linejoin="round"/>')
    body+=group('NavMore','<path d="M505 935H534V959H505ZM511 965H514M519 965H522M527 965H530" stroke="#9FB0B9" stroke-width="4"/>')
    return group('BottomNavigation',body)


def build_qr():
    body=text(288,152,'Scan at the QR Code Reader',25,700,anchor='middle')
    body+=rect(77,193,423,422,'#DCEEDC',69)+rect(103,220,370,370,'#F6F8F5',42)
    placeholder=rect(116,234,345,345,'#E6EBE5',12,'#B4C5B7',2)
    placeholder+='<path d="M155 315L421 499M421 315L155 499" stroke="#CAD5C9" stroke-width="7"/>'
    placeholder+=text(288,378,'DEMO',36,700,'#526551','middle')+text(288,422,'No QR code',25,700,'#526551','middle')+text(288,459,'Cannot be scanned',19,400,'#617660','middle')
    body+=group('NonScannableDemoPlaceholder',placeholder)
    body+=group('DemoIdentity',text(288,674,'Student Example · DEMO',25,700,anchor='middle'))
    body+=group('UnverifiedStatusBar',rect(72,699,433,12,'#EFEFEF',6)+rect(72,699,173,12,'#B9D952',6))
    body+=group('HelpInfo','<circle cx="43" cy="813" r="11" stroke="#727783" stroke-width="2"/>'+text(43,820,'?',20,700,'#727783','middle'))
    for i,s in enumerate(['Please note that the QR Code provided is','only for use by the student to whom the QR','Code is assigned. Sharing or allowing','others to use QR codes is strictly']):body+=text(68,818+30*i,s,22,color='#737986')
    body+=rect(560,103,13,731,'#C6C6C6',7)
    screen('qr-demo.svg','My Campus Access QR — Non-scannable DEMO','qr-174024-code-and-identity-redacted.png',body+header('My Campus Access QR',True,True)+bottom_nav('QR'),'The entire native QR and identity regions were removed. The central illustration is a crossed rectangle with text, has no QR finder patterns or encoded payload, and cannot function as a campus credential. The bar uses an arbitrary demo fraction; its native meaning was not established. Only the visible instruction fragment is included; tapping help or scrolling did not confirm a new result.',True)


def time_icon(x,y,kind='clock'):
    if kind=='clock':return f'<circle cx="{x}" cy="{y}" r="11" fill="#59B29F"/>'+f'<path d="M{x} {y-6}V{y}H{x+5}" stroke="#FFFFFF" stroke-width="1.3"/>'
    if kind=='pin':return f'<path d="M{x} {y+11}C{x-20} {y-10} {x+20} {y-10} {x} {y+11}Z" fill="#59B29F"/><circle cx="{x}" cy="{y-3}" r="2.5" fill="#FFFFFF"/>'
    return f'<g transform="translate({x-9},{y-9})" stroke="#59B29F" stroke-width="2.5"><rect width="18" height="19"/><path d="M0 5H18M5 -3V3M13 -3V3M5 9H10V14H5Z"/></g>'


def class_card(y):
    body=rect(82,y,427,207,'#F8FDED',16,'#C9E148',1.5)+rect(83,y+167,425,39,'#D0EB38',0)
    body+=time_icon(104,y+27)+text(128,y+34,'09:00–10:00',23,700)
    body+=time_icon(104,y+56,'pin')+text(128,y+64,'EXAMPLE ROOM',22,700)
    body+=text(95,y+123,'Creative Research and Practice',22)+text(95,y+152,'Synthetic class schedule · DEMO',22)
    body+=text(295,y+196,'EXM2001  (DEMO CLASS)',22,700,anchor='middle')
    return group('DemoClassCard',body)


def exam_card(y):
    body=rect(28,y,426,229,'#FFFFFF',16,'#E3F0F8',1.5)+rect(29,y+188,424,40,'#EFF9FF')
    body+=time_icon(49,y+25,'calendar')+text(72,y+35,'Nov 01, 2030',22,700)
    body+=time_icon(49,y+55)+text(72,y+64,'10:00–11:00',22,700)
    body+=time_icon(49,y+87,'pin')+text(72,y+95,'EXAMPLE HALL',22,700)
    body+=text(40,y+174,'Example Assessment · DEMO',22)+text(238,y+217,'EXM2001',22,700,anchor='middle')
    body+='<circle cx="417" cy="'+str(y+55)+'" r="25" fill="#E2F5FF"/><g transform="translate(409,'+str(y+44)+')" stroke="#333D3F" stroke-width="1.4"><rect width="15" height="22"/><path d="M4 0V22M-3 3H3M-3 9H3M-3 15H3M-3 21H3"/></g>'
    # Second card is only the observed partially visible neighbour, using demo text.
    body+=rect(470,y,426,229,'#FFFFFF',16,'#E3F0F8',1.5)+rect(471,y+188,424,40,'#EFF9FF')
    body+=time_icon(491,y+25,'calendar')+text(514,y+35,'Nov 02, 2030',22,700)+time_icon(491,y+55)+text(514,y+64,'09:00–10:00',22,700)+time_icon(491,y+87,'pin')+text(514,y+95,'EXAMPLE',22,700)+text(482,y+174,'Example task',22)
    return group('DemoExamCards',body)


def home_date(tuesday=False):
    body=text(121,148,'Week',27,700,anchor='middle')+text(400,147,'Event',27,700,anchor='middle')
    body+='<circle cx="121" cy="221" r="56" stroke="#F3F3F3" stroke-width="12"/><path d="M121 165A56 56 0 0 1 163 258" stroke="#CEEB43" stroke-width="12" stroke-linecap="round"/>'
    body+=text(121,233,'5',30,700,'#565656','middle')+text(121,310,'Semester 1',21,color='#939393',anchor='middle')+line(233,122,233,313,'#DADADA')
    body+=rect(253,160,294,122,'#F8FDEE',16,'#CCE047',1.5)+text(269,207,'SEP',19,700)+text(269,247,'29' if tuesday else '28',31,700,'#585858')
    if tuesday:body+=text(531,209,'Today',16,400,'#65744B','end')
    names=['MON','TUE','W','T','F','S','S'];centers=[286,343,383,423,461,496,533]
    for i,(name,x) in enumerate(zip(names,centers)):
        selected=(i==1 if tuesday else i==0)
        label=name if selected else ('M' if i==0 else 'T' if i==1 else name)
        tab=rect(x-36,291,72,25,'#FBFFED',14,'#CDE246',1.5) if selected else ''
        tab+=text(x,311,label,20,700 if selected else 400,'#171717' if selected else '#B8B8B8','middle')
        body+=group('Date'+['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][i],tab)
    return group('WeekAndEvent',body)


def feature_icon(kind,x,y):
    s='<g transform="translate('+str(x)+','+str(y)+')" stroke="#818381" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round">'
    if kind=='Map':s+='<path d="M1 10C1 -10 32 -10 32 10C32 21 17 36 17 36C17 36 1 21 1 10Z"/><path d="M10 8C10 -3 27 -3 27 8C27 17 19 27 19 27Z" fill="#D5E639" stroke="none"/><circle cx="17" cy="9" r="3" fill="#818381" stroke="none"/>'
    elif kind=='Room':s+='<rect x="0" y="-1" width="31" height="37" rx="4"/><path d="M-5 39H36"/><rect x="12" y="23" width="19" height="15" rx="5" fill="#DEE73D" stroke="none"/><path d="M8 38V29Q8 22 19 24V38"/>'
    elif kind=='Food':s+='<path d="M-2 11Q15 -8 37 11ZM-2 23Q3 17 8 23Q13 28 18 23Q25 17 37 23M-2 32H37V42H-2Z"/><path d="M3 34H38V39H3" fill="#D7E530" stroke="none"/>'
    elif kind=='Apps':s+='<rect x="-1" y="0" width="15" height="15" rx="3"/><rect x="22" y="2" width="20" height="20" rx="4" fill="#D9E438" stroke="none"/><rect x="21" y="0" width="15" height="15" rx="3"/><rect x="-1" y="23" width="15" height="15" rx="3"/><path d="M28 24V38M21 31H35"/>'
    elif kind=='StudyProgress':s+='<path d="M-2 6H13M-2 21H13M-2 36H13"/><path d="M24 3L34 13M34 3L24 13M24 23L29 28L38 18M24 38L29 43L38 33" stroke="#D9E438" stroke-width="7"/><path d="M22 1L32 11M32 1L22 11M22 21L27 26L36 16M22 36L27 41L36 31"/>'
    else:s+='<rect x="-4" y="1" width="37" height="32" rx="4" fill="#E3F769"/><path d="M-4 25H33M9 33L4 43M20 33L25 43M7 1V-3M15 24Q21 16 26 24"/>'
    return s+'</g>'


def home_features():
    body=''
    for name,kind,x,y in [('Map','Map',106,661),('Room','Room',289,662),('Food','Food',470,659),('Apps','Apps',105,760),('Study progress','StudyProgress',288,760),('My Courses','MyCourses',470,760)]:
        body+=group('Feature'+kind,feature_icon(kind,x-16,y)+text(x,y+69,name,22,color='#545454',anchor='middle'))
    return group('Features',body)


def home_sheet():
    body='<path d="M14 920V878Q14 835 57 835H519Q562 835 562 878V920Z" fill="#F5F5F5"/>'
    body+=rect(239,853,99,7,'#409889',2)+rect(15,876,545,44,'#FFFFFF')
    body+=bitmap('home-demo-public-preview.png',44,899,489,22,'PublicNewsPreview')+rect(544,879,13,80,'#FFFFFF',7,'#ECECEC',1.5)
    return group('BottomSheet',body)


def build_home():
    for slug,tuesday,scrolled in [('top',False,False),('tuesday',True,False),('scrolled',False,True)]:
        if scrolled:
            body=class_card(45)+text(27,340,'My Exam',27,700)+rect(147,315,36,26,'#F0F0F0',14)+text(165,337,'2',21,anchor='middle')+exam_card(361)+home_features()
        else:
            body=home_date(tuesday)+text(27,379,'My Class',27,700)+rect(146,351,35,26,'#F0F0F0',14)+text(164,374,'1',21,anchor='middle')
            body+=group('MyClassCalendar','<circle cx="538" cy="369" r="20" fill="#EEF3A6"/>'+chevron(538,369,color='#5F6450'))
            body+=class_card(398)+text(27,695,'My Exam',27,700)+rect(147,669,36,26,'#F0F0F0',14)+text(165,691,'2',21,anchor='middle')+exam_card(714)
        body='<g clip-path="url(#HomeContentClip)">'+body+'</g>'+home_sheet()+header('Hi, Student',True,True)+bottom_nav()
        source='home-174141-today-event-panel-only.png' if tuesday else 'home-174126-week-event-panel-only.png' if not scrolled else 'home-134424-navigation-only.png; native Home scrolled geometry at 17:30:48 UTC'
        screen(f'home-demo-{slug}.svg',f'Home — DEMO — {slug.title()}',source,body,'All private class/exam body content is synthetic, including the card counts, dates, times, rooms, titles and codes. Only public week/date/navigation structures follow screenshot evidence. The small decorative image strip comes from the public home-134424-navigation-only.png crop (84,483,986,523), not a private screenshot. These are static scroll-position samples. Tuesday changes the visible public date and Today label; synthetic schedules stay fixed and do not assert the actual agenda.',True)


if __name__ == '__main__':
    copyfile(ASSETS/'polyu-web-wordmark.png',ASSETS/'courses-polyu-wordmark.png')
    if not (ASSETS/'home-demo-public-preview.png').exists():
        from PIL import Image
        Image.open(EVIDENCE/'home-134424-navigation-only.png').crop((84,483,986,523)).save(ASSETS/'home-demo-public-preview.png')
    build_study()
    build_courses()
    build_qr()
    build_home()
    print('Built 13 Study/Courses/QR/Home SVGs with synthetic private content.')
