# Figma 复现与证据对应约定

本页定义从真实 PolyULife 观察到可编辑、可点击 Figma 的对应关系。实际覆盖由 [coverage.json](coverage.json) 记录。本页同时记录已经确认的文件状态和后续制作、验证方法；实际存在文件不等于节点和交互已经完成。

## 当前修正版（Room V2）

同一 [Figma Design 文件](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)新增 **`01 · Observed UI`** 页面。四张 Room 设计源码已按 576×970 的真实截图几何制作并导入为原生 Frame、Text、Vector 和 group；普通编辑器导入及连线不依赖 Agents 额度。

[当前原型：Room Finder · A → AG206](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-198&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A198&show-proto-sidebar=1)。在独立浏览器标签页选择 **Fit width and height** 后，已实际复走四步：点击输入区域并按 A → 选择 AG206 → Available → ALL。每步目标节点均由真实原型 URL/AX 确认。

| 状态 | 设计源码 | 当前真实节点 |
| --- | --- | --- |
| `S-EMPTYQUERY` | [room-empty.svg](../../design/polyulife/room-empty.svg) | [12:198](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-198) |
| `S-SUGGESTION` | [room-suggest.svg](../../design/polyulife/room-suggest.svg) | [12:380](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-380) |
| `S-ALL` | [room-all.svg](../../design/polyulife/room-all.svg) | [12:243](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-243) |
| `S-AVAILABLE` | [room-available.svg](../../design/polyulife/room-available.svg) | [12:105](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-105) |

### 修正版原型验证

当前公开证据：[空查询完整画面](../../evidence/2026-09-28-full-audit/figma-v2-present-153153-room-empty.png)、[联想完整画面](../../evidence/2026-09-28-full-audit/figma-v2-present-153616-room-suggest-a.png)、[ALL 完整画面](../../evidence/2026-09-28-full-audit/figma-v2-present-153240-room-all.png)、[Available 完整画面](../../evidence/2026-09-28-full-audit/figma-v2-present-153302-room-available.png)、[原生导入图层与尺寸](../../evidence/2026-09-28-full-audit/figma-v2-151317-available-vector-frame.png)。最终 ALL 返回图像与先前 ALL 图字节相同，公共证据复用该图；操作时间与 URL 另行确认。

| 实际操作 | 配置位置 | 实际目标 | 结论 |
| --- | --- | --- | --- |
| 点击输入区域使画布获得焦点，再按 A | 空状态 root `12:198`，Key A | `12:380` | 有限 A 查询样例通过；不是自由输入 |
| 点击 AG206 | Suggestion group `12:421` | `12:243` | 点击连接通过 |
| 点击 Available | FilterAvailable `12:301` | `12:105` | 独立标签页完整复验通过 |
| 点击 ALL | FilterAll `12:160` | `12:243` | 返回连接通过；真实 App 同日期数据状态仍须精确复核 |

早先可见面板中的一次 Available 点击没有导航、仅闪现热点；原因尚不能确定。后续独立标签页在正确缩放和焦点下完整通过四步，因此这次早期未成功点击保留为工具/定位不确定的尝试记录，不当成已确认的设计连接缺陷。

修正版已目视核对标题/控件几何、结果页白色背景及按行的时间排列，相比旧草稿得到改善。空查询与联想页的下方浅灰区域本就存在于来源，不应误改为白色。最终完整原型视口为 357×601 的缩放显示，对应源 576×970；不能把早先截断视口作为全高验收。字形和矢量图标仍有近似，不称逐像素一致。

当前限制仍包括：自由文字输入、任意查询、清空、其它日期、Preview、地图、时段滚动及其它已观察边界没有全部接入原型。样例四步通过不证明 Room 全交互或全应用完成。

## More / Weather：四步原型运行已通过

[天气流程入口：More · Weather and Assistant](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-435&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A435&show-proto-sidebar=1)来自真实编辑器 Copy flow link。本轮在独立 tab 10 中选择 Fit width and height，实跑 More → Weather → expanded image → Weather → More。流程名含 Assistant，但这次四步测试只验证天气分支。

| 原生状态 | 源码 | Figma Frame | 画布位置 |
| --- | --- | --- | --- |
| `S-MORE` | [more.svg](../../design/polyulife/more.svg) | [12:435](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-435) | 0, 1200 |
| `S-WEATHER` | [weather-detail.svg](../../design/polyulife/weather-detail.svg) | [12:480](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-480) | 700, 1200 |
| `S-WEATHER-EXPANDED` | [weather-image.svg](../../design/polyulife/weather-image.svg) | [12:510](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-510) | 1400, 1200 |

| 操作时间（UTC） | 热点 | 实际节点转换 | 验证 |
| --- | --- | --- | --- |
| 16:21:05.847 | MoreWeatherCard；确切热点 ID 未记录 | `12:435 → 12:480` | URL/AX 确认通过 |
| 16:21:23.237 | ExpandImage `12:490` | `12:480 → 12:510` | URL/AX 与截图通过 |
| 16:21:36.723 | CloseImage `12:512` | `12:510 → 12:480` | URL/AX 与截图通过 |
| 16:21:47.485 | Back `12:507` | `12:480 → 12:435` | URL/AX 与截图通过 |

公开原型画面：[展开图片](../../evidence/2026-09-28-full-audit/figma-v2-present-162123-weather-hero-expanded.png)、[返回详情](../../evidence/2026-09-28-full-audit/figma-v2-present-162137-weather-detail.png)、[返回 More](../../evidence/2026-09-28-full-audit/figma-v2-present-162147-more-list.png)。三张为 357×601 的完整帧缩放图，不是 App 原始截图。首个详情步骤依靠其当时 URL/AX，稳定详情图来自后续返回，不将其时间混用。

对应真实 App 的天气 Back 在 15:45:42 已独立确认返回 More（`A-WEATHER-BACK`），所以此原型返回有实际来源。字体、矢量图标仍近似，天气正文的 `of` 与下划线链接之间过挤，记为 `D-WEATHER-TEXT-SPACING`；导航通过不代表视觉验收通过。官方网页链接、问号、文章滚动等未在本次原型运行中验证。

## 后续18帧：导入与映射已确认

16:23:55 UTC，真实编辑器已完成18个新增 SVG 的重命名与位置核验。`01 · Observed UI` 当前合计25帧（Room 4 + More/Weather 3 + Assistant 4 + Calendar 10 + Notification/Search 4）。下表左侧是 Figma 图层标签别名，右侧是覆盖台账的既有原生状态 ID；两者显式对应，不另造重复 App 状态。

| Figma 标签 → 原生状态 | 设计源码 | 实际节点 |
| --- | --- | --- |
| `S-SEARCH-ROOM-NONE` → `S-MORE-SEARCH-ROOM` | [search-room-no-results.svg](../../design/polyulife/search-room-no-results.svg) | [42:1686](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1686&t=u9E3LqVQD7AiByx8-0) |
| `S-SEARCH-WEATHER-NONE` → `S-MORE-SEARCH-WEATHER` | [search-weather-no-results.svg](../../design/polyulife/search-weather-no-results.svg) | [42:1656](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1656&t=u9E3LqVQD7AiByx8-0) |
| `S-SEARCH-EMPTY` → `S-MORE-SEARCH-EMPTY` | [search-empty.svg](../../design/polyulife/search-empty.svg) | [42:1716](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1716&t=u9E3LqVQD7AiByx8-0) |
| `S-NOTIFICATION` → `S-NOTIFICATION-EMPTY` | [notification-empty.svg](../../design/polyulife/notification-empty.svg) | [42:1617](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1617&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-HISTORY` → `S-CALENDAR-HISTORY` | [calendar-events-history.svg](../../design/polyulife/calendar-events-history.svg) | [42:1493](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1493&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-EVENTS` → `S-CALENDAR-EVENTS` | [calendar-events-upcoming.svg](../../design/polyulife/calendar-events-upcoming.svg) | [42:1375](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1375&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-SEP1` → `S-CALENDAR-SEP1` | [calendar-sep1.svg](../../design/polyulife/calendar-sep1.svg) | [42:1215](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1215&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-OCT1` → `S-CALENDAR-OCT1` | [calendar-oct1.svg](../../design/polyulife/calendar-oct1.svg) | [42:1062](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-1062&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-FILTER-NONE` → `S-CALENDAR-FILTER-NONE` | [calendar-filter-none.svg](../../design/polyulife/calendar-filter-none.svg) | [42:876](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-876&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-FILTER-ALL` → `S-CALENDAR-FILTER-ALL` | [calendar-filter-all.svg](../../design/polyulife/calendar-filter-all.svg) | [42:680](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-680&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-FILTER-ACAD` → `S-CALENDAR-FILTER-ACAD` | [calendar-filter-acad.svg](../../design/polyulife/calendar-filter-acad.svg) | [42:492](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-492&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-HOLIDAY` → `S-CALENDAR-EVENT` | [calendar-holiday-detail.svg](../../design/polyulife/calendar-holiday-detail.svg) | [42:479](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-479&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-SEP26` → `S-CALENDAR-SEP26` | [calendar-sep26.svg](../../design/polyulife/calendar-sep26.svg) | [42:325](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-325&t=u9E3LqVQD7AiByx8-0) |
| `S-CAL-SEP28` → `S-CALENDAR-ACAD-EMPTY` | [calendar-sep28.svg](../../design/polyulife/calendar-sep28.svg) | [42:165](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-165&t=u9E3LqVQD7AiByx8-0) |
| `S-VA-WELCOME` → `S-ASSISTANT-WELCOME` | [virtual-assistant-welcome.svg](../../design/polyulife/virtual-assistant-welcome.svg) | [42:111](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-111&t=u9E3LqVQD7AiByx8-0) |
| `S-VA-DISCLAIMER` → `S-ASSISTANT-DISCLAIMER` | [virtual-assistant-disclaimer.svg](../../design/polyulife/virtual-assistant-disclaimer.svg) | [42:43](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-43&t=u9E3LqVQD7AiByx8-0) |
| `S-VA-IMAGE` → `S-ASSISTANT-IMAGE` | [virtual-assistant-image.svg](../../design/polyulife/virtual-assistant-image.svg) | [42:37](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-37&t=u9E3LqVQD7AiByx8-0) |
| `S-VA-DETAIL` → `S-ASSISTANT-DETAIL` | [virtual-assistant-detail.svg](../../design/polyulife/virtual-assistant-detail.svg) | [42:6](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%25E2%2580%2594-Observed-UI---Interaction-Atlas?node-id=42-6&t=u9E3LqVQD7AiByx8-0) |


这18帧在导入时均为 `prototype_status: not_run`；随后 Assistant 四帧、Calendar 十帧的实际运行分别记录如下。Notification/Search 的四帧仍只有导入和位置证据。Selected Virtual Assistant detail 的576×970 Frame属性已检查；其它帧的源码尺寸为576×970，尚未逐帧独立检查全部子图层或最终字体。

Calendar 的三个筛选面板用公共 Acad calendar / No event 画面作为背景；原公开 all/none/acad 来源最初只有面板裁切，个人课程背景没有公开。这是明确的脱敏背景重构差异（`D-CALENDAR-FILTER-PUBLIC-BACKGROUND`），不能称全帧原样。共用 Search 外观也不能抹掉 More 与 Notification 不同来源的返回上下文或搜索范围未知问题。

旧页已改名为 `00 · Archive — initial AI draft`（原 `Page 1`），四帧与三条旧连接仍保留为历史草稿；下面的旧节点和偏差不指代 `01 · Observed UI` 的当前节点。

## Virtual Assistant：导航通过，返回图片视觉问题未解决

同一 More 流程在 16:30–16:33 UTC 实跑七条连接。`PROTO-VA-V2-001` 的整体结果记为 `failed`：七条导航及一次负向热点检查通过，但网页关闭返回详情时头图重复消失，视觉稳定性未通过，不能称 VA 整体通过。

| 动作时间（UTC） | 热点与实际动作 | 实际节点转换 | 导航结果 |
| --- | --- | --- | --- |
| 16:30:27.239 | MoreAssistantCard `12:446` | `12:435 → 42:6` | 通过 |
| 16:30:44.738 | ExpandImage `42:13` | `42:6 → 42:37` | 通过 |
| 16:30:57.791 | CloseImage `42:39` | `42:37 → 42:6` | 通过 |
| 16:31:10.177 | VirtualAssistantWebLink `42:26` | `42:6 → 42:43` | 通过 |
| 16:31:22.864 | 先点 Disclaimer 正文，再点 AcceptDisclaimer `42:94` | 正文停在 `42:43`；ACCEPT 才到 `42:111` | 负向点击与确认连接均通过 |
| 16:31:42.498 | CloseWeb `42:120` | `42:111 → 42:6` | 节点通过；头图变空白 |
| 16:31:58.808 | Back `42:34` | `42:6 → 12:435` | 通过 |

公开证据：[首次详情有头图](../../evidence/2026-09-28-full-audit/figma-v2-present-163028-va-detail-with-hero.png)、[图片展开](../../evidence/2026-09-28-full-audit/figma-v2-present-163047-va-hero-expanded.png)、[Disclaimer](../../evidence/2026-09-28-full-audit/figma-v2-present-163110-va-disclaimer.png)、[Welcome](../../evidence/2026-09-28-full-audit/figma-v2-present-163123-va-welcome.png)、[返回详情后头图空白](../../evidence/2026-09-28-full-audit/figma-v2-present-163143-va-return-hero-missing-renderer-unresolved.png)。这些都是 Figma 重建截图，不是新的 App 状态。

头图空白时，绿色展开图标和原布局空间仍在。16:31:43、16:31:59 和 16:32:19 的缺图画面相同，公共截图复用同一份；16:32:31 重载后，16:33:06.714 截图再次出现头图，与首次有图画面的原始截图字节相同，复用该公开图。接着重新执行 `here → ACCEPT → CloseWeb`，16:33:53 又返回 `42:6` 且头图消失；16:33:54.022 截图与 16:31:43.076 缺图画面字节相同，复用失败图。因此不能只记录重载恢复而把问题关闭；`D-VA-HERO-RETURN-RENDER` 保持 open，来源图片没有被修改，后续需检查 Figma 导入图片/渲染并复验，尚未确定根因。

这条原型只采样稳定状态：More 直接到头图已加载的详情，`here` 直接到 Disclaimer，跳过真实 App 的中间加载态。另一个来源边界是：真实 App 已确认的网页 X 返回起点为输入尝试后的空白网页，当前原型 X 从 Welcome 返回同一详情；精确起点尚未在原 App 独立复验，记为 `D-VA-SOURCE-STATE-SAMPLING`。原 App 的输入定位/空白页面问题与这里的 Figma 头图消失是两件不同的观察，不相互证明。

聊天输入/发送、问号、网页浏览器控件、部门链接、滚动和所有返回边界仍未全部实现。ACCEPT 热点在编辑时已修正为单一按钮，正文负向测试是其范围验证；没有把点击整页直接进入 Welcome 当作正确交互。


## Calendar：13 条固定样例连接已实跑

[Calendar · Public academic events](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=42-165&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=42%3A165&show-proto-sidebar=1)是编辑器实际复制的 flow link。16:50–16:52 UTC 在独立 tab 11 中选择 Fit width and height，逐条点击并核对 URL/AX；`PROTO-CALENDAR-V2-001` 的13条不同连接通过，覆盖十张公开校历状态。通过范围是固定日期、公共事件与筛选样例，Calendar 全交互仍未完成。

| 动作时间（UTC） | 热点与操作 | 实际节点转换 | 结果 |
| --- | --- | --- | --- |
| 16:50:49.747 | Day26 `42:255` | `42:165 → 42:325` | 通过 |
| 16:50:55.706 | EventCard `42:447`，实际点击省略号位置 | `42:325 → 42:479` | 通过；整卡热点范围差异保留 |
| 16:51:01.226 | Back `42:489` | `42:479 → 42:325` | 通过 |
| 16:51:08.183 | ViewMode `42:334` | `42:325 → 42:1375` | 通过 |
| 16:51:14.444 | HistoryToggle `42:1379` | `42:1375 → 42:1493` | 通过 |
| 16:51:35.025 | NextMonth `42:332`，重置测试起点后执行 | `42:325 → 42:1062` | 通过 |
| 16:51:41.019 | PreviousMonth `42:1067` | `42:1062 → 42:1215` | 通过，九月选中1日 |
| 16:51:49.003 | Day28 `42:1311` | `42:1215 → 42:165` | URL/AX通过；该步未单独截图 |
| 16:51:55.371 | Filter `42:278` | `42:165 → 42:492` | 通过，保留 Acad 选中 |
| 16:52:03.163 | SelectAll `42:660` | `42:492 → 42:680` | 通过 |
| 16:52:08.758 | SelectAll `42:848` | `42:680 → 42:876` | 通过 |
| 16:52:16.269 | AcadCalendar `42:1056` | `42:876 → 42:492` | 通过 |
| 16:52:24.782 | Apply `42:677` | `42:492 → 42:165` | 通过，公共 Sep28 空态 |

显示历史后，16:51:23.554 使用 **Figma Restart** 回到 `42:165`，16:51:29.272 再点26日到 `42:325` 才测试月份分支。这个重置是测试操作，没有把它冒充为原 App 的历史返回、周视图或额外设计连线。

公开运行证据：[完整演示上下文](../../evidence/2026-09-28-full-audit/figma-v2-present-165044-calendar-context-account-redacted.png)、[公共假期详情](../../evidence/2026-09-28-full-audit/figma-v2-present-165056-calendar-holiday-detail.png)、[Sep26](../../evidence/2026-09-28-full-audit/figma-v2-present-165101-calendar-sep26.png)、[Events](../../evidence/2026-09-28-full-audit/figma-v2-present-165108-calendar-events.png)、[History](../../evidence/2026-09-28-full-audit/figma-v2-present-165114-calendar-history.png)、[Oct1](../../evidence/2026-09-28-full-audit/figma-v2-present-165135-calendar-oct1.png)、[Sep1](../../evidence/2026-09-28-full-audit/figma-v2-present-165141-calendar-sep1.png)、[Acad filter](../../evidence/2026-09-28-full-audit/figma-v2-present-165155-calendar-filter-acad.png)、[All filter](../../evidence/2026-09-28-full-audit/figma-v2-present-165203-calendar-filter-all.png)、[None filter](../../evidence/2026-09-28-full-audit/figma-v2-present-165209-calendar-filter-none.png)、[Apply 后 Sep28](../../evidence/2026-09-28-full-audit/figma-v2-present-165225-calendar-sep28-applied.png)。完整上下文只对右上账户头像作显式黑色遮罩；其余图为357×601原像素裁片。

初始 Sep28 与最终 Apply 图裁片逐像素相同；首次选择 Sep26 与详情返回图裁片相同，分别复用后者。再次选中 Acad 的16:52:17.626截图与16:51:55.883截图字节相同，也复用既有图。Sep1→Sep28 的动作结果有独立 URL/AX，目标画面引用之后 Apply 的截图，没有伪称该步已截图。

这次十张目的状态中没有观察到 VA 那类缺图现象，主要结构可辨。字体、图标和部分几何仍近似；三个筛选状态共用公开 Sep28 背景的合成差异保持显式。原生 App 已观察的详情入口是省略号，当前连接附在整张 EventCard 上；本轮原型仍点省略号位置，只证明这个区域可用。更大的点击区域未在原 App 验证，登记 `D-CALENDAR-EVENT-HITAREA`，需限制热点或补查来源。

其它日期/事件、Hide History、筛选 Close、All/None 的 Apply、其它分类组合、周视图/周选择器、事件列表滚动及底部导航仍未全部连接。不能把13条样例通过当成完整 Calendar、所有筛选结果或逐像素验收通过。

## 新增11帧：Menu / Settings / Policies / Food

16:56–16:57 UTC，普通 SVG 导入和实际编辑器节点 URL 确认了以下11帧，导入后 `01 · Observed UI` 共36帧。此批导入时11帧均为 `not_run`；随后Food五帧的实际运行与新增两张地图单列在下一节，六张菜单/设置/政策帧仍未运行。当前合计 **38帧**。源码哈希和来源证据在 [coverage.json](coverage.json)，详细素材边界见 [design/README.md](../../design/README.md)。

| 原生状态（如有别名则显式列出） | SVG 源码 | 真实 Figma 节点 | 位置 |
| --- | --- | --- | --- |
| `S-DRAWER` | [drawer-menu-items.svg](../../design/polyulife/drawer-menu-items.svg) | [50:1846](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1846) | 0, 8400 |
| `S-SETTINGS` | [settings.svg](../../design/polyulife/settings.svg) | [50:1794](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1794) | 700, 8400 |
| `S-EMERGENCY` | [emergency-dialog.svg](../../design/polyulife/emergency-dialog.svg) | [50:1778](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1778) | 1400, 8400 |
| `S-PROFILE-DEMO` → `S-PROFILE` | [profile-demo.svg](../../design/polyulife/profile-demo.svg) | [50:1818](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1818) | 2100, 8400 |
| `S-PRIVACY` | [privacy-policy.svg](../../design/polyulife/privacy-policy.svg) | [50:2058](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2058) | 0, 9600 |
| `S-TERMS` | [terms-of-use.svg](../../design/polyulife/terms-of-use.svg) | [50:1862](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1862) | 700, 9600 |
| `S-FOOD-LIST` | [food-list.svg](../../design/polyulife/food-list.svg) | [50:1911](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-1911) | 0, 10800 |
| `S-FOOD-HOURS` | [food-list-hours.svg](../../design/polyulife/food-list-hours.svg) | [50:2124](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2124) | 700, 10800 |
| `S-FOOD-DETAIL` | [food-detail.svg](../../design/polyulife/food-detail.svg) | [50:2013](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2013) | 1400, 10800 |
| `S-FOOD-TAG` → `S-FOOD-TAG-RESULT` | [food-tag-search.svg](../../design/polyulife/food-tag-search.svg) | [50:2107](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2107) | 2100, 10800 |
| `S-FOOD-IMAGE` | [food-image.svg](../../design/polyulife/food-image.svg) | [50:2230](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2230) | 0, 12000 |

多数源码576×970；菜单仅489×642公开菜单裁片，紧急提示仅520×462独立弹窗，不代表完整抽屉或原 App 背景。Profile 带可见 DEMO 标签，全部个人值与头像为合成示例。政策网页只重建实际可见首屏；Food 地图、品牌图为真实素材裁片，应用文字/按钮为原生文字与矢量，未把整页截图用作设计底图。以上区别保持在台账 `content_policy` 中，既不恢复被遮盖的个人资料，也不把裁片、合成页或导入当成原生功能验收。

## Food：11个连接控件通过导航，图片显示仍未通过

[Food · VA210 and Chinese Soup](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=50-1911&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=50%3A1911&show-proto-sidebar=1)来自实际 Copy flow link。`PROTO-FOOD-V2-001` 截至17:11:57.912 UTC，**11个不同连接控件的样例导航已通过，整体结果为 `failed`**：列表和详情存在重复图片丢失/恢复，视觉验收 `failed_unresolved`。不能将正确目标节点当成整条流程复现通过。

17:01:15.286 UTC 已确认另两张地图导入，令当前文件达到38帧。两张源码都采用指针位于标题栏时补拍的完整地图可见区域，标题/Back为可编辑元素；地图地形和地点文字是公开地图图像，不代表原型支持动态地图。

| 状态 | SVG | 实际节点 | 位置与运行状态 |
| --- | --- | --- | --- |
| `S-FOOD-MAP` | [food-map.svg](../../design/polyulife/food-map.svg) | [50:2246](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2246) | 700,12000；展开及Back已测 |
| `S-FOOD-MAP-PANNED` | [food-map-panned.svg](../../design/polyulife/food-map-panned.svg) | [50:2267](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=50-2267) | 1400,12000；未连线、`not_run` |

Food配置了四个真正的 **Back** 动作：图片X `50:2234`、Search Back `50:2111`、详情Back `50:2055`、地图Back `50:2264`。它们按原型历史返回前一帧，没有为详情硬编码固定列表目的地。下表包含主路径11次导航，以及重置后的直接详情入口及复验；其中同一详情Back控件在不同栈中多次使用，不重复计算为新连接。

| 动作时间（UTC） | 控件 | 实际节点转换 | 导航结果 |
| --- | --- | --- | --- |
| 17:03:06.068 | OpeningHours1 `50:1928` | `50:1911 → 50:2124` | 通过 |
| 17:03:16.650 | 展开列表的 VenueMenu1 `50:2151` | `50:2124 → 50:2013` | 通过 |
| 17:03:26.372 | ExpandImage `50:2020` | `50:2013 → 50:2230` | 通过 |
| 17:03:36.545 | CloseImage `50:2234`，Back | `50:2230 → 50:2013` | 通过 |
| 17:03:44.422 | TagDetail0 `50:2036` | `50:2013 → 50:2107` | 通过 |
| 17:03:52.844 | SearchResult `50:2121` | `50:2107 → 50:2013` | 通过 |
| 17:04:03.977 | ExpandMap `50:2050` | `50:2013 → 50:2246` | 通过 |
| 17:04:13.710 | 地图Back `50:2264` | `50:2246 → 50:2013` | 通过 |
| 17:04:24.115 | 详情Back `50:2055` | `50:2013 → 50:2107` | 通过，回搜索结果 |
| 17:04:33.366 | Search Back `50:2111` | `50:2107 → 50:2013` | 通过，回原详情 |
| 17:04:43.395 | 详情Back `50:2055` | `50:2013 → 50:2124` | 节点通过；列表地图/品牌图短暂缺失 |
| 17:05:30.262 | 未展开列表的 VenueMenu1 `50:1934` | `50:1911 → 50:2013` | 节点通过；详情头图/地图缺失 |
| 17:11:45.972 | 新tab13复测同一 `50:1934` | `50:1911 → 50:2013` | 节点通过；缺图再次出现 |
| 17:11:57.504 | 详情Back `50:2055` | `50:2013 → 50:1911` | 通过，回未展开列表 |

17:05:21.897、17:11:20.033 的 Figma Restart 是测试重置；后者第一张截图仍黑屏加载，17:11:32.950 才显示列表。直接从未展开列表进详情是当前原型的额外来源样例：原生 App 精确记录的详情入口来自已展开营业时间的列表，这个未展开起点还需独立核实。原生结果/地图进入过程也有加载态，当前样例跳到稳定详情/地图；这些差异记为 `D-FOOD-SOURCE-STATE-SAMPLING`。

公开证据：[完整演示上下文](../../evidence/2026-09-28-full-audit/figma-v2-present-170259-food-context-account-redacted.png)、[初始列表](../../evidence/2026-09-28-full-audit/figma-v2-present-170259-food-list.png)、[营业时间展开](../../evidence/2026-09-28-full-audit/figma-v2-present-170306-food-hours-expanded.png)、[详情图片正常](../../evidence/2026-09-28-full-audit/figma-v2-present-170317-food-detail-images-loaded.png)、[图片展开](../../evidence/2026-09-28-full-audit/figma-v2-present-170326-food-hero-expanded.png)、[标签结果](../../evidence/2026-09-28-full-audit/figma-v2-present-170344-food-tag-result.png)、[全屏地图](../../evidence/2026-09-28-full-audit/figma-v2-present-170404-food-full-map.png)。多数为357×601原像素裁片，对应576×970设计帧；完整上下文仅遮盖右上账户头像。

视觉失败与复查如下：

- 17:04:43.907 返回正确 hours 节点，但[列表地图和品牌图消失](../../evidence/2026-09-28-full-audit/figma-v2-present-170443-food-list-images-missing-renderer-unresolved.png)。17:05:08.893 再截图已恢复，裁片像素与原营业时间图一致；该工具调用仅截图，没有执行重载。
- 17:05:30.730 Restart 后直接进详情，[头图和嵌入地图缺失](../../evidence/2026-09-28-full-audit/figma-v2-present-170530-food-detail-images-missing-renderer-unresolved.png)。17:05:41、17:06:41以及最终17:11:46.294的原始截图字节相同，公开图复用同一失败证据。
- 中途[17:08:05图片恢复](../../evidence/2026-09-28-full-audit/figma-v2-present-170805-food-detail-images-restored.png)和[17:08:17缩放后的详情](../../evidence/2026-09-28-full-audit/figma-v2-present-170817-food-detail-resized.png)分别为471×794、305×515原像素裁片；捕获视口发生变化，未人为缩放图片。17:10:52新tab也暂时出现正常详情，随后直接进入又缺图。无法据此确定恢复或缺图的根因，`D-FOOD-IMAGE-RENDER` 保持open。
- 关闭旧测试标签后，视口变化伴随点击坐标不匹配；17:07:06和17:07:22均未导航，属于定位不确定尝试。新tab13的直接入口和Back已成功复验，这些早先失败没有被归为原App缺陷或已确认的设计连接缺陷。

正常详情的17:03:17、17:03:36、17:03:53、17:04:14、17:04:35截图字节相同；两次标签结果也相同。最终列表与17:11:32原图相同，和公开初始列表裁片仅一小块地图纹理不同，属于同一状态；公开初始图作外观参照，最终返回另有URL/AX记录，不声称两图字节相同。17:10:52正常详情同样只有小块地图像素差异，不新增设计状态。

原型地图尚无任意平移/缩放，panned帧没有接入；其它商户/标签/查询、营业时间收起、列表面板/滚动、Call、Online Order、定位和外部地图均未完整实现。四个Back只验证上述栈；字体、图标和细部布局仍近似。当前38帧、39个连接控件的存在及局部运行不证明Food、Room或全应用完成。

## 第一版草稿：历史验证与偏差

- 文件：[PolyULife — Observed UI & Interaction Atlas](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)。此处记录第一版原生 Agents 草稿，保留作为历史比较。
- [可运行原型入口](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI---Interaction-Atlas?node-id=2-50&starting-point-node-id=2%3A50)。14:55–14:57 UTC 已实际点击三条连接并核对节点 URL：联想 `2:50` → ALL `2:98` → Available `2:211` → ALL `2:98`。
- 原生 Agents 完成报告列出 **4 frames、7 components、3 connections**。其中三条连接已独立运行；`room-suggest-a` 在编辑器中确认是 576×970 的 Frame，Auto layout 已启用。随后通过 Return 选出 Header、DaySelector、SearchRowContainer、Line、EmptyState 五个子图层；15:03:27 UTC 进一步选中原生 [Text 2:55](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-55)，右栏确认 Inter Bold 18 px、111×22。这个 frame 的原生结构与标题可编辑属性已核对，其余 frame 和全部组件仍需逐项检查。
- **第一版视觉核验未通过**：生成稿在标题高度、字号/控件比例、日期边框、搜索图标与清空外观、Available 时段排列和背景颜色上偏离来源。下面逐项列出；可运行原型不等于忠实复现。
- Figma 原生 Agents 已提示免费 Starter 计划的 **daily credits** 用尽，后续提示生成受限；没有付费或升级。现有文件及编辑器仍可核验/修改。主线另外验证普通 SVG 粘贴可生成原生 Frame、Vector、Text，检查测试 Text 12:5 后已删除临时 Frame 12:2；后续四张源码已完成并导入，当前节点与验证见上方 Room V2。这条替代制作路线不受 Agents 提示额度影响。
- 当前路线为浏览器 Computer Use 操作 Figma Design 与其原生 Agents。Codex Figma 插件连接仍未确认；该连接不影响当前浏览器路径。

### 来源与真实节点

| 观察状态 | 来源截图 | 已核对 Figma 节点 |
| --- | --- | --- |
| `S-EMPTYQUERY` | [初始空查询](../../evidence/2026-09-28-full-audit/room-135521-empty-query.png) | 生成报告称已创建 `room-empty`；节点 ID 与内部结构待核验 |
| `S-SUGGESTION` | [A 联想](../../evidence/2026-09-28-full-audit/room-135612-a-suggestion.png) | [room-suggest-a · 2:50](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-50) |
| `S-ALL` | [AG206 ALL](../../evidence/2026-09-28-full-audit/room-135628-ag206-all.png) | [room-all · 2:98](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-98) |
| `S-AVAILABLE` | [AG206 Available](../../evidence/2026-09-28-full-audit/room-135653-ag206-available.png) | [room-available · 2:211](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-211) |

### 原型实际运行

公开运行截图：[联想页](../../evidence/2026-09-28-full-audit/figma-present-145546-room-suggest-a.png)、[ALL 稳定状态](../../evidence/2026-09-28-full-audit/figma-present-145617-room-all.png)、[Available 稳定状态](../../evidence/2026-09-28-full-audit/figma-present-145645-room-available.png)。[帧属性与额度提示](../../evidence/2026-09-28-full-audit/figma-145434-frame-properties-and-credits.png)证明编辑器状态，不能代替视觉验收。最后一次 ALL 返回依据 URL/AX，没有单独的返回截图。

| 动作时间（UTC） | 点击 | 实际结果 | 判定范围 |
| --- | --- | --- | --- |
| 14:56:01 | 联想页 AG206 项 | URL 从 `2:50` 变为 `2:98`，进入 ALL 状态 | 该点击连接通过；不证明输入框有真实联想逻辑 |
| 14:56:31 | ALL 页 Available | URL 从 `2:98` 变为 `2:211`，显示六个可用时段 | 该连接通过；时段排列视觉不通过 |
| 14:57:31 | Available 页 ALL | URL 从 `2:211` 返回 `2:98` | 该返回连接通过；真实 App 的同日期这一步仍需与既有观察精确对应 |

本轮真实 App 已观察在 Sun 04-Oct 的 Available 空结果切换 ALL；原型第三条使用 Tue 29-Sep 的有结果版本。二者操作机制相近，仍须补做同日期数据状态的精确复核，不能修改原始 App 记录来迁就原型。

### 已发现的复现偏差

| 偏差 | 来源与生成稿差异 | 状态与修复要求 |
| --- | --- | --- |
| `D-ROOM-HEADER-SCALE` | 生成稿标题区约 60 px，来源截图约 100 px；整体字体及控件偏小 | 未解决；在相同 576×970 比例核对尺寸并重排，不用整体放大掩盖局部差异 |
| `D-ROOM-DATE-BORDER` | 生成稿给日期增加了来源中未观察到的边框 | 未解决；按来源恢复未选日期外观 |
| `D-ROOM-SEARCH-DECORATION` | 生成稿输入区增加 leading magnifier，并出现不应有的模糊 clear 外观 | 未解决；区分 App 真实控件与截图中的 Computer Use 指针/高亮，不把工具覆盖物做进设计 |
| `D-ROOM-SLOT-ORDER` | Available 来源前两行是 `08:30 / 09:00`、`11:30 / 12:00`；生成稿是 `08:30 / 11:30`、`09:00 / 12:00`。ALL 第一行也从来源 `08:30 / 09:00` 变成生成稿 `08:30 / 12:30` | 未解决；保持时间与行列对应，修复后在 Present 再看六个时段 |
| `D-ROOM-BACKGROUND` | 第一版 ALL/Available 结果区使用灰白，与来源的白色背景不同；空查询/联想下方浅灰是来源真实样式 | 未解决；分别核对页面、容器与卡片填充 |

这些是 Figma 草稿的复现偏差，不是 PolyULife 新发现的缺陷。

第一版的 Processing、失败视觉检查和三条连接通过均保留为历史记录。继续工作应使用上方 Room V2 的当前节点，不能以旧节点的检查结果代替新节点验收。

## 文件组织

当前免费计划最多三个工作页。现有 `00 · Archive — initial AI draft`（原 `Page 1`）保存旧草稿，`01 · Observed UI` 保存当前复现；后续优先在当前页面增加 **sections**，整个文件保持不超过三个工作页。下表为当前组织和预留位置：

| 工作页（最多三页） | 其中的 sections |
| --- | --- |
| `00 · Archive — initial AI draft`（已有） | 旧 Room 草稿与原生 Agents 组件；保留历史，不作为当前验收入口 |
| `01 · Observed UI`（已有） | 当前 Room 四状态与 flow，后续模块、组件和分析优先按 sections 增补 |
| 第三个工作页（预留） | 确有需要时分出共享组件或分析，创建前先核对实际页数 |

旧页的 `Flow 1` 已改名为 `Archive · Initial AI draft — not validated`；页面和流程改名已通过实际编辑器确认，原节点ID与历史三条导航记录保持不变。这里的“not validated”说明其视觉/整体状态，没有抹掉已有的局部点击证据。

[17:24:56最终编辑器截图](../../evidence/2026-09-28-full-audit/figma-v2-editor-172456-observed-ui-pages-calendar-connections-account-redacted.png)确认Archive/Observed UI页名、可见图层及Calendar选中帧与连线；右上账户头像已显式遮盖。这是编辑器结构证据，不能替代全部节点清点或Present运行。

先按真实 UI 完成复现；用户尚未批准的改进建议保留为分析或独立方案，不能覆盖原应用证据。课程后续 redesign 可复用组件并建立独立版本。

## 从状态到节点

每个 `state` 对应一个可定位的 Figma frame、overlay 或 component variant。节点命名使用 `[state_id] 实际页面/状态名`，名称来自观察记录。`state_node_mappings` 记录：

- `state_id`、`node_id`、`node_url`、Figma 工作页及节点类型。
- `source_evidence_ids`：真实截图和辅助 AX 引用。
- `viewport`：截图内容区域尺寸、缩放及 Figma frame 尺寸；窗口装饰与应用内容边界分开记录。
- `content_policy`：真实界面中的个人字段在共享版替换为明确的示例值；保留文案长度、层级和交互作用。
- `visual_review`：检查时间、证据、结果和未解决差异；真实核对前为 `not_run`。

截图用作对照来源。可编辑文字、图形、组件和布局承载正式页面内容；整页截图加少量热点只能作为临时取证或对照层，不能满足完整可编辑复现。控件样式由已观察截图量取；尚未出现的颜色、字体、状态和页面结构保持待补，不用惯例当成原应用事实。

加载、空状态、错误提示、弹窗、筛选、展开菜单和键盘相关变化在实际观察到后分别建模；共享组件可使用 variant，出现/退出方式由实际动作决定。多种数据内容若交互等价可采用脱敏示例，但记录所依据的状态及差异。

## 从动作到连接

每个已经实际执行并得到反馈的 `action` 对应 Figma 连接或组件交互。`action_connection_mappings` 记录：

- `action_id`、起点 `source_node_id`、目标 `target_node_id` 或明确目标 URL。
- `trigger`、`behavior`、`transition`、必要前置条件，以及关联的反馈状态。
- 返回、关闭、取消、清空等恢复路径对应的动作 ID。
- `implementation_status` 与 `prototype_run_ids`；只配置连线而未运行不能记为验证通过。

普通导航使用实际目标；弹层使用 overlay/关闭交互；滚动与固定导航按真实截图和操作复现。文本输入、日期、搜索、筛选等按实际反馈表现，用变量、组件或明确样例实现。Figma 能力不足时登记 `reconstruction_deviations`，写明原应用行为、当前实现、影响范围和补齐方式；静态画面不能证明输入流程完整。

外部网页、系统权限、登录和设备能力在原型中标明入口及真实观察到的交接结果。展示示例成功反馈时必须是原型模拟并有来源状态，不得执行真实预约或伪装成真实业务完成。无法观察的分支在台账保留缺口。

## 验证和交付

1. 在 Figma 编辑界面打开真实节点，核对文字、图标、布局、比例、可见状态和个人字段处理。保存节点 URL 和核对证据后，才更新相应视觉检查状态。
2. 打开 Figma Present，从每个流程起点按台账动作操作。每次运行登记 `id`、时间、起点节点、动作序列、预期状态、实际结果、证据和失败项。
3. 检查导航、弹层、选择、输入反馈、滚动、外部跳转说明和返回路径。页面是否可达、控件是否响应、结束后是否可继续操作分别验证。
4. 失败关联到原动作，修复后新增复验记录。共享链接以实际可访问性检查为准；URL 存在不证明成员可以查看或使用。
5. 将节点和动作映射与全应用台账逐条比对。任何尚未观察、缺截图、缺节点、缺连线、未复验或仍有阻碍的项均保持未完成；全应用完成判定见 [README](README.md#完成判定)。

交付包含真实 Figma 文件及原型链接、状态/动作映射、证据索引、HCI 分析及明确的剩余缺口。Agent 对原型的走查是功能验证记录；课程真人可用性评估另按 [项目说明](../project-brief.md) 执行。
