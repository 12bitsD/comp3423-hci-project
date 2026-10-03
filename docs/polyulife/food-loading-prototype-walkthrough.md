# Food 两种地图加载态与调用者返回 — 2026-10-01

后续[加载校徽缺图复核与重传](food-loading-mark-repair-walkthrough.md)确认24缺少校徽，保留失败并重传相同PNG；两个连续直接重入样例有图。本页73次统计为该批次快照，当前75次。

既有原生[详情地图加载](../../evidence/2026-09-28-full-audit/food-160725-vending-detail-map-loading.png)与[全屏地图加载](../../evidence/2026-09-28-full-audit/food-161013-full-map-loading.png)分别重建为633:19/633:61。两帧576×970、Clip content逐一读回，位置0/700,60000。详情保留公开商户图与文字，移除已加载地图/气泡，嵌入加载校徽；展开控件上移241px匹配观察位置。全图保留Header/Back，灰色空白底图顶部校徽。文字、几何可编辑，图片/校徽为公开原图素材；字体/图标近似，指针未复制。

## 连接及回放

展开营业时间列表50:2151和原型直接列表50:1934的既有Open overlay改为633:19；详情根After delay800ms Swap overlay→50:2013对应A-FOOD-DETAIL-MAP-LOAD。已加载详情ExpandMap50:2050改Open overlay→633:61；全图加载根After delay800ms Swap overlay→50:2246，action_id:null的观察序列推进。两个800ms均为演示代理，不能当原生耗时；既有返回栈不增加加载导航历史。原生准确详情起点是营业时间展开列表，直接列表仍是旧原型推广。

10–22实际Tuesday DEMO Home→Food→展开营业时间→详情加载14→详情15→全图加载16→全图17→固定平移→详情20→原展开列表21→Home22。23–27重入直接列表→详情加载24→详情25→同一未展开列表26→Home27。两个加载阶段是实际Present截图，非本地渲染。28/29和30检查根无额外起点及最终延时/Swap overlay/Instant；新增2控件、替换3入口，共134映射画板、305控件、73次原型运行。

九项裁片比较8项相等、1项差异；见[清单](../../evidence/2026-10-01-food-loading/manifest.json)与[截图对照](../../evidence/2026-10-01-food-loading/contact-sheet.png)。比较只证明原型有限样例一致。地图平移后立即工具画面曾空白，但首个保存截图18已恢复地图，19再次可见；没有宣称保存到缺图截图或进行了图片重传。既有图片稳定性差异保持open。

## 尝试与未完成

配置直接入口成功后，编辑器导航到地图控件报中断；读取当前同一tab确认仍活跃，重新定位目标后完成，不重建浏览器。原生应用清单显示运行，bundle歧义解析后的Wrapper绑定继续超时，没有重启或新原生成功记录。

加载中的Back/图像展开/地图展开/标签控件未配置，原生提前动作未知；Search结果入口的加载状态与其它调用者尚未接入，固定地图仍不支持任意平移/缩放，全部地点/列表边界和逐像素保真未通过。未发起Call、位置授权、订单或业务提交。全应用 `not_verified`，原生135状态/268动作不变，Agent回放不替代真人评估。

源码：[生成脚本](../../design/scripts/build_food_loading_svg.py)、[来源资产](../../design/polyulife/food-loading-assets.json)、[连接清单](../../design/polyulife/food-loading-connections.json)。
