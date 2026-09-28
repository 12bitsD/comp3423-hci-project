# Home、Study progress、My Courses、主 Map 与校园 QR 实际走查

观察区间：2026-09-28 17:30:30–17:44:00 UTC（香港时间 2026-09-29 01:30:30–01:44:00）。使用 Computer Use 操作 Mac 上的真实 PolyULife，沿用已有登录会话。从 Apps All 返回 Home，分别进入 Study progress、My Courses、主 Map 和 QR，再检查 Home 日期与 My Class 通往周历的路径；最后返回 Home。本批结果采集截止为 `2026-09-28T17:44:00.905Z`。

App 版本沿用同日已观察的 3.0.0；本段未重新做版本验收，macOS 具体版本未记录。表中为动作开始时间，截图采集时间、尺寸和哈希以 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json) 为准。时间间隔不是加载性能或真人任务耗时。

本批公开 37 张经过隐私审核的截图/裁片。Completed、My Courses、Home 和周历只保留通用标题、标签、日期或选择器，个人课程、成绩、进度数值及日程不公开；截图裁片不能证明被裁掉的正文可读性。校园二维码和身份整块遮盖，不保留可识别码点。原始私人截图不进入共享仓库，后续 Figma 采用明确标记的合成资料。

## Study progress：名称展开、要求分类与搜索后的空白边界

| 时间（UTC） | 实际动作与反馈 | 证据与边界 |
| --- | --- | --- |
| 17:30:46 | Apps Back 返回 Home | 本次实际补测 `A-APPS-HOME-BACK`；Home 个人截图不公开 |
| 17:30:54 → 17:31:08 | Home Study progress 先显示加载，随后出现 Completed / Requirements 标签和已修科目结构 | [加载](../../evidence/2026-09-28-full-audit/study-173055-loading.png)、[Completed 标题裁片](../../evidence/2026-09-28-full-audit/study-173108-completed-header-only.png)；真实课程内容不公开 |
| 17:31:19 → 17:31:25 | 点击一条长科目名称的展开控件，再点击同处收起，名称由截断变为展开后恢复 | 脱敏动作/AX 记录；共享截图只保留标题，不用它证明课程正文或展开布局 |
| 17:31:32 | 点击 Requirements | [要求分类](../../evidence/2026-09-28-full-audit/study-173133-requirements-categories.png)；截图只有通用类别与学期说明，没有个人进度数值、成绩或完成标记 |
| 17:32:34 | 点击一个通识要求类别的入口 | [Subjects on Offer](../../evidence/2026-09-28-full-audit/study-173235-car-a-public-subject-offerings.png)；是公开科目目录，不是个人已修/在读列表 |
| 17:32:59 → 17:33:09 | 点击搜索控件并尝试输入一个科目代码，随后两次观察正文为空白 | [空白内容](../../evidence/2026-09-28-full-audit/study-173300-empty-content.png)；输入值不公开，无法确认输入是否被接收、搜索是否提交或空白原因，不标为“无搜索结果” |
| 17:33:21 | 点击空白状态 Back | 实际回到 Home；没有确认回到目录/Requirements 的中间栈 |

尚待检查 Requirements 其它分类、Completed 反向切换、完整列表和科目详情、搜索清除/成功查询/错误反馈及各层返回。空白结果保持未解决，不能由一次 Computer Use 输入尝试诊断 App 搜索故障。

## My Courses：Canvas / Blackboard 与嵌入登录页

| 时间（UTC） | 实际动作与反馈 | 证据与边界 |
| --- | --- | --- |
| 17:33:32 → 17:33:48 | Home My Courses 先加载，随后显示 Canvas 标签和课程列表结构 | [加载](../../evidence/2026-09-28-full-audit/courses-173334-loading.png)、[Canvas 标题裁片](../../evidence/2026-09-28-full-audit/courses-173348-canvas-header-only.png) |
| 17:33:56 → 17:34:05 | 点击一条长课程名称的箭头展开，再点击收起；AX 箭头和截断状态相应改变 | 只记录通用动作，课程标题/代码/学期内容不公开；收起动作没有独立截图 |
| 17:34:14 | 点击 Blackboard 标签 | [Blackboard 标题裁片](../../evidence/2026-09-28-full-audit/courses-173415-blackboard-header-only.png)；标签选中且存在课程/Open 结构，不是已验证空态 |
| 17:34:26 → 17:35:08 | 点击 Blackboard 的一项 Open，立即观察仍为原列表；稍后重新读取 PolyULife，确认内嵌 Blackboard 登录页 | [空字段登录](../../evidence/2026-09-28-full-audit/courses-173508-blackboard-login-empty-fields.png)；期间查询应用/Chrome 未证明成功交接到 Chrome。没有输入凭证或登录 |
| 17:35:17 | 登录页左上 Back `[31,177]` | 返回 Home；未证明先返回 My Courses |

尚待检查 Canvas 的 Open、其它课程链接、反向标签切换、列表边界、网页其它控制与登录后页面。空登录页只说明本次交接停在认证边界，不推断所有服务的 SSO 行为。

## 主 Map：多选筛选、设施详情、列表与未确认手势

| 时间（UTC） | 实际动作与反馈 | 证据 |
| --- | --- | --- |
| 17:35:25 | Home Map 打开校园地图及 Toilets、Water Stations、Clinics、Banks、AEDs、Bookstores 六个类别 | [主地图初始状态](../../evidence/2026-09-28-full-audit/map-173526-initial-campus.png) |
| 17:35:37 | 点击 Toilets，出现设施标记和列表 | [Toilets](../../evidence/2026-09-28-full-audit/map-173539-toilets-selected.png) |
| 17:35:45 → 17:35:55 | 点 Toilet (Core C) 行右侧省略号，再展开详情地图 | [设施详情](../../evidence/2026-09-28-full-audit/map-173546-toilet-core-c-detail.png)、[全屏地图](../../evidence/2026-09-28-full-audit/map-173556-toilet-core-c-full-map.png) |
| 17:36:06 → 17:36:17 | 两次拖动地图，分别 `[286,687]→[398,516]` 与 `[323,866]→[172,758]` | [第一次拖动后](../../evidence/2026-09-28-full-audit/map-173606-toilet-full-map-second-observation.png)、[第二次拖动后](../../evidence/2026-09-28-full-audit/map-173618-toilet-full-map-third-observation.png)；地图范围与标记基本未变，未确认平移成功 |
| 17:36:36 → 17:36:44 | 全屏地图 Back → 设施详情 Back | [回详情](../../evidence/2026-09-28-full-audit/map-173637-full-map-return-detail.png)、[回 Toilets 列表](../../evidence/2026-09-28-full-audit/map-173646-detail-return-toilets.png)；筛选保留 |
| 17:36:57 | Toilets 选中时点击 Water Stations，两类同时保持选中 | [组合筛选](../../evidence/2026-09-28-full-audit/map-173659-toilets-and-water-selected.png)；是多选叠加，不是替换 |
| 17:37:13 | 再点 Toilets，只留下 Water Stations | [仅饮水站](../../evidence/2026-09-28-full-audit/map-173714-water-only.png) |
| 17:37:21 | 尝试将列表把手 `[288,744]→[286,373]` 向上拖动 | [拖动后面板](../../evidence/2026-09-28-full-audit/map-173722-water-list-sheet.png)；面板边界和首项基本未变，未确认展开 |
| 17:37:40 | 在 `[305,934]` 向下滚动一次 | [列表后续片段](../../evidence/2026-09-28-full-audit/map-173741-water-list-scrolled.png)；可见项从前面的 Core C/D 移至后面的 Core R/T，确认这一次列表滚动。未到达或验证列表末端 |
| 17:37:57 | 再点 Water Stations，取消最后一个类别 | [筛选清空](../../evidence/2026-09-28-full-audit/map-173758-water-deselected.png)；结果面板消失 |
| 17:38:09 / 17:38:26 | 选择 Clinics，随后取消 | [Clinics](../../evidence/2026-09-28-full-audit/map-173810-clinics.png)；取消以 AX 记录为证 |
| 17:38:38 / 17:38:51 | 选择 Banks，随后取消 | [Banks](../../evidence/2026-09-28-full-audit/map-173839-banks.png)；取消以 AX 记录为证 |
| 17:39:05 / 17:39:18 | 选择 AEDs，随后取消 | [AEDs](../../evidence/2026-09-28-full-audit/map-173906-aeds.png)；取消以 AX 记录为证 |
| 17:39:27 → 17:39:42 | 选择 Bookstores，再点击地图上的 Bookshop 标记 | [Bookstores](../../evidence/2026-09-28-full-audit/map-173929-bookstores.png)、[标记点击后](../../evidence/2026-09-28-full-audit/map-173943-bookstores-map-observation.png)；未确认新气泡、详情或范围变化 |
| 17:39:55 | 主地图 Back | 返回 Home，AX 记录确认 |

已确认的是六类的首批可见结果、Toilets＋Water Stations 组合、一个设施详情和返回链，以及一次饮水站列表滚动。其它设施详情、完整列表、其它组合、地图缩放/My location/Google Maps 交接仍待检查；地图拖动、面板展开和标记点击需要重新确认定位与反馈。Room 或 Food 中的地图结果不能代替主 Map 的独立验收。这里没有个人定位证据，不把设施标记解释为用户位置。

## 校园 QR：显示与 Home 返回，真实二维码完全遮盖

| 时间（UTC） | 实际动作与反馈 | 证据与边界 |
| --- | --- | --- |
| 17:40:06 → 17:40:24 | 底部 QR 入口先加载，随后显示 My Campus Access QR、使用文字、身份区域与底部导航 | [加载](../../evidence/2026-09-28-full-audit/qr-174007-loading.png)、[整块遮盖后的显示状态](../../evidence/2026-09-28-full-audit/qr-174024-code-and-identity-redacted.png) |
| 17:40:41 | 点击使用提示旁的问号图标 | 没有确认新对话框或说明内容；后续含动态码的截图不公开 |
| 17:40:53 | 向下滚动提示区域一次 | 未确认更多文字被揭示，不能称已经读完全部提示或诊断滚动故障 |
| 17:41:10 | 点击底部 Home 导航 | 返回 Home；此动作不是关闭按钮 |

没有扫描、解码或使用二维码，没有验证实体门禁、码的有效性、过期/刷新或倒计时含义。Figma 只能使用明确的演示占位，不能复制可用码或身份。

## Home 日期、My Class 与周选择器

| 时间（UTC） | 实际动作与反馈 | 证据与边界 |
| --- | --- | --- |
| 17:41:24 | 向上滚动 Home，看到顶部日期与 My Class / My Exam 结构 | [日期区域裁片](../../evidence/2026-09-28-full-audit/home-174126-week-event-panel-only.png)；课程、考试、数值和个人身份均排除 |
| 17:41:39 | 点击 Tuesday 日期入口，日期由 September 28 / Monday 改为 September 29 / Tuesday，并出现 Today | [Tuesday 日期裁片](../../evidence/2026-09-28-full-audit/home-174141-today-event-panel-only.png)；不评价被排除的私人日程是否正确 |
| 17:41:52 | 点击 My Class 右侧入口 | [Week 5 标题裁片](../../evidence/2026-09-28-full-audit/calendar-174154-week-five-header-only.png)；打开 Calendar 周历，复用既有 `S-CALENDAR-WEEK`，课程正文不公开 |
| 17:42:26 | 点击 Week 5 标题，展开周选择器 | [选择器](../../evidence/2026-09-28-full-audit/calendar-174230-week-selector-only.png) |
| 17:42:42 | 点击看似下一周的位置 `[400,378]` | [点击后](../../evidence/2026-09-28-full-audit/calendar-174245-week-selector-second-observation-only.png)；未确认切周，标题仍为 Week 5 |
| 17:42:57 | 在 `[405,318]` 向下滚动选择器 | [滚轮可见 13，标题仍 5](../../evidence/2026-09-28-full-audit/calendar-174300-selector-thirteen-header-five-only.png)；只确认滚轮画面改变，不能记为已应用 Week 13 |
| 17:43:41 | 点击标题收起选择器 | [收起后 Week 5](../../evidence/2026-09-28-full-audit/calendar-174344-selector-closed-week-five-header-only.png)；其它周仍未成功应用 |
| 17:43:58 → 17:44:00 | 点击底部 Home | [返回日期区域裁片](../../evidence/2026-09-28-full-audit/home-174400-return-event-panel-only.png)；本批停止在 Home |

周选择器的输入定位、提交机制和真实 iPhone 行为仍需复查；当前没有根因证据，不把 Computer Use 操作未生效直接写为 App 缺陷。Home 其它日期、完整滚动边界、My Class / My Exam 各项内容及周历课程详情仍待观察。

## 分析与完成边界

主 Map 的叠加筛选与返回保留、长名称展开/收起、各入口加载后的稳定状态是当前观察事实；本批不强行增加缺陷数量。Study 输入后空白、周选择器未应用、地图手势/标记未见变化均作为待复核结果。需要重新确认输入目标、状态和设备差异后，才判断是否构成用户问题。

原生17:44批次之后，13个Home/Study/Courses/QR设计帧已导入，并对22个连接进行原型走查，见 [Figma记录](figma-spec.md)。个人页面重建采用明确标记的合成资料，不能把脱敏裁片之外的正文宣称为公共视觉证据。全部模块仍有未尝试动作，`coverage.json` 的全应用完成状态维持 `not_verified`；Agent 走查不替代真人 Maze 评估。

## 后补核查：Home四个入口与返回

2026-09-28 18:35:22–18:37:26 UTC（香港时间2026-09-29 02:35:22–02:37:26）重新连接当前实际Wrapper运行路径并取得真实Home截图；常规安装路径或bundle发现不单独作为成功证明。当前为Tuesday Home，继续已有登录会话。个人日程与身份仍不公开，没有修改资料或输入凭证。

| 动作开始时间（UTC） | 实际操作与结果 | 证据 |
| --- | --- | --- |
| 18:35:48 | Home底部Notification → My Notification空态 | [Home进入通知](../../evidence/2026-09-28-full-audit/notification-183550-home-entry-empty.png) |
| 18:36:02 | Notification底部Home → Home | 新截图的公共日期区域与 [此前Home裁片](../../evidence/2026-09-28-full-audit/home-174400-return-event-panel-only.png)逐像素相同，复用文件，实际新采集时间为18:36:05.987 |
| 18:36:18 | Home底部Calendar → **Week5周课表** | 新18:36:21.486截图标题裁片与 [此前Week5标题](../../evidence/2026-09-28-full-audit/calendar-174154-week-five-header-only.png)逐像素相同。课程正文不公开；这不是Sep28 Acad空月历 |
| 18:36:38 | 同一调用中先点Calendar底部Home，再点Home右上Search | [空Search](../../evidence/2026-09-28-full-audit/home-search-183641-empty.png)；两个子动作共用调用开始时间，不编造独立时间戳 |
| 18:36:55 | Search Back → Home | [返回日期裁片](../../evidence/2026-09-28-full-audit/home-183657-search-return-event-panel-only.png) |
| 18:37:09 | Home左上Menu → 抽屉 | [菜单项裁片](../../evidence/2026-09-28-full-audit/drawer-183710-home-entry-menu-items-only.png)；个人账户头部和右侧背景全部排除 |
| 18:37:23 | 点击抽屉右侧遮罩 → Home | [关闭后日期裁片](../../evidence/2026-09-28-full-audit/home-183726-drawer-closed-event-panel-only.png)；结果截止18:37:26.319 |

四个Home入口已独立补测，复用已存在的状态，返回目标按真实起点记录。先前More进入Search/抽屉的返回，不能替代这里Home的返回。原Figma Home Calendar指向Sep28 Acad空月历，与这次实际Week5落点冲突；随后已用合成Week5重建、改线，并于18:44:36之前实际复验往返通过，见 [Figma修正记录](figma-spec.md)。旧偏差及修复前测试保留为历史。其它入口能到达相同空态/菜单不证明其中所有控制或数据边界已完整覆盖。
