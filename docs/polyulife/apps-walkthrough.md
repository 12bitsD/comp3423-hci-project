# Apps 分类与 VRS 登录边界实际走查

观察区间：2026-09-28 17:13:42–17:17:44 UTC（香港时间 2026-09-29 01:13:42–01:17:44）。使用 Computer Use 操作 Mac 上的真实 PolyULife，沿用已有登录会话。从 Food 的 H Café 列表按 Back 回到 Home，再进入 Apps；最后停在 Apps 的 All 分类。前置 Home 截图含个人内容，未公开。本页引用的 14 张截图均为 Apps 公开服务界面或空登录表单。

应用版本沿用同日抽屉已观察的 3.0.0，本段未重新读取版本；macOS 具体版本未在本段记录。截图时间是采集时间，不作为真人任务耗时或加载性能指标。

## 实际路径与证据

表内时间为动作开始时间；截图文件名和 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json) 记录结果采集时间。

| 时间（UTC） | 实际动作与观察 | 证据 |
| --- | --- | --- |
| 17:13:42 → 17:13:57 | Food 列表 Back 返回 Home，再点击 Apps。Apps 初始选中 All，顶部为横向分类栏，下方为服务卡片 | [Apps 初始 All](../../evidence/2026-09-28-full-audit/apps-171359-all.png)；前置 Home 仅保留脱敏动作说明，个人截图不公开 |
| 17:14:11 | 点击 Campus，选中标记移至 Campus，显示 Visitor Registration System (VRS) 和 PolyU Internal Search 两张卡片 | [Campus](../../evidence/2026-09-28-full-audit/apps-171411-campus.png) |
| 17:14:24 | 点击 VRS 卡片右侧省略号 `[540,380]`，进入 App 内部详情。详情显示名称、用途说明与 Open VRS 链接 | [VRS 详情](../../evidence/2026-09-28-full-audit/apps-171424-vrs-detail.png)；本步没有点击列表内的 Open VRS |
| 17:14:40 | 点击详情的 Open VRS，打开内嵌网页；顶部有 X 和菜单，底部有网页导航及地址栏，中间先显示 PolyU 标识 | [网页加载状态](../../evidence/2026-09-28-full-audit/apps-171442-vrs-web-loading.png)；地址栏显示 `fmovrs.polyu.edu.hk/vr...` |
| 17:14:49 → 17:15:22 | 两次重新观察，第一次仍为加载画面，后一次显示 “Sign in with your NetID and NetPassword” 登录页，两个字段均为空 | [空字段登录页](../../evidence/2026-09-28-full-audit/apps-171522-vrs-login-empty-fields.png)；没有输入、登录或提交访客申请 |
| 17:15:48 | 点击内嵌网页左上 X，截图确认回到 VRS 详情 | [关闭网页后](../../evidence/2026-09-28-full-audit/apps-171549-vrs-web-closed.png)；本次返回的 AX 未列出详情内容，视觉截图确认返回状态，不据此判断 App 丢失内容 |
| 17:16:03 | 点击详情左上 Back `[30,177]`，返回 Apps，Campus 仍选中，两张卡片恢复 | [保留 Campus 筛选](../../evidence/2026-09-28-full-audit/apps-171603-campus-filter-retained.png) |
| 17:16:12 | 点击 Study，显示学习服务卡片；截图完整显示 LEARN@PolyU、Library、eStudent、Research Student Portal，并露出下一张卡片的上部 | [Study](../../evidence/2026-09-28-full-audit/apps-171613-study.png)；未向下滚动 |
| 17:16:25 | 点击 IT Tips，分类栏同时移位以显示所选项，显示 Connect Email、Identity Portal、FAQ for IT Services、IT Online ServiceDesk | [IT Tips](../../evidence/2026-09-28-full-audit/apps-171626-it-tips.png) |
| 17:16:38 | 点击 Health，显示 University Health Service、Optometry Clinic、Rehabilitation Clinic 三张卡片 | [Health](../../evidence/2026-09-28-full-audit/apps-171639-health.png) |
| 17:16:51 | 点击 Wellness，显示 POSS 和 Scholarship 两张卡片 | [Wellness](../../evidence/2026-09-28-full-audit/apps-171652-wellness.png) |
| 17:17:04 | 点击 Job，显示一张 PolyU Job Board 卡片 | [Job](../../evidence/2026-09-28-full-audit/apps-171705-job.png) |
| 17:17:22 | 分类栏从 `[101,251]` 向右拖到 `[500,251]`，栏的左端重新可见，包括 All、Campus、Study；内容仍为 PolyU Job Board，AX 仍标记 Job 选中 | [拖动分类栏后](../../evidence/2026-09-28-full-audit/apps-171722-category-bar-dragged.png)；只是移动分类栏，没有切换分类 |
| 17:17:43 | 点击重新可见的 All，All 选中，列表回到以 VRS、PolyU Internal Search 开头的视口 | [回到 All](../../evidence/2026-09-28-full-audit/apps-171744-all-return.png)；结果采集截止为 `2026-09-28T17:17:44.298Z` |

All 的 AX 中包含 18 项服务条目；初始截图只显示前几张卡片，Study 同样有屏外条目。AX 数量用于发现后续检查范围，不证明所有条目已经进入可见视口、可点击或验证完整。未对任何分类做垂直滚动到底检查。

## 观察事实、问题假设与边界

- **已观察事实：** 分类选择会改变服务列表，并显示选中标记；VRS 的“卡片省略号 → 内部详情 → 内嵌网页 → X → 详情 Back”路径已走通，返回列表时保留 Campus。列表按钮直接打开服务的路径尚未试过。
- **已观察事实：** 横向拖动分类栏可以露出 All，同时保留 Job 的内容与选择状态；此时选中项在视口外。随后点击 All 才切换内容。
- **问题假设：** 选中分类滚出视口后，用户可能难以确认当前列表属于哪个分类。这与“系统状态可见性”有关；是否造成困惑、是否需要固定当前分类提示，需由真人任务验证，不能从一次 Agent 操作推定发生率。
- **已观察事实：** VRS 在当前已有 App 会话下仍显示独立登录表单。它只证明这次网页需要登录，不证明所有服务都要求重复登录，也不证明 SSO 有缺陷。
- **边界：** 加载画面后来到达登录页，不能将其记为永久空白错误；本次没有测试网页菜单、刷新、前进/后退、表单错误或登录后的 VRS 功能。网页 X 返回时 AX 信息暂时不足，与截图内容分开记录。

## 未完成范围

- Apps 的 All、各分类列表完整内容、垂直滚动边界、其它卡片详情及各自返回；本次只深入 VRS 一项。
- 列表中 Open VRS 的直接入口，以及其它服务的 Open 按钮、外部交接和登录后页面；目前只确认卡片存在与可见文字。
- VRS 登录、错误反馈、登录帮助及账号相关链接；本次未输入凭证，也未提交访客申请。
- VRS 网页顶部菜单、底部导航/刷新与其它网页状态，详情的更多内容边界。
- 分类栏反向拖动、重复切换及不同分类滚动位置是否保留、网络错误或空结果等边界状态。
- Apps 的 Back 返回 Home 已在后续17:30:46独立执行；见下方补测。完整列表及其它服务返回仍待检查。

本段17:17:44截止时的状态为 `S-APPS-ALL`。11张Apps SVG重建源码随后导入Figma，12个连接的导航样例已实跑，首次中文缺字修复后通过定向复验；其它范围仍未验收，见 [Figma记录](figma-spec.md)。全应用完成状态仍为 `not_verified`。Study分类与Home的Study progress是独立模块。

## 后续Home返回补测

17:30:30重新观察确认仍为Apps All；17:30:46点击Apps Back，17:30:48结果确认返回Home。个人Home截图不公开，只保留脱敏动作记录。后续Study progress、My Courses、Home主Map、QR和Home日期分别有独立观察，见 [Home/Study/Map走查](home-study-map-walkthrough.md)。这项补测关闭Apps→Home这一动作缺口，不改变其它服务、完整列表和Figma尚未验收的边界。

## 后续原型返回改造

[Apps分类与返回回放](apps-return-prototype-walkthrough.md)记录Home来源保留、分类同层切换和VRS嵌套关闭。本段引用的是Figma验证，没有新增原生App观察；原有实测记录保持不变。

后续更新：[可见分类互跳验证](apps-category-prototype-walkthrough.md)已新增并回放33个连接；本页的固定链限制作为历史记录保留。
