# 素材、数据与证据边界

## 来源

团队公开仓库：[12bitsD/comp3423-hci-project](https://github.com/12bitsD/comp3423-hci-project)。参考版本为本轮下载的 main：`182eb5616eb114b3a3b467780495a2dc0490f5ce`。

- `assets/original-list.png` 对应 `evidence/2026-09-28-full-audit/food-165444-list-scrolled-h-cafe.png`。
- `assets/original-search.png` 对应 `evidence/2026-09-28-full-audit/food-160820-chinese-soup-tag-result.png`。
- `assets/food-thumb-*.png` 和 `food-map-full-campus.png` 来自 `design/polyulife/assets/`。
- 原图日期：香港时间 2026-09-29。地图保留可见 Google Maps 归属，不新增官方标识。
- 事实说明：[Food 走查](https://github.com/12bitsD/comp3423-hci-project/blob/main/docs/polyulife/food-walkthrough.md)。该记录基于 Mac 上的原应用，不直接证明手机触控问题。

## 观察事实

旧卡片显示 Closed / Further information，展开后提供分日营业时间。VA210 详情经省略号进入；Chinese Soup 标签搜索返回单条同名结果。旧应用已具有状态文字、时间表展开和上下文返回，不能把这些说成缺失功能。

## 设计假设

明确的详情入口、今日营业摘要和带区分信息的搜索卡片可能改善识别与理解；默认列表可能更适合比较。均待真人验证，没有性能提升结论。

## 演示数据

全部记录用于固定周二 00:54 场景，不是实时服务。H Café 每周时间、VA210 全天营业时间取自历史记录。中文汤品来自实测标签；Drinks、Coffee & light meals 和部分类型分类是演示性归类，不能作为核实的商户菜单。页面上的 TAOBIN 类别明确带 Demo category。

Communal Student Restaurant 与 Gourmet Shop 在演示中使用未知时间，以呈现数据缺失状态，不断言原应用实际缺少这些时间。

地图图像来自 VA210 历史观察；列表标记的布局为示意，其他地点详情明确说明地图不代表该商户的已核实标记。不访问当前位置，不计算步行时间、距离或导航路线。

## 限制

没有执行新的原应用走查、访谈或 Maze 测试。本地浏览器测试用于确认代码与流程；不作为课程真人评估数据。原型使用商户品牌素材仅用于课程内对比与设计研究，不宣称已获商户背书或额外再授权。


## v0.2 原创视觉资产

餐碗与咖啡 SVG 复用用户在本地确认的 Fresh Campus 方向样稿。它们是设计装饰，不是校园餐厅照片。界面、报告图与 PPT 以同一份 tokens.json 生成配色。新版未新增访谈或真人评估数据。
