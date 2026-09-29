"""Build editable menu and Mac handoff views from recorded geometry; identity is DEMO."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parents[1]/'polyulife'
def text(x,y,s,size=21,color='#686868',weight=400):return f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(s)}</text>'
def group(id,body):return f'<g id="{id}">{body}</g>'
def svg(w,h,title,body):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none"><title>{title}</title>{body}</svg>'
# Context-independent backdrop: source content intentionally not fabricated.
b='<rect width="576" height="970" fill="#FFFFFF"/>'+group('DrawerOutside','<rect x="490" width="86" height="970" fill="#808080"/>')+'<rect width="490" height="970" fill="#FFFFFF"/>'
b+=group('DemoIdentity','<circle cx="113" cy="183" r="45" fill="#E59A7B"/>'+text(76,199,'DEMO',20,'#FFFFFF',600)+text(68,264,'00000000A',16)+text(68,306,'Student Example',22,'#161616')+text(68,342,'DEMO — synthetic identity',15,'#797979'))
for name,label,y in [('DrawerProfile','Profile',407),('DrawerSettings','Settings',485),('DrawerEmergency','Emergency Contact',563),('DrawerLogout','Log Out',687),('DrawerPrivacy','Privacy Policy',771),('DrawerTerms','Terms of Use',855)]:
 b+=group(name,f'<rect x="60" y="{y-40}" width="360" height="72" fill="#FFFFFF"/>'+text(82,y,label,20 if y<700 else 21,'#C64236' if name=='DrawerEmergency' else '#686868',600 if y<600 else 400))
 b+=f'<path d="M87 {y+31}H402" stroke="#E7E8EC" stroke-width="1.2"/>'
b+=text(50,969,'version: 3.0.0',15)
(R/'drawer-full-demo.svg').write_text(svg(576,970,'Side drawer — synthetic identity; neutral source backdrop',b))
b='<rect width="1382" height="320" rx="30" fill="#2C2B29"/>'+group('MacGeneralClose','<circle cx="32" cy="28" r="12" fill="#545352"/>')+'<circle cx="72" cy="28" r="12" fill="#545352"/><circle cx="112" cy="28" r="12" fill="#545352"/>'+text(640,35,'General',25,'#81807E',600)+'<path d="M0 160H1382" stroke="#111111"/>'
b+='<rect x="470" y="56" width="111" height="91" rx="14" fill="#3A3937"/>'+text(486,94,'⚙',36,'#A2A19F')+text(484,132,'General',24,'#A2A19F')+text(595,132,'Touch Alternatives',24,'#72716E')+text(817,132,'System',24,'#72716E')+text(485,226,'Window Size:',27,'#DEDDDC')+'<circle cx="674" cy="216" r="14" fill="#60605F"/><circle cx="674" cy="264" r="14" fill="#60605F"/><circle cx="674" cy="264" r="6" fill="#DDDDDD"/>'+text(700,226,'Smaller',27,'#DEDDDC')+text(700,274,'Larger (default)',27,'#DEDDDC')
(R/'mac-general.svg').write_text(svg(1382,320,'Mac-only PolyULife General preferences — no setting change',b))
