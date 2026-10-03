# Food 加载校徽重入缺图与重传 — 2026-10-01

[加载批次](food-loading-prototype-walkthrough.md)的24-direct-detail-loading保存到正文/商户图，但地图加载校徽缺失；14正常。九项比较中的差异框为应用裁片(157,435,222,485)，复核像素确认属于校徽区，不能当作两次加载视觉通过。失败截图保留，原型run视觉结论改为failed。

Figma实际选中校徽图片633:54，位置257,671、62×59、STRETCH/identity。通过Image→Upload from computer重传相同[PNG](../../design/polyulife/assets/food-detail-loading-mark.png)，没有替换根、移动图层、改连接或新增控件。读回imageThumbnail增加、imageShouldColorManage从false变true；并未隔离因果机制，不归因原生App。

重载后两次连续Tuesday DEMO Home→未展开Food列表→详情加载→已加载详情→同一列表→Home，05/10实际短暂加载截图均有校徽。六项裁片比较6项相等、0项差异，见[清单](../../evidence/2026-10-01-food-loading-mark/manifest.json)、[对照图](../../evidence/2026-10-01-food-loading-mark/contact-sheet.png)。[编辑记录](../../design/polyulife/food-loading-mark-repair.json)保留节点、来源和边界。

本轮只重传详情加载标志并复验两个直接重入样例；展开营业时间、全图加载、其它来源和长会话未在重传后重复。早退/加载控件、原生直接入口、全部Food和应用仍未完成。累计134画板、305控件、75次原型运行；原生135状态/268动作不变，全应用 `not_verified`。
