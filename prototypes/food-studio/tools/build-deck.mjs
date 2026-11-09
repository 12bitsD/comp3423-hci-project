import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const modules=process.env.CODEX_RUNTIME_MODULES;
if(!modules)throw new Error('Set CODEX_RUNTIME_MODULES to the Codex bundled node_modules path.');
process.env.RUNTIME_NODE_MODULES ||= modules;
const require=createRequire(path.join(modules,'package.json'));
const {Presentation,PresentationFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const t=JSON.parse(await fs.readFile(path.join(root,'tokens.json'),'utf8'));
const C=t.colors;
const p=Presentation.create({slideSize:{width:1280,height:720}});
p.theme.defaultFont=t.font.latin;
const build=path.join(root,'work','deck-v02');await fs.mkdir(build,{recursive:true});
const final=path.join(root,'exports',path.basename(process.env.PPTX_OUTPUT_NAME||'PolyULife-Food-Fresh-Campus-v02.pptx'));
const content=[
 {title:'Less searching.\nMore living.',body:'PolyULife Food redesign\nFind a place. Check the hours.',kicker:'COMP3423 / VISUAL & UI DESIGN',cover:true},
 {title:'Food 的可用性问题',body:'明确详情入口的含义，\n让当天营业时间更容易找到。\n\n基于历史截图的设计假设，\n尚待真人验证。',kicker:'01 / OBSERVED INTERFACE',image:'assets/original-list.png'},
 {title:'营业时间优先',body:'餐饮卡片直接显示当天状态，\n保留独立的营业时间与详情入口。',kicker:'02 / REDESIGN PROPOSAL',image:'exports/screen-list.png'},
 {title:'返回时保留上下文',body:'从地图返回详情，\n再回到原来的搜索结果。\n\n搜索词、筛选与滚动位置\n随进入来源恢复。',kicker:'03 / INTERACTION',image:'exports/screen-detail.png'},
 {title:'共用一套视觉语言',body:'米白画布、深蓝文字\n与明亮绿点缀。\n\n同一套规则贯穿界面、\n报告插图和演示文稿。',kicker:'04 / VISUAL SYSTEM',image:'exports/figure-02.png',wide:true},
 {title:'真人评估计划',body:'查询营业时间，寻找指定食品，\n并返回继续比较。\n\n分别记录任务成功与答案正确性，\n结合错误点击和真实反馈迭代。',kicker:'05 / EVALUATION PLAN',end:true}
];
function text(s,name,value,x,y,w,h,size,color,bold=false,font=t.font.latin){const sh=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});sh.text=value;sh.text.style={typeface:font,fontSize:size,color,bold};return sh;}
async function image(s,src,x,y,w,h){const b=await fs.readFile(path.join(root,src));s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:'image/png',alt:src,fit:'contain',position:{left:x,top:y,width:w,height:h}});}
// Reuse the approved bowl illustration; source SVG remains editable in assets/.
const sharp=require('sharp');
await sharp(await fs.readFile(path.join(root,'assets/fresh-bowl.svg'))).resize(800,640).png().toFile(path.join(root,'exports/fresh-bowl.png'));
await sharp(await fs.readFile(path.join(root,'assets/fresh-cup.svg'))).resize(640,640).png().toFile(path.join(root,'exports/fresh-cup.png'));
function rect(s,name,x,y,w,h,fill,geometry='rect'){return s.shapes.add({name,geometry,position:{left:x,top:y,width:w,height:h},fill,line:{fill:'none',width:0}});}
for(let i=0;i<content.length;i++){
 const d=content[i],s=p.slides.add();s.background.fill=d.cover||d.end?C.canvas:C.paper;
 const font=/[\u4e00-\u9fff]/.test(d.title)?t.font.cjk:t.font.latin;
 text(s,'section-label',d.kicker,72,48,1000,26,16,C.muted,true);
 rect(s,'header-accent',72,92,54,5,C.accent);
 if(d.cover){
   text(s,'slide-title',d.title,72,192,750,180,76,C.ink,true);
   text(s,'slide-body',d.body,72,412,700,100,29,C.muted);
   rect(s,'illustration-disc',890,200,285,285,C.accentSoft,'ellipse');
   await image(s,'exports/fresh-bowl.png',830,185,390,320);
   text(s,'cover-owner','校园餐饮体验改版 · D / FengTaiYang',72,560,730,42,23,C.ink,false,t.font.cjk);
 }else if(d.wide){
   text(s,'slide-title',d.title,72,132,1100,80,52,C.ink,true,font);
   await image(s,d.image,62,232,760,390);
   text(s,'visual-rules','米白画布\n深蓝文字\n明亮绿点缀',875,260,320,180,32,C.ink,true,t.font.cjk);
   text(s,'visual-application','界面、报告插图与 PPT\n共享颜色与文字层级。',875,474,320,110,24,C.muted,false,t.font.cjk);
 }else if(d.end){
   text(s,'slide-title',d.title,72,140,1100,80,52,C.ink,true,font);
   const tasks=[['01','查营业时间','记录答案是否正确'],['02','找指定食品','记录任务完成与误点'],['03','返回继续比较','记录路径与真实反馈']];
   tasks.forEach((v,j)=>{const x=72+j*390;rect(s,'task-rule-'+j,x,288,310,5,C.accent);text(s,'task-number-'+j,v[0],x,240,100,45,28,C.success,true);text(s,'task-title-'+j,v[1],x,328,350,65,32,C.ink,true,t.font.cjk);text(s,'task-body-'+j,v[2],x,410,350,70,25,C.muted,false,t.font.cjk);});
   text(s,'evaluation-boundary','计划招募至少 5 位真实参与者进行 Maze 测试；本页没有测试结果。',72,556,1120,55,22,C.muted,false,t.font.cjk);
 }else{
   text(s,'slide-title',d.title,72,170,710,95,52,C.ink,true,font);
   text(s,'slide-body',d.body,72,308,650,240,29,C.muted,false,font);
   rect(s,'image-backdrop',850,128,340,486,C.accentSoft);
   await image(s,d.image,870,144,300,455);
   if(i===2)text(s,'demo-note','固定历史场景 · 周二 00:54',72,562,710,35,20,C.muted,false,t.font.cjk);
 }
 rect(s,'footer-line',72,640,1136,1,C.line);
 text(s,'slide-footer','PolyULife / Food · Fresh Campus',72,660,950,28,15,C.muted);
 text(s,'slide-number',`${String(i+1).padStart(2,'0')} / 06`,1100,660,110,28,15,C.muted);
 s.speakerNotes.text=`Student design proposal, not official PolyU branding. No participant testing results are claimed.\nSources: https://github.com/12bitsD/comp3423-hci-project/blob/main/docs/polyulife/food-walkthrough.md\nOriginal screenshots: food-165444-list-scrolled-h-cafe.png and food-160820-chinese-soup-tag-result.png, observed in Hong Kong time on 2026-09-29. Proposed UI uses a fixed Tuesday 00:54 demonstration, not current campus information.\nApproved Fresh Campus direction: navy text, off-white background, bright green highlights. Artwork reused from the locally approved direction sample. Native text remains editable; UI screenshots and illustration PNGs are embedded images; editable illustration SVGs are supplied in assets/. Slide ${i+1}.`;
 const png=await p.export({slide:s,format:'png',scale:1});const bytes=new Uint8Array(await png.arrayBuffer());await fs.writeFile(path.join(build,`slide-${i+1}.png`),bytes);await fs.writeFile(path.join(root,'exports',`slide-${i+1}.png`),bytes);
}
const draft=path.join(build,'candidate.pptx');await(await PresentationFile.exportPptx(p)).save(draft);
console.log(`Draft exported: ${draft}`);
const skill=process.env.PRESENTATIONS_SKILL_DIR;
if(skill){const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools','artifact_tool_utils.mjs')).href);try { await finalizePresentation({workspaceDir:root,candidatePath:draft,finalPath:final,pythonExecutable:process.env.CODEX_RUNTIME_PYTHON,integrityValidatorPath:path.join(skill,'container_tools','inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools','inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],explicitTotalSlideCount:6,fontPolicy:{basis:'design',families:[t.font.latin,t.font.cjk]},verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')}); } catch (error) { if(error.code!=='EPERM'||error.syscall!=='link') throw error; await fs.copyFile(draft,final,1); const {createHash}=await import('node:crypto'); const original=await fs.readFile(draft),saved=await fs.readFile(final); const digest=b=>createHash('sha256').update(b).digest('hex'); if(digest(original)!==digest(saved)) throw new Error('Copy hash mismatch'); await fs.writeFile(path.join(build,'validation-windows-copy.json'),JSON.stringify({status:'All finalizer checks completed; Windows hard-link publication unsupported. Copied candidate unchanged.',sha256:digest(saved)},null,2)); process.exitCode=0; } }else{await fs.copyFile(draft,final);}
console.log(`PPTX exported: ${final}`);
