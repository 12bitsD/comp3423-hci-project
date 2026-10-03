"""Prepare LibCafe card/background correction from archived visible evidence.

The small contour SVG replaces one actual Figma child. The full SVG records
the intended/current structure, not a Figma export or exact native geometry.
"""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as E

R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';N='{http://www.w3.org/2000/svg}'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    original=D/'food-oct3-libcafe-detail.svg';root=E.parse(original).getroot()
    bg=next(n for n in root.iter() if n.get('id')=='ScreenBackground')
    assert bg.get('fill')=='#FFFFFF';bg.set('fill','#F7F9F6')
    content=next(n for n in root.iter() if n.get('id')=='DetailContent')
    card=next(n for n in content if n.tag==N+'rect' and n.get('x')=='18' and n.get('height')=='1013')
    index=list(content).index(card);content.remove(card)
    shape=E.Element(N+'path',dict(id='LibCafeObservedCard',d='M18 100H557V986Q557 1024 519 1024H56Q18 1024 18 986Z',fill='#FFFFFF',stroke='#C5C9CA',**{'stroke-width':'1'}))
    content.insert(index,shape)
    inline=next(n for n in root.iter() if n.get('id')=='PublicInlineMap')
    image=inline.find(N+'image');assert image.get('height')=='309';image.set('height','307')
    full=D/'food-oct3-libcafe-card-corrected.svg';E.ElementTree(root).write(full,encoding='unicode',xml_declaration=True)
    helper=D/'food-oct3-libcafe-card-contour.svg'
    helper.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="539" height="924" viewBox="0 0 539 924"><path id="LibCafeObservedCard" d="M0 0H539V886Q539 924 501 924H38Q0 924 0 886Z" fill="#FFFFFF" stroke="#C5C9CA" stroke-width="1"/></svg>\n')
    p=D/'food-oct3-libcafe-card-correction.json';old=json.loads(p.read_text()) if p.exists() else {}
    rec=dict(original_source_file=original.name,original_source_sha256=sha(original),file=full.name,sha256=sha(full),contour_file=helper.name,contour_sha256=sha(helper),state_id='S-FOOD-OCT3-LIBCAFE-DETAIL',source_evidence_ids=['E-FOOD-MENU-05','E-FOOD-MENU-07'],root_node_id='949:248',status='prepared_for_actual_UI_correction',before_card=dict(position=[18,100],dimensions=[539,1013]),after_card=dict(position=[18,100],dimensions=[539,924],bottom_corner_reconstruction_radius=38),background_color='#F7F9F6',inline_map_height_before=309,inline_map_height_after=307,limits=['Card bottom contour and dimensions inferred from visible archived viewport; exact native card/window boundary unknown.','Only ScreenBackground fill, card contour and inline map height309->307 changed; old SVG/asset bytes retained.','Full corrected source records intended/actual UI edits, not Figma export. No new navigation/scrolling behavior.'])
    if old.get('sha256')==rec['sha256']:rec.update(old)
    p.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(file=full.name,contour_file=helper.name,figma_mutations=0)))

if __name__=='__main__':main()
