# PolyULife Apps Design Studio / Fresh Campus v0.1

A 的 Apps 服务查找改版与 Figma 迁移材料。核心任务是从共同首页找到 Visitor Registration System (VRS)，查看详情，理解外部 NetID 登录交接，并返回原服务列表。

## 打开与操作

直接双击 `index.html`，或在本目录运行：

```bash
python3 -m http.server 4187 --bind 127.0.0.1
```

然后打开 `http://127.0.0.1:4187`。所有代码和素材均在本地，无框架、在线字体、CDN、账号或构建依赖。

推荐走查：Home → Apps & services → 输入 `visitor` → View service → Continue to VRS → 等待官方登录演示 → Close → Back to results。返回后应仍显示 `visitor` 和一条 VRS 结果。

右侧场景按钮可直接查看 A00–A07。输入不存在的文字可检查无结果；Clear search 只清查询，Show all categories/Reset search 可恢复列表。Escape 可从登录演示或加载状态返回详情。

## 场景与导出

| Frame | 内容 | 导出 |
| --- | --- | --- |
| A00 | 共同首页与 Apps 入口 | `exports/A00-home.png` |
| A01 | 全部服务、搜索与可见分类 | `exports/A01-all.png` |
| A02 | Campus 筛选与 VRS | `exports/A02-campus.png` |
| A03 | Job 当前筛选持续可见 | `exports/A03-job.png` |
| A04 | VRS 详情与外交接说明 | `exports/A04-detail.png` |
| A05 | 外部服务加载状态 | `exports/A05-loading.png` |
| A06 | 官方 NetID 登录演示 | `exports/A06-web.png` |
| A07 | 无结果与恢复 | `exports/A07-empty.png` |

PNG 为 922 × 2000 的高分辨率导出，对应 390 × 844 逻辑画框。报告图为 1200 × 760：

- `exports/figure-01-category-status.png`：当前分类可见性，对应 Week 7 Feedback。
- `exports/figure-02-external-handoff.png`：VRS 外部服务交接，对应 Semantic Priming 与 Constraints。
- `exports/figure-03-apps-stn.png`：Week 7 FSM/STN 状态转换网络，含返回、取消与空结果恢复。

`?capture=1&scenario=campus` 等地址只显示手机画框，便于复查和重新导出。

## 证据与交付边界

- 原 App 事实来自 2026-09-28 的 PolyULife 3.0.0 观察；四张原图保存在 `assets/`，来源和处理见 `docs/EVIDENCE.md`。
- 服务数据是覆盖核心任务的本地演示集，不宣称是当前完整线上目录；所有外部登录和提交均被禁用。
- 浏览器实现用于交互验证和 Figma 迁移，不替代课程要求的 Figma 原型或至少五位真实参与者的 Maze 评估。
- 八张 SVG 是迁移源；共享文件已接通三帧。剩余画框、返回要求和验收步骤见[迁移规格](docs/FIGMA-HANDOFF.md)。SVG 文字为 Vector 轮廓，报告说明文字请保留为可编辑文本。
- 真人结果、成功率、耗时和迭代结论仍为待补充，不得用 Agent 走查代替。

## 相关文件

- [Figma 迁移与连线](docs/FIGMA-HANDOFF.md)
- [证据边界](docs/EVIDENCE.md)
- [英文报告小节](../../docs/report/apps.md)
- [全组 Maze 计划](../../docs/evaluation/maze-plan.md)
- [Food / Fresh Campus 共用视觉](../food-studio/docs/STYLE-GUIDE.md)
