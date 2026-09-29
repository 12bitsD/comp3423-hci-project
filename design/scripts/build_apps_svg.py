"""Rebuild observed Apps views from public evidence, without app or network access.

Run with Python 3. Pillow is only required when regenerating the two brand assets.
The SVGs are editable design sources, not screenshots or live web integrations.
"""
from base64 import b64encode
from pathlib import Path
from shutil import copyfile
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "design/polyulife"
ASSETS = OUT / "assets"
EVIDENCE = ROOT / "evidence/2026-09-28-full-audit"


def text(x, y, value, size=22, weight=400, color="#141414", anchor=None):
    align = f' text-anchor="{anchor}"' if anchor else ''
    font = 'Noto Sans TC' if '理學網' in value else 'Noto Sans SC' if value == '登录' else 'sans-serif'
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{weight}"{align}>{escape(value)}</text>'


def bitmap(name, x, y, width, height, gid):
    data = b64encode((ASSETS / name).read_bytes()).decode()
    return f'<g id="{gid}"><image x="{x}" y="{y}" width="{width}" height="{height}" preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/></g>'


def screen(filename, title, source, body, extra=''):
    desc = (f'Editable observed-interface reconstruction from {source}. Source viewport 576x970. '
            'All visible interface text, card boundaries, category controls and ordinary icons are native editable SVG elements. '
            'Fonts and icons are approximations; cursor and hover effects are omitted. '
            'Only visible content is reconstructed. No unseen service pages or list entries invented. '
            'SVG import does not implement navigation, scrolling, text entry, network access or login. ' + extra)
    content = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="970" viewBox="0 0 576 970" fill="none">'
    content += f'<title>{escape(title)}</title><desc>{escape(desc)}</desc>'
    content += '<defs><clipPath id="ViewportClip"><rect width="576" height="970"/></clipPath><clipPath id="CategoryViewport"><rect y="100" width="576" height="74"/></clipPath></defs>'
    content += '<g clip-path="url(#ViewportClip)"><rect id="ScreenBackground" width="576" height="970" fill="#FFFFFF"/>' + body + '</g></svg>'
    (OUT / filename).write_text(content)


def header(title='Apps'):
    return '<g id="Header"><rect x="0.5" y="0.5" width="575" height="99" fill="#FFFFFF" stroke="#E1E1E1"/><g id="Back"><path d="M34.5 57.5L27 65L34.5 72.5" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' + text(288, 75.5, title, 27, anchor='middle') + '</g>'


TABS = [('All', 0, 69, 34), ('Campus', 69, 195, 132), ('Study', 195, 297, 246),
        ('IT Tips', 297, 409, 352), ('Health', 409, 519, 464),
        ('Wellness', 519, 653, 584), ('Job', 653, 732, 694)]


def categories(selected, offset=0):
    result = '<g id="CategoryBar" clip-path="url(#CategoryViewport)"><rect y="100" width="576" height="74" fill="#FFFFFF"/><path d="M0 173.5H576" stroke="#ECECEC"/>'
    for label, left, right, center in TABS:
        # Only include controls intersecting the observed viewport.
        if right - offset <= 0 or left - offset >= 576:
            continue
        gid = label.replace(' ', '')
        color = '#398F7F' if label == selected else '#818181'
        result += f'<g id="Category{gid}"><rect x="{left-offset}" y="101" width="{right-left}" height="72" fill="#FFFFFF" fill-opacity="0.001"/>'
        result += text(center-offset, 145.5, label, 23, color=color, anchor='middle')
        if label == selected:
            result += f'<path d="M{left-offset} 171H{right-offset}" stroke="#398F7F" stroke-width="4.5"/>'
        result += '</g>'
    return result + '</g>'


def icon(kind, y, gid):
    result = f'<g id="{gid}"><rect x="25" y="{y}" width="70" height="70" rx="12" fill="#E0E0E0"/>'
    if len(kind) == 1:
        result += text(60, y+48, kind, 35, color='#080808', anchor='middle')
    else:
        result += f'<g transform="translate(46,{y+24})" stroke="#575757" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round">'
        if kind == 'books':
            result += '<path d="M3 2H6V20H3ZM9 0H13V20H9ZM17 4L20 3L23 20L19 21Z" fill="#575757" stroke-width="1"/><path d="M3 6H6M9 4H13M9 16H13" stroke="#E0E0E0" stroke-width="1"/>'
        elif kind == 'mail':
            result += '<rect x="3" y="2" width="22" height="16" rx="1"/><path d="M4 4L14 12L24 4"/>'
        elif kind == 'identity':
            result += '<circle cx="8" cy="4" r="5" fill="#575757"/><path d="M1 20V15Q8 6 15 15V20Z" fill="#575757"/><circle cx="21" cy="15" r="5"/><circle cx="21" cy="15" r="1.8"/><path d="M21 8V10M21 20V22M14 15H16M26 15H28M16 10L18 12M24 18L26 20M16 20L18 18M24 12L26 10"/>'
        elif kind == 'bulb':
            result += '<path d="M10 15C10 10 6 10 8 5C10 -1 18 -1 20 5C22 10 17 10 17 15M11 16H16M11 19H15"/><path d="M14 4L12 7" stroke-width="1.5"/>'
        elif kind == 'chat':
            result += '<ellipse cx="12" cy="10" rx="9" ry="6"/><path d="M5 14L4 19L10 16M21 7Q29 14 20 18L23 21L16 19"/>'
        elif kind == 'health':
            result += '<rect x="3" y="3" width="22" height="18" rx="2" fill="#575757" stroke-width="1"/><path d="M9 3V0H18V3"/><path d="M10 12H18M14 8V16" stroke="#E0E0E0" stroke-width="1.5"/>'
        elif kind == 'eye':
            result += '<path d="M2 12Q14 -2 26 12Q14 26 2 12Z" stroke-width="1.8"/><circle cx="14" cy="12" r="5"/><circle cx="15" cy="10" r="1.5" fill="#575757"/>'
        result += '</g>'
    return result + '</g>'


def question(x, y, gid):
    return f'<g id="{gid}"><circle cx="{x}" cy="{y}" r="8.6" stroke="#B2B5B4" stroke-width="2.5"/>' + text(x, y+5.4, '?', 16, 700, '#B2B5B4', 'middle') + '</g>'


def chain(x, y):
    return f'<g transform="translate({x},{y})" stroke="#60AE9F" stroke-width="3.2" stroke-linecap="round"><path d="M9 5L14 0C19 -5 24 2 20 6L15 11M13 12L8 17C3 22 -2 15 2 11L7 6M7 11L15 3"/></g>'


def open_button(y, label, width, gid, url=None):
    x = 35 if url else 119
    h = 65 if url else 50
    result = f'<g id="{gid}"><rect x="{x+0.5}" y="{y+0.5}" width="{width}" height="{h}" rx="{h/2}" fill="#FFFFFF" stroke="#DEDEDE" stroke-width="1.5"/>'
    result += chain(x+26, y+(30 if url else 23))
    result += text(x+57, y+32, label, 19, color='#4C4C4C')
    if url:
        result += text(x+57, y+53, url, 16, color='#656565')
    else:
        ax = x+width-40
        result += f'<path d="M{ax} {y+30}L{ax+10} {y+20}M{ax} {y+20}H{ax+10}V{y+30}" stroke="#818181" stroke-width="2.7"/>'
    return result + '</g>'


def card(y, height, key, title, kind, description, label, button_width, partial=False):
    offset = 0 if y == 174 else -4
    result = f'<g id="Service{key}"><g id="CardContent{key}" transform="translate(0,{offset})">' + icon(kind, y+25, f'Icon{key}')
    for index, line in enumerate(title if isinstance(title, list) else [title]):
        result += text(119, y+46+index*28, line, 22, 700)
    if description:
        result += question(130, y+79, f'Info{key}')
        for index, line in enumerate(description):
            result += text(149, y+87+index*27, line, 21, color='#333333')
    if not partial:
        result += open_button(y+58 if not description else y+74+len(description)*27, label, button_width, f'Open{key}')
        center_y = y+height/2-4 + (2 if offset else 0)
        result += f'<g id="ServiceMenu{key}"><circle cx="532" cy="{center_y}" r="2.7" fill="#9FB2BE"/><circle cx="540" cy="{center_y}" r="2.7" fill="#9FB2BE"/><circle cx="548" cy="{center_y}" r="2.7" fill="#9FB2BE"/></g>'
    result += '</g>'
    if not partial:
        result += f'<path d="M0 {y+height-0.5}H576" stroke="#DADADA" stroke-width="1.4"/>'
    return result + '</g>'


VRS = ('VRS', 'Visitor Registration System (VRS)', 'V', ['Request QR code for your guests to', 'access campus'], 'Open VRS', 193)
INTERNAL = ('InternalSearch', 'PolyU Internal Search', 'P', ['Search PolyU internal documents', 'available to staff and students'], 'Open Internal Search', 288)
LEARN = ('Learn', 'LEARN@PolyU(理學網)', 'L', ['Learning Management System of', 'PolyU'], 'Open LEARN@PolyU', 285)
LIBRARY = ('Library', 'Library', 'books', [], 'Open Library Home', 275)
ESTUDENT = ('eStudent', 'eStudent', 'e', ['Get access to applications related to', 'studies and info on upcoming', 'activities'], 'Open eStudent', 237)
RESEARCH = ('Research', 'Research Student Portal', 'R', ['Research students admitted in', '2017/18 or before'], 'Open Research Student Portal', 369)


def build_lists():
    all_cards = [(174,196,VRS),(370,192,INTERNAL),(562,192,LEARN),(754,124,LIBRARY)]
    all_body = ''.join(card(y,h,*data) for y,h,data in all_cards)
    all_body += card(878,220,*ESTUDENT,partial=True)
    variants = [
        ('all','All',0,'apps-171359-all.png',all_body),
        ('campus','Campus',0,'apps-171411-campus.png',card(174,196,*VRS)+card(370,192,*INTERNAL)),
        ('study','Study',0,'apps-171613-study.png',card(174,196,*LEARN)+card(370,124,*LIBRARY)+card(494,220,*ESTUDENT)+card(714,192,*RESEARCH)+card(906,220,'StudentAccount',['Student Account Portal - Student in','Taught Programmes'],'S',[],'',0,partial=True)),
        ('it-tips','IT Tips',64,'apps-171626-it-tips.png',
         card(174,196,'ConnectEmail','Connect Email','mail',['Official channel for communication','and collaboration'],'Open Connect Email',283)+
         card(370,220,'Identity','Identity Portal (IdPortal)','identity',['Manage your PolyU Network Identity','(NetID) and Password (NetPassword),','Update Password'],'Open ID Portal',233)+
         card(590,124,'ITFAQ','FAQ for IT Services','bulb',[],'Open IT FAQ',214)+
         card(714,192,'ServiceDesk','IT Online ServiceDesk','chat',['Submit enquiry relating to ITS','services and facilities'],'Open ServiceDesk',267)),
        ('health','Health',156,'apps-171639-health.png',
         card(174,224,'Health','University Health Service','health',['Medical consultations, Traditional','Chinese Medicine, and subsidised','primary dental care etc'],'Open Link',193)+
         card(398,192,'Optometry','Optometry Clinic','eye',['Primary eye care services, Contact','lens fitting, Optical dispensing, etc'],'Open Link',193)+
         card(590,220,'Rehabilitation','Rehabilitation Clinic','R',['Musculoskeletal Rehabilitation,','Physiotherapy, Occupational Therapy,','etc.'],'Open Link',193)),
        ('wellness','Wellness',156,'apps-171652-wellness.png',
         card(174,168,'POSS','POSS','P',['PolyU Online Student Services'],'Open POSS',207)+
         card(342,164,'Scholarship','Scholarship','S',['Scholarships open for application'],'Open Scholarship',260)),
        ('job','Job',156,'apps-171705-job.png',card(174,196,'JobBoard','PolyU Job Board','P',['Explore full-time, part-time graduate /','internship opportunities'],'Open Job Board',246)),
        ('job-category-left','Job',0,'apps-171722-category-bar-dragged.png',card(174,196,'JobBoard','PolyU Job Board','P',['Explore full-time, part-time graduate /','internship opportunities'],'Open Job Board',246)),
    ]
    for slug, selected, offset, source, body in variants:
        extra = 'The category strip is a static captured offset; horizontal dragging and service actions need separate prototype configuration.'
        if slug == 'job-category-left':
            extra += ' Job remains selected but its category label is offscreen after the observed rightward drag. No selected underline is visible in this viewport.'
        screen(f'apps-{slug}.svg', f'Apps — {selected}' + (' — Categories at Left' if slug=='job-category-left' else ''), source, body+categories(selected,offset)+header(), extra)


def build_detail():
    body = '<g id="DetailContent"><rect y="100" width="576" height="870" fill="#F7F9F6"/><rect x="19.5" y="100" width="539" height="870" fill="#FFFFFF" stroke="#CED3D3"/>'
    body += text(35,135,'Visitor Registration System (VRS)',22,700)
    body += question(46,169,'DescriptionInfo') + text(64,177,'Request QR code for your guests to access',21,color='#3C3C3C') + text(64,204,'campus',21,color='#3C3C3C')
    body += '<path d="M35 233H543" stroke="#DADADA" stroke-width="1.5"/>'
    body += open_button(258,'Open VRS',308,'OpenVRS','https://fmovrs.polyu.edu.hk/vrs') + '</g>' + header('Visitor Registration Syst...')
    screen('apps-vrs-detail.svg','Apps — VRS Detail','apps-171424-vrs-detail.png',body,'Visible public official URL is plain editable text. This link was observed opening an embedded web view; no visitor registration was submitted.')


def web_shell(title=''):
    body = header('Visitor Registration Syst...')
    body += '<g id="EmbeddedWebView"><path d="M8 878V101Q8 76 32 76H545Q570 76 570 101V878Z" fill="#FFFFFF" stroke="#BFC3C0"/>'
    body += '<path d="M9 141V101Q9 77 33 77H545Q569 77 569 101V141Z" fill="#F7F9F6"/><path d="M8 146H570" stroke="#DFDFDF" stroke-width="11"/>'
    body += '<g id="CloseWeb"><path d="M32 104L52 124M52 104L32 124" stroke="#2E302F" stroke-width="3.4" stroke-linecap="round"/></g>'
    if title:
        body += text(293,122,title,23,anchor='middle')
    body += '<g id="WebMenu"><circle cx="515" cy="113.5" r="4.1" fill="#343434"/><circle cx="528" cy="113.5" r="4.1" fill="#343434"/><circle cx="541" cy="113.5" r="4.1" fill="#343434"/></g></g>'
    return body


def web_bottom(back_active):
    color = '#429685' if back_active else '#B0B5B1'
    body = '<g id="WebBottomBar"><path d="M0 879H576V930Q576 970 536 970H40Q0 970 0 930Z" fill="#F7F9F6"/><path d="M8 878.5H570" stroke="#C6C9C7"/>'
    body += f'<g id="WebBack"><path d="M55 910L41 924L55 938" stroke="{color}" stroke-width="3.5" stroke-linecap="round"/></g>'
    body += '<g id="WebForward"><path d="M110 910L124 924L110 938" stroke="#B0B5B1" stroke-width="3.5" stroke-linecap="round"/></g>'
    body += '<g id="AddressBar"><rect x="151" y="895" width="388" height="61" rx="13" fill="#FFFFFF" stroke="#9EAAA4"/>'
    body += '<g id="AddressLock"><rect x="175" y="923" width="13" height="10" rx="1" fill="#252825"/><path d="M178 923V920Q181.5 913 185 920V923" stroke="#252825" stroke-width="2"/></g>'
    body += text(200,934,'fmovrs.polyu.edu.hk/vr...',23,color='#808080')
    body += '<g id="WebReload"><path d="M516 917A12 12 0 1 0 525 929M515 911L521 917L515 923" stroke="#272C28" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></g></g></g>'
    return body


def build_web():
    loading = web_shell() + bitmap('apps-vrs-loading-mark.png',263,535,53,54,'LoadingBrandMark') + web_bottom(False)
    screen('apps-vrs-web-loading.svg','Apps — VRS Web Loading','apps-171442-vrs-web-loading.png',loading,
           'Only the public PolyU mark crop (263,535,316,589) is raster. This observed transient loading state later reached the empty login page. The static frame is not a performance or permanent-error claim; auto-transition would require explicit prototype configuration.')
    login = web_shell('登录') + bitmap('apps-vrs-wordmark.png',47,211,385,77,'PublicUniversityWordmark')
    login += text(47,412,'Sign in with your NetID and NetPassword',20.5,color='#171717')
    for gid, y, placeholder in [('NetIDField',467,'NetID'),('NetPasswordField',525,'NetPassword')]:
        login += f'<g id="{gid}"><rect x="47.5" y="{y}" width="483" height="44.5" fill="#FFFFFF" stroke="#ABABAB" stroke-width="1.2"/>' + text(52,y+28,placeholder,17,color='#A0A0A0') + '</g>'
    login += '<g id="LoginButton"><rect x="49" y="637" width="96" height="41" fill="#C80000" stroke="#A90000"/>' + text(97,664,'登录',19,700,'#FFFFFF','middle') + '</g>'
    login += '<g id="ForgotPassword">' + text(47,768,'Forgot Your NetPassword?',21,color='#2868D2') + '</g>' + web_bottom(True)
    screen('apps-vrs-web-login.svg','Apps — VRS Web Login — Empty Fields','apps-171522-vrs-login-empty-fields.png',login,
           'Both observed login fields are empty. No credentials, login attempt, form error, account links or authenticated page are reconstructed. The two fields, login and help text are editable design controls only. The public PolyU wordmark reuses the existing clean policy-page branding crop (polyu-web-wordmark.png), scaled to this observed placement; this avoids copying the native pointer shadow over the login wordmark. The website body and browser chrome are reconstructed, not a live browser or embedded screenshot.')


if __name__ == '__main__':
    if not (ASSETS / 'apps-vrs-loading-mark.png').exists():
        from PIL import Image, ImageCms
        im = Image.open(EVIDENCE / 'apps-171442-vrs-web-loading.png')
        crop = im.crop((263,535,316,589))
        if im.info.get('icc_profile'):
            import io
            crop = ImageCms.profileToProfile(crop, ImageCms.ImageCmsProfile(io.BytesIO(im.info['icc_profile'])), ImageCms.createProfile('sRGB'), outputMode='RGB')
        crop.save(ASSETS / 'apps-vrs-loading-mark.png')
    copyfile(ASSETS / 'polyu-web-wordmark.png', ASSETS / 'apps-vrs-wordmark.png')
    build_lists()
    build_detail()
    build_web()
    print('Built eleven Apps SVGs: eight category viewports, VRS detail, loading and empty login.')
