# Apps 可见分类互跳验证

2026-09-29。本批继续使用 Computer Use 编辑与回放 Figma；原生连接仍返回 Mac locked。原生台账不变：121个状态、265个动作（179 observed / 86 not_attempted）。完整应用仍为 `not_verified`。

## 变更与依据

[上一批返回栈](apps-return-prototype-walkthrough.md)只接通固定分类链。本批为八个分类条状态中当前可见、未选中且未连接的标签新增33条 On click → Swap overlay → Instant；包括窄幅露出的边缘标签。选中标签保持无操作。当前共171个配置控件、76个映射Frame、2个内部状态和2个垂直滚动区域。

目的页面来自[原生Apps观察](apps-walkthrough.md)，新增来源组合是原型推广，不能据此声称原生每一种切换已观察。连接的 `action_id` 为null，单独引用原生目的状态证据及Figma实际回放证据。配置逐项读回见[连接配置](../../design/polyulife/apps-category-connections.json)。

54步分类路线覆盖全部33个新增触发器，其中包含既有连接与Job条拖动作为转场。全部新增连接到达预期分类。随后Campus → VRS详情 → 空登录 → 关闭登录 → 详情Back → Campus → Apps Back → Monday首页通过。首页前后应用区域 `(581,60,938,661)` 像素完全相同，证明这条原型回放保留了调用来源和滚动位置。

## 配置

| 来源Frame | 触发节点 | 目标Frame |
| --- | --- | --- |
| 61:2 | 61:112 · CategoryStudy | 61:215 |
| 61:2 | 61:115 · CategoryITTips | 61:344 |
| 61:2 | 61:118 · CategoryHealth | 61:475 |
| 61:2 | 61:121 · CategoryWellness | 61:585 |
| 61:135 | 61:185 · CategoryAll | 61:2 |
| 61:135 | 61:195 · CategoryITTips | 61:344 |
| 61:135 | 61:198 · CategoryHealth | 61:475 |
| 61:135 | 61:201 · CategoryWellness | 61:585 |
| 61:215 | 61:314 · CategoryAll | 61:2 |
| 61:215 | 61:317 · CategoryCampus | 61:135 |
| 61:215 | 61:327 · CategoryHealth | 61:475 |
| 61:215 | 61:330 · CategoryWellness | 61:585 |
| 61:344 | 61:448 · CategoryCampus | 61:135 |
| 61:344 | 61:451 · CategoryStudy | 61:215 |
| 61:344 | 61:461 · CategoryWellness | 61:585 |
| 61:475 | 61:555 · CategoryCampus | 61:135 |
| 61:475 | 61:558 · CategoryStudy | 61:215 |
| 61:475 | 61:561 · CategoryITTips | 61:344 |
| 61:475 | 61:571 · CategoryJob | 61:663 |
| 61:585 | 61:633 · CategoryCampus | 61:135 |
| 61:585 | 61:636 · CategoryStudy | 61:215 |
| 61:585 | 61:639 · CategoryITTips | 61:344 |
| 61:585 | 61:642 · CategoryHealth | 61:475 |
| 61:663 | 61:691 · CategoryCampus | 61:135 |
| 61:663 | 61:694 · CategoryStudy | 61:215 |
| 61:663 | 61:697 · CategoryITTips | 61:344 |
| 61:663 | 61:700 · CategoryHealth | 61:475 |
| 61:663 | 61:703 · CategoryWellness | 61:585 |
| 61:721 | 61:752 · CategoryCampus | 61:135 |
| 61:721 | 61:755 · CategoryStudy | 61:215 |
| 61:721 | 61:758 · CategoryITTips | 61:344 |
| 61:721 | 61:761 · CategoryHealth | 61:475 |
| 61:721 | 61:764 · CategoryWellness | 61:585 |

## 实际回放证据

时间为UTC。加载截图只记录Figma重载状态，随后另行取得说明读回证据。

| 时间 | 观察 | 截图 |
| --- | --- | --- |
| 2026-09-28T22:13:35.301Z | figma-apps-cross-home-start | [E-APPS-CROSS-P-01](../../evidence/2026-09-28-full-audit/figma-apps-cross-home-start.png) |
| 2026-09-28T22:13:45.707Z | figma-apps-cross-all-start | [E-APPS-CROSS-P-02](../../evidence/2026-09-28-full-audit/figma-apps-cross-all-start.png) |
| 2026-09-28T22:14:37.523Z | 61:2 → 61:215 via 61:112 | [E-APPS-CROSS-P-03](../../evidence/2026-09-28-full-audit/figma-apps-cross-01.png) |
| 2026-09-28T22:14:48.044Z | 61:215 → 61:2 via 61:314 | [E-APPS-CROSS-P-04](../../evidence/2026-09-28-full-audit/figma-apps-cross-02.png) |
| 2026-09-28T22:14:56.732Z | 61:2 → 61:344 via 61:115 | [E-APPS-CROSS-P-05](../../evidence/2026-09-28-full-audit/figma-apps-cross-03.png) |
| 2026-09-28T22:15:07.672Z | 61:344 → 61:135 via 61:448 | [E-APPS-CROSS-P-06](../../evidence/2026-09-28-full-audit/figma-apps-cross-04.png) |
| 2026-09-28T22:15:17.975Z | 61:135 → 61:2 via 61:185 | [E-APPS-CROSS-P-07](../../evidence/2026-09-28-full-audit/figma-apps-cross-05.png) |
| 2026-09-28T22:15:26.127Z | 61:2 → 61:475 via 61:118 | [E-APPS-CROSS-P-08](../../evidence/2026-09-28-full-audit/figma-apps-cross-06.png) |
| 2026-09-28T22:15:35.067Z | 61:475 → 61:135 via 61:555 | [E-APPS-CROSS-P-09](../../evidence/2026-09-28-full-audit/figma-apps-cross-07.png) |
| 2026-09-28T22:15:45.791Z | 61:135 → 61:344 via 61:195 | [E-APPS-CROSS-P-10](../../evidence/2026-09-28-full-audit/figma-apps-cross-08.png) |
| 2026-09-28T22:15:56.816Z | 61:344 → 61:215 via 61:451 | [E-APPS-CROSS-P-11](../../evidence/2026-09-28-full-audit/figma-apps-cross-09.png) |
| 2026-09-28T22:16:06.656Z | 61:215 → 61:135 via 61:317 | [E-APPS-CROSS-P-12](../../evidence/2026-09-28-full-audit/figma-apps-cross-10.png) |
| 2026-09-28T22:16:20.231Z | 61:135 → 61:475 via 61:198 | [E-APPS-CROSS-P-13](../../evidence/2026-09-28-full-audit/figma-apps-cross-11.png) |
| 2026-09-28T22:16:30.002Z | 61:475 → 61:215 via 61:558 | [E-APPS-CROSS-P-14](../../evidence/2026-09-28-full-audit/figma-apps-cross-12.png) |
| 2026-09-28T22:16:39.760Z | 61:215 → 61:475 via 61:327 | [E-APPS-CROSS-P-15](../../evidence/2026-09-28-full-audit/figma-apps-cross-13.png) |
| 2026-09-28T22:16:49.059Z | 61:475 → 61:344 via 61:561 | [E-APPS-CROSS-P-16](../../evidence/2026-09-28-full-audit/figma-apps-cross-14.png) |
| 2026-09-28T22:16:59.165Z | 61:344 → 61:585 via 61:461 | [E-APPS-CROSS-P-17](../../evidence/2026-09-28-full-audit/figma-apps-cross-15.png) |
| 2026-09-28T22:17:09.262Z | 61:585 → 61:135 via 61:633 | [E-APPS-CROSS-P-18](../../evidence/2026-09-28-full-audit/figma-apps-cross-16.png) |
| 2026-09-28T22:17:18.758Z | 61:135 → 61:585 via 61:201 | [E-APPS-CROSS-P-19](../../evidence/2026-09-28-full-audit/figma-apps-cross-17.png) |
| 2026-09-28T22:17:27.678Z | 61:585 → 61:215 via 61:636 | [E-APPS-CROSS-P-20](../../evidence/2026-09-28-full-audit/figma-apps-cross-18.png) |
| 2026-09-28T22:17:36.721Z | 61:215 → 61:585 via 61:330 | [E-APPS-CROSS-P-21](../../evidence/2026-09-28-full-audit/figma-apps-cross-19.png) |
| 2026-09-28T22:17:46.369Z | 61:585 → 61:344 via 61:639 | [E-APPS-CROSS-P-22](../../evidence/2026-09-28-full-audit/figma-apps-cross-20.png) |
| 2026-09-28T22:17:58.522Z | 61:344 → 61:585 via 61:461 | [E-APPS-CROSS-P-23](../../evidence/2026-09-28-full-audit/figma-apps-cross-21.png) |
| 2026-09-28T22:17:58.793Z | 61:585 → 61:475 via 61:642 | [E-APPS-CROSS-P-24](../../evidence/2026-09-28-full-audit/figma-apps-cross-22.png) |
| 2026-09-28T22:18:12.268Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-25](../../evidence/2026-09-28-full-audit/figma-apps-cross-23.png) |
| 2026-09-28T22:18:23.457Z | 61:663 → 61:135 via 61:691 | [E-APPS-CROSS-P-26](../../evidence/2026-09-28-full-audit/figma-apps-cross-24.png) |
| 2026-09-28T22:18:33.951Z | 61:135 → 61:2 via 61:185 | [E-APPS-CROSS-P-27](../../evidence/2026-09-28-full-audit/figma-apps-cross-25.png) |
| 2026-09-28T22:18:34.221Z | 61:2 → 61:585 via 61:121 | [E-APPS-CROSS-P-28](../../evidence/2026-09-28-full-audit/figma-apps-cross-26.png) |
| 2026-09-28T22:18:44.762Z | 61:585 → 61:663 via CategoryJob | [E-APPS-CROSS-P-29](../../evidence/2026-09-28-full-audit/figma-apps-cross-27.png) |
| 2026-09-28T22:18:45.031Z | 61:663 → 61:215 via 61:694 | [E-APPS-CROSS-P-30](../../evidence/2026-09-28-full-audit/figma-apps-cross-28.png) |
| 2026-09-28T22:19:04.283Z | 61:215 → 61:475 via 61:327 | [E-APPS-CROSS-P-31](../../evidence/2026-09-28-full-audit/figma-apps-cross-29.png) |
| 2026-09-28T22:19:04.551Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-32](../../evidence/2026-09-28-full-audit/figma-apps-cross-30.png) |
| 2026-09-28T22:19:04.788Z | 61:663 → 61:344 via 61:697 | [E-APPS-CROSS-P-33](../../evidence/2026-09-28-full-audit/figma-apps-cross-31.png) |
| 2026-09-28T22:19:18.143Z | 61:344 → 61:585 via 61:461 | [E-APPS-CROSS-P-34](../../evidence/2026-09-28-full-audit/figma-apps-cross-32.png) |
| 2026-09-28T22:19:18.411Z | 61:585 → 61:663 via CategoryJob | [E-APPS-CROSS-P-35](../../evidence/2026-09-28-full-audit/figma-apps-cross-33.png) |
| 2026-09-28T22:19:18.712Z | 61:663 → 61:475 via 61:700 | [E-APPS-CROSS-P-36](../../evidence/2026-09-28-full-audit/figma-apps-cross-34.png) |
| 2026-09-28T22:19:31.202Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-37](../../evidence/2026-09-28-full-audit/figma-apps-cross-35.png) |
| 2026-09-28T22:19:31.471Z | 61:663 → 61:585 via 61:703 | [E-APPS-CROSS-P-38](../../evidence/2026-09-28-full-audit/figma-apps-cross-36.png) |
| 2026-09-28T22:19:42.546Z | 61:585 → 61:663 via CategoryJob | [E-APPS-CROSS-P-39](../../evidence/2026-09-28-full-audit/figma-apps-cross-37.png) |
| 2026-09-28T22:19:42.912Z | 61:663 → 61:721 via DragLeft | [E-APPS-CROSS-P-40](../../evidence/2026-09-28-full-audit/figma-apps-cross-38.png) |
| 2026-09-28T22:19:52.279Z | 61:721 → 61:135 via 61:752 | [E-APPS-CROSS-P-41](../../evidence/2026-09-28-full-audit/figma-apps-cross-39.png) |
| 2026-09-28T22:20:06.735Z | 61:135 → 61:475 via 61:198 | [E-APPS-CROSS-P-42](../../evidence/2026-09-28-full-audit/figma-apps-cross-40.png) |
| 2026-09-28T22:20:07.003Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-43](../../evidence/2026-09-28-full-audit/figma-apps-cross-41.png) |
| 2026-09-28T22:20:07.298Z | 61:663 → 61:721 via DragLeft | [E-APPS-CROSS-P-44](../../evidence/2026-09-28-full-audit/figma-apps-cross-42.png) |
| 2026-09-28T22:20:07.560Z | 61:721 → 61:215 via 61:755 | [E-APPS-CROSS-P-45](../../evidence/2026-09-28-full-audit/figma-apps-cross-43.png) |
| 2026-09-28T22:20:20.386Z | 61:215 → 61:475 via 61:327 | [E-APPS-CROSS-P-46](../../evidence/2026-09-28-full-audit/figma-apps-cross-44.png) |
| 2026-09-28T22:20:20.651Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-47](../../evidence/2026-09-28-full-audit/figma-apps-cross-45.png) |
| 2026-09-28T22:20:20.966Z | 61:663 → 61:721 via DragLeft | [E-APPS-CROSS-P-48](../../evidence/2026-09-28-full-audit/figma-apps-cross-46.png) |
| 2026-09-28T22:20:21.234Z | 61:721 → 61:344 via 61:758 | [E-APPS-CROSS-P-49](../../evidence/2026-09-28-full-audit/figma-apps-cross-47.png) |
| 2026-09-28T22:20:33.286Z | 61:344 → 61:585 via 61:461 | [E-APPS-CROSS-P-50](../../evidence/2026-09-28-full-audit/figma-apps-cross-48.png) |
| 2026-09-28T22:20:33.553Z | 61:585 → 61:663 via CategoryJob | [E-APPS-CROSS-P-51](../../evidence/2026-09-28-full-audit/figma-apps-cross-49.png) |
| 2026-09-28T22:20:33.860Z | 61:663 → 61:721 via DragLeft | [E-APPS-CROSS-P-52](../../evidence/2026-09-28-full-audit/figma-apps-cross-50.png) |
| 2026-09-28T22:20:34.125Z | 61:721 → 61:475 via 61:761 | [E-APPS-CROSS-P-53](../../evidence/2026-09-28-full-audit/figma-apps-cross-51.png) |
| 2026-09-28T22:20:45.397Z | 61:475 → 61:663 via 61:571 | [E-APPS-CROSS-P-54](../../evidence/2026-09-28-full-audit/figma-apps-cross-52.png) |
| 2026-09-28T22:20:45.725Z | 61:663 → 61:721 via DragLeft | [E-APPS-CROSS-P-55](../../evidence/2026-09-28-full-audit/figma-apps-cross-53.png) |
| 2026-09-28T22:20:45.993Z | 61:721 → 61:585 via 61:764 | [E-APPS-CROSS-P-56](../../evidence/2026-09-28-full-audit/figma-apps-cross-54.png) |
| 2026-09-28T22:21:01.253Z | After 54 category/drag steps, Wellness to Campus for VRS regression | [E-APPS-CROSS-P-57](../../evidence/2026-09-28-full-audit/figma-apps-cross-vrs-campus.png) |
| 2026-09-28T22:21:19.653Z | Campus VRS ellipsis opens detail after category-cross replay | [E-APPS-CROSS-P-58](../../evidence/2026-09-28-full-audit/figma-apps-cross-vrs-detail.png) |
| 2026-09-28T22:21:38.267Z | Detail opens empty login overlay; no fields entered | [E-APPS-CROSS-P-59](../../evidence/2026-09-28-full-audit/figma-apps-cross-vrs-login.png) |
| 2026-09-28T22:21:51.591Z | Login X restores detail after cross-category chain | [E-APPS-CROSS-P-60](../../evidence/2026-09-28-full-audit/figma-apps-cross-vrs-close.png) |
| 2026-09-28T22:24:43.986Z | VRS detail Back restores Campus after full cross-category replay | [E-APPS-CROSS-P-61](../../evidence/2026-09-28-full-audit/figma-apps-cross-vrs-back-campus.png) |
| 2026-09-28T22:24:51.834Z | Apps Back restores original Monday Home feature scroll after cross-category and VRS replay | [E-APPS-CROSS-P-62](../../evidence/2026-09-28-full-audit/figma-apps-cross-return-home.png) |
| 2026-09-28T22:25:45.944Z | Present reloading; loading screen only, not description verification | [E-APPS-CROSS-P-63](../../evidence/2026-09-28-full-audit/figma-apps-cross-home-description.png) |
| 2026-09-28T22:25:53.925Z | Updated Home flow description visible after reload | [E-APPS-CROSS-P-64](../../evidence/2026-09-28-full-audit/figma-apps-cross-home-description-ready.png) |
| 2026-09-28T22:26:41.424Z | Apps standalone reference and updated limitation description read back | [E-APPS-CROSS-P-65](../../evidence/2026-09-28-full-audit/figma-apps-cross-apps-description.png) |

## 尚未完成

- 只覆盖当前可见标签。IT的All完全裁掉，未连接；部分Frame没有完整七个标签，不能称连续、任意横向分类条已完成。
- 原生不同来源组合下分类条自动居中、位置保留及列表滚动需要解锁后继续取证。
- 完整列表滚动、其它服务、独立Apps起点退出、其它模块返回、十个Home复制入口回放及既有图片缺陷仍待完成。
- Home和Apps的范围说明均已保存，并在Present重载后读回。
- 本批65张Present截图仅遮盖右上账号区域后转PNG，哈希、尺寸与遮盖后像素均校验。原始JPEG留在忽略目录。原型截图不能替代原生观察或真人Maze测试。
