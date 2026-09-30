# Figma 复现与证据对应约定

最新[Calendar节假日详情上下文](calendar-detail-context-prototype-walkthrough.md)新增一张详情画板和两条连接，Monday/Tuesday月视图返回及后续模式循环实际回放。八项比较六项相等、两个Home底部局部差异保留。累计122画板、284控件、61次回放，全应用仍 `not_verified`。

最新[Home图片填充回归](home-image-repair-prototype-walkthrough.md)重传Monday/Tuesday公开照片素材，六个保存的Calendar返回均保留照片；九项比较五项相等、四项底部局部差异，长期稳定性和完整保真仍开放。累计121画板、282控件、59次原型运行，全应用 `not_verified`。

最新[Calendar模式循环](calendar-modes-prototype-walkthrough.md)接入公共月/事件/历史三个上下文和八条控件，保留Monday/Tuesday调用者。Monday底部Calendar漏接失败已修复并回放，Home缺图仍开放。累计121画板、282控件、56次运行，全应用仍 `not_verified`。以下统计为历史批次快照。

最新[Calendar周选择器回放](calendar-week-picker-prototype-walkthrough.md)补入展开/滚轮13两个状态和四条控件；收起仍Week5，拖动仅代理原生滚动。Tuesday Home返回的底部缺图失败保留。累计118画板、274控件、53次运行，全应用仍 `not_verified`。以下统计为历史批次快照。

最新[天气官方网页回放](weather-web-prototype-walkthrough.md)新增既有原生状态的一个网页画板和两条控件。入口与原型返回已回放，工具瞬时缺图（留存图已恢复）、原PNG重传及两轮复验保留；累计116画板、270控件、51次运行。网页关闭原生结果、Cookie/浏览器控制、完整滚动与可编辑保真仍待补。全应用为 `not_verified`；以下统计是历史批次快照。

2026-09-30最新[Food地图平移与返回](food-map-pan-prototype-walkthrough.md)在既有画板50:2246/50:2267补接MapViewport拖动与平移Back；一个Tuesday来源链路已回放，累计115画板、268控件、48次运行。地理内容为截图裁片，On drag与300ms动画为离散原型，完整范围仍为 `not_verified`。以下批次数字保留为历史快照。

2026-09-30最新批次见[Preview登录边界与复制反馈](room-preview-controls-prototype-walkthrough.md)：画板452:19为576×1024、位置0,43000，校徽来自公开原生截图，表单及导航未连线；Copy文字312:242为On click→Close overlay，顶部和滚动后均已回放。当前109个映射画板、245个配置控件、40次运行。完整认证/指南/调用者和实际剪贴板语义尚未完成，全应用保持 `not_verified`。本页后续较早批次数字为历史快照。

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

2026-09-30后续：[图片填充修复与四轮分阶段回放](virtual-assistant-image-repair-walkthrough.md)保存本次缺图复现、头图原素材重传、随后发现并修复的四处网页校徽/头像，以及最终两轮回放。原失败运行和截图不改；两项图片偏差改为 `partially_resolved`，图片区域像素差异、来源状态与完整视觉仍开放。

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

## Apps：11帧导入、12个连接与中文修复复验

[Apps · Categories and VRS 原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI---Interaction-Atlas?node-id=61-2&t=Ohxzpdr7gRXrVgsv-0&scaling=scale-down&content-scaling=fixed&starting-point-node-id=61%3A2&show-proto-sidebar=1)已在独立tab16按Fit width and height实跑；完整帧显示为357×601。11张576×970源码已确认原生Frame/Group/Text层级、节点和位置。首次12个连接导航通过，但All/Study的LEARN中文及登录页中文缺字，首次run保留failed；修复四个Text字体后，三个受影响状态和相关路径已重新观察通过。全像素、全Apps交互仍未验收。

| State | SVG source | Figma node | Canvas |
| --- | --- | --- | --- |
| `S-APPS-ALL` | [apps-all.svg](../../design/polyulife/apps-all.svg) | [61:2](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-2) | 0, 13200 |
| `S-APPS-CAMPUS` | [apps-campus.svg](../../design/polyulife/apps-campus.svg) | [61:135](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-135) | 700, 13200 |
| `S-APPS-STUDY` | [apps-study.svg](../../design/polyulife/apps-study.svg) | [61:215](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-215) | 1400, 13200 |
| `S-APPS-IT-TIPS` | [apps-it-tips.svg](../../design/polyulife/apps-it-tips.svg) | [61:344](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-344) | 2100, 13200 |
| `S-APPS-HEALTH` | [apps-health.svg](../../design/polyulife/apps-health.svg) | [61:475](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-475) | 0, 14400 |
| `S-APPS-WELLNESS` | [apps-wellness.svg](../../design/polyulife/apps-wellness.svg) | [61:585](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-585) | 700, 14400 |
| `S-APPS-JOB` | [apps-job.svg](../../design/polyulife/apps-job.svg) | [61:663](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-663) | 1400, 14400 |
| `S-APPS-JOB-BAR-LEFT` | [apps-job-category-left.svg](../../design/polyulife/apps-job-category-left.svg) | [61:721](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-721) | 2100, 14400 |
| `S-APPS-VRS-DETAIL` | [apps-vrs-detail.svg](../../design/polyulife/apps-vrs-detail.svg) | [61:778](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-778) | 0, 15600 |
| `S-APPS-VRS-WEB-LOADING` | [apps-vrs-web-loading.svg](../../design/polyulife/apps-vrs-web-loading.svg) | [61:805](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-805) | 700, 15600 |
| `S-APPS-VRS-LOGIN` | [apps-vrs-web-login.svg](../../design/polyulife/apps-vrs-web-login.svg) | [61:843](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=61-843) | 1400, 15600 |


Figma标签`S-APPS-IT`、`S-APPS-JOB-CATEGORIES-LEFT`、`S-APPS-VRS-WEB-LOGIN`分别映射到上表既有状态ID。Health曾被临时误命名，按实际服务分组修正并核对。

| 执行时间（UTC） | 热点 | 转换 | 结果 |
| --- | --- | --- | --- |
| 18:01:51 | CategoryCampus `61:109` | `61:2 → 61:135` | 通过 |
| 18:02:03 | ServiceMenuVRS `61:155` | `61:135 → 61:778` | 通过 |
| 18:02:16 | OpenVRS `61:791` | `61:778 → 61:843` | 通过，跳过加载帧 |
| 18:02:55，18:05后确认 | CloseWeb `61:855` | `61:843 → 61:778` | 点击后工具中断；重新连接后的URL和截图确认返回 |
| 18:05:45 | Back `61:799` | `61:778 → 61:135` | 通过，固定返回Campus |
| 18:06:00 | CategoryStudy `61:192` | `61:135 → 61:215` | 通过 |
| 18:08:52 | CategoryITTips `61:324` | `61:215 → 61:344` | 通过 |
| 18:08:58 | CategoryHealth `61:458` | `61:344 → 61:475` | 通过 |
| 18:09:06 | CategoryWellness `61:568` | `61:475 → 61:585` | 通过 |
| 18:09:14 | CategoryJob `61:649` | `61:585 → 61:663` | 通过 |
| 18:09:22 | CategoryBar `61:688`，On drag | `61:663 → 61:721` | 通过，一个固定拖动样例 |
| 18:09:29 | CategoryAll `61:749` | `61:721 → 61:2` | 通过 |

运行截图：[Campus](../../evidence/2026-09-28-full-audit/figma-v2-present-180152-apps-campus.png)、[VRS详情](../../evidence/2026-09-28-full-audit/figma-v2-present-180203-apps-vrs-detail.png)、[IT Tips](../../evidence/2026-09-28-full-audit/figma-v2-present-180852-apps-it-tips.png)、[Health](../../evidence/2026-09-28-full-audit/figma-v2-present-180859-apps-health.png)、[Wellness](../../evidence/2026-09-28-full-audit/figma-v2-present-180906-apps-wellness.png)、[Job](../../evidence/2026-09-28-full-audit/figma-v2-present-180914-apps-job.png)、[拖动后](../../evidence/2026-09-28-full-audit/figma-v2-present-180922-apps-job-category-bar-dragged.png)。返回详情/Campus/All与先前状态裁片相同，复用原图；动作时间和URL分别保留。

### 中文缺字修复

首次 [All](../../evidence/2026-09-28-full-audit/figma-v2-present-180104-apps-all-cjk-missing.png)、[Study](../../evidence/2026-09-28-full-audit/figma-v2-present-180600-apps-study-cjk-missing.png)、[Login](../../evidence/2026-09-28-full-audit/figma-v2-present-180217-apps-vrs-login-cjk-missing.png)实际存在缺字；这是Figma字体复现问题，不是PolyULife缺陷。编辑器将All标题Text `61:54`和Study标题Text `61:223`设为Noto Sans TC，登录按钮 `61:873`和网页标题 `61:857`设为Noto Sans SC。相同定向字体改动已同步到 [生成脚本](../../design/scripts/build_apps_svg.py)及SVG，台账hash记录更新后源码；没有重新创建frame或热点。

修复后的 [All：18:11:11](../../evidence/2026-09-28-full-audit/figma-v2-present-181111-apps-all-cjk-fixed.png)、[Study：18:13:53](../../evidence/2026-09-28-full-audit/figma-v2-present-181353-apps-study-cjk-fixed.png)、[Login：18:14:46](../../evidence/2026-09-28-full-audit/figma-v2-present-181446-apps-vrs-login-cjk-fixed.png)均显示先前缺失中文。复验重走All→Campus→Study，再通过Figma Restart进入All→Campus→详情→Login→X返回详情，截止`2026-09-28T18:15:07.103Z`。一次Restart鼠标点击未跳转，随后Enter执行成功，只记测试重置。独立修复run通过只关闭这些缺字，字体指标/图标近似和其它视觉范围仍待查。

12个热点覆盖10个运行帧；加载帧`61:805`导入但未连线、未运行。原生Open先加载再到登录，这里直接进入稳定空登录；未模拟加载时延、登录、网页控制或其它服务。CategoryBar的On drag跳转到一个固定状态，不支持任意滚动，也未限制为原生向右距离。各分类间只连已记录顺序；Apps→Home尚未接线，原生后续返回已有独立证据。

VRS加载标识为公开加载截图的53×54局部，登录字标复用已有公开PolyU素材；其它卡片、分类、文字和按钮是可编辑重建，没有整页截图背景。字体修复不代表全部画面逐像素验收。此前VA和Food的图片消失问题仍保持未解决。

## Home / Study / Courses / QR：13帧与22个连接样例

[Home · Study, Courses and Campus QR 原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=67-820&scaling=scale-down&content-scaling=fixed&starting-point-node-id=67%3A820&show-proto-sidebar=1)已从Home实际播放。13个576×970 SVG已导入为原生可编辑Frame/Group/Text，源码由 [生成脚本](../../design/scripts/build_study_svg.py)维护。后补的Week5修正版另增一帧及返回控件，该批截止时累计63帧、74个连接控件（地图增量后为75帧/94控件）。本批原22个新热点均有导航反馈，Calendar目标偏差也已按原生证据修正并复验；**Home装饰图消失/恢复仍未解决**，整体视觉不能记通过。

| State | SVG source | Figma node | Canvas |
| --- | --- | --- | --- |
| `S-STUDY-COMPLETED` | [study-completed-demo.svg](../../design/polyulife/study-completed-demo.svg) | [67:2](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-2) | 0, 16800 |
| `S-STUDY-COMPLETED-EXPANDED` | [study-completed-demo-expanded.svg](../../design/polyulife/study-completed-demo-expanded.svg) | [67:71](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-71) | 700, 16800 |
| `S-STUDY-REQUIREMENTS` | [study-requirements.svg](../../design/polyulife/study-requirements.svg) | [67:141](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-141) | 1400, 16800 |
| `S-STUDY-OFFERINGS` | [study-subjects-public.svg](../../design/polyulife/study-subjects-public.svg) | [67:188](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-188) | 2100, 16800 |
| `S-STUDY-BLANK` | [study-blank-unresolved.svg](../../design/polyulife/study-blank-unresolved.svg) | [67:259](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-259) | 0, 18000 |
| `S-COURSES-CANVAS` | [courses-canvas-demo.svg](../../design/polyulife/courses-canvas-demo.svg) | [67:271](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-271) | 700, 18000 |
| `S-COURSES-CANVAS-EXPANDED` | [courses-canvas-demo-expanded.svg](../../design/polyulife/courses-canvas-demo-expanded.svg) | [67:360](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-360) | 1400, 18000 |
| `S-COURSES-BLACKBOARD` | [courses-blackboard-demo.svg](../../design/polyulife/courses-blackboard-demo.svg) | [67:450](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-450) | 2100, 18000 |
| `S-COURSES-BB-LOGIN` | [courses-blackboard-login.svg](../../design/polyulife/courses-blackboard-login.svg) | [67:485](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-485) | 0, 19200 |
| `S-QR-DISPLAY` | [qr-demo.svg](../../design/polyulife/qr-demo.svg) | [67:513](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-513) | 700, 19200 |
| `S-HOME-SCHEDULE-MON` | [home-demo-top.svg](../../design/polyulife/home-demo-top.svg) | [67:569](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-569) | 1400, 19200 |
| `S-HOME-SCHEDULE-TUE` | [home-demo-tuesday.svg](../../design/polyulife/home-demo-tuesday.svg) | [67:694](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-694) | 2100, 19200 |
| `S-HOME` | [home-demo-scrolled.svg](../../design/polyulife/home-demo-scrolled.svg) | [67:820](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-820) | 0, 20400 |


Home顶部Monday/Tuesday两帧未连线、未运行。Blank没有搜索入边，仅以独立URL起点检查Back；不把无法确认的原生搜索输入写成成功搜索。其余11个新帧已在本批Present出现，原型窗口内完整帧通常为357×601。跨模块Drawer采用先前局部裁片，实际显示为457×601；不能冒称全高原始手机布局。

| 热点（均为67前缀） | 实际目标 | 已测范围 |
| --- | --- | --- |
| Home FeatureStudyProgress `898` | Completed `67:2` | 进入、名称展开/收起、Requirements和公开目录 |
| Completed toggle `29` / Expanded toggle `99` | `67:71` / `67:2` | 以DEMO长名称复现双向切换 |
| TabRequirements `11` / RequirementCARA `157` | `67:141` / `67:188` | 一项公开类别目录 |
| Home FeatureMyCourses `904` | Canvas `67:271` | 进入、名称展开/收起、切Blackboard |
| Canvas toggle `292` / Expanded toggle `382` | `67:360` / `67:271` | 以DEMO课程复现双向切换 |
| TabBlackboard `280` / Blackboard Open `465` | `67:450` / `67:485` | 到达空登录表单，没有真实登录 |
| Blackboard login Back `507` | Home `67:820` | 按原生实际目标返回Home |
| Blank Back `264` | Home `67:820` | 独立Blank起点返回，没有模拟目录搜索 |
| Home NavQR `938` / QR NavHome `551` | `67:513` / `67:820` | 不可扫描的DEMO占位及返回 |
| Home Apps `890` / Food `885` / Room `878` | `61:2` / `50:1911` / `12:198` | 进入已有样例，未重测模块全部内部控件 |
| Home More `946` / Notification `944` | `12:435` / `42:1617` | 进入已有More/通知空态 |
| Home Calendar `935` | 当前`70:973`（先前`42:165`） | 先前目标偏差保留历史；Week5修正后复验通过 |
| Home Search `923` / Menu `921` | `42:1716` / `50:1846` | 进入搜索空态/公开菜单裁片；内部控件尚未完整运行 |

18:27:46–18:28:21实跑Home→Completed→展开→收起→Requirements→公开科目目录。通过Figma Restart重置后，18:28:30–18:29:23实跑Home→Canvas→展开→收起→Blackboard→空登录→Back Home；18:29:34–18:29:44实跑QR往返。随后八个跨模块入口分别从Home重置测试，Blank另以独立URL起点检查Back。这些Restart和URL导航属于测试设置，不能代替App内返回。完整每步时间、热点和证据见`coverage.json`。

18:30批量入口调用的截图已显示对应目的页，部分立即读取的URL仍为先前节点；后续分步重查确认Food `50:1911`、Room `12:198`、More `12:435`、Calendar `42:165`、Search `42:1716`。这类观察时序差异不作为确定的连接失败，也不把旧URL当成目标成功的证明。

### 中文修复与Home图片不稳定

[Blackboard首次登录](../../evidence/2026-09-28-full-audit/figma-v2-present-182909-courses-login-cjk-missing.png)红按钮缺少一个中文字。将Text `67:500`改为Noto Sans SC，并同步脚本与SVG后，重新走Home→Canvas→Blackboard→Open；[18:33:59修复画面](../../evidence/2026-09-28-full-audit/figma-v2-present-183359-courses-login-cjk-fixed.png)显示完整“登录”。此定向复验通过只关闭缺字缺陷，不包含登录提交，也不消除其它视觉问题。

[Home初始](../../evidence/2026-09-28-full-audit/figma-v2-present-182725-home-demo-with-decoration.png)有公开素材重建的装饰预览条，[课程返回Home](../../evidence/2026-09-28-full-audit/figma-v2-present-182923-home-return-decoration-missing.png)中该图缺失，QR返回重复缺失；18:31:16从Blank返回后的裁片又与初始图逐像素相同。记录为消失/恢复不稳定，根因尚未确认，不能称修复成功，也不能因症状相近就断言与VA/Food同根因或归为原App缺陷。

### 后补原生来源核查：Calendar目标已修正

18:35–18:37重新通过Computer Use操作真实Home后，Notification、Search、Menu入口分别到达此前同类空态/抽屉，原生来源缺口已补充。**Home底部Calendar实际进入Week5周课表；Figma原先却跳到Sep28的Acad空月历 `42:165`。**该按钮“能导航”与“复现正确”是两项结论，首次run保留这项来源偏差历史。实际步骤见 [原生后补核查](home-study-map-walkthrough.md#后补核查home四个入口与返回)。

随后用 [calendar-week-demo.svg](../../design/polyulife/calendar-week-demo.svg)和 [生成脚本](../../design/scripts/build_week_svg.py)重建纯文字/矢量周历，导入节点 [70:973](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=70-973)，位置700,20400，尺寸576×970。两个课表块的数量、位置、时长、代码和教室全部是显式DEMO合成值；只沿用公共标题/日期和已观察网格结构，未复制私人课程正文。

Home NavCalendar `67:935`现改连`70:973`，新周历NavHome `70:1045`返回`67:820`。18:44:10实际进入Week5，18:44:35实际返回Home，URL与截图均确认，结果截止`2026-09-28T18:44:36.057Z`。`D-HOME-CALENDAR-TARGET`因此记为已解决的限定入口偏差；旧run中的Sep28目标不被改写。此复验不证明周/日期选择和课程控件已经实现，返回时Home装饰图虽恢复可见，历史图片不稳定仍保持open。

证据：[实际Week5演示画面](../../evidence/2026-09-28-full-audit/figma-v2-present-184410-home-calendar-week-five-demo.png)、[包含修正后流程说明的上下文](../../evidence/2026-09-28-full-audit/figma-v2-present-184410-home-calendar-fixed-context-account-redacted.png)。后者账户头像已整块遮盖。18:44:36返回Home裁片与此前初始Home逐像素相同，复用原文件而保留新动作时间。

### 资料与样例边界

Completed、My Courses与Home的课程、学分、数量、日程、时间地点和考试均为显式DEMO合成资料；没有私人源像素嵌入。公共标题裁片不能证明私人课程正文的内容或完全视觉一致。QR是画叉的`DEMO / No QR code / Cannot be scanned`占位，无编码payload或二维码定位结构，条形比例也无有效期语义。公共Requirements/Subjects与空Blackboard登录保留已观察结构。

Home Room进入的是后续清空查询样例，区别于最初原生Home→Room的状态；Study/Courses/QR跳过了原生加载。Home/课程是静态滚动位置与有限数据样例，没有任意滚动、自由输入、登录、其它目录分类、反向标签或真实二维码能力。各原生待测项继续保留；Figma测试不改变原生观察状态，更不替代真人Maze评估。


## 文件组织

当前免费计划最多三个工作页。现有 `00 · Archive — initial AI draft`（原 `Page 1`）保存旧草稿，`01 · Observed UI` 保存当前复现；后续优先在当前页面增加 **sections**，整个文件保持不超过三个工作页。下表为当前组织和预留位置：

| 工作页（最多三页） | 其中的 sections |
| --- | --- |
| `00 · Archive — initial AI draft`（已有） | 旧 Room 草稿与原生 Agents 组件；保留历史，不作为当前验收入口 |
| `01 · Observed UI`（已有） | 当前 Room 四状态与 flow，后续模块、组件和分析优先按 sections 增补 |
| 第三个工作页（预留） | 确有需要时分出共享组件或分析，创建前先核对实际页数 |

旧页的 `Flow 1` 已改名为 `Archive · Initial AI draft — not validated`；页面和流程改名已通过实际编辑器确认，原节点ID与历史三条导航记录保持不变。这里的“not validated”说明其视觉/整体状态，没有抹掉已有的局部点击证据。

后续Present侧栏出现另一个`Flow 1`，实际点击定位到当前Available `12:105`，并非归档草稿。现已改名`Room · Available slots reference`，说明它是历史可用时段的直接参考入口，完整查询使用`Room Finder · A → AG206`，不提供实时预约数据。[18:17:36上下文截图](../../evidence/2026-09-28-full-audit/figma-v2-present-181736-room-reference-flow-renamed-account-redacted.png)确认新名称，账户头像已遮盖。此命名核验不新增原型导航通过记录。

[17:24:56最终编辑器截图](../../evidence/2026-09-28-full-audit/figma-v2-editor-172456-observed-ui-pages-calendar-connections-account-redacted.png)确认Archive/Observed UI页名、可见图层及Calendar选中帧与连线；右上账户头像已显式遮盖。这是编辑器结构证据，不能替代全部节点清点或Present运行。

先按真实 UI 完成复现；用户尚未批准的改进建议保留为分析或独立方案，不能覆盖原应用证据。课程后续 redesign 可复用组件并建立独立版本。

## 从状态到节点

每个 `state` 对应可定位的 Figma frame、overlay 或 component variant。同一原生状态可有不同日期、数据或聚焦上下文；额外画板使用明确的 `context_variant`，并引用与该状态对应的原生证据，不新增原生观察次数。节点命名使用 `[state_id] 实际页面/状态名`，名称来自观察记录。`state_node_mappings` 记录：

- `state_id`、`node_id`、`node_url`、Figma 工作页及节点类型。
- `context_variant`（可选）：同一原生状态的日期、数据或聚焦变体。`node_id` 必须唯一，`(state_id, context_variant)` 必须唯一；没有变体字段的历史基础画板每个状态最多一个。画板数量与原生状态数量分别统计。
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

[台账校验脚本](../../design/scripts/validate_polyulife_records.py)检查引用、文件哈希、PNG尺寸、SVG结构及节点/上下文唯一性；此结构检查不证明全应用完成或全部视觉保真。

## 校园地图增量

[地图原型与分类栏补测](map-prototype-walkthrough.md)记录12个新增可编辑Frame、20个实际回放控件、图片缺失和初始底图定向修复。地图批次结束时总计75个映射画板、94个交互控件；完整应用仍未通过。

## 菜单与 Mac 设置交接增量

[菜单原型记录](menu-prototype-walkthrough.md)将完整 DEMO 抽屉替换当前菜单映射，并新增 Mac General 窗口。15 个菜单控件已在 Present 回放（包含1个现有连接改目标），该菜单批次为76个映射画板、108个交互控件；后续政策 cookie 增量为110个控件，另有2个画板内状态。政策文字裁切和 cookie 关闭已修复，滚动、加载、弹层背景及标志图片稳定性仍未完成。

## 政策 cookie 画板内状态

[独立组件与实跑记录](policy-cookie-prototype-walkthrough.md)对应既有两张政策画板；关闭不增加导航历史。`coverage.json` 的 `figma.component_state_mappings` 单独记录内部状态及源稿哈希，避免把状态变体算成新全屏画板。

## 首页日期与返回状态增量

[日期与返回回放记录](home-date-prototype-walkthrough.md)补齐8个控件并修改Week5 Home为按历史返回。Monday→Tuesday及五条入口往返、既有功能区Calendar/Search回归已通过记录路径；当前76个Frame、2个内部状态、118个控件。直接起点与其它来源底部Home、其它日期和连续滚动仍未实现，整体保持未完成。

## 首页连续滚动增量

[连续滚动与Apps返回](home-scroll-prototype-walkthrough.md)将Monday/Tuesday既有正文转换成2个垂直滚动区域，并复制12个功能入口实例、补1个Apps返回。日期区至功能区的连续/反向/中间滚动和Apps直接往返通过；新复制的其它10个入口实例仅配置已读回、尚未回放。该连续滚动批次为76个映射Frame、131个配置控件；当时尚未实现的Apps分类绕行返回见下方增量，完整原生滚动边界仍未验证。

## Apps 分类与逐层返回增量

[Apps返回回放记录](apps-return-prototype-walkthrough.md)修改16个既有控件、补7个分类Back，当前138个配置控件。Home打开Apps覆盖层，分类切换不累积导航历史，VRS详情/登录各关闭一层。周二完整分类链、周一七个分类状态直接Back、历史Home往返已回放并保留来源与滚动位置。任意分类互跳与独立Apps退出未验证；新增分类Back的原生逐项来源仍待补查。39张Present证据与[配置读回](../../design/polyulife/apps-overlay-layout.json)已归档。

## Apps 可见分类互跳更新

[分类互跳回放](apps-category-prototype-walkthrough.md)新增33条Swap overlay并逐条实跑，当前171个配置控件。54步路线后VRS逐层返回和Monday首页滚动位置保留通过。原生记录没有增加；源分类组合、完整横向条/列表和独立退出仍待验证。配置及说明见[配置读回](../../design/polyulife/apps-category-connections.json)。

## Home功能入口与直接返回更新

[十入口回放](home-feature-return-prototype-walkthrough.md)确认五个模块初始页Back原先未连接，现补接history Back。Monday/Tuesday共十组直接往返通过并保留滚动位置，当前176个配置控件。内部绕行和独立起点未完成；Tuesday Food缺图复现，视觉保持未通过。原生记录未增加。

## Study/Courses返回栈更新

[返回栈回放](study-courses-return-prototype-walkthrough.md)更新17个控件并新增5个外层Back，当前181个配置控件。三个Home来源的六条样例链路及Tuesday八个外层出口通过，12次返回保留原Home滚动区域。中间状态原生出口仍为推断；列表、搜索、逆向页签、blank来源和其它模块内部绕行未完成。

## Map返回栈更新

[Map回放](map-return-prototype-walkthrough.md)更新23个控件、新增8个外层Back，当前189个配置控件。Home来源样例返回和详情逐层关闭通过，8个新增来源的原生行为仍待核。独立Map起点退出无效及重复进入缺图明确失败，完整地图行为未完成。

后续：[Map底图重新上传与复测](map-image-repair-walkthrough.md)在两轮Monday路径显示8个筛选页底图。此前失败记录保留；这不证明所有图片或完整应用已通过。

后续：[Room返回栈](room-return-prototype-walkthrough.md)更新8个控件、补3个外层出口，三个Home来源的既有样例返回通过；独立Room退出和未实现交互仍保留。

后续：[Food返回栈](food-return-prototype-walkthrough.md)更新15个控件、补1个外层出口，三个Home来源的既有样例返回通过；图片不稳定、独立Food退出和完整范围仍未完成。

后续：[Food图片重新上传与复测](food-image-repair-walkthrough.md)更新14项填充，连续两轮Tuesday深层路径所见图片可见。图片问题部分解决，其它上下文和完整范围仍待验证。

## Food展开列表与H Café增量

[本批实现与回放](food-hcafe-prototype-walkthrough.md)新增4个Frame、11个控件，累计80个映射Frame、204个配置控件。离散拖动只覆盖两个已观察视口；外链提示四侧关闭、正文不关闭和三个Tuesday Home返回已验证。完整连续列表、其它来源、收起和外站Open未完成。

## Room Preview增量

[实现与回放](room-preview-prototype-walkthrough.md)新增3个Frame、1个内部组件状态、6个控件及1个竖向滚动区域；累计83个映射Frame、3个组件状态、210个配置控件和3个竖向滚动区域。观察范围内网页/照片切换、菜单取消与Tuesday返回通过样例回放，原生重开规则、完整网页和全应用覆盖仍未验证。

## Room日期与Sunday增量

[实现与回放](room-sunday-prototype-walkthrough.md)新增3个Frame、7个连接，Available日期条改为水平滚动，Sunday ALL有已观察范围内连续竖向滚动。累计86个映射Frame、217个配置控件、4个垂直和1个水平滚动区域。过渡延时仅演示，三个出口及反向筛选为原型推断；完整日期、列表、地图与查询仍未完成。
