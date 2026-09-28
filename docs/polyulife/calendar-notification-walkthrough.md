# Calendar 与 Notification 实际走查

本记录覆盖 2026-09-28 15:50:41–15:57:32 UTC（香港时间 23:50:41–23:57:32）的实际 Computer Use 动作。原生 iPhone App 在 Mac 上运行；保留已有登录状态。个人课程、账户和原始 AX 内容不公开，所附 Calendar 全页图均为只选 `Acad calendar` 后的公共校历，筛选面板图只保留面板。

## Calendar：筛选与公共校历

| 时间（UTC） | 实际动作与结果 | 证据 |
| --- | --- | --- |
| 15:50:41 → 15:50:56 | 从 More 底栏进入 Calendar，后续出现 September / 2026-27 Semester 1 月历及当天状态 | `E-CALENDAR-TRACE`；默认页面含个人课程，未公开截图 |
| 15:51:13 | 打开筛选面板。Select All、Class、Exam、Payment、Acad calendar 均选中，另有 Apply 与 X | [全选面板](../../evidence/2026-09-28-full-audit/calendar-155114-filter-all-panel-only.png) |
| 15:51:30 | 点击 Select All，所有复选框取消选中；尚未 Apply | [取消全选](../../evidence/2026-09-28-full-audit/calendar-155131-filter-none-panel-only.png)；不推定“空选择应用后的结果” |
| 15:51:42 → 15:51:55 | 只选 Acad calendar 并 Apply；面板关闭，September 28 下显示 Acad calendar 和 No event | [只选校历](../../evidence/2026-09-28-full-audit/calendar-155143-filter-acad-panel-only.png) → [空状态](../../evidence/2026-09-28-full-audit/calendar-155155-acad-only-no-event.png) |
| 15:52:24 | 选择有标记的 September 26；出现 General holiday (The day following Mid-Autumn Festival) | [公共假期](../../evidence/2026-09-28-full-audit/calendar-155225-sep26-public-holiday.png) |
| 15:52:42 → 15:52:55 | 点击该事件右侧省略号，进入只有事件标题和 2026-09-26 日期的详情；返回后仍为 September 26 与同一事件 | [详情](../../evidence/2026-09-28-full-audit/calendar-155243-public-holiday-detail.png) → [保留日期返回](../../evidence/2026-09-28-full-audit/calendar-155255-public-holiday-back.png) |
| 15:53:03 | 点击右上视图控件进入 Events 列表，顶部为 Show History，列表从 October 公共事件开始 | [Events 列表](../../evidence/2026-09-28-full-audit/calendar-155307-public-events-list.png) |
| 15:53:19 | 点击 Show History，变成 Hide History，显示 August/September 的较早公共事件 | [历史事件](../../evidence/2026-09-28-full-audit/calendar-155322-public-events-history.png)；反向 Hide History 尚未测试 |
| 15:53:38 → 15:53:57 | 再点右上视图控件进入 Week 5 周课表；点击周标题后展开周次选择结构 | `E-CALENDAR-TRACE`；包含个人课程的截图不公开。没有选择另一周，也未打开课程详情 |
| 15:54:28 | 再点右上控件返回月视图，September 26 和公共假期仍在 | [月视图返回](../../evidence/2026-09-28-full-audit/calendar-155429-month-return.png)；实际观察到月历 → Events → 周课表 → 月历这一轮，不泛化为所有初始状态 |
| 15:54:39 | 点击下一月箭头，显示 October 且选中 1 日，显示 National Day | [October 1](../../evidence/2026-09-28-full-audit/calendar-155440-oct1-public-holiday.png) |
| 15:54:50 | 点击上一月箭头，显示 September 且选中 1 日，No event | [September 1](../../evidence/2026-09-28-full-audit/calendar-155451-sep1-no-event.png)；本次跨月返回没有恢复先前的 26 日 |
| 15:55:02 → 15:55:19 | 点击 28 日恢复当天；重开筛选面板，仍只有 Acad calendar 选中 | [恢复28日](../../evidence/2026-09-28-full-audit/calendar-155503-sep28-no-event.png) → [筛选保持](../../evidence/2026-09-28-full-audit/calendar-155519-acad-filter-persisted.png) |
| 15:55:30 → 15:55:45 | 点击 Select All，AX 确認所有类别选中；Apply 后回到月历，恢复原来全部类别 | `E-CALENDAR-TRACE`；本步为 AX 结果记录，不使用早期全选截图替代 |

`No event` 下的提示是 “Make sure you are viewing the calendar with all filters enabled!”。只选公共校历后，当前空态是已知筛选下的结果，不是网络错误或整个日期没有任何个人安排的证据。周视图仍出现个人课表，而返回月视图后 Acad calendar 筛选保持；目前只能确认两个视图展示范围不同，需补产品预期和其它筛选组合才能评价一致性。

月历 AX 中，部分实际周六日期的可访问名称写成 Sunday，Thursday 也出现 `Thursdya` 拼写；例如 2026-09-26 的日期格 AX 为 Sunday，但页面当前日期文案与事件列表为 Saturday。这里只记录 Mac AX 标签差异，不把它写成视觉日历排错，也不宣称已完成 VoiceOver 测试。

## Notification：空状态和搜索

| 时间（UTC） | 实际动作与结果 | 证据 |
| --- | --- | --- |
| 15:56:02 | 从 Calendar 底栏打开 Notification，标题 My Notification，显示 No new notification / Please come back later | [通知空状态](../../evidence/2026-09-28-full-audit/notification-155603-empty.png) |
| 15:56:22 | 点右上搜索，进入 Search 页，有空输入字段和返回控件 | [搜索起点](../../evidence/2026-09-28-full-audit/notification-155622-search-empty.png) |
| 15:56:36 → 15:56:55 | 输入 `weather` 后出现 No record found 及更换关键词指引；按 Return 后仍无结果 | [输入后无结果](../../evidence/2026-09-28-full-audit/notification-155637-weather-no-results.png) → [Return后仍无结果](../../evidence/2026-09-28-full-audit/notification-155656-weather-return-no-results.png)；当前没有有效通知数据可用于成功结果或通知详情测试 |
| 15:57:12 | 点击输入右侧清除控件，AX 字段恢复 Search 占位，无 weather 值和无结果文案 | [清空后的搜索页](../../evidence/2026-09-28-full-audit/notification-155714-search-cleared.png) |
| 15:57:32 | 点击返回，AX 恢复 My Notification 空状态及 Notification 底栏选中 | `E-NOTIFICATION-TRACE`；本步没有独立返回截图 |

这里没有发送或删除通知。一个关键词无结果不能说明系统搜索失败；搜索范围究竟只包括通知、还是跨模块内容，仍需核实。随后从 More 打开的搜索另见 [More 走查](more-walkthrough.md)。

## 未完成范围

- Calendar：X 关闭筛选的提交/取消语义；空选择 Apply；Class、Exam、Payment 单独切换；全部月份/学期边界；其它事件详情与列表末端；Hide History 反向动作；周次选择、周课表和课程详情。个人数据场景应以脱敏示例或单独授权的证据呈现，不能用公共校历图冒充。
- Notification：菜单、刷新/空态图标、通知成功列表和详情、搜索成功结果、全部滚动边界。当前只有空通知和无结果查询，不能从空态推断功能不存在。
- 日历 AX 标签：补独立复现和真实辅助技术体验；不得把 Mac AX 异常直接泛化到 iOS VoiceOver。

这些路径证明了部分真实状态和转换；整体覆盖状态仍为 `not_verified`。Figma 还需逐状态核实节点及连接，真实 App 返回成功不等于 Figma 原型已经可返回。

## 后续Home入口与周选择器补测

2026-09-28 17:41:52 UTC，从Home的My Class右侧入口到达Week5周历。随后打开选择器，点击下一周位置未确认变化；滚轮可见值移至13时标题仍为Week5，收起后也仍为Week5。17:43:58点击底部Home返回，结果截止17:44:00.905。见 [详细步骤及隐私裁片](home-study-map-walkthrough.md#home-日期my-class-与周选择器)。这补充了真实输入尝试，不证明已成功切换周；个人课程内容继续不公开，周选择与其余边界保持未完成。

18:36:18另从Home底部Calendar实际进入Week5，标题裁片与前次Week5相同；Notification、Search、菜单的Home入口及返回也已独立补测。原型原先固定月历落点因此被纠正为Week5 DEMO，18:44:36前完成往返复验，见 [来源核查](home-study-map-walkthrough.md#后补核查home四个入口与返回)及 [Figma记录](figma-spec.md)。此修复不改变原生切周尚未成功的边界。
