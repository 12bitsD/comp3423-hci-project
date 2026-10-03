# Food 与 VA210 Vending Machine 实际走查

观察区间：2026-09-28 16:06:21–16:11:05、16:52:49–16:55:19 UTC（香港时间 2026-09-29 00:06:21–00:11:05、00:52:49–00:55:19），另补17:13:42的Food返回Home。通过 Computer Use 操作 Mac 上的真实 PolyULife；从 Home 的 Food 入口开始，第二段继续原导航栈，停在 H Café 营业时间展开的列表，随后返回Home继续Apps。只查看公开食品点内容；Online Order 仅到第三方链接提示并关闭，没有打开外站、呼叫、下单或修改资料。

## 实际路径与证据

| 时间（UTC） | 动作与观察 | 证据 |
| --- | --- | --- |
| 16:06:21 → 16:06:42 | 点击 Home 的 Food。先出现食品点列表；随后地图加载，可见地图和下部列表卡片 | [地图与列表](../../evidence/2026-09-28-full-audit/food-160642-map-list-loaded.png)；当前视口只显示部分条目，AX 中出现更多公开地点不等于逐项走查 |
| 16:06:56 | 点击第一项 VA210 Vending Machine 的营业时间箭头，展开 “Mon - Sun, public holiday: 00:00 - 23:59” | [营业时间展开](../../evidence/2026-09-28-full-audit/food-160657-opening-hours-expanded.png)；收起动作尚未执行 |
| 16:07:24 → 16:07:38 | 点击该卡片省略号进入详情。显示配图、P/F, Block VA、Call、Open Now、营业时间和三项标签；下方小地图随后加载地点标记 | [详情地图加载前](../../evidence/2026-09-28-full-audit/food-160725-vending-detail-map-loading.png) → [加载完成](../../evidence/2026-09-28-full-audit/food-160738-vending-detail-map-loaded.png) |
| 16:08:20 | 点击 `#Chinese Soup`，进入 Search，字段自动为 Chinese Soup，出现一条 VA210 Vending Machine 结果 | [标签搜索结果](../../evidence/2026-09-28-full-audit/food-160820-chinese-soup-tag-result.png) |
| 16:08:48 | 点击结果，进入同一 VA210 Vending Machine 详情，图片、位置、营业时间与标签恢复 | [从结果进入详情](../../evidence/2026-09-28-full-audit/food-160849-tag-result-detail.png)；这一步是打开结果，不是按系统返回 |
| 16:09:32 → 16:09:48 | 点击配图展开，再点击右上 X，回到详情和小地图 | [配图展开](../../evidence/2026-09-28-full-audit/food-160932-hero-expanded.png) → [配图关闭后](../../evidence/2026-09-28-full-audit/food-160949-hero-return.png) |
| 16:10:13 → 16:10:36 | 点击小地图右下展开控件，进入标题仍为 VA210 Vending Machine 的全屏地图；地图随后加载，AX 中有地点标记、缩放 slider、My location 与 Google Maps | [全屏地图加载前](../../evidence/2026-09-28-full-audit/food-161013-full-map-loading.png) → [加载完成](../../evidence/2026-09-28-full-audit/food-161037-full-map-loaded.png) |
| 16:11:04 | 在全屏地图从 `[268,716]` 拖到 `[371,578]`；后续截图的视野已离开原校园标记区域，AX 中原地点标记也不再列出 | [拖动后地图](../../evidence/2026-09-28-full-audit/food-161105-full-map-panned.png)；只确认本次 Food 全屏地图平移，不外推 Room 地图或 Home 的 Main Map |

地图加载前后与卡片营业状态都是采集瞬间的观察；不从截图间隔计算加载时间，也不把 Open Now 当成已经线下核实的营业承诺。地图中的地点标记是所选公开食品点，不代表用户实时位置。My location 只确认入口存在，没有触发定位。

## 后续返回与列表检查

| 时间（UTC） | 动作与观察 | 证据 |
| --- | --- | --- |
| 16:52:57 | 将指针移到标题栏，补拍原先平移后的完整地图；没有再次平移 | [地图视野补拍](../../evidence/2026-09-28-full-audit/food-165258-full-map-panned-pointer-on-header.png)；地图像素不再被指针覆盖 |
| 16:53:08 | 全屏地图 Back 返回 VA210 详情与原校园小地图 | [第一次地图返回](../../evidence/2026-09-28-full-audit/food-165309-full-map-return-detail.png) |
| 16:53:17 → 16:53:25 | 再展开地图，显示原校园食品点视野；将指针移到标题栏后补拍 | [重新展开的校园地图](../../evidence/2026-09-28-full-audit/food-165325-full-map-campus-pointer-on-header.png)；此次未保留前次平移视野 |
| 16:53:49 | 再按地图 Back，回到同一 VA210 详情 | [第二次地图返回](../../evidence/2026-09-28-full-audit/food-165350-full-map-return-detail.png) |
| 16:53:56 | 在从搜索结果进入的详情按 Back，返回 Chinese Soup 搜索及同一条结果 | [详情返回搜索](../../evidence/2026-09-28-full-audit/food-165357-detail-back-tag-result.png) |
| 16:54:04 | Search Back 回到先前发起标签查询的 VA210 详情 | [搜索返回原详情](../../evidence/2026-09-28-full-audit/food-165405-tag-back-detail.png) |
| 16:54:24 | 原详情 Back 返回 Food 列表，第一项的营业时间仍展开 | [详情返回列表](../../evidence/2026-09-28-full-audit/food-165425-detail-back-list.png) |
| 16:54:34 | 将列表把手由 `[289,487]` 向上拖到 `[287,256]`，列表扩展到接近标题栏 | [列表面板展开](../../evidence/2026-09-28-full-audit/food-165435-list-sheet-expanded.png) |
| 16:54:43 | 在列表向下滚动，出现 Communal Student Restaurant、Gourmet Shop、H Café 和部分 Homantin Hall Canteen | [滚动至 H Café](../../evidence/2026-09-28-full-audit/food-165444-list-scrolled-h-cafe.png)；不是列表末端检查 |
| 16:54:54 | 展开 Closed 的 H Café 营业时间，显示 Mon–Fri 08:00–22:00、Sat 08:00–18:00、Sun/public holiday 10:00–18:00 | [关闭餐厅的营业时间](../../evidence/2026-09-28-full-audit/food-165455-h-cafe-hours-expanded.png) |
| 16:55:05 | 点击 H Café Online Order，出现将进入第三方网站的提示，含截断的公开订餐 URL 和 Open | [外链提示](../../evidence/2026-09-28-full-audit/food-165505-online-order-external-link-prompt.png)；没有点击 Open，外站内容未观察 |
| 16:55:18 | 点击提示外遮罩区域 `[531,424]`，提示关闭，回到同一 H Café 列表位置，营业时间仍展开 | [提示关闭后](../../evidence/2026-09-28-full-audit/food-165519-external-link-prompt-dismissed.png) |

详情的 Back 目的地取决于进入栈：从 Search 结果进入的详情先回 Search，再回标签来源详情，最后回列表。因此不能把详情 Back 固定连到列表而宣称复现这条路径。地图两次返回与 Search 返回均已截图；其它入口、其它商户及更深的导航栈尚未推定。

17:13:42.693 在 H Café 营业时间展开的列表按 Back，17:13:45.141 的实际结果确认返回Home，随后进入Apps。Home包含个人内容，未新增公开截图；这里只引用 `E-APPS-TRACE` 的脱敏动作/AX说明，详见 [Apps前置路径](apps-walkthrough.md)。这补齐本次Food返回Home，不代表Apps自己的Back也已验证。

## HCI 观察与边界

- 营业时间可以在列表内展开，无需先进入详情。VA210 的全天营业样例与 Closed H Café 的分日时间表均已观察；反向收起和其它商户仍待查。
- 标签能带入关键词并返回实际地点结果，提供了已验证的搜索成功样本。这说明 Food 的这条标签检索可用；不能据此推定 More/Notification 搜索采用相同数据源或匹配规则。
- 当前列表多个条目同名为 VA210 Vending Machine，但品牌图标和标签不同。它们可能代表不同机器或供应商，不能先判重复数据；如要研究选择成本，应先确认区别是否足够、再让真人选择指定食品。
- 图片展开/X关闭与地图展开/平移是不同交互。原型应保留分开的状态和返回边界，不能用一张大图代替两种动作。

## 未完成范围

- Food 主列表：下部完整范围、面板向下收起、其它地点卡片与地图标记、全部滚动边界、营业时间收起。一次展开/滚动及 H Café 样例不代表全部列表完成。
- 地点详情：其它标签、Call、文章/地图区域的完整滚动范围、其它进入栈的返回。H Café Online Order 已观察到外链提示及遮罩关闭；Open 后的外站仍待观察，没有打开或下单。
- 图片：除展开和 X 以外的缩放/平移/手势。
- 小地图与全屏地图：标记点选、缩放 slider、My location、Google Maps 外部交接及更多视野边界；已有一次平移、两次返回详情和一次重新展开恢复校园视野的样例。
- 搜索：其它标签/关键词、多结果和无结果、编辑/清除以及其它来源返回。Chinese Soup 样例的结果→详情→Search→原详情已验证。

本页主观察截止为 `S-FOOD-HCAFE-HOURS`，后续返回Home并开始 [Apps独立走查](apps-walkthrough.md)。全应用完成状态仍为 `not_verified`；Study progress、My Courses、Home 主 Map、QR 和 Home 更深层内容仍待独立观察。

## October3补查

后续[营业时间往返与列表反向走查](food-oct3-reverse-walkthrough.md)记录当前Block Y首项、Open H Café和28条可见场所目录，补到指定VA210收起及列表有限上下边界。面板下移未确认；本页夜间VA210首项/Closed H Café样本保留历史上下文，不用新数据覆盖。
