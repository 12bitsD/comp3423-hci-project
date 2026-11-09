# Apps · Figma 迁移与连线规格

更新：2026-11-09。小组 Figma 已建立 `02 · Apps Redesign`，并导入 `A04 · VRS details`（390 × 844，Frame/Group/Vector）。`figma/` 保存八张 SVG 迁移源。**其余七张画框和 Prototype 连线尚未完成；以下是剩余施工规格，不是完成记录。**

## 1. 画框和组件

- 新建八个 390 × 844 画框，名称使用 `A00 / Home` 至 `A07 / No results`。
- `exports/` 中的 922 × 2000 PNG 与 390 × 844 逻辑画框等比。可将 PNG 作为重建参照或临时底图，但最终应把标题、正文、按钮、输入框和状态拆成可编辑对象，不能只交付整图。
- 共用组件：`Status bar`、`App nav`、`Search field`、`Category chip`、`Result summary`、`Service card`、`Primary/Secondary button`、`External browser chrome`。
- 沿用 Fresh Campus：Ink `#182F46`、Muted `#526579`、Canvas `#F6F7F2`、Paper `#FFFFFF`、Accent `#C4EF71`、AccentSoft `#ECF6DD`、Success `#286144`、Line `#DCE3DA`。亮色按钮用深蓝文字。
- 字体 Arial；主标题 31px、服务名 15px、正文 12–13px、辅助标签 9–11px。主要点击区域至少 44px；状态不能仅靠颜色表达。
- A00 的其他四个模块在独立 Apps 版本只作占位。最终整合时替换为团队共同首页，并接入各负责人模块。

## 2. 画框内容

| Frame | 对应导出 | 必须保留的状态 |
| --- | --- | --- |
| A00 / Home | `A00-home.png` | Apps & services 是唯一本次演示入口；其他模块待整合 |
| A01 / All services | `A01-all.png` | 空查询、All 选中、10 条演示结果计数 |
| A02 / Campus | `A02-campus.png` | Campus 选中、VRS 与 Internal Search、2 条结果 |
| A03 / Job status | `A03-job.png` | Job chip 与 `Job services / Current filter: Job / 1 result` 同时可见 |
| A04 / VRS details | `A04-detail.png` | 服务用途、NetID 可能要求、`fmovrs.polyu.edu.hk/vrs`、继续与返回 |
| A05 / External loading | `A05-loading.png` | 服务名、官方域名、加载指示、Cancel and return |
| A06 / Official sign-in | `A06-web.png` | 官方域名、外部服务说明、禁用凭证演示、关闭返回 |
| A07 / No results | `A07-empty.png` | 查询 `not-a-service`、0 results、Clear search、Reset search |

A01/A02/A03/A07 都使用同一列表结构；在 Figma 中用组件 variants 表示分类、查询和结果状态，避免复制后样式漂移。

## 3. Prototype 连线（Week 7 FSM / STN）

将 A00 设为 starting point，Present 使用 Fit width and height。连线使用 On click → Navigate to → Instant；A05 的自动前进使用 After delay。下表同时是 Week 7 pp. 8–10 所要求的 State Transition Network：S0 Home、S1 列表、S2 详情、S3 加载、S4 官方登录演示、S5 无结果。报告图见 `../exports/figure-03-apps-stn.png`；分类和查询变化作为 S1 内部 variants，返回详情前保存、返回列表后恢复查询/分类/滚动位置。

| 起点与触发器 | 目标 | 状态要求 |
| --- | --- | --- |
| A00 · Apps & services | A01（或最后离开的列表 variant） | 最终整合时保留共同首页来源 |
| A01/A02/A03/A07 · Home | A00 | 保留列表状态供再次进入 |
| 列表 · Category chip | 对应分类 variant | 更新选中 chip、结果标题、当前筛选和计数 |
| 列表 · View service: VRS | A04 | 保存当前查询、分类和列表滚动位置 |
| A04 · Back / Back to results | 进入前的列表 variant | 恢复查询、分类和滚动位置 |
| A04 · Continue to VRS | A05 | 保留 VRS 为当前服务 |
| A05 · After delay 900 ms | A06 | 仅演示交接，不打开真实网址 |
| A05 · Cancel and return | A04 | 取消计时器/延迟 |
| A06 · × / Close and return | A04 | 不收集或保存任何输入 |
| A07 · Clear search | A01 | 清空查询，分类保持 All |
| 任意空结果 · Show all categories | A01 | 查询和分类同时复位 |

若制作搜索中间帧，可增加 `A01-S / visitor`：显示一条 VRS 结果；A04 返回该帧。Maze 的核心路径采用此状态以验证保留行为。

## 4. 实际迁移后的验收

- 从 A00 完整点击到 A06，再返回 A04 和搜索后的列表；确认 `visitor` 与 VRS 结果仍在。
- 逐条切换七个分类，确认当前 chip、标题和计数同步；Job 不得只在不可见区域表达。
- 验证 A05 的延迟和取消、A06 的关闭；无真实外部跳转、凭证字段或提交。
- 检查所有按钮、返回目标、画框文字裁切、长服务名和空结果恢复；重新打开 Present 后复验。
- 保存带日期的测试版本副本，之后再做真人反馈迭代。测试版与提交版链接分别登记。
- Share 设置需满足课程要求的查看/评论权限；用非编辑账号实际打开链接复核。

## 5. 当前阻塞与完成定义

当前 Chrome 账号具备编辑权限，但 Kimi 扩展的本机文件上传权限尚未开启，剩余七张 SVG 未能批量导入。只有“八张画框全部导入、Prototype 连线实际走通、权限复核、证据登记”全部完成，才能把 Apps 标为 Figma 完成；单张画框、HTML 走查和 PNG 导出都不算替代完成。
