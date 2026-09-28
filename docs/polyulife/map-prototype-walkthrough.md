# 校园地图原型与分类栏补测

本轮原生取证 2026-09-28 18:46–18:49 UTC；Figma 回放 19:00–19:04 UTC，随后进行局部图片修复。使用 PolyULife 3.0.0 的既有 Mac 登录会话（版本本轮未重查），原生交互仅通过 Computer Use。

## 观察事实

- Map 未选类别时，分类栏从左侧滑到 Clinics / Banks / AEDs / Bookstores，再反向滑回；地图内容和未选状态保留。横向滑动不等于选择类别。
- Figma 新增 12 个 576×970 可编辑 Frame，并配置 20 个控件。实际从 Home 进入 Map，逐条走完六类筛选、多选、列表样本、Core C 详情及展开/返回、类别栏双向拖动和书店返回 Home。
- 列表标题、行文字、类别和返回控件可编辑；地图地理、标记和标签使用已公开截图的裁图。原型不能作为真实地图或手机手势体验证据。

## 源码与节点

| 画板 | SVG | 节点 |
| --- | --- | --- |
| [S-MAINMAP-INITIAL] Map — no category | [mainmap-initial.svg](../../design/polyulife/mainmap-initial.svg) | 70:1064 |
| [S-MAINMAP-RIGHT] Map — categories right | [mainmap-initial-right.svg](../../design/polyulife/mainmap-initial-right.svg) | 70:1097 |
| [S-MAINMAP-TOILETS] Map — Toilets | [mainmap-toilets.svg](../../design/polyulife/mainmap-toilets.svg) | 70:1130 |
| [S-MAINMAP-TOILETS-WATER] Map — Toilets + Water | [mainmap-combined.svg](../../design/polyulife/mainmap-combined.svg) | 70:1200 |
| [S-MAINMAP-WATER] Map — Water Stations | [mainmap-water.svg](../../design/polyulife/mainmap-water.svg) | 70:1270 |
| [S-MAINMAP-WATER-SCROLLED] Map — Water list scrolled | [mainmap-water-scrolled.svg](../../design/polyulife/mainmap-water-scrolled.svg) | 70:1339 |
| [S-MAINMAP-CLINICS] Map — Clinics | [mainmap-clinics.svg](../../design/polyulife/mainmap-clinics.svg) | 70:1396 |
| [S-MAINMAP-BANKS] Map — Banks | [mainmap-banks.svg](../../design/polyulife/mainmap-banks.svg) | 70:1456 |
| [S-MAINMAP-AEDS] Map — AEDs | [mainmap-aeds.svg](../../design/polyulife/mainmap-aeds.svg) | 70:1505 |
| [S-MAINMAP-BOOKSTORES] Map — Bookstores | [mainmap-bookstores.svg](../../design/polyulife/mainmap-bookstores.svg) | 70:1565 |
| [S-MAINMAP-DETAIL] Toilet Core C — Detail | [mainmap-detail.svg](../../design/polyulife/mainmap-detail.svg) | 70:1614 |
| [S-MAINMAP-FULL] Toilet Core C — Expanded map | [mainmap-full.svg](../../design/polyulife/mainmap-full.svg) | 70:1635 |

## 实际原型回放

| 时间 UTC | 控件 | 实际目标节点 | 视觉结果 |
| --- | --- | --- | --- |
| 19:00:32 | C-MAINMAP-20 | 70:1064 | failed_image_missing |
| 19:01:02 | C-MAINMAP-01 | 70:1130 | visible_sample_checked |
| 19:01:12 | C-MAINMAP-09 | 70:1614 | visible_sample_checked |
| 19:01:32 | C-MAINMAP-13 | 70:1635 | visible_sample_checked |
| 19:01:41 | C-MAINMAP-15 | 70:1614 | visible_sample_checked |
| 19:01:51 | C-MAINMAP-14 | 70:1130 | failed_image_missing |
| 19:02:02 | C-MAINMAP-08 | 70:1200 | visible_sample_checked |
| 19:02:12 | C-MAINMAP-10 | 70:1270 | visible_sample_checked |
| 19:02:22 | C-MAINMAP-11 | 70:1339 | visible_sample_checked |
| 19:02:33 | C-MAINMAP-12 | 70:1064 | failed_image_missing |
| 19:02:45 | C-MAINMAP-02 | 70:1396 | visible_sample_checked |
| 19:02:56 | C-MAINMAP-16 | 70:1064 | failed_image_missing |
| 19:03:10 | C-MAINMAP-03 | 70:1097 | visible_sample_checked |
| 19:03:19 | C-MAINMAP-04 | 70:1064 | visible_sample_checked |
| 19:03:32 | C-MAINMAP-03 | 70:1097 | visible_sample_checked |
| 19:03:43 | C-MAINMAP-05 | 70:1456 | visible_sample_checked |
| 19:03:53 | C-MAINMAP-17 | 70:1097 | visible_sample_checked |
| 19:04:03 | C-MAINMAP-06 | 70:1505 | visible_sample_checked |
| 19:04:12 | C-MAINMAP-18 | 70:1097 | visible_sample_checked |
| 19:04:22 | C-MAINMAP-07 | 70:1565 | visible_sample_checked |
| 19:04:33 | C-MAINMAP-19 | 67:820 | failed_image_missing |

导航样本通过，但整次运行保留为 failed：初始地图、洗手间返回和 Home 的图片区域出现缺失。初始页面有一次第二次截图恢复，另一次再次截图仍空白，不能简单归因于一次加载等待。

局部修复：在 Figma 图片选择器中直接上传 `assets/mainmap-initial-geography.png`，恢复为 Image / Fill、位置 (0,154)、尺寸576×816。设置试验曾误触 Shader，已恢复并用真实PNG替换。修复后两次 Clinics→初始页面都显示底图；这是初始图片的定向复验，其余图片与全局稳定性仍未解决。

## 证据清单

| 时间 UTC | 证据 |
| --- | --- |
| 18:46:10 | [native-map-initial](../../evidence/2026-09-28-full-audit/184610-native-map-initial.png) |
| 18:46:28 | [native-map-categories-right](../../evidence/2026-09-28-full-audit/184628-native-map-categories-right.png) |
| 18:49:33 | [native-map-right-recheck](../../evidence/2026-09-28-full-audit/184933-native-map-right-recheck.png) |
| 18:49:42 | [native-map-categories-left-return](../../evidence/2026-09-28-full-audit/184942-native-map-categories-left-return.png) |
| 19:00:32 | [map-initial-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190032-map-initial-image-missing.png) |
| 19:00:41 | [map-initial](../../evidence/2026-09-28-full-audit/figma-v2-190041-map-initial.png) |
| 19:00:53 | [map-toilets-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190053-map-toilets-image-missing.png) |
| 19:01:02 | [map-toilets](../../evidence/2026-09-28-full-audit/figma-v2-190102-map-toilets.png) |
| 19:01:12 | [map-detail](../../evidence/2026-09-28-full-audit/figma-v2-190112-map-detail.png) |
| 19:01:32 | [map-expanded](../../evidence/2026-09-28-full-audit/figma-v2-190132-map-expanded.png) |
| 19:01:41 | [map-detail-return](../../evidence/2026-09-28-full-audit/figma-v2-190141-map-detail-return.png) |
| 19:01:51 | [map-toilets-return-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190151-map-toilets-return-image-missing.png) |
| 19:02:02 | [map-toilets-water](../../evidence/2026-09-28-full-audit/figma-v2-190202-map-toilets-water.png) |
| 19:02:12 | [map-water](../../evidence/2026-09-28-full-audit/figma-v2-190212-map-water.png) |
| 19:02:22 | [map-water-scrolled](../../evidence/2026-09-28-full-audit/figma-v2-190222-map-water-scrolled.png) |
| 19:02:33 | [map-cleared-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190233-map-cleared-image-missing.png) |
| 19:02:45 | [map-clinics](../../evidence/2026-09-28-full-audit/figma-v2-190245-map-clinics.png) |
| 19:02:56 | [map-clinics-cleared-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190256-map-clinics-cleared-image-missing.png) |
| 19:03:10 | [map-categories-right](../../evidence/2026-09-28-full-audit/figma-v2-190310-map-categories-right.png) |
| 19:03:19 | [map-categories-left](../../evidence/2026-09-28-full-audit/figma-v2-190319-map-categories-left.png) |
| 19:03:32 | [map-right-return](../../evidence/2026-09-28-full-audit/figma-v2-190332-map-right-return.png) |
| 19:03:43 | [map-banks](../../evidence/2026-09-28-full-audit/figma-v2-190343-map-banks.png) |
| 19:03:53 | [map-banks-cleared](../../evidence/2026-09-28-full-audit/figma-v2-190353-map-banks-cleared.png) |
| 19:04:03 | [map-aeds](../../evidence/2026-09-28-full-audit/figma-v2-190403-map-aeds.png) |
| 19:04:12 | [map-aeds-cleared](../../evidence/2026-09-28-full-audit/figma-v2-190412-map-aeds-cleared.png) |
| 19:04:22 | [map-bookstores](../../evidence/2026-09-28-full-audit/figma-v2-190422-map-bookstores.png) |
| 19:04:33 | [map-home-return-decoration-missing](../../evidence/2026-09-28-full-audit/figma-v2-190433-map-home-return-decoration-missing.png) |
| 19:04:47 | [map-flow-context-image-missing](../../evidence/2026-09-28-full-audit/figma-v2-190447-map-flow-context-image-missing.png) |
| 19:04:57 | [map-flow-context-image-still-missing](../../evidence/2026-09-28-full-audit/figma-v2-190457-map-flow-context-image-still-missing.png) |
| 19:06:51 | [map-fill-experiment-wrong-shader](../../evidence/2026-09-28-full-audit/figma-v2-190651-map-fill-experiment-wrong-shader.png) |
| 19:10:41 | [map-png-replacement-first-return](../../evidence/2026-09-28-full-audit/figma-v2-191041-map-png-replacement-first-return.png) |
| 19:12:40 | [map-png-replacement-second-return-context](../../evidence/2026-09-28-full-audit/figma-v2-191240-map-png-replacement-second-return-context.png) |

## 待验证与实现差异

- Figma On drag 只切换固定状态，不区分左右方向或连续滚动；真实饮水站列表使用 scroll 观察。
- 筛选清除后原型使用固定初始地理视图；Native 的连续地图视窗保留需要单独验证。
- 类别栏底色、图标和字体近似；公开底图可能保留原始指针，不能算可编辑地图对象。
- 未实现完整地点列表、其他设施详情、其余多选组合、自由缩放/平移、定位、Google Maps 外跳。
- 本次未进行人类 Maze 测试，未提交业务操作，未改 School Wiki。

后续更新：[Map返回栈](map-return-prototype-walkthrough.md)已保留三个Home来源并补8个筛选外层出口。独立Map启动退出及重复进入缺图仍未解决；上文连接配置保留作历史。
