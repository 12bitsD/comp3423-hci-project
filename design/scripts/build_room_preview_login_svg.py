"""Create an editable authentication boundary from native screenshot14.

Header/form/browser controls remain editable; institutional wordmark is a
public raster crop. Fullscreen capture geometry is recorded, not phone fidelity.
"""
from pathlib import Path
import base64,json,hashlib
from PIL import Image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';A=D/'assets';A.mkdir(exist_ok=True)
source=R/'evidence/2026-09-30-room-preview-controls/14-login-boundary.png';logo=A/'room-preview-login-wordmark.png'
Image.open(source).crop((46,211,437,292)).save(logo)
encoded=base64.b64encode(logo.read_bytes()).decode(); h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="1024" viewBox="0 0 576 1024">
<rect width="576" height="1024" fill="white"/>
<g id="RoomHeader"><path d="M35 56L27 64L35 72" fill="none" stroke="#222" stroke-width="6" stroke-linecap="round"/><text x="288" y="74" text-anchor="middle" font-family="Arial" font-size="27">Room Finder</text></g>
<rect x="8" y="76" width="560" height="948" rx="26" fill="#f7f9f7" stroke="#ccc"/>
<g id="PreviewClose"><rect x="18" y="88" width="48" height="48" fill="#fff" fill-opacity="0.001"/><path d="M31 104L52 124M52 104L31 124" stroke="#555" stroke-width="3.5" stroke-linecap="round"/></g>
<text x="292" y="124" text-anchor="middle" font-family="Arial" font-size="23">登录</text>
<g id="PreviewMore"><rect x="504" y="88" width="48" height="48" fill="#fff" fill-opacity="0.001"/><circle cx="516" cy="114" r="4" fill="#444"/><circle cx="528" cy="114" r="4" fill="#444"/><circle cx="540" cy="114" r="4" fill="#444"/></g>
<rect x="8" y="141" width="560" height="11" fill="#ddd"/>
<g id="LoginWebContent"><rect x="8" y="152" width="560" height="726" fill="white"/>
<image id="PolyULoginWordmark" x="46" y="211" width="391" height="81" xlink:href="data:image/png;base64,{encoded}"/>
<text x="47" y="412" font-family="Arial" font-size="20" fill="#222">Sign in with your NetID and NetPassword</text>
<g id="NetIDPlaceholder"><rect x="43" y="462" width="492" height="54" rx="3" fill="white" stroke="#7dc8ff" stroke-width="4"/><rect x="48" y="467" width="482" height="44" fill="white" stroke="#888"/><text x="53" y="496" font-family="Arial" font-size="16" fill="#aaa">NetID</text></g>
<g id="PasswordPlaceholder"><rect x="48" y="525" width="482" height="45" fill="white" stroke="#aaa"/><text x="53" y="554" font-family="Arial" font-size="16" fill="#aaa">NetPassword</text></g>
<g id="LoginSubmitUnimplemented"><rect x="49" y="637" width="96" height="41" fill="#c00000"/><text x="97" y="663" text-anchor="middle" font-family="Arial" font-size="20" fill="white">登录</text></g>
<text id="ForgotPasswordUnimplemented" x="47" y="767" font-family="Arial" font-size="20" fill="#3377ff">Forgot Your NetPassword?</text></g>
<path d="M8 878H568" stroke="#ccc"/>
<g id="BrowserBack"><rect x="28" y="897" width="40" height="57" fill="#fff" fill-opacity="0.001"/><path d="M55 909L42 923L55 937" fill="none" stroke="#359787" stroke-width="3.5" stroke-linecap="round"/></g>
<g id="BrowserForwardDisabled"><path d="M111 909L124 923L111 937" fill="none" stroke="#bbb" stroke-width="3.5" stroke-linecap="round"/></g>
<rect x="151" y="894" width="386" height="61" rx="14" fill="white" stroke="#aaa"/>
<g id="BrowserAddress"><rect x="176" y="922" width="11" height="10" rx="1" fill="#333"/><path d="M178 922V919A3.5 3.5 0 0 1 185 919V922" fill="none" stroke="#333" stroke-width="2"/><text x="199" y="934" font-family="Arial" font-size="22" fill="#888">www.polyu.edu.hk/learn...</text></g>
<g id="BrowserReloadUnimplemented"><path d="M521 914A13 13 0 1 0 523 930M520 909L525 915L518 920" fill="none" stroke="#444" stroke-width="2.7" stroke-linecap="round"/></g>
</svg>'''
q=D/'room-preview-login.svg';q.write_text(svg)
(D/'room-preview-login-source.json').write_text(json.dumps({'status':'prepared_not_imported','state_id':'S-PREVIEW-LOGIN','frame_dimensions':[576,1024],'source_evidence_id':'E-ROOM-PREVIEW-CONTROLS-10','source_file':'../../evidence/2026-09-30-room-preview-controls/14-login-boundary.png','source_sha256':h(source),'file':q.name,'sha256':h(q),'wordmark_file':'assets/'+logo.name,'wordmark_sha256':h(logo),'wordmark_crop_xyxy':[46,211,437,292],'limitations':['Editable reconstruction approximates typography/icons; wordmark raster from observed public login.','Placeholder fields and Login/ForgotPassword/More/Close/Reload not connected; no credentials submitted.','Browser Back observed against current AX-only page; historical public Preview layout return is not yet integrated with this new context.','Fullscreen-derived1024px source, not guaranteed real phone geometry.']},ensure_ascii=False,indent=2)+'\n')
print(q)
