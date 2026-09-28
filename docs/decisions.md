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

## 尚未作出的决定

- PolyULife 是否作为最终选题，以及具体 5 项主要功能。
- 各成员的最终角色与任务分工。
- 界面问题是否成立及改进方案是否有效；这些结论须经真实页面证据和用户评估支持。

## 2026-09-28 · 用 GitHub 集中协作

按最新决定，团队直接通过私有 GitHub 仓库同步项目，不再以 Google 文档作为当前协作入口。成员向 owner 提供 GitHub 用户名，接受邀请后访问仓库；任务使用 Issues，改动使用分支与 PR，已达成的决定保存在本文件。仓库已创建为 [12bitsD/comp3423-hci-project](https://github.com/12bitsD/comp3423-hci-project)。
