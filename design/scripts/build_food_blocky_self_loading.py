"""Prepare the observed Taiwanese self-result detail with inline loading mark.
Source generation only; actual Figma import/display is recorded separately.
"""
from pathlib import Path
import base64,hashlib,json,xml.etree.ElementTree as E
from PIL import Image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';N='{http://www.w3.org/2000/svg}';X='{http://www.w3.org/1999/xlink}'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    cov=json.loads((R/'docs/polyulife/coverage.json').read_text());ev=next(x for x in cov['evidence'] if x['id']=='E-FOOD-TAGS-07');src=(R/'docs/polyulife'/ev['path']).resolve();assert sha(src)==ev['sha256'];im=Image.open(src).convert('RGB');assert im.size==(576,1024)
    assets=[]
    for name,box in [('hero',(151,100,429,326)),('inline-loading',(258,758,318,818)),('expand-map',(445,755,518,824))]:
        file='assets/food-oct3-blocky-self-'+name+'.png';im.crop(box).save(D/file);assets.append(dict(file=file,sha256=sha(D/file),dimensions=[box[2]-box[0],box[3]-box[1]],crop_xyxy=list(box),source_evidence_id=ev['id'],source_sha256=ev['sha256'],limits='Unmodified public source crop; cursor/halo retained if present; raster appearance only'))
    root=E.parse(D/'food-oct3-blocky-detail.svg').getroot();root.find(N+'title').text='Block Y self-result detail — observed inline map loading';root.find(N+'desc').text='Finite archived Taiwanese caller sample; independent editable text and raster hero/loading/button appearance. No transition duration or settled map proven; exact geometry/fonts unknown.'
    next(x for x in root.iter() if x.get('id')=='ScreenBackground').set('fill','#F7F9F6');content=next(x for x in root.iter() if x.get('id')=='DetailContent');card=next(x for x in content if x.tag==N+'rect' and x.get('x')=='18' and x.get('height')=='1013');idx=list(content).index(card);content.remove(card);content.insert(idx,E.Element(N+'path',dict(id='ObservedCardContour',d='M18 100H557V986Q557 1024 519 1024H56Q18 1024 18 986Z',fill='#FFFFFF',stroke='#C5C9CA',**{'stroke-width':'1'})))
    def image(group,asset):
        box=asset['crop_xyxy'];g=next(x for x in root.iter() if x.get('id')==group);g.clear();g.set('id',group);E.SubElement(g,N+'image',dict(x=str(box[0]),y=str(box[1]),width=str(box[2]-box[0]),height=str(box[3]-box[1]),**{X+'href':'data:image/png;base64,'+base64.b64encode((D/asset['file']).read_bytes()).decode()}))
    image('PublicHero',assets[0]);image('PublicInlineMap',assets[1]);next(x for x in root.iter() if x.get('id')=='PublicInlineMap').set('id','ObservedInlineMapLoading');image('ExpandMap',assets[2]);E.register_namespace('',N[1:-1]);E.register_namespace('xlink',X[1:-1]);file='food-oct3-blocky-self-map-loading.svg';E.ElementTree(root).write(D/file,encoding='unicode',xml_declaration=True)
    path=D/'food-oct3-blocky-self-loading-sources.json';old=json.loads(path.read_text()) if path.exists() else {};rec=dict(file=file,sha256=sha(D/file),state_id='S-FOOD-OCT3-BLOCKY-SELF-MAP-LOADING',source_evidence_ids=['E-FOOD-TAGS-07'],dimensions=[576,1024],assets=assets,status='prepared_not_imported',node_id=None,base_source_file='food-oct3-blocky-detail.svg',base_source_sha256=sha(D/'food-oct3-blocky-detail.svg'),limits=['Archived native self-detail sample only; no settled nested map or loading latency saved.','Card bottom and radius38 approximate visible reconstruction; fonts/geometry unverified.','Hero includes captured cursor/halo; loading and expand-map are separate raster crops, not interactive controls.','No native input or Figma import by this generator; no caller/Back/zoom/map navigation.'])
    if old.get('sha256')==rec['sha256']:rec.update(old)
    path.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(file=file,source_hash=rec['sha256'],assets=assets),ensure_ascii=False))
if __name__=='__main__':main()
