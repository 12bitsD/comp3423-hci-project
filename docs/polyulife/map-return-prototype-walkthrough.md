# Map 从首页进入后的筛选、详情与返回

2026-09-29。原生Computer Use仍返回Mac locked，本批只修改并回放Figma。原生记录保持121状态/265动作（179 observed / 86 not_attempted），完整应用保持`not_verified`。

## 修复内容

原型Bookstores Back固定跳到legacy Home，不能保留Monday/Tuesday来源；内部Navigate to还会累积历史。本批将三个Home入口改为Open overlay，分类/列表固定样例改为Swap overlay，设施详情与展开地图分别Open overlay并逐层Close，Map外层Back关闭模块回到调用首页。更新23个原控件，补8个原本无连接的筛选页外层Back。当前189个配置控件，映射Frame/内部状态/滚动区域数量不变。

## 回放结果

- Tuesday从Home进入，走完全部既有筛选样例、Toilets+Water多选、列表片段、Core C详情与展开/返回、分类栏双向切换、Clinics/Banks/AEDs选择与清除、Bookstores返回。每个原有内部控件均有实际回放。
- Tuesday十个外层出口逐个通过。Monday和legacy Home另验证了嵌套详情返回、Bookstores返回。14次正式Home返回与各自基线的应用区域 `(581,60,938,661)` 像素完全相同；Tuesday详情/筛选逐层返回各有一次像素比较通过。
- 一次Monday准备点击没有切换，实际仍为Tuesday，随后的返回同样通过但不计入Monday覆盖；三张截图修正了状态标注，保留错误命名和准备失败说明。随后Restart并确认28/MON后才执行正式Monday路径。该额外实际Tuesday返回也有像素比较，合计17项比较。
- 三个流程说明已修改并在Present重载后读回。

## 视觉与独立起点失败

首次Tuesday长路径底图可见；随后重复进入Toilets、组合、Water、列表后段、Clinics、Banks、AEDs、Bookstores时地图区域空白，文字/筛选/导航仍在，`D-MAINMAP-IMAGES`未解决。不能把导航通过写成视觉通过。

独立Map起点不含Home调用层，初始Back实跑无效果；改为Close overlay还取代了旧Bookstores固定返回legacy Home的兜底。该独立流程退出是本批记录的兼容缺口 `D-MAINMAP-STANDALONE-EXIT`，推荐从Home流程进入，尚未完成独立启动处理。没有删除历史失败或声称已解决。

## 原生依据和未完成范围

[原生走查](home-study-map-walkthrough.md)证实Core C全屏→详情→筛选列表的返回链和Bookstores→Home；[分类栏补测](map-prototype-walkthrough.md)支持左右无选择状态。8个新增筛选状态外层Back是原型推广，相同原生来源未独立观察，action_id为null。原型拖动仍是固定状态切换，不能代替连续滚动、自由平移缩放、完整设施列表、其它多选组合、定位或Google Maps交接。Room/Food内部绕行和其它模块未实现分支继续保留。

## 配置读回

[完整配置、历史与像素比较](../../design/polyulife/map-return-connections.json)。coverage映射保留23个旧配置。

| 来源Frame | 触发节点 | 行为 | 目的/返回 | 变更 |
| --- | --- | --- | --- | --- |
| 70:1064 | 70:1071 | On click → Swap overlay | 70:1130 | 更新，保留旧配置 |
| 70:1064 | 70:1080 | On click → Swap overlay | 70:1396 | 更新，保留旧配置 |
| 70:1064 | 70:1069 | On drag → Swap overlay | 70:1097 | 更新，保留旧配置 |
| 70:1097 | 70:1102 | On drag → Swap overlay | 70:1064 | 更新，保留旧配置 |
| 70:1097 | 70:1109 | On click → Swap overlay | 70:1456 | 更新，保留旧配置 |
| 70:1097 | 70:1113 | On click → Swap overlay | 70:1505 | 更新，保留旧配置 |
| 70:1097 | 70:1118 | On click → Swap overlay | 70:1565 | 更新，保留旧配置 |
| 70:1130 | 70:1142 | On click → Swap overlay | 70:1200 | 更新，保留旧配置 |
| 70:1130 | 70:1167 | On click → Open overlay | 70:1614 | 更新，保留旧配置 |
| 70:1200 | 70:1207 | On click → Swap overlay | 70:1270 | 更新，保留旧配置 |
| 70:1270 | 70:1295 | On drag → Swap overlay | 70:1339 | 更新，保留旧配置 |
| 70:1339 | 70:1351 | On click → Swap overlay | 70:1064 | 更新，保留旧配置 |
| 70:1614 | 70:1624 | On click → Open overlay | 70:1635 | 更新，保留旧配置 |
| 70:1614 | 70:1629 | On click → Close overlay | Caller | 更新，保留旧配置 |
| 70:1635 | 70:1642 | On click → Close overlay | Caller | 更新，保留旧配置 |
| 70:1396 | 70:1412 | On click → Swap overlay | 70:1064 | 更新，保留旧配置 |
| 70:1456 | 70:1468 | On click → Swap overlay | 70:1097 | 更新，保留旧配置 |
| 70:1505 | 70:1521 | On click → Swap overlay | 70:1097 | 更新，保留旧配置 |
| 70:1565 | 70:1608 | On click → Close overlay | Caller | 更新，保留旧配置 |
| 67:820 | 67:872 | On click → Open overlay | 70:1064 | 更新，保留旧配置 |
| 67:569 | 113:58 | On click → Open overlay | 70:1064 | 更新，保留旧配置 |
| 67:694 | 113:13 | On click → Open overlay | 70:1064 | 更新，保留旧配置 |
| 70:1064 | 70:1091 | On click → Close overlay | Caller | 更新，保留旧配置 |
| 70:1130 | 70:1194 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1097 | 70:1124 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1200 | 70:1264 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1270 | 70:1333 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1339 | 70:1390 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1396 | 70:1450 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1456 | 70:1499 | On click → Close overlay | Caller | 新增，原生来源待核 |
| 70:1505 | 70:1559 | On click → Close overlay | Caller | 新增，原生来源待核 |

## 实际截图

全部为Computer Use取得的Present截图，UTC时间；只遮盖Figma账号区域，原始JPEG在忽略目录，公开PNG逐像素核对转码/遮盖并校验哈希和尺寸。Agent回放不代替原生观察或Maze真人评估。

| 时间 | 观察 | 结果 | 证据 |
| --- | --- | --- | --- |
| 2026-09-28T23:24:17.663Z | Tuesday selected before Map replay | recorded | [E-MAP-STACK-P-01](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-date.png) |
| 2026-09-28T23:24:27.822Z | Tuesday feature scroll baseline | recorded | [E-MAP-STACK-P-02](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-baseline.png) |
| 2026-09-28T23:24:28.092Z | Tuesday Home opens Map | recorded | [E-MAP-STACK-P-03](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-initial.png) |
| 2026-09-28T23:24:36.633Z | Toilets filter selected | recorded | [E-MAP-STACK-P-04](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-toilets.png) |
| 2026-09-28T23:24:46.654Z | Core C detail opens over Toilets filter | recorded | [E-MAP-STACK-P-05](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-detail.png) |
| 2026-09-28T23:24:59.906Z | Map expands above detail | recorded | [E-MAP-STACK-P-06](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-full.png) |
| 2026-09-28T23:25:00.209Z | Expanded map closes to the same detail | recorded | [E-MAP-STACK-P-07](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-full-back.png) |
| 2026-09-28T23:25:11.388Z | Detail closes to Toilets with filter retained | recorded | [E-MAP-STACK-P-08](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-detail-back.png) |
| 2026-09-28T23:25:11.656Z | Toilets and Water selected together | recorded | [E-MAP-STACK-P-09](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-combined.png) |
| 2026-09-28T23:25:23.999Z | Only Water remains after Toilets deselection | recorded | [E-MAP-STACK-P-10](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-water.png) |
| 2026-09-28T23:25:24.345Z | Discrete drag advances to recorded Water list fragment | recorded | [E-MAP-STACK-P-11](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-water-scrolled.png) |
| 2026-09-28T23:25:36.341Z | Water cleared after list sample | recorded | [E-MAP-STACK-P-12](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-cleared.png) |
| 2026-09-28T23:25:36.613Z | Clinics selected | recorded | [E-MAP-STACK-P-13](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-clinics.png) |
| 2026-09-28T23:25:50.808Z | Clinics cleared | recorded | [E-MAP-STACK-P-14](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-clinics-clear.png) |
| 2026-09-28T23:25:51.156Z | Category strip switches to right-hand sample | recorded | [E-MAP-STACK-P-15](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-right.png) |
| 2026-09-28T23:26:04.051Z | Category strip left sample restored | recorded | [E-MAP-STACK-P-16](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-left.png) |
| 2026-09-28T23:26:04.599Z | Banks selected after strip switch | recorded | [E-MAP-STACK-P-17](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-banks.png) |
| 2026-09-28T23:26:16.179Z | Banks cleared retaining right category strip | recorded | [E-MAP-STACK-P-18](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-banks-clear.png) |
| 2026-09-28T23:26:16.447Z | AEDs selected | recorded | [E-MAP-STACK-P-19](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-aeds.png) |
| 2026-09-28T23:26:31.296Z | AEDs cleared | recorded | [E-MAP-STACK-P-20](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-aeds-clear.png) |
| 2026-09-28T23:26:31.562Z | Bookstores selected after full sample route | recorded | [E-MAP-STACK-P-21](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-bookstores.png) |
| 2026-09-28T23:26:31.833Z | Bookstores exits to original Tuesday Home after full sample route | return_pixel_equal | [E-MAP-STACK-P-22](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-bookstores-return.png) |
| 2026-09-28T23:26:50.071Z | Outer exit check tue-initial-exit | recorded | [E-MAP-STACK-P-23](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-initial-exit-before.png) |
| 2026-09-28T23:26:50.337Z | Outer Back returns Home after tue-initial-exit | return_pixel_equal | [E-MAP-STACK-P-24](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-initial-exit-return.png) |
| 2026-09-28T23:26:50.853Z | Outer exit check tue-toilets-exit | image_missing | [E-MAP-STACK-P-25](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-toilets-exit-before.png) |
| 2026-09-28T23:26:51.116Z | Outer Back returns Home after tue-toilets-exit | return_pixel_equal | [E-MAP-STACK-P-26](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-toilets-exit-return.png) |
| 2026-09-28T23:27:04.666Z | Outer exit check tue-combined-exit | image_missing | [E-MAP-STACK-P-27](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-combined-exit-before.png) |
| 2026-09-28T23:27:04.935Z | Outer Back returns Home after tue-combined-exit | return_pixel_equal | [E-MAP-STACK-P-28](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-combined-exit-return.png) |
| 2026-09-28T23:27:05.934Z | Outer exit check tue-water-exit | image_missing | [E-MAP-STACK-P-29](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-water-exit-before.png) |
| 2026-09-28T23:27:06.202Z | Outer Back returns Home after tue-water-exit | return_pixel_equal | [E-MAP-STACK-P-30](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-water-exit-return.png) |
| 2026-09-28T23:27:20.685Z | Outer exit check tue-scrolled-exit | image_missing | [E-MAP-STACK-P-31](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-scrolled-exit-before.png) |
| 2026-09-28T23:27:20.920Z | Outer Back returns Home after tue-scrolled-exit | return_pixel_equal | [E-MAP-STACK-P-32](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-scrolled-exit-return.png) |
| 2026-09-28T23:27:21.431Z | Outer exit check tue-clinics-exit | image_missing | [E-MAP-STACK-P-33](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-clinics-exit-before.png) |
| 2026-09-28T23:27:21.703Z | Outer Back returns Home after tue-clinics-exit | return_pixel_equal | [E-MAP-STACK-P-34](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-clinics-exit-return.png) |
| 2026-09-28T23:27:40.078Z | Outer exit check tue-right-exit | recorded | [E-MAP-STACK-P-35](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-right-exit-before.png) |
| 2026-09-28T23:27:40.392Z | Outer Back returns Home after tue-right-exit | return_pixel_equal | [E-MAP-STACK-P-36](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-right-exit-return.png) |
| 2026-09-28T23:27:41.225Z | Outer exit check tue-banks-exit | image_missing | [E-MAP-STACK-P-37](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-banks-exit-before.png) |
| 2026-09-28T23:27:41.496Z | Outer Back returns Home after tue-banks-exit | return_pixel_equal | [E-MAP-STACK-P-38](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-banks-exit-return.png) |
| 2026-09-28T23:28:00.470Z | Outer exit check tue-aeds-exit | image_missing | [E-MAP-STACK-P-39](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-aeds-exit-before.png) |
| 2026-09-28T23:28:00.739Z | Outer Back returns Home after tue-aeds-exit | return_pixel_equal | [E-MAP-STACK-P-40](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-aeds-exit-return.png) |
| 2026-09-28T23:28:01.014Z | Tuesday date still selected after all ten outer exits | recorded | [E-MAP-STACK-P-41](../../evidence/2026-09-28-full-audit/figma-map-stack-tue-date-after.png) |
| 2026-09-28T23:28:31.225Z | Monday setup failed; actual caller remained Tuesday. Monday feature scroll baseline | setup_target_not_reached | [E-MAP-STACK-P-42](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-baseline.png) |
| 2026-09-28T23:28:32.692Z | Monday setup failed; actual caller remained Tuesday. Outer exit check mon-nested | image_missing | [E-MAP-STACK-P-43](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-nested-before.png) |
| 2026-09-28T23:28:32.940Z | Monday setup failed; actual caller remained Tuesday. Outer Back returns Home after mon-nested | setup_target_not_reached | [E-MAP-STACK-P-44](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-nested-return.png) |
| 2026-09-28T23:29:18.370Z | Confirmed Monday feature scroll baseline after Restart | recorded | [E-MAP-STACK-P-45](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-fixed-baseline.png) |
| 2026-09-28T23:29:19.838Z | Outer exit check mon-fixed-nested | image_missing | [E-MAP-STACK-P-46](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-fixed-nested-before.png) |
| 2026-09-28T23:29:20.108Z | Outer Back returns Home after mon-fixed-nested | return_pixel_equal | [E-MAP-STACK-P-47](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-fixed-nested-return.png) |
| 2026-09-28T23:29:35.988Z | Outer exit check mon-fixed-bookstores | image_missing | [E-MAP-STACK-P-48](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-fixed-bookstores-before.png) |
| 2026-09-28T23:29:36.259Z | Outer Back returns Home after mon-fixed-bookstores | return_pixel_equal | [E-MAP-STACK-P-49](../../evidence/2026-09-28-full-audit/figma-map-stack-mon-fixed-bookstores-return.png) |
| 2026-09-28T23:29:52.348Z | Legacy Home feature baseline | recorded | [E-MAP-STACK-P-50](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-baseline.png) |
| 2026-09-28T23:29:53.830Z | Outer exit check legacy-nested | image_missing | [E-MAP-STACK-P-51](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-nested-before.png) |
| 2026-09-28T23:29:54.100Z | Outer Back returns Home after legacy-nested | return_pixel_equal | [E-MAP-STACK-P-52](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-nested-return.png) |
| 2026-09-28T23:30:07.409Z | Outer exit check legacy-bookstores | image_missing | [E-MAP-STACK-P-53](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-bookstores-before.png) |
| 2026-09-28T23:30:07.678Z | Outer Back returns Home after legacy-bookstores | return_pixel_equal | [E-MAP-STACK-P-54](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-bookstores-return.png) |
| 2026-09-28T23:30:35.118Z | Standalone Map start has no Home overlay caller | recorded | [E-MAP-STACK-P-55](../../evidence/2026-09-28-full-audit/figma-map-stack-standalone-before.png) |
| 2026-09-28T23:30:35.386Z | Standalone initial Back has no effect without Home caller | standalone_exit_failed | [E-MAP-STACK-P-56](../../evidence/2026-09-28-full-audit/figma-map-stack-standalone-after.png) |
| 2026-09-28T23:32:26.097Z | Standalone Map scope description persisted after reload | recorded | [E-MAP-STACK-P-57](../../evidence/2026-09-28-full-audit/figma-map-stack-map-description.png) |
| 2026-09-28T23:32:52.944Z | Legacy flow Map scope persisted | recorded | [E-MAP-STACK-P-58](../../evidence/2026-09-28-full-audit/figma-map-stack-legacy-description.png) |
| 2026-09-28T23:33:06.503Z | Dates flow Map scope persisted | recorded | [E-MAP-STACK-P-59](../../evidence/2026-09-28-full-audit/figma-map-stack-dates-description.png) |

后续：[Map底图重新上传与复测](map-image-repair-walkthrough.md)在两轮Monday路径显示8个筛选页底图。此前失败记录保留；这不证明所有图片或完整应用已通过。
