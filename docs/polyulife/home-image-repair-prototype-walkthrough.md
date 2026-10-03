# Home 预览图片填充重传与 Calendar 返回回归 — 2026-09-30

通过 Computer Use 在既有 Monday、Tuesday Home 图片层重新上传公开素材后，六个保存的返回样例均保留图片。九项裁片比较五项相等、四项不等；四处差异均位于底部局部，因此视觉完全一致仍未通过。全应用仍 `not_verified`，本批没有新增原生观察或画板、控件。

## 修改及素材来源

Monday 根67:569的图片67:660，Tuesday根67:694的图片67:786，均通过Design→Image→Upload from computer上传[公开裁剪素材](../../design/polyulife/assets/home-demo-public-preview.png)。实际属性读回仍为x44、y899、489×22，原图902×40、STRETCH。图片内容哈希保持相同；可见属性imageShouldColorManage从false变true并出现thumbnail，这只是UI读回差异，不是已证明的故障原因。没有替换Home根、重建控件或修改滚动结构。来源是历史公开home-134424-navigation-only.png裁片(84,483,986,523)，已由build_study_svg.py记录；私人课表和身份仍是合成DEMO。

## 保存的实际回放

01保留上一轮返回后的空白图片。02保存Monday上传后的编辑器。03是重载过程中的Figma加载画面；04才是图片可见的Monday基线。05进入Week，06返回Monday；07–09经过Month、Events、History并直接Home返回。10保存Tuesday图片上传后的编辑器。11第一次点击Tuesday位置未命中，仍为Monday并有热点反馈；12修正点击后显示29/Today。13–14为Tuesday Week往返，15–17经Month、Events、History直接Home返回；18–20再次经过全部模式并从History回Week再回Tuesday。21尝试Tuesday→Monday未成功，保持Tuesday；该反向日期动作原本未配置，没有因此添加推测的原生行为。22直接重开Monday，23–25完成History→Week→Home的完整循环。

06、09、14、17、20、25实际保存截图的照片都可见。04/06、04/22、12/14、13/19、05/24裁片相等；04/09、22/25、12/17、12/20不等，差异框均为应用裁片内(22,588,358,613)。照片保留不等于像素完全相等；未确定这些局部差异的原因。即时工具截图与随后保存截图分开判断，结论以保存文件为准。[25张截图、哈希与比较](../../evidence/2026-09-30-home-image/manifest.json)及[对照图](../../evidence/2026-09-30-home-image/contact-sheet.png)可复查。

## 结论边界

既有Calendar缺图偏差追加为partially_resolved：本轮短样例中照片保留，历史失败证据不删除。完整长期稳定性、更多入口、其它日期与滚动返回、原生保真仍待验证。此处是Figma原型回归，不是PolyULife缺陷结论，不新增原生成功次数，也不是真人Maze数据。[修复属性记录](../../design/polyulife/home-image-repair.json)供Agent接力。累计仍121映射画板、282控件；新增三组回放后59次运行。
