# Virtual Assistant 图片填充修复与回放（2026-09-30）

这是通过 Mac Computer Use 操作实际 Figma 编辑器和 Present 的原型验证，不是新的 PolyULife 原生观察，也不是真人评估。原生仍为135状态/268动作（193 observed、75 not_attempted）；本次原生AX和截图读取先后超时，没有执行待补控件。连接失败不作为 App 缺陷。完整应用完成状态保持 `not_verified`。

## 修复前复现

从 More `12:435` 点击 Virtual Assistant，详情 `42:6` 有头图；`here → Disclaimer42:43 → ACCEPT → Welcome42:111 → X` 返回后，头图消失。无输入再读仍缺图。编辑器同一图层可见。

- [首次有图](../../evidence/2026-09-30-va-image-repair/01-detail-baseline.png)
- [返回后缺图的无输入复查](../../evidence/2026-09-30-va-image-repair/05-web-return-baseline-held.png)
- [图片修复前后拼图](../../evidence/2026-09-30-va-image-repair/contact-sheet.png)

`04-web-return-baseline` 的URL在截图之前采样，仍为Welcome，而截图已显示详情；保留 `node_match:false`，以05无输入读取确认最终节点。此差异不能单独证明导航失败。

## 原始素材重新载入

使用编辑器 Image fill → Upload from computer 上传仓库已有PNG，不改源像素、导航连接或图层几何。来源见原生 `E-ASSISTANT-DETAIL`、`E-ASSISTANT-DISCLAIMER`、`E-ASSISTANT-WELCOME`。表内位置为画板坐标。

| 根画板 | 图片图层 | 原素材 | 位置与尺寸 |
| --- | --- | --- | --- |
| 详情42:6 | 42:12 | virtual-assistant-hero.png | 19,100；538×214 |
| Disclaimer42:43 | 42:77 | virtual-assistant-avatar.png | 32,334；64×59 |
| Disclaimer42:43 | 42:65 | virtual-assistant-logo.png | 35,192；63×63 |
| Welcome42:111 | 42:133 | virtual-assistant-logo.png | 35,192；63×63 |
| Welcome42:111 | 42:145 | virtual-assistant-avatar.png | 32,334；64×59 |

[头图编辑记录](../../design/polyulife/virtual-assistant-image-repair.json)和[四处网页图片记录](../../design/polyulife/virtual-assistant-web-image-repair.json)保存素材哈希、节点、截图与填充读回。头图及三处完整读回保留STRETCH/尺寸，出现thumbnail与color management属性变化；这些变化不是渲染根因证明。Disclaimer头像上传后的AX diff省略未改变字段，记录其独立读回限制。展开图素材未重传。

## 两阶段实际回放

头图重传后，主动刷新Present一次，随后连续两轮展开/X、here/ACCEPT/X、Back/More再次进入，两轮之间不刷新。详情头图保持可见，但第二轮网页校徽和小头像消失，见[第二轮Welcome](../../evidence/2026-09-30-va-image-repair/21-welcome-round2.png)。因此第一阶段只确认头图局部改善，不能称整条流程视觉通过。

随后重传Disclaimer及Welcome各自的校徽和小头像，再主动刷新一次。又连续执行两轮相同七步路径，两轮之间不刷新；网页校徽/头像和返回后的头图均可见。

- [最终两轮拼图](../../evidence/2026-09-30-va-web-image-repair/contact-sheet.png)
- [第三轮Welcome](../../evidence/2026-09-30-va-web-image-repair/34-welcome-round3.png)与[第四轮Welcome](../../evidence/2026-09-30-va-web-image-repair/41-welcome-round4.png)
- [第三轮返回详情](../../evidence/2026-09-30-va-web-image-repair/35-web-return-round3-held.png)与[第四轮返回详情](../../evidence/2026-09-30-va-web-image-repair/42-web-return-round4-held.png)
- [最终再次进入](../../evidence/2026-09-30-va-web-image-repair/44-detail-reentry-round4.png)

ACCEPT只是Figma按钮跳转，没有在真实服务接受协议、输入或发送聊天消息。现有七条连接没有修改，原始失败运行 `PROTO-VA-V2-001` 及其证据保持不变。

## 差异与验证限制

两份[头图阶段清单](../../evidence/2026-09-30-va-image-repair/manifest.json)、[网页阶段清单](../../evidence/2026-09-30-va-web-image-repair/manifest.json)合计49个脱敏PNG，含两张拼图；41次Present截图、6次编辑器截图。全部保留时间、哈希、尺寸及URL/预期节点。

共26项原型裁片比较：10项相等、16项不等。第一阶段16项中6项相等；第二阶段10项中4项相等，分别是展开关闭后首次详情、两轮Disclaimer、两轮Welcome、两轮More。第二阶段其余6项差异集中于头图或展开图区域，图片仍可见；没有确定差异根因，不宣称逐像素一致。修复前缺图、网页校徽/头像缺失与图片区域差异分别记录。

除了04外，18、35、42也出现转场URL与期望节点不一致；均保留原始采样并用随后无输入读取确认目标。不能把转场采样当作稳定失败，也不能丢弃它。

公开截图遮盖账户/协作者头像区域；原始AX及未脱敏截图保持在忽略目录。结构验证检查引用/哈希/尺寸/链接，不建立完整覆盖率。

`D-VA-HERO-RETURN-RENDER` 和新发现的 `D-VA-WEB-IMAGE-RETURN-RENDER` 标为 `partially_resolved`：本次样例显示改善，所有会话、调用者、加载状态与整体视觉尚未通过。聊天输入/发送、问号、部门链接、网页控件和原生来源状态差异仍待继续观察与重建。
