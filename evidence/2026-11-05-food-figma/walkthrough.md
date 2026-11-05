# Food 独立 Figma Present 走查

日期：2026-11-05，Windows / Chrome，Figma 网页版，已登录编辑账号。起点：F00 / Home（4:16）；页面 4:2；文件 RGbquBbhRlgHI9el7V9TgT。采用 Fit width and height。Agent 通过可见界面实际点击，未收集真人指标。

| 实际动作 | 观察结果 |
|---|---|
| Home → Explore campus food | 显示 5 个地点的 All 列表 |
| H Café Opening hours → 再点一次 | 周一至周五、周六、节假日时间展开后收起 |
| H Café View details → Online order → Stay in PolyULife | 显示外部服务提示，再返回 H Café 详情 |
| H Café 详情 Back | 返回 All 列表 |
| Search → Chinese Soup → View details → View location map | 显示单条结果、VA210 详情和历史地图，见 map.png |
| 地图 Back → 详情 Back | 返回 Chinese Soup 单条结果，见 search-return.png |
| Search → Sushi → Clear search | 无结果状态可清除并回到 All，见 empty.png |
| Open now | 显示两台营业中的售卖机 |
| Restaurants → Communal 详情 → Back | 显示 Hours unavailable，返回 Restaurants 单条结果，见 filter-return.png |
| Share 设置 | 已确认 Anyone can view；未使用第二个独立账号做访问测试 |

修复：生成时当前筛选按钮自跳转被 Figma 拒绝，已排除指向当前顶层画框的连接，并重新建立其余按钮连接。首页文字与咖啡插图已分开。Present 默认 Actual size 会被顶部工具栏遮挡返回按钮，分享链接采用 scale-down，走查使用 Fit width and height。图片首访会延迟出现，地图加载后已再次视觉确认。

截图为 Figma 改版原型，非原应用取证。未逐一走查五个商户的全部地图/分类组合、不同设备尺寸、匿名访问或真实外部点餐。搜索为预设分支；地图及营业时间为历史/演示数据。
