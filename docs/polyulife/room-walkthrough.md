# Room Finder 实际走查

记录日期：2026-09-28。观察区间为 13:43–14:07 UTC（香港时间 21:43–22:07）。本记录来自真实 PolyULife 窗口的 Computer Use 操作、AX 反馈及截图，覆盖查询、筛选、Preview、房间地图和返回路径的一轮走查。**Room 仍有未检查分支，完整应用和 Figma 尚未完成。**

## 环境与证据边界

- 运行方式：已安装的 iPhone App 在 Mac 上运行，通过 Computer Use 观察与交互；沿用现有登录状态。
- App 历史已确认版本为 3.0.0，本记录没有再次读取版本号；macOS 具体版本尚未登记。
- 早期窗口捕获曾失败；用户恢复后，13:50:53 UTC 起重新取得可读 Room 截图。工具捕获故障不归为应用缺陷。
- 公共截图仅保留本次分析所需内容。首页仅保存[导航区域裁剪](../../evidence/2026-09-28-full-audit/home-134424-navigation-only.png)，可确认 Map、Room、Food、Apps、Study progress、My Courses 以及 Home、Calendar、QR 图标、Notification、More 可见；它不代表完整首页，也不证明这些目的页面已经走查。
- 截图索引、时间、尺寸与哈希见 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json)。动作与状态对应见 [coverage.json](coverage.json)。截图中的数据只代表采集当时，不是实时房间可用性保证。

## 实际动作和反馈

| 动作 | 实际结果 | 对应截图 |
| --- | --- | --- |
| Home → Room | 打开 Room Finder，显示日期条、房间输入与搜索按钮 | [初始状态](../../evidence/2026-09-28-full-audit/room-134522-empty.png) |
| 输入并查询 `PQ604`，再查询 `PQ604B` | 两次均显示 `No room found`；不能由此推定这些房间应当存在于此数据源 | [PQ604](../../evidence/2026-09-28-full-audit/room-135149-pq604-no-room.png)、[PQ604B](../../evidence/2026-09-28-full-audit/room-135331-pq604b-no-room.png) |
| 选择 Tue 29-Sep；清空房间号 | Tue 选中；输入清空后，先前的 `No room found` 仍显示 | [日期选择](../../evidence/2026-09-28-full-audit/room-135352-next-date.png)、[清空后](../../evidence/2026-09-28-full-audit/room-135506-input-cleared.png) |
| 点击空输入搜索 | 返回初始查询提示/状态 | [空搜索](../../evidence/2026-09-28-full-audit/room-135521-empty-query.png) |
| 输入 `A`，选择 `AG206` 联想项 | 出现联想；选择后显示 AG206、29-Sep (Tue) 及可用/不可用时段 | [联想](../../evidence/2026-09-28-full-audit/room-135612-a-suggestion.png)、[ALL 结果](../../evidence/2026-09-28-full-audit/room-135628-ag206-all.png) |
| 点击 Available | 显示六个绿色时段：08:30–09:00、09:00–09:30、11:30–12:00、12:00–12:30、21:30–22:00、22:00–22:30 | [Available](../../evidence/2026-09-28-full-audit/room-135653-ag206-available.png) |
| 点击一个绿色时段卡片 | 本次点击后未见变化；没有进入预约或详情，不推定所有时段是否可点击 | [点击后](../../evidence/2026-09-28-full-audit/room-135724-available-slot.png) |
| 点击 Preview | 打开标题为 Room Search 的内嵌网页；先加载，随后出现官方页面内容 | [加载](../../evidence/2026-09-28-full-audit/room-preview-135751-loading.png)、[加载后](../../evidence/2026-09-28-full-audit/room-preview-135826-top.png) |
| 打开网页更多菜单，再点 Cancel | 菜单包含 Open in system browser、Share via...、Copy link、Cancel；已取消返回网页，前三项未执行 | [更多菜单](../../evidence/2026-09-28-full-audit/room-preview-135842-more-menu.png) |
| 向下滚动网页，点击轮播 Next | 显示 Room: AG206 与教室照片；Next 切换为另一张照片 | [照片一](../../evidence/2026-09-28-full-audit/room-preview-135905-ag206-photo-1.png)、[照片二](../../evidence/2026-09-28-full-audit/room-preview-135932-ag206-photo-2.png) |
| 关闭 Preview | 回到 Room Finder，AG206、Tue 29-Sep 和 Available 均保留 | [返回后](../../evidence/2026-09-28-full-audit/room-140021-preview-return-available.png) |
| 横向滚动尝试后，将日期条向左拖动 | 滚动尝试未建立有效变化；拖动后露出 Sun 04-Oct | [拖动后](../../evidence/2026-09-28-full-audit/room-140053-date-row-scrolled.png) |
| 点击 Sun 04-Oct 并继续观察 | 选中状态先变化，短暂仍保留 29-Sep 结果；随后无需再搜索，结果自动更新为 04-Oct (Sun)，显示 `No available room / Please search another room.` | [过渡状态](../../evidence/2026-09-28-full-audit/room-140117-sun-selected-old-result.png)、[更新完成](../../evidence/2026-09-28-full-audit/room-140214-sun-no-available-room.png) |
| 切回 ALL，向下滚动时段列表 | 可见时段全红；下滚见约 14:30 至 21:30，最末行被裁切，第二次滚动未见变化。实际末端尚未确认 | [ALL](../../evidence/2026-09-28-full-audit/room-140253-sun-all-unavailable.png)、[下滚](../../evidence/2026-09-28-full-audit/room-140323-sun-all-scrolled.png)、[第二次](../../evidence/2026-09-28-full-audit/room-140341-sun-all-scrolled.png) |
| 点击 AG206 左侧位置图标 | 打开标题 AG206 的校园 3D 地图；该图标是实际入口，不能作为装饰处理 | [房间地图](../../evidence/2026-09-28-full-audit/room-map-140441-ag206-campus.png) |
| 地图 slider 执行 Increment、Decrement | 两次均观察到缩放变化；AX 识别 Google Maps 按钮，未点击 | [放大](../../evidence/2026-09-28-full-audit/room-map-140635-ag206-zoomed.png)、[缩小](../../evidence/2026-09-28-full-audit/room-map-140652-ag206-campus.png) |
| 在地图上拖动 | 未见明显平移；不标记为拖动成功 | [拖动后](../../evidence/2026-09-28-full-audit/room-map-140707-ag206-campus.png) |

### 返回闭环的操作记录

14:07:29.674 UTC 点击地图返回，AX 反馈确认回到 Room Finder，保留 Sun 04-Oct + ALL；14:07:49.772 UTC 再次返回，AX 确认回到 Home。这两步的结论来自实际操作和后续 AX 状态；本记录没有将早先截图冒充这两步的截图。

本轮已建立 Home → Room 查询 → Available/ALL → Preview 或 AG206 地图 → Room → Home 的基本路径。仍须检查下述分支，不能把“基本路径跑通”解释为“Room 每个交互均已完成”。

## HCI 分析：事实、假设与待验证事项

| 观察事实 | 问题假设或设计含义 | 原则与建议 | 待验证 |
| --- | --- | --- | --- |
| 清空输入仍保留旧的无结果文案，空搜索后才恢复初始提示 | 用户可能把旧结果理解为当前空输入的结果；尚无真人误解证据 | 系统状态可见性：评估标出已提交查询，或清空输入时清理结果 | 重走查询语义，观察真人清空再查时的理解 |
| 一个绿色时段点击后无变化 | 卡片可能让部分用户期待进一步操作；不能据此断言预约功能损坏 | 操作暗示与反馈：先确认产品是否仅展示可用性，再评估列表或卡片的表现 | 可靠定位再试另一时段，确认产品意图，询问真人预期 |
| Preview 初始页面有站点头部与说明；滚动后才看到目标教室照片 | 到达目标信息可能多一步滚动；没有测得实际用户成本 | 与用户目标匹配：评估直接定位所选房间内容；保留已验证的返回上下文 | 复走初始滚动位置，检查照片下方信息及 PDF 链接 |
| 选择 Sun 后结果最终自行更新，无须再次 Search | 中间的新日期/旧结果组合是已观察的异步过渡，不能下缺陷结论 | 系统状态可见性：原型区分过渡与稳定结果 | 复走并检查加载反馈，避免由截图间隔推断真实延迟 |

以上均为 Agent 观察与问题假设，不是人类可用性指标；不能替代课程真人 Maze 评估。Mac 上的鼠标和 AX 结果也不能证明手机上的触控、定位或手势体验。

## 未完成与接力

- Room：其它日期与日期范围、更多查询变体、列表真实末端、其它时段点击含义和空/错误/网络状态。
- Preview：更多菜单前三项及其返回、Previous 与轮播边界、浏览器前进/后退/刷新、照片下方完整信息、已发现的 PDF 链接。
- AG206 地图：Google Maps 跳转及返回、缩放边界、平移的有效动作、其它可见地图控件与地图滚动范围。
- Home：导航区域之外的完整可操作项；其它模块与底部导航各自目的页面保持待观察。
- Figma：当前真实文件、已运行的原型连接、仍存在的视觉偏差与额度状态统一见 [Figma 当前状态](figma-spec.md)。本页的 App 观察不会因原型已生成而自动变为全部覆盖。
