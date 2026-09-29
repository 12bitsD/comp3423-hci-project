# 首页日期与返回状态原型复验

2026-09-29（本地时间；下表为 UTC）。本批依据既有原生 Computer Use 观察补齐 Figma 首页连接。用户回复恢复后，原生工具复查仍提示 Mac 已锁定，没有新增原生状态；121 个原生状态、265 个动作及86个未尝试动作均不变。完整应用保持 `not_verified`。

## 依据与实现

原生依据见 [Home、Study、Map 走查](home-study-map-walkthrough.md)：Monday28 → Tuesday29/Today、My Class → Week5、Week5 Home返回周二，以及后续 Home Calendar、Notification、Search、Menu 与返回补测。课程、考试数量、名称、日期、时间和地点在设计中均为明确标注的合成 DEMO，不发布实际学生日程。

既有 Monday `67:569` 与 Tuesday `67:694` Frame 保留；新增8个连接控件，修改既有 Week5 Home 返回方式。当前76个全屏映射Frame、2个画板内状态、118个连接控件；没有将回放截图算成新原生状态或新设计Frame。

| 控件 | 触发节点 | 结果 |
| --- | --- | --- |
| Monday Tuesday日期 | 67:587 | Tuesday67:694 |
| Tuesday My Class | 67:728 | Week5 70:973 |
| Tuesday Menu | 67:790 | 完整DEMO抽屉75:1669 |
| Tuesday Search | 67:792 | 空Search42:1716 |
| Tuesday底部Calendar | 67:804 | Week5 70:973 |
| Tuesday底部Notification | 67:813 | 空通知42:1617 |
| Search Back | 42:1720 | Back，验证周二与功能区两种来源 |
| Notification Home | 42:1640 | Back，仅验证周二来源 |
| 既有Week5 Home | 70:1045 | 从固定功能区目标改为Back，验证周二与功能区来源 |

新流程 **Home · Dates, agenda and return state** 已保存；实际回放 Monday→Tuesday后，My Class、Calendar、Menu、Search、Notification及各自返回均保留周二。既有功能区样例67:820 → Calendar → Home，以及功能区 → Search → Back也已回归通过。

## 实际 Present 证据

| UTC | 观察 | 截图 |
| --- | --- | --- |
| 20:59:14.220 | 周一首页起点 | [E-HOME-DATE-P-01](../../evidence/2026-09-28-full-audit/figma-home-date-monday-start.png) |
| 20:59:26.619 | 点击 Tuesday，显示29/Today | [E-HOME-DATE-P-02](../../evidence/2026-09-28-full-audit/figma-home-date-tuesday-selected.png) |
| 20:59:38.815 | My Class打开Week5 | [E-HOME-DATE-P-03](../../evidence/2026-09-28-full-audit/figma-home-date-myclass-week.png) |
| 20:59:51.192 | Week5 Home返回周二 | [E-HOME-DATE-P-04](../../evidence/2026-09-28-full-audit/figma-home-date-week-return-tuesday.png) |
| 21:03:01.018 | 底部Calendar打开Week5 | [E-HOME-DATE-P-05](../../evidence/2026-09-28-full-audit/figma-home-date-bottom-calendar-week.png) |
| 21:03:07.100 | Week5 Home再次返回周二 | [E-HOME-DATE-P-06](../../evidence/2026-09-28-full-audit/figma-home-date-bottom-calendar-return.png) |
| 21:03:13.659 | Menu打开完整DEMO抽屉 | [E-HOME-DATE-P-07](../../evidence/2026-09-28-full-audit/figma-home-date-menu.png) |
| 21:03:21.264 | 抽屉外侧关闭返回周二 | [E-HOME-DATE-P-08](../../evidence/2026-09-28-full-audit/figma-home-date-menu-return.png) |
| 21:03:27.119 | Search打开空搜索 | [E-HOME-DATE-P-09](../../evidence/2026-09-28-full-audit/figma-home-date-search.png) |
| 21:03:36.973 | Search Back返回周二 | [E-HOME-DATE-P-10](../../evidence/2026-09-28-full-audit/figma-home-date-search-return.png) |
| 21:03:43.685 | Notification打开空态 | [E-HOME-DATE-P-11](../../evidence/2026-09-28-full-audit/figma-home-date-notification.png) |
| 21:03:55.483 | Notification Home返回周二 | [E-HOME-DATE-P-12](../../evidence/2026-09-28-full-audit/figma-home-date-notification-return.png) |
| 21:04:20.830 | 回归起点：既有首页功能区 | [E-HOME-DATE-P-13](../../evidence/2026-09-28-full-audit/figma-home-return-regression-features-start.png) |
| 21:04:28.167 | 功能区Calendar打开Week5 | [E-HOME-DATE-P-14](../../evidence/2026-09-28-full-audit/figma-home-return-regression-features-week.png) |
| 21:04:35.453 | Week5 Home返回功能区原样例 | [E-HOME-DATE-P-15](../../evidence/2026-09-28-full-audit/figma-home-return-regression-features-week-return.png) |
| 21:04:42.879 | 功能区Search打开空搜索 | [E-HOME-DATE-P-16](../../evidence/2026-09-28-full-audit/figma-home-return-regression-features-search.png) |
| 21:04:53.243 | Search Back返回功能区原样例 | [E-HOME-DATE-P-17](../../evidence/2026-09-28-full-audit/figma-home-return-regression-features-search-return.png) |
| 21:06:21.404 | 新流程说明保存并在Present读回 | [E-HOME-DATE-P-18](../../evidence/2026-09-28-full-audit/figma-home-date-final-flow-context.png) |

## 边界与下一步

- `PROTO-HOME-DATE-RETURN-001` 与 `PROTO-HOME-RETURN-REGRESSION-001` 的记录路径通过；整体为 partial。Week/Notification Home使用历史Back只覆盖已测试的Home进入路径；直接起于Week/Notification或其它来源的导航栈没有实现正确的全局Home语义。
- 首页三张画板仍是固定滚动位置样例，没有真实连续滚动。其它星期、卡片详情、搜索输入/结果、周选择器及底部其它入口仍需补齐；未编造Tuesday→Monday行为。
- 抽屉外侧只有灰底，未还原来源页面背景。字体、图标、尺寸仍为近似；原生观察不等于逐像素验收。
- 本次返回截图的装饰条可见，但没有修复历史间歇消失的根因，`D-HOME-PREVIEW-IMAGE`保持open。
- 18张截图来自真实Figma Present；共享副本仅遮盖右上账户头像区域 `[1017,0,1075,49]`，转换及遮盖逐像素校验，原始JPEG留在忽略目录。Figma截图不能替代原生证据，Agent回放不能替代Maze真人测试。
