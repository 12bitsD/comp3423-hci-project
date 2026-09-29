# Home 十个功能入口与直接返回

2026-09-29。本批通过Computer Use回放Figma，原生仍明确返回Mac locked。原生台账保持121个状态、265个动作（179 observed / 86 not_attempted），完整应用保持 `not_verified`。

## 问题与修改

[连续滚动批次](home-scroll-prototype-walkthrough.md)复制的Map、Room、Food、Study progress、My Courses在Monday和Tuesday各有一份，共十个入口未回放。本批先从Monday逐个进入，五个入口都到达既有目的Frame；五个页面Back点击均无导航，失败截图保留。随后为这五个初始样例Frame的Back各添加一条历史Back动作，配置逐项读回。

修复后从Monday和Tuesday各自连续执行五组「进入模块 → 立即Back」，全部回到原Home功能区。十次返回与各日期基线在应用区域 `(581,60,938,661)` 像素完全相同。Tuesday五组完成后再滚回顶部，仍显示29日和TUE。当前176个配置控件，Frame/内部状态/滚动区域数量不变。

本批只证明直接往返。内部页依然存在Navigate to，历史Back可能回上个内部状态而非Home；模块内绕行、其它状态的出口和独立起点尚未完成，需继续做来源保留。新增返回是基于原生模块退出观察的原型推广，原生退出来源与本批初始样例不完全相同，不增加原生实测动作。Room仍进入后续清空查询的Tuesday样例，Study/Courses为合成DEMO且跳过加载。

## 配置读回

[完整配置与像素比较](../../design/polyulife/home-feature-return-connections.json)。

| 来源Frame | 返回节点 | 动作 |
| --- | --- | --- |
| 67:271 | 67:351 | On click → Back |
| 67:2 | 67:62 | On click → Back |
| 50:1911 | 50:2010 | On click → Back |
| 70:1064 | 70:1091 | On click → Back |
| 12:198 | 12:203 | On click → Back |

## 视觉结果

Tuesday Food入口再次出现地图和店铺图片全部缺失，文字和卡片仍在。返回导航通过，视觉验收失败；既有 `D-FOOD-IMAGE-RENDER` 保持open。其它入口的本次可见图片不证明长期渲染稳定。

## 回放证据

时间为UTC。重载曾保留Courses旧帧，Restart后一次立即滚动未生效；两次准备状态均保留并正确标注，随后重新确认功能区作为比较基线。

| 时间 | 观察 | 截图 |
| --- | --- | --- |
| 2026-09-28T22:31:40.869Z | Monday features before copied-entry tests | [E-HOME-FEATURE-P-01](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-start.png) |
| 2026-09-28T22:31:51.024Z | Monday Map copied entry reaches facility map | [E-HOME-FEATURE-P-02](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-map.png) |
| 2026-09-28T22:31:58.984Z | Failure before repair: map Back had no navigation after Monday entry | [E-HOME-FEATURE-P-03](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-map-back.png) |
| 2026-09-28T22:32:30.428Z | Monday Room copied entry reaches room enquiry | [E-HOME-FEATURE-P-04](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-room.png) |
| 2026-09-28T22:32:39.905Z | Failure before repair: room Back had no navigation after Monday entry | [E-HOME-FEATURE-P-05](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-room-back.png) |
| 2026-09-28T22:32:50.101Z | Monday Food copied entry reaches venue list | [E-HOME-FEATURE-P-06](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-food.png) |
| 2026-09-28T22:32:58.231Z | Failure before repair: food Back had no navigation after Monday entry | [E-HOME-FEATURE-P-07](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-food-back.png) |
| 2026-09-28T22:33:17.295Z | Monday Study progress copied entry reaches Completed DEMO | [E-HOME-FEATURE-P-08](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-study.png) |
| 2026-09-28T22:33:24.841Z | Failure before repair: study Back had no navigation after Monday entry | [E-HOME-FEATURE-P-09](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-study-back.png) |
| 2026-09-28T22:33:39.243Z | Monday My Courses copied entry reaches Canvas DEMO | [E-HOME-FEATURE-P-10](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-courses.png) |
| 2026-09-28T22:33:48.942Z | Failure before repair: courses Back had no navigation after Monday entry | [E-HOME-FEATURE-P-11](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-courses-back.png) |
| 2026-09-28T22:38:16.000Z | Reload retained previous Courses frame; not Monday start | [E-HOME-FEATURE-P-12](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-fixed-start.png) |
| 2026-09-28T22:38:28.374Z | Monday top after Restart; immediate scroll did not advance during reset | [E-HOME-FEATURE-P-13](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-fixed-ready.png) |
| 2026-09-28T22:38:39.508Z | Monday feature-region baseline before direct round trips | [E-HOME-FEATURE-P-14](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-fixed-baseline.png) |
| 2026-09-28T22:38:54.168Z | Monday Map entry after Back repair | [E-HOME-FEATURE-P-15](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-map-fixed-entry.png) |
| 2026-09-28T22:38:54.443Z | Map direct Back restores Monday Home features | [E-HOME-FEATURE-P-16](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-map-fixed-return.png) |
| 2026-09-28T22:39:05.709Z | Monday Room entry after Back repair | [E-HOME-FEATURE-P-17](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-room-fixed-entry.png) |
| 2026-09-28T22:39:05.979Z | Room direct Back restores Monday Home features | [E-HOME-FEATURE-P-18](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-room-fixed-return.png) |
| 2026-09-28T22:39:16.747Z | Monday Food entry after Back repair | [E-HOME-FEATURE-P-19](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-food-fixed-entry.png) |
| 2026-09-28T22:39:17.016Z | Food direct Back restores Monday Home features | [E-HOME-FEATURE-P-20](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-food-fixed-return.png) |
| 2026-09-28T22:39:28.638Z | Monday Study entry after Back repair | [E-HOME-FEATURE-P-21](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-study-fixed-entry.png) |
| 2026-09-28T22:39:28.916Z | Study direct Back restores Monday Home features | [E-HOME-FEATURE-P-22](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-study-fixed-return.png) |
| 2026-09-28T22:39:41.532Z | Monday Courses entry after Back repair | [E-HOME-FEATURE-P-23](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-courses-fixed-entry.png) |
| 2026-09-28T22:39:41.802Z | Courses direct Back restores Monday Home features | [E-HOME-FEATURE-P-24](../../evidence/2026-09-28-full-audit/figma-home-feature-mon-courses-fixed-return.png) |
| 2026-09-28T22:40:03.835Z | Tuesday selected before copied-entry tests | [E-HOME-FEATURE-P-25](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-top.png) |
| 2026-09-28T22:40:13.601Z | Tuesday feature-region baseline before direct round trips | [E-HOME-FEATURE-P-26](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-fixed-baseline.png) |
| 2026-09-28T22:40:26.229Z | Tuesday Map copied entry | [E-HOME-FEATURE-P-27](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-map-fixed-entry.png) |
| 2026-09-28T22:40:26.501Z | Map direct Back restores Tuesday Home features | [E-HOME-FEATURE-P-28](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-map-fixed-return.png) |
| 2026-09-28T22:40:38.092Z | Tuesday Room copied entry | [E-HOME-FEATURE-P-29](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-room-fixed-entry.png) |
| 2026-09-28T22:40:38.363Z | Room direct Back restores Tuesday Home features | [E-HOME-FEATURE-P-30](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-room-fixed-return.png) |
| 2026-09-28T22:40:49.844Z | Tuesday Food entry works, but existing map and venue-image missing defect recurred | [E-HOME-FEATURE-P-31](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-food-fixed-entry.png) |
| 2026-09-28T22:40:50.115Z | Food direct Back restores Tuesday Home features | [E-HOME-FEATURE-P-32](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-food-fixed-return.png) |
| 2026-09-28T22:41:04.295Z | Tuesday Study copied entry | [E-HOME-FEATURE-P-33](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-study-fixed-entry.png) |
| 2026-09-28T22:41:04.551Z | Study direct Back restores Tuesday Home features | [E-HOME-FEATURE-P-34](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-study-fixed-return.png) |
| 2026-09-28T22:41:17.572Z | Tuesday Courses copied entry | [E-HOME-FEATURE-P-35](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-courses-fixed-entry.png) |
| 2026-09-28T22:41:17.809Z | Courses direct Back restores Tuesday Home features | [E-HOME-FEATURE-P-36](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-courses-fixed-return.png) |
| 2026-09-28T22:41:28.577Z | After all five Tuesday round trips, scrolling to top confirms Tuesday date retained | [E-HOME-FEATURE-P-37](../../evidence/2026-09-28-full-audit/figma-home-feature-tue-final-top.png) |
| 2026-09-28T22:42:31.142Z | Home description saved and read back after reload; direct-return-only and visual failure limits visible | [E-HOME-FEATURE-P-38](../../evidence/2026-09-28-full-audit/figma-home-feature-description.png) |

本批38张实际Present截图仅遮盖账号区域后转PNG，哈希/尺寸/遮盖像素校验通过；原始JPEG位于忽略目录。Home说明已在Present重载后读回。Agent回放不替代原生观察或Maze真人评估。

后续更新：[Study/Courses返回栈](study-courses-return-prototype-walkthrough.md)将这两个模块的样例内部路径改为overlay并验证三个Home来源；上文历史Back配置保留作历史。其它模块内部绕行仍待完成。

后续更新：[Map返回栈](map-return-prototype-walkthrough.md)已保留三个Home来源并补8个筛选外层出口。独立Map启动退出及重复进入缺图仍未解决；上文连接配置保留作历史。

后续：[Room返回栈](room-return-prototype-walkthrough.md)更新8个控件、补3个外层出口，三个Home来源的既有样例返回通过；独立Room退出和未实现交互仍保留。
