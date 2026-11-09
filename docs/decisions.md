# 决策与验证记录

本文件记录决定及其证据边界；后续更新追加日期，并明确是否替代旧决定。团队讨论使用 [GitHub Issues](https://github.com/12bitsD/comp3423-hci-project/issues)，材料和决定的修改通过 Pull Request 同步。

## 2026-09-25 · 暂定选题与并行工作

- 暂定 PolyULife 为 HCI case，探索让 Agent 观察真实界面、参与流程分析的方法。
- 并行收集更多 Web case；iBooking 是已有备选。
- 两条工作线在下次会议 2026-10-02 前汇总，根据证据收敛选题；时段、负责人和具体功能待确认。

## 2026-09-28 · 采用 Mac 原生应用与 Computer Use 路线

**决定**：优先运行官方 PolyULife iPhone App on Mac，通过 Codex Computer Use 观察和操作；当前无需配置 Xcode、Simulator 或 Appium。依据与备选见 [接入研究](research/ios-computer-use.md)。

**已验证**：按本次安装与接入会话记录，原生 App Store 完成获取，PolyULife 3.0.0 已运行。按实际发现的 Wrapper 运行路径连接后，Computer Use 取得首页 AX 状态，可读到 Home、Calendar、Notification、More、Room、Food 等入口。用户随后确认接入链路已通。

**验证边界**：取得的是首页结构化读取证据；未留存 PolyULife 窗口截图和 Room 查询的“点击 → 反馈 → 返回”验收记录。本会话首次读取已是登录后首页，没有独立复现 PolyU 登录过程。AX 文字不自动证明所有对应元素同时可见。

**沉淀**：本仓库嵌入 [polyulife-ui-analysis skill](../.agents/skills/polyulife-ui-analysis/SKILL.md)，包含安装配置、应用连接恢复、逐步观察和 HCI 分析方法。嵌入版本完整复制自当日使用的 skill。

**下一步**：用当前窗口验证截图读取与一条短流程。Room 查询是候选，入口和步骤以实际页面为准；记录每步动作、反馈和返回路径，留存脱敏证据后再判断其是否适合深入分析。

## 当时尚未作出的决定（后续更新见下文）

- PolyULife 是否作为最终选题，以及具体 5 项主要功能。
- 各成员的最终角色与任务分工。
- 界面问题是否成立及改进方案是否有效；这些结论须经真实页面证据和用户评估支持。

## 2026-09-28 · 用 GitHub 集中协作

最初决定通过私有 GitHub 仓库同步项目，不再以 Google 文档作为当前协作入口；成员接受邀请后访问仓库。仓库创建为 [12bitsD/comp3423-hci-project](https://github.com/12bitsD/comp3423-hci-project)。**其中私有可见性及读取须邀请的安排，已被下方同日公开决定替代。** 任务使用 Issues、改动使用分支与 PR、已达成的决定保存在本文件的协作方式继续有效。

## 2026-09-28 · 将仓库改为公开

用户明确决定将仓库改为 public，方便组员读取材料、复用 skill 和让 AI 接续任务。任何人都可以浏览和克隆；组员接受协作者邀请后获得直接推送工作分支的写入权限，尚无写入权限时可通过 fork 和 PR 提交改动。任务认领与进度继续通过 Issues 同步，材料修改通过 PR 审阅。

公开仓库仅保存适合公开的项目材料，不登记个人邮箱或账号名单，不提交原始个人截图及未经脱敏的参与者资料。本条替代上方私有仓库决定中的可见性和读取权限安排。

## 2026-10-23 · D 的 Food 改版与 Fresh Campus 本地验收

用户说明小组选题为 PolyULife，其 D 分工为 Food 餐饮查询及共用视觉、报告插图、PPT 整合。本轮用户确认 Fresh Campus（米白、深蓝、明亮绿）方向，并通过完整 v0.2 本地验收，明确授权上传工作分支与 PR。材料见 [Food Studio](../prototypes/food-studio/README.md)。此记录更新上述待确认项中用户已明确的选题与 D 范围，不推定其他组员已确认整套视觉标准。

包含完整浏览器交互、两张报告对比图、六页可编辑 PPT、使用规范、局部 AGENTS.md 与 Figma 迁移说明。历史截图保留来源；营业时间为演示场景；尚无真人评估结果。此验收不代表 Figma/Maze 课程交付已完成，也不授权直接合并 main。

## 2026-11-05 · D 的 Food 独立 Figma

按用户与小组提出的分模块交付方式，Food 改版创建独立 Figma 文件，沿用 Fresh Campus 风格；设计和 Present 链接见 [说明](food-figma.md)。已执行核心交互与返回走查。原小组文件保留，最终合并后须重新验证跨功能导航。本次不等同于真人 Maze 评估。

## 2026-11-09 · 确认五项分工并进入测试与最终整合

依据 2026-10-02 小组分工及 10-03 协作记录，最终研究对象为 PolyULife，功能为 Apps、Calendar、Room、Food、Map；A–E 的个人功能和公共职责见 [项目简述](project-brief.md)。本条替代早期“暂定选题、待确认功能与分工”的状态，但不把各功能“尚未入库”解释为“尚未开始”。

当前优先完成可测试改版、统一 Maze 和最终报告，而不是继续扩张原 App 的全量复现。Food PR #7 经本地交互、JavaScript、PPTX 结构、导出素材和差异检查后在 2026-11-09 合并，作为 Fresh Campus 共同视觉基线；这不替代团队对其他模块的视觉复核，也不代表已有真人评估结果。

A 的 Apps 工作进入 `feat/apps-redesign` 分支。设计聚焦真实观察到的分类状态可见性问题及 VRS 任务链，所有效果结论仍待至少五位真实参与者的 Maze 数据验证。
