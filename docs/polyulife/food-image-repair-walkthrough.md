# Food 图片重新上传与连续进入复测

2026-09-29。原生 Computer Use 仍返回 Mac locked。本批为实际 Figma 图片填充修改和 Present 回放，没有新增原生状态或动作，完整应用仍 `not_verified`。

## 修改

此前 Food 重复进入和深层返回出现地图、logo、hero空白，重载又可能恢复。通过 Figma 的 Image → Upload from computer，将14个现有图片填充替换为仓库中对应的原始 PNG：列表5项、营业时间展开列表5项、详情2项、展开图片1项、全屏校园地图1项。没有改图片内容或导航连接。

全部14项填充读回的图片内容哈希、缩放模式和变换保持一致；新增 thumbnail，imageShouldColorManage 从 false 变为 true。这是上传前后的字段差异，不是故障原因已证明。过程中误触一次详情锁定已恢复，键盘位移操作已撤回；最终详情图像位置读回 X=207、Y=100、225×244，与源素材一致。

## 实跑结果

从 Tuesday Home 连续两次执行：Food→营业时间展开→原详情→Chinese Soup→结果详情→展开图片→关闭→展开地图→返回详情→Search→原详情→展开列表→Home。两轮所见列表地图/logo、详情hero/小地图、展开图片及校园地图均显示，返回时也未出现此前空白。

两次 Home 返回与进入前基线应用区域 `(581,60,938,661)` 像素完全一致。共29张截图，包括日期来源、基线、两轮每步和流程说明读回；PNG转换与账号遮盖逐像素核对。

`D-FOOD-IMAGE-RENDER` 调整为 **partially_resolved**。历史缺图证据保留。本批没有复测 Monday/legacy、未展开列表直接详情、独立入口或长时稳定性，不能把这两轮结果扩展为整体视觉验收。

## 剩余范围

营业时间展开页第四个logo位于现有画板底部之外，本次只确认填充已更新，未证明完整运行时可见；现有列表滚动和完整内容仍待实现。平移地图仍为未连线参考，本批未修改。其它地点、H Café、其它标签、自由搜索、完整地图/列表、加载状态与订餐提示等尚未补齐。独立 Food/Map/Room 返回仍未完成。

三份相关流程说明已更新，Home Dates 说明在 Present 重载后读回。Agent回放不等于原生观察或真人Maze测试。

[14项填充前后读回与像素比较](../../design/polyulife/food-image-repair.json) · [此前Food返回栈及失败证据](food-return-prototype-walkthrough.md)

| 实跑步骤 | 结果 | 证据 |
| --- | --- | --- |
| Tuesday Home selected before consecutive Food image checks | recorded | [E-FOOD-PNG-P-01](../../evidence/2026-09-28-full-audit/food-png-tue-top.png) |
| Tuesday Home features baseline for two returns | recorded | [E-FOOD-PNG-P-02](../../evidence/2026-09-28-full-audit/food-png-home-baseline.png) |
| Round 1 Food list map and logos | observed_imagery_visible | [E-FOOD-PNG-P-03](../../evidence/2026-09-28-full-audit/food-png-r1-list.png) |
| Round 1 expanded hours map and visible logos | observed_imagery_visible | [E-FOOD-PNG-P-04](../../evidence/2026-09-28-full-audit/food-png-r1-hours.png) |
| Round 1 original detail hero and map | observed_imagery_visible | [E-FOOD-PNG-P-05](../../evidence/2026-09-28-full-audit/food-png-r1-origin.png) |
| Round 1 tag opens Search | recorded | [E-FOOD-PNG-P-06](../../evidence/2026-09-28-full-audit/food-png-r1-search.png) |
| Round 1 repeated result detail hero and map | observed_imagery_visible | [E-FOOD-PNG-P-07](../../evidence/2026-09-28-full-audit/food-png-r1-result.png) |
| Round 1 expanded venue artwork visible | observed_imagery_visible | [E-FOOD-PNG-P-08](../../evidence/2026-09-28-full-audit/food-png-r1-image.png) |
| Round 1 image close retains detail imagery | observed_imagery_visible | [E-FOOD-PNG-P-09](../../evidence/2026-09-28-full-audit/food-png-r1-image-return.png) |
| Round 1 expanded campus map visible | observed_imagery_visible | [E-FOOD-PNG-P-10](../../evidence/2026-09-28-full-audit/food-png-r1-map.png) |
| Round 1 map Back retains result detail imagery | observed_imagery_visible | [E-FOOD-PNG-P-11](../../evidence/2026-09-28-full-audit/food-png-r1-map-return.png) |
| Round 1 detail Back to Search | recorded | [E-FOOD-PNG-P-12](../../evidence/2026-09-28-full-audit/food-png-r1-search-return.png) |
| Round 1 Search Back to original detail with imagery | observed_imagery_visible | [E-FOOD-PNG-P-13](../../evidence/2026-09-28-full-audit/food-png-r1-origin-return.png) |
| Round 1 hours-list return retains map and logos | observed_imagery_visible | [E-FOOD-PNG-P-14](../../evidence/2026-09-28-full-audit/food-png-r1-hours-return.png) |
| Round 1 returns to original Tuesday Home | home_return_pixel_equal | [E-FOOD-PNG-P-15](../../evidence/2026-09-28-full-audit/food-png-r1-home-return.png) |
| Round 2 repeated Food entry map and logos visible | observed_imagery_visible | [E-FOOD-PNG-P-16](../../evidence/2026-09-28-full-audit/food-png-r2-list.png) |
| Round 2 expanded hours map and visible logos | observed_imagery_visible | [E-FOOD-PNG-P-17](../../evidence/2026-09-28-full-audit/food-png-r2-hours.png) |
| Round 2 original detail hero and map | observed_imagery_visible | [E-FOOD-PNG-P-18](../../evidence/2026-09-28-full-audit/food-png-r2-origin.png) |
| Round 2 tag Search | recorded | [E-FOOD-PNG-P-19](../../evidence/2026-09-28-full-audit/food-png-r2-search.png) |
| Round 2 result detail images visible | observed_imagery_visible | [E-FOOD-PNG-P-20](../../evidence/2026-09-28-full-audit/food-png-r2-result.png) |
| Round 2 expanded image visible | observed_imagery_visible | [E-FOOD-PNG-P-21](../../evidence/2026-09-28-full-audit/food-png-r2-image.png) |
| Round 2 image close retains detail imagery | observed_imagery_visible | [E-FOOD-PNG-P-22](../../evidence/2026-09-28-full-audit/food-png-r2-image-return.png) |
| Round 2 expanded campus map visible | observed_imagery_visible | [E-FOOD-PNG-P-23](../../evidence/2026-09-28-full-audit/food-png-r2-map.png) |
| Round 2 map Back retains detail images | observed_imagery_visible | [E-FOOD-PNG-P-24](../../evidence/2026-09-28-full-audit/food-png-r2-map-return.png) |
| Round 2 detail Back to Search | recorded | [E-FOOD-PNG-P-25](../../evidence/2026-09-28-full-audit/food-png-r2-search-return.png) |
| Round 2 Search Back retains original detail images | observed_imagery_visible | [E-FOOD-PNG-P-26](../../evidence/2026-09-28-full-audit/food-png-r2-origin-return.png) |
| Round 2 final hours-list retains map and visible logos | observed_imagery_visible | [E-FOOD-PNG-P-27](../../evidence/2026-09-28-full-audit/food-png-r2-hours-return.png) |
| Round 2 returns to original Tuesday Home | home_return_pixel_equal | [E-FOOD-PNG-P-28](../../evidence/2026-09-28-full-audit/food-png-r2-home-return.png) |
| Reloaded Tuesday Home with updated image verification scope; no extra Food circuit | recorded | [E-FOOD-PNG-P-29](../../evidence/2026-09-28-full-audit/food-png-description-readback.png) |
