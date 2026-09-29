# Food 样例保留来源与分层返回

2026-09-29。通过 Computer Use 修改和回放 Figma。用户回复恢复后，原生 PolyULife 连接仍返回 Mac locked；本批没有新原生状态或动作。原生台账保持 121 状态 / 265 动作（179 observed、86 not_attempted），全应用保持 `not_verified`。

## 修改与结果

Food 从 Home 进入后需要保留调用来源；详情→标签搜索→再次进入同一详情则需要保留多层返回。将三个 Home 入口和内部详情/搜索/图片/地图入口改为 Open overlay，列表营业时间展开使用 Swap overlay，各层返回使用 Close overlay。更新15个已有控件，新增1个营业时间列表外层返回，共193个配置控件。

- Monday：Home→列表→详情→图片→详情→地图→详情→列表→原 Home。
- Tuesday：Home→展开营业时间→原详情→Chinese Soup→结果详情→图片/地图绕行→Search→原详情→营业时间仍展开的列表→原 Home。
- legacy Home：验证同一标签搜索及重复详情的深层链，然后逐层返回展开列表及原 Home。

三次 Home 返回与各自进入前基线的应用区域 `(581,60,938,661)` 像素一致。legacy 营业时间列表返回也像素一致。Tuesday 展开列表返回时底图和logo重新出现，因此与缺图的进入截图不相等；视觉上营业时间仍展开，不能把此差异抹为通过。

## 原生依据与限制

[原生 Food 记录](food-walkthrough.md)已观察到结果详情→Search→原详情→展开营业时间列表的返回层级。新增 VA210 营业时间列表外层返回依据另一地点 H Café→Home 的原生记录推广，确切来源尚未观察，action_id=null。原先未展开列表→详情也继续保留原生来源未验证说明。固定样例未实现加载态、其它地点/标签、完整列表/地图、H Café、自由搜索或订餐外链提示等完整范围。

独立 Food 起点没有 Home 调用层：列表 Back 无效果；营业时间能展开，但展开页 Back 也不产生可见变化。后一项前后截图像素完全一致，属于退出失败，不是返回成功。记录 `D-FOOD-STANDALONE-EXIT`。证据文件名 `standalone-hours-back-list` 是采集时初始预期，截图和台账明确记录实际仍停留在 S-FOOD-HOURS。

## 图片仍不稳定

Monday 图片、地图可见；Tuesday 和 legacy 重复进入出现地图、logo、hero空白。Tuesday 回到营业时间列表时图片恢复；更新流程说明后重载独立 Food，图片也恢复。本批没有修改图片，无法据此认定图片修复或断言故障原因。`D-FOOD-IMAGE-RENDER` 保持 open。导航通过与视觉验收分别记录。

三份流程说明已更新，Food 说明在 Present 重载后读回。39张真实 Present 截图已转 PNG 并遮盖账号区域，转码与遮盖逐像素核对。这些是 Agent 原型回放，不是原生观察或 Maze 真人结果。

[配置与像素比较](../../design/polyulife/food-return-connections.json)。

| 步骤 | 结果与视觉限制 | 证据 |
| --- | --- | --- |
| Monday Home feature-area baseline | recorded | [E-FOOD-STACK-P-01](../../evidence/2026-09-28-full-audit/food-stack-mon-baseline.png) |
| Monday Home opens Food list | recorded | [E-FOOD-STACK-P-02](../../evidence/2026-09-28-full-audit/food-stack-mon-list.png) |
| Open VA210 directly from unexpanded list | recorded | [E-FOOD-STACK-P-03](../../evidence/2026-09-28-full-audit/food-stack-mon-detail.png) |
| Expand image from direct-list detail | recorded | [E-FOOD-STACK-P-04](../../evidence/2026-09-28-full-audit/food-stack-mon-image.png) |
| Image X restores source detail | recorded | [E-FOOD-STACK-P-05](../../evidence/2026-09-28-full-audit/food-stack-mon-image-return.png) |
| Expand map from same detail | recorded | [E-FOOD-STACK-P-06](../../evidence/2026-09-28-full-audit/food-stack-mon-map.png) |
| Map Back restores original detail | recorded | [E-FOOD-STACK-P-07](../../evidence/2026-09-28-full-audit/food-stack-mon-map-return.png) |
| Detail Back restores unexpanded list | recorded | [E-FOOD-STACK-P-08](../../evidence/2026-09-28-full-audit/food-stack-mon-detail-return-list.png) |
| Food list Back restores Monday Home | return_pixel_equal | [E-FOOD-STACK-P-09](../../evidence/2026-09-28-full-audit/food-stack-mon-home-return.png) |
| Confirmed Tuesday Home source | recorded | [E-FOOD-STACK-P-10](../../evidence/2026-09-28-full-audit/food-stack-tue-top.png) |
| Tuesday feature-area baseline | recorded | [E-FOOD-STACK-P-11](../../evidence/2026-09-28-full-audit/food-stack-tue-baseline.png) |
| Tuesday Food entry | recorded; Map and list logos missing on repeat Food entry | [E-FOOD-STACK-P-12](../../evidence/2026-09-28-full-audit/food-stack-tue-list.png) |
| Expand first venue opening hours | recorded; Map and logos missing | [E-FOOD-STACK-P-13](../../evidence/2026-09-28-full-audit/food-stack-tue-hours.png) |
| Details opened from expanded-hours list | recorded; Hero and mini-map images missing | [E-FOOD-STACK-P-14](../../evidence/2026-09-28-full-audit/food-stack-tue-origin-detail.png) |
| Chinese Soup search opened from source detail | recorded | [E-FOOD-STACK-P-15](../../evidence/2026-09-28-full-audit/food-stack-tue-tag.png) |
| Search result opens same detail above Search | recorded; Hero and mini-map missing | [E-FOOD-STACK-P-16](../../evidence/2026-09-28-full-audit/food-stack-tue-result-detail.png) |
| Image opened from search-result detail | recorded; Expanded image missing | [E-FOOD-STACK-P-17](../../evidence/2026-09-28-full-audit/food-stack-tue-nested-image.png) |
| Image close restores search-result detail | recorded; Hero and mini-map remain missing | [E-FOOD-STACK-P-18](../../evidence/2026-09-28-full-audit/food-stack-tue-nested-image-return.png) |
| Map opened from search-result detail | recorded; Full map geography missing | [E-FOOD-STACK-P-19](../../evidence/2026-09-28-full-audit/food-stack-tue-nested-map.png) |
| Map Back restores search-result detail | recorded; Hero and mini-map missing | [E-FOOD-STACK-P-20](../../evidence/2026-09-28-full-audit/food-stack-tue-nested-map-return.png) |
| Search-result detail Back restores Search | recorded | [E-FOOD-STACK-P-21](../../evidence/2026-09-28-full-audit/food-stack-tue-detail-back-search.png) |
| Search Back restores original tag-source detail | recorded; Hero and miniature map blank on Tuesday repeat entry. | [E-FOOD-STACK-P-22](../../evidence/2026-09-28-full-audit/food-stack-tue-search-back-origin.png) |
| Original detail Back returns to expanded-hours list; map and logos visible again on return (earlier entry had missing imagery) | recorded | [E-FOOD-STACK-P-23](../../evidence/2026-09-28-full-audit/food-stack-tue-back-hours.png) |
| Expanded-hours Back returns to Tuesday Home features | return_pixel_equal | [E-FOOD-STACK-P-24](../../evidence/2026-09-28-full-audit/food-stack-tue-home-return.png) |
| Legacy Home baseline before Food | recorded | [E-FOOD-STACK-P-25](../../evidence/2026-09-28-full-audit/food-stack-legacy-baseline.png) |
| Legacy Home opens Food list | recorded; Map and logos blank on entry | [E-FOOD-STACK-P-26](../../evidence/2026-09-28-full-audit/food-stack-legacy-list.png) |
| Opening hours expanded from legacy Home caller | recorded; Map and logos blank | [E-FOOD-STACK-P-27](../../evidence/2026-09-28-full-audit/food-stack-legacy-hours.png) |
| Expanded-hours entry opens original VA210 detail | recorded; Hero and miniature map blank | [E-FOOD-STACK-P-28](../../evidence/2026-09-28-full-audit/food-stack-legacy-origin-detail.png) |
| Original detail opens Chinese Soup tag results | recorded | [E-FOOD-STACK-P-29](../../evidence/2026-09-28-full-audit/food-stack-legacy-tag.png) |
| Chinese Soup result opens second instance of VA210 detail | recorded; Hero and miniature map blank | [E-FOOD-STACK-P-30](../../evidence/2026-09-28-full-audit/food-stack-legacy-result-detail.png) |
| Result detail Back returns to Search | recorded | [E-FOOD-STACK-P-31](../../evidence/2026-09-28-full-audit/food-stack-legacy-detail-back-search.png) |
| Search Back returns to original detail | recorded; Hero and miniature map blank | [E-FOOD-STACK-P-32](../../evidence/2026-09-28-full-audit/food-stack-legacy-search-back-origin.png) |
| Original detail returns to expanded-hours list | recorded; Map and logos blank | [E-FOOD-STACK-P-33](../../evidence/2026-09-28-full-audit/food-stack-legacy-back-hours.png) |
| Food hours outer Back returns to legacy Home caller | return_pixel_equal | [E-FOOD-STACK-P-34](../../evidence/2026-09-28-full-audit/food-stack-legacy-home-return.png) |
| Standalone Food starts at list | recorded; Map and logos blank | [E-FOOD-STACK-P-35](../../evidence/2026-09-28-full-audit/food-stack-standalone-baseline.png) |
| Standalone list Back has no effect without Home caller | failed_no_home_caller; Map and logos blank | [E-FOOD-STACK-P-36](../../evidence/2026-09-28-full-audit/food-stack-standalone-back-noop.png) |
| Standalone opening hours still expands | recorded; Map and logos blank | [E-FOOD-STACK-P-37](../../evidence/2026-09-28-full-audit/food-stack-standalone-hours.png) |
| Standalone hours Back has no visible effect; expanded hours remain, no Home caller | failed_no_home_caller; Map and logos blank | [E-FOOD-STACK-P-38](../../evidence/2026-09-28-full-audit/food-stack-standalone-hours-back-list.png) |
| Reloaded standalone Food with updated scope description, not a navigation test | recorded | [E-FOOD-STACK-P-39](../../evidence/2026-09-28-full-audit/food-stack-description-readback.png) |

后续：[Food图片重新上传与复测](food-image-repair-walkthrough.md)更新14项填充，连续两轮Tuesday深层路径所见图片可见。图片问题部分解决，其它上下文和完整范围仍待验证。
