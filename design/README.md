# PolyULife 可编辑界面源文件

本目录保存从公开、已脱敏截图离线重建的 SVG，供 Figma 导入与原型连线。它们是设计源文件，不是原始截图。主要证据在 `evidence/2026-09-28-full-audit/`；每个 SVG 的 `<desc>` 标明来源和近似处理。

## 当前文件

| 页面组 | SVG 文件名，位于 `polyulife/` |
| --- | --- |
| Room | `room-empty.svg`、`room-suggest.svg`、`room-all.svg`、`room-available.svg` |
| More / Weather | `more.svg`、`weather-detail.svg`、`weather-image.svg` |
| Virtual Assistant | `virtual-assistant-detail.svg`、`virtual-assistant-image.svg`、`virtual-assistant-disclaimer.svg`、`virtual-assistant-welcome.svg` |
| Calendar | `calendar-sep28.svg`、`calendar-sep26.svg`、`calendar-holiday-detail.svg`、`calendar-filter-acad.svg`、`calendar-filter-all.svg`、`calendar-filter-none.svg`、`calendar-oct1.svg`、`calendar-sep1.svg`、`calendar-events-upcoming.svg`、`calendar-events-history.svg` |
| Notification / Search | `notification-empty.svg`、`search-empty.svg`、`search-weather-no-results.svg`、`search-room-no-results.svg` |
| Menu / Settings / Profile | `drawer-menu-items.svg`、`settings.svg`、`emergency-dialog.svg`、`profile-demo.svg` |
| Public policies | `privacy-policy.svg`、`terms-of-use.svg` |
| Food | `food-list.svg`、`food-list-hours.svg`、`food-detail.svg`、`food-tag-search.svg`、`food-image.svg`、`food-map.svg`、`food-map-panned.svg` |

共 38 个 SVG。一般画布为 576×970；`drawer-menu-items.svg` 是 489×642 的公开菜单裁片，`emergency-dialog.svg` 是 520×462 的独立弹窗。菜单截图在原 576×1082 图上的裁片范围为 `(0,440,489,1082)`；不能把这张裁片当成完整抽屉页面。

## 编辑与素材边界

- 界面文字使用原生 `<text>`，统一声明 `sans-serif`。Figma 可能替换为可用字体；字体度量、换行、图标和矢量插图存在近似，需要导入后视觉检查。
- 普通控件、背景和图标由可编辑矢量及具名分组组成。Figma 导入 SVG 本身不附带页面跳转、点击动作、滚动、文本输入或网页行为，需另行连线及测试。
- `polyulife/assets/` 只含真实品牌图、插图、头像组件或公开地图的必要裁片。SVG 内以 data URI 内嵌相同素材，文件可单独导入；没有把完整应用截图作为底图。
- Food 地图的道路及地名是地图图像的一部分；应用标题、结果、状态、标签和按钮仍是原生文字/矢量。`food-detail.svg` 保留已观察到的 Google 标识；列表地图可见裁片本来没有显示提供方标识，没有删除原图中可见的归属。
- Food 全屏地图使用补拍的 `food-165325-full-map-campus-pointer-on-header.png` 与 `food-165258-full-map-panned-pointer-on-header.png`。指针位于标题栏，标题栏已改为原生矢量；地图使用完整可见区域 `(0,100,576,970)`，没有为了移除指针截去地图内容。原全屏视图未显示 Google 标识，未补造归属。两张图是实测静态状态，不代表原型已支持任意地图拖动或定位。
- `scripts/build_food_svg.py` 可使用现有裁片重新生成已交付的七张 Food SVG；不会调用网络或访问应用。

## 明确的合成与未验证边界

- `profile-demo.svg` 只保留脱敏截图的字段结构。Student Example、00000000A、student@example.edu、Example Department 和通用头像均为合成演示值，页面有可见 DEMO 标记。
- `calendar-filter-all.svg` 与 `calendar-filter-none.svg` 将实际观察到、已移除私人背景的筛选面板置于公开 Sep28 背景上。它们是已标注的合成设计，不能作为点击 Apply 后结果已观察到的证据。
- Settings 第三行在证据中只有无标签开关，重建也保留该现象；没有猜测其功能。
- Privacy / Terms 只重建实际可见的公共网页首屏与部分 cookie 提示。网页内搜索、菜单、cookie 操作和页面后续滚动结果未由这些源文件验证。
- 电话、退出登录等控件的存在不代表执行过该动作。原型中若需演示，应由设计者明确配置演示行为。
- 本地验证覆盖 XML 可解析、ID 唯一、原生文字属性、画布尺寸与渲染结果。本目录不声明 Figma 交互测试已通过；导入、连线和演示的验证结果由负责该环节的记录单独提供。Agent 检查不能替代课程真人参与者测试。
