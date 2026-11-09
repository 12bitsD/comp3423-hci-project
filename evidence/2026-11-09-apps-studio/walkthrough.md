# Food 基线复核与 Apps Studio 实际走查

日期：2026-11-09。执行环境为本机内置浏览器和本地静态服务器；以下是 Agent 的实现检查，不是真人用户研究。

## Food PR #7 复核

- 对 `app.js`、本地服务器和构建脚本执行 JavaScript 语法检查，通过。
- `exports/PolyULife-Food-Fresh-Campus-v02.pptx` 通过 ZIP 包结构检查；`git diff --check origin/main...HEAD` 通过。
- 查看报告图和六页 PPT 的封面导出，确认 Fresh Campus 视觉方向。
- 在本地 Food 页面输入 `Chinese Soup`，实际显示一条 VA210 结果；进入 VA210 详情，再 Back，搜索框仍为 `Chinese Soup`。
- 复核后通过 GitHub 标准 merge 流程合并 PR #7，没有使用 admin 绕过，没有删除其源分支。

## Apps 主链路

在 `prototypes/apps-studio/index.html` 的本地页面执行：

1. A00 点击 Apps & services，到达服务列表。
2. 在 Service name or task 输入 `visitor`，结果变为一条 Visitor Registration System (VRS)。
3. 点击 View service，到达 VRS 详情；页面显示服务用途、NetID 可能要求和 `fmovrs.polyu.edu.hk/vrs`。
4. 点击 Continue to VRS，经过加载状态后到达 Official sign-in 演示。凭证区域不可输入，未发生认证或访客申请。
5. 点击 Close and return to service details，再点击 Back to results；搜索框仍为 `visitor`，列表仍为一条 VRS 结果。
6. 打开 A07 无结果场景，显示 `not-a-service` 和 0 results；点击 Clear search 后搜索框为空，恢复 10 条演示结果。

这些步骤验证实现行为，不测量真人成功率、理解程度或任务耗时。

## 场景与视觉检查

使用浏览器 iPhone 14 Pro 预览配置检查 A00–A07，并导出八张 922 × 2000 PNG；它们对应 390 × 844 逻辑画框，不代表真机测试。检查了：分类 chips、当前筛选和结果计数、长 VRS 名称、按钮、官方域名、无结果恢复及画框底部内容。

两张 1200 × 760 报告图初次导出后，发现底部长句跨栏；改为双栏两行注释并重新导出复查，当前无文字重叠。原 App 截图保持原比例，没有用改版图替换旧证据。

## 静态与文档检查

- `node --check prototypes/apps-studio/app.js`：通过。
- `git diff --check`：通过。
- 检查根说明、项目简述、决策、Apps Studio、报告和评估目录共 10 份 Markdown：所有相对链接均可解析。
- 对 Apps Studio 和 `docs/` 执行凭证、私钥、访问令牌、学生编号和邮箱敏感模式扫描：无命中。
- 当前 main 不存在 `design/scripts/validate_polyulife_records.py`，因此无法执行该历史校验命令；没有把它记为通过。该脚本位于未合并的大型 PR #6 工作范围，本 Apps PR 不引入或合并该分支。

## 尚未完成

- Chrome 中已确认 LIN HAO 账号的编辑权限，并建立 `02 · Apps Redesign` 和 `A04 · VRS details`。其余七张画框、Prototype 连线和 Present 验收尚未完成；Figma 查看/评论权限仍需最终复核。迁移规格见 `prototypes/apps-studio/docs/FIGMA-HANDOFF.md`。
- 未执行至少五位真实参与者的 Maze；本文件和浏览器导出不能计入样本。
- 其他四功能、共同首页整合、最终报告、PPT、视频和 Canvas 提交不属于本次 Apps 实现验收的已完成范围。

## 课件原则对齐补充

复核本地课程 PDF 后，Apps 报告已改为课程框架为主、Nielsen 为补充：Week 7 Feedback/Constraints/FSM-STN，Visuals Part 2 Semantic Priming/CRAP/Recognition over Recall，Human Part 2 Fitts’ Law，以及 Week 5 的可测量 UI Specification。新增 `figure-03-apps-stn.png`，把 A00–A07 映射为 S0–S5 并标明返回、取消和空结果恢复。

Week 6 的 Design Thinking 仅用于说明迭代过程：当前界面观察支持 Define/Prototype，不把界面检查冒充 Empathize 用户研究，Test 仍待真人 Maze。课件用于设计论证，不替代项目要求的 10–20 篇相关研究文献。此次补充没有改变 Apps 交互行为，因此不重复声称新增真人或性能验证。

## Chrome Figma 迁移实测

通过用户明确授权的 Chrome 会话确认当前 Figma 账号为 LIN HAO，文件显示 Add new page、Export、Share 和 Design/Prototype 等编辑能力。已把默认 Page 3 重命名为 `02 · Apps Redesign`。免费版提示每文件最多三页，当前正好三页，未升级或修改付费设置。

`A04 · VRS details` 已导入画布，实测尺寸 390 × 844，图层含 Frame、Group、Vector；画面中的服务名、用途、NetID 提示、官方域名和按钮均清晰。SVG 文字成为 Vector 轮廓，因此不能声称所有文字都可直接编辑，后续报告说明需另保留文本对象。

其余七张 SVG 已生成，但浏览器扩展的本机文件上传权限默认关闭，批量导入尚未完成。尝试官方 Figma MCP 后确认其需要额外授权配置，没有修改 MCP 或账号设置。当前未把单张导入记为完整 Figma 交付，也未进行 Present 主链路验收。
