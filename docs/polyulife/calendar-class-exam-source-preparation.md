# Calendar Class / Exam / Notice 来源准备

本批使用已经归档的 [October 2 原生补查](native-calendar-resume-20261002.md)，准备 **13 份可编辑 SVG、15 条原生动作对应的连线计划及 1 条演示延时计划**。文件已本地渲染并检查，**尚未导入、连线或在 Figma Present 回放**。原生状态/动作和正式 Figma 映射数量没有增加；完整应用仍 `not_verified`。

[来源与哈希清单](../../design/polyulife/calendar-oct2-class-exam-sources.json)、[未配置连线清单](../../design/polyulife/calendar-oct2-class-exam-plan.json)和[本地渲染清单](../../evidence/2026-10-03-calendar-class-exam-source/manifest.json)分别记录素材、计划和实际本地输出。[渲染总览](../../evidence/2026-10-03-calendar-class-exam-source/contact-sheet.png)逐格标明 LOCAL SOURCE / NOT IMPORTED；它不是新的原生截图或 Figma 回放。

## 来源与状态

所有页面为原生全屏样例归一化后的 576×1024 参考，固定 October 2；不宣称 iPhone 真实视口保真。日历文字和矢量复用已观察的公共界面结构，私人课程值用合成 DEMO，个人日期点阵省略。

| SVG 文件（`design/polyulife/`） | 原生证据 | 保留的语义 |
| --- | --- | --- |
| `calendar-oct2-draft-class-none.svg` | 11 | 应用结果仍 None，草稿单选 Class |
| `calendar-oct2-class.svg` | 12、19 | 应用 Class；课程卡显示合成信息；详情返回同日期/类别 |
| `calendar-oct2-class-detail.svg` | 13、18 | 省略号进入课程详情，包含 Class Type、Class Notice 和地图 |
| `calendar-oct2-notice-loading.svg` | 14 | 内嵌网页加载标识 |
| `calendar-oct2-notice-blank.svg` | 15、17 | 标识消失、正文空白；不等于网页成功加载 |
| `calendar-oct2-notice-menu.svg` | 16 | 系统浏览器、Share via、Copy link、Cancel |
| `calendar-oct2-draft-class-class.svg` | 20 | 重开 Class，原应用背景与勾选均 Class |
| `calendar-oct2-draft-none-class.svg` | 21 | 草稿取消 Class，原应用背景仍 Class |
| `calendar-oct2-draft-exam-class.svg` | 22 | 草稿单选 Exam，原应用背景仍 Class |
| `calendar-oct2-exam.svg` | 23 | 应用 Exam；这个日期 No event |
| `calendar-oct2-draft-exam-exam.svg` | 24 | 重开 Exam，应用背景与勾选均 Exam |
| `calendar-oct2-draft-none-exam.svg` | 25 | 草稿取消 Exam，原应用背景仍 Exam |
| `calendar-oct2-draft-payment-exam.svg` | 26 | 草稿单选 Payment，原应用背景仍 Exam |

表内序号指 [原生清单](../../evidence/2026-10-02-native-calendar-resume/manifest.json) 的公开截图编号。生成器核对每张原生截图的哈希与状态关联，计划中的 15 个动作逐一取自 observed 台账；不把通用取消规则自动扩展到未执行的来源状态。

## 连线与后续验收

入口是既有全不选重开画板 `791:873` 的 Class 控件，需先在实时 Figma 中核对该节点。计划接入 Class 草稿→Apply→Class 课程卡→省略号→详情→Notice 加载→空白→More→菜单→Cancel→空白→X→详情→Back→Class；随后 Class 筛选清空→Exam 草稿→Apply→Exam→重开清空→Payment 草稿。

各连线目前均为 `planned_not_configured`，没有分配新 Figma 节点。Navigate to 是准备阶段建议的整帧实现；必须在实际编辑与回放中验证背景、返回与调用者保留，不据此推断原生页面栈。加载→空白拟用 800ms 演示延时，既不是实测原生等待时间，也不是成功加载的证据。

Payment Apply 的输入与结果仍未知，因此没有创建 Payment 结果画板或 Apply 连线。课程地图全屏/手势、Notice Reload、系统浏览器、分享、复制，以及未观察的草稿 X 出口保持未完成。只有 Cancel 和空白网页 X 的已观察返回被列入这次计划。主 Home/More 调用路径与保留模式仍待整合；本批不替代完整 Calendar 或完整应用的验收。

## 可编辑与视觉检查

课程详情的标题、说明、教师、时间和地点都是明确 DEMO 文本，不能反向当作原生字段内容。Class Type 的 `LEC+TUT/LAB`、Class Notice 和菜单文字来自公开原生截图。文字、背景、按钮、勾选和图标近似均为可编辑矢量；原图的个人信息遮罩不被恢复。

地图是公开脱敏截图 13 的裁片 `(35,677,541,984)`，保留校园地理标签和 Google 标识，覆盖层中的全屏箭头重建为可编辑控件，但尚未配置。加载标识是截图 14 的裁片 `(260,532,319,592)`。两份 PNG 的尺寸、源证据哈希和裁片范围记录在来源清单；它们不是实时地图或矢量校徽。

检查了 13 格总览及详情单页：筛选应用背景按 None/Class/Exam 保留；课程和地图内容在画板内；菜单和网页空白状态可辨。字体指标、图标形状、卡片文本、按钮位置和裁片地图仍存在近似或替代，未进行原生像素保真验收。后续导入时还须检验嵌入图片是否实际可见，不能只以 SVG 含有图片数据为通过。

## 本轮连接与接力

GitHub 先前成果已推送并核对到 `4f79a3d`。本次发现 PolyULife 运行项及 Wrapper 路径，但连接实际窗口超时、没有建立 app 句柄。随后 Computer Use 调用报告工具不可用，可调用工具清单也未暴露该能力。因此本轮没有新原生执行，也没有新增 Figma 导入；不把超时直接判定为 App 崩溃或当前锁屏。

恢复工具后，按 [skill](../../.agents/skills/polyulife-ui-analysis/SKILL.md) 重新读取实际原生窗口，先确认 Payment 当前状态；继续使用已有 Figma 文件，核对 `791:873` 后导入本批 SVG、读回尺寸/图层/图片、配置计划中的连接。实际回放 Class/Notice 往返及 Exam/Payment 草稿链，保存失败和成功截图，再登记正式节点与控件。主调用者、其他分类/日期与地图等剩余交互继续逐项补查。

本地生成命令：

```bash
python3 design/scripts/build_calendar_class_exam_oct2.py
```

需要 Pillow；可选 `--render-dir evidence/2026-10-03-calendar-class-exam-source` 另需 resvg_py。生成器只写本地来源与计划，不操作 App/Figma、不修改覆盖台账；若来源已经标为导入，将拒绝覆盖导入记录。不要重跑原生归档脚本。
