# Food 地图平移与返回样例 — 2026-09-30

通过 Computer Use，在实际 Figma 的既有 Food 地图中补接两条连接，未新增画板或原生观察。当前总计115个映射画板、268个配置控件、48次原型运行；全应用保持 `not_verified`。

## 原生来源与原型区别

既有原生 A-FOOD-MAP-PAN 记录了一次从[268,716]到[371,578]的拖动，进入其它地图区域；A-FOOD-MAP-BACK 记录从平移地图返回VA210详情及其校园嵌入地图。公共截图 E-FOOD-MAP-CLEAN / E-FOOD-MAP-PANNED-CLEAN 是随后取得的干净参考状态，不与首次拖动时间混同。两张地图的地理内容仍为来源截图裁片，标题、导航和Back为可编辑图层；不是实时地图。

初始地图50:2246的MapViewport实际节点50:2248设置On drag → Swap overlay → 平移图50:2267；平移图Back实际节点50:2279设置On click → Close overlay。读取平移帧属性为576×970、位置1400,12000、Clip content。Prototype面板显示Add flow starting point，没有新增该帧起点。见[配置与原生来源](../../design/polyulife/food-map-pan-connections.json)。

On drag对当前Figma连接禁用Instant，保留Smart animate 300ms；这是原型动画，不是原生延时或动画实测。热点把拖动转成固定状态切换；只回放来源对应的一次方向，不能证明任意方向、范围、连续平移或地图缩放。平移图在本次Present中直接可见，无需重传素材；历史其它Food缺图失败与修复记录继续保留。

## 实际回放

从[Tuesday Home](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-694&starting-point-node-id=67%3A694&scaling=scale-down&content-scaling=fixed)选择Fit width and height，关闭流程侧栏，滚动到功能区：Food → 第一行右侧省略号 → VA210详情 → 地图右下展开 → 拖动[627,503]到[691,418] → 平移地图Back → 详情Back → Food Back → Home。

本次标题点击[626,326]没有进入详情，保留05截图与步骤，不作为原生缺陷或标题入口实现。使用已配置的省略号后成功进入详情。返回详情时头图与校园嵌入地图可见；随后返回列表和Home，首页仍在同一功能区位置。截图与像素比较见[清单](../../evidence/2026-09-30-food-pan/manifest.json)。三项比较分别是Home、列表与详情返回的一致性，属于原型内部比较，不验证原生保真。

Present的overlay URL保持Home调用者，不能只用该URL识别地图；状态判断来自实际画面、编辑器配置和操作路径。只采样Tuesday来源的一次完整链路，其它入口、独立Food起点、再次打开地图规则及长期图片稳定性尚未验证。

## 后续范围

原生当前连接仍有超时问题，本批未执行新的App动作。地图边界、其它手势、缩放、定位、外部Google Maps以及完整可编辑地理内容均未实现；不调用定位或外部服务。Home日程继续使用DEMO合成资料，公共证据遮盖账户头像。此回放是Agent原型验证，不形成真人可用性成功率、耗时或Maze数据。
