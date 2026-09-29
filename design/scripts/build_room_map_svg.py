"""AG206 observed map snapshots with editable header/back.
Arrow-key prototype controls substitute native AX slider actions; no live map claim.
"""
from pathlib import Path
from base64 import b64encode
import hashlib,json
from PIL import Image
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';A=D/'assets';E=R/'evidence/2026-09-28-full-audit'
rows=[('initial','room-map-140441-ag206-campus.png','S-MAP','E-MAP'),('zoomed','room-map-140635-ag206-zoomed.png','S-MAPZOOM','E-MAPZOOM'),('out','room-map-140652-ag206-campus.png','S-MAPOUT','E-MAPOUT')]
manifest=[]
for label,filename,state,evidence in rows:
 src=E/filename;asset=A/('room-map-'+label+'-geography.png');im=Image.open(src).convert('RGB');assert im.size==(576,970);im.crop((0,100,576,970)).save(asset)
 manifest.append({'file':asset.name,'source':str(src.relative_to(R)),'source_evidence_id':evidence,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'crop':[0,100,576,970],'dimensions':[576,870],'sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'transformation':'Crop only; captured cursor and transient map labels deliberately retained, no invented pixel repair.'})
 data=b64encode(asset.read_bytes()).decode()
 body=f'<rect width="576" height="970" fill="#FFFFFF"/><g id="ObservedMapGeography"><image x="0" y="100" width="576" height="870" preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/></g>'
 header='<g id="Header"><rect x="0.5" y="0.5" width="575" height="99" fill="#FFFFFF" stroke="#E1E1E1"/><g id="Back"><rect x="12" y="36" width="52" height="54" fill="#FFFFFF" fill-opacity="0.001"/><path d="M34.5 57.5L27 65L34.5 72.5" fill="none" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g><text x="288" y="75.5" fill="#080808" font-family="sans-serif" font-size="27" text-anchor="middle">AG206</text></g>'
 (D/('room-map-'+label+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="970" viewBox="0 0 576 970"><title>AG206 map — {label}</title><desc>Source {filename}. Header and Back are editable. Map geography, labels and captured pointer artifact are raster evidence, not live or editable map objects. Prototype ArrowUp/ArrowDown represent observed AX Increment/Decrement results, not observed native keyboard input. No arbitrary pan, zoom bounds or Google Maps handoff is implemented.</desc>{body}{header}</svg>')
(D/'room-map-assets.json').write_text(json.dumps({'assets':manifest,'scope':'Reviewed public campus map, no personal account or user-position marker. Cursor/halo remains a known reconstruction deviation.'},ensure_ascii=False,indent=2)+'\n')
print('Built three observed Room map SVGs and public crop provenance.')
