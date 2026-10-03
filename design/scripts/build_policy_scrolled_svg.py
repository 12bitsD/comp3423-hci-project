"""Reconstruct two observed, noncontiguous policy viewports, not whole documents."""
from pathlib import Path
from html import escape
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'design/polyulife'

def lines(words, y, weight=400, underline=False):
    return ''.join(f'<text x="103" y="{y+i*33.1:.1f}" font-family="Roboto" font-size="21.7" font-weight="{weight}" fill="#292929"'+(' text-decoration="underline"' if underline else '')+f'>{escape(s)}</text>' for i,s in enumerate(words))

privacy = lines(['so long as necessary to fulfil the purpose','of collection; and will erase your personal','data thereafter. We will ensure the security','of your personal data and protect them','from unauthorised access.'],159)
privacy += '<text x="65" y="341" font-family="Roboto" font-size="21.7" fill="#A3273D">4.</text>'
privacy += lines(['We will keep your personal data','confidential. Your personal data will be','used (and disclosed) to third parties for','the purposes for which they were','collected, and where we are required to do','so by law and as specified in the relevant','Personal Information Collection','Statement.'],341)
privacy += '<text x="65" y="623" font-family="Roboto" font-size="21.7" fill="#A3273D">5.</text>'
privacy += lines(['You have the right to request access to','and correction of your personal data held','by us. Any data access and correction','request should be made in writing to the','Departmental Personal Data Officer of the','relevant department as specified in the','relevant Personal Information Collection','Statement or Data Protection Officer','(dpo.email@polyu.edu.hk). Data access','request should be made by completing','and submitting the Data Access Request'],623)
privacy += '<path d="M103 890 H351 M288 956 H494" stroke="#292929" stroke-width="1"/>'
terms = lines(['websites or the information, products,','advertising, or other materials available on','those websites.'],186)
terms += '<text x="65" y="302" font-family="Roboto" font-size="21.7" fill="#A3273D">3.</text>'
terms += lines(['Intellectual Property Rights'],302,700)
terms += lines(['All intellectual property rights subsisting in','respect of this Website belong to us or','have been lawfully licensed to us for use','on this Website. All rights under applicable','laws are hereby reserved. Except with our','express written permission, you are not','allowed to upload, post, publish,','reproduce, transmit or distribute in any','way any component of this Website itself','or create derivative works with respect','thereto, as this Website is copyrighted','under applicable laws.'],352)
terms += lines(['You may only download such part of this','Website as is expressly permitted to be','downloaded for the purposes specified.','You have no rights in or to the contents','and you will not use them except as','permitted under these Terms of Use.'],766)

records=[]
for slug,title,state,eid,file,body,thumb in [
    ('privacy','Privacy Policy','S-PRIVACY-SCROLLED','E-MENU-N-19','native-menu-192932-privacy-scrolled-01.png',privacy,(402,216)),
    ('terms','Terms of Use','S-TERMS-SCROLLED','E-MENU-N-24','native-menu-193010-terms-scrolled-01.png',terms,(388,204)),
]:
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="576" height="970" viewBox="0 0 576 970" fill="none"><title>{title} — observed scrolled viewport</title><desc>Editable finite reconstruction of {eid}. Only legible visible lines transcribed. Noncontiguous with initial page; no invented intermediate text, exact scroll offset or document boundaries. Approximate font/geometry. Cursor omitted. Top and bottom clipped fragments remain incomplete.</desc><rect width="576" height="970" fill="#F7F9F6"/><g id="EmbeddedPublicWebPage"><rect x="18.5" y="100" width="539" height="870" fill="white" stroke="#CACFD0"/><g id="ObservedBody">{body}</g><rect x="19" y="101" width="519" height="53" fill="white"/><text x="81" y="135" font-family="Roboto" font-size="22" fill="#292929">{title}</text><rect x="540.5" y="102" width="14" height="814" rx="7" fill="white" stroke="#EEEEEE"/><rect x="525" y="{thumb[0]}" width="13" height="{thumb[1]}" rx="6.5" fill="#BFBFBF"/></g><g id="Header"><rect x="0.5" y="0.5" width="575" height="99" fill="white" stroke="#E1E1E1"/><g id="Back"><rect x="12" y="36" width="52" height="54" fill="white" fill-opacity="0.001"/><path d="M34.5 57.5L27 65L34.5 72.5" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g><text x="288" y="75.5" fill="#141414" font-family="Roboto" font-size="27" text-anchor="middle">{title}</text></g></svg>'''
    output=DEST/f'{slug}-scrolled.svg';output.write_text(svg+'\n')
    source=ROOT/'evidence/2026-09-28-full-audit'/file
    records.append({'state_id':state,'source_evidence_ids':[eid],'native_path':'../../evidence/2026-09-28-full-audit/'+file,'native_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'output':output.name,'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'dimensions':[576,970],'limits':['Finite visible text only; intermediate text and full document boundaries missing.','Editable transcription with approximate typography and geometry; cursor omitted.','Prototype input proxy does not establish native keyboard behavior or continuous scrolling.','Clipped edge fragments incomplete; links not configured.']})
(DEST/'policy-scrolled-sources.json').write_text(json.dumps({'sources':records},ensure_ascii=False,indent=2)+'\n')
