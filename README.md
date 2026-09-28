# COMP3423 HCI Project

本仓库记录 COMP3423 小组项目的研究、界面证据、设计决策与评估过程。当前**暂定 PolyULife 为研究对象，并行收集 Web 备选**；选题、具体功能和分工仍由小组讨论确认。

协作入口为私有仓库 [12bitsD/comp3423-hci-project](https://github.com/12bitsD/comp3423-hci-project)。用 GitHub Issues 记录任务和待讨论问题，Pull Request 审阅改动，仓库文件保存研究材料与重要决策。

## 当前进展

2026-09-28 已通过原生 Mac App Store 安装并运行官方 PolyULife 3.0.0，通过 **Codex Computer Use** 连接应用，取得首页可访问性控件树（AX）信息。实际路线为：

**iPhone App on Apple Silicon Mac → Computer Use 连接真实窗口 → 观察画面/控件 → 执行动作并确认反馈。**

无需先搭建 Xcode 或 iOS Simulator。本次已验证的是安装、运行和首页 AX 读取；PolyULife 窗口截图、Room 查询的“点击 → 反馈 → 返回”闭环尚待实测。用户已确认接入链路可用，后续分析仍逐项记录实测结果。

## 从哪里开始

| 内容 | 入口 |
| --- | --- |
| 课程交付、截止时间与待确认事项 | [项目简述](docs/project-brief.md) |
| 选题和工具路线的决策记录 | [决策记录](docs/decisions.md) |
| 为什么选 Mac 路线、备选方案和下一轮验收 | [接入研究](docs/research/ios-computer-use.md) |
| 可复用的应用操作与 HCI 分析流程 | [PolyULife skill](.agents/skills/polyulife-ui-analysis/SKILL.md) |
| 新机器安装、权限配置和验收 | [安装与配置](.agents/skills/polyulife-ui-analysis/references/setup.md) |
| 截图、步骤记录和隐私处理约定 | [证据目录说明](evidence/README.md) |
| 获取访问权限、分支与 PR 协作 | [协作说明](CONTRIBUTING.md) |

## 在 Codex 中使用嵌入的 skill

1. 获得仓库访问权限后克隆 `https://github.com/12bitsD/comp3423-hci-project.git`，在 Codex 中将仓库根目录打开为项目。
2. 本仓库已包含 `.agents/skills/polyulife-ui-analysis/`，无需依赖某位组员的全局 skill。首次运行先按 [安装与配置](.agents/skills/polyulife-ui-analysis/references/setup.md) 完成 Mac 应用和 Computer Use 配置。
3. 在项目聊天中输入：

   > 用 $polyulife-ui-analysis 分析 PolyULife 的 Room 查询流程，把实际操作和脱敏证据保存在 evidence/ 下，区分观察事实、问题假设与待验证事项。

4. 若当前客户端未列出项目 skill，可明确要求 Agent 先读取 `.agents/skills/polyulife-ui-analysis/SKILL.md`。skill 是操作说明；真实界面的观察与交互仍通过 Computer Use 完成。

## 协作方式

- 将 GitHub 用户名或个人主页 URL 提供给仓库 owner `12bitsD`，接受协作者邀请后访问和克隆私有仓库；不需要 Google 邮箱。
- 工作分支使用 `feat/` 前缀，例如 `feat/room-enquiry-analysis`。按一次可复查的研究或修改提交，发起 Pull Request 并注明证据和未完成项。
- 一次流程分析至少记录运行环境、起点、实际动作、页面反馈及证据位置。已观察与未观察的内容分别标注，具体格式见 [证据约定](evidence/README.md)。
- 仓库只提交适合团队共享的材料。不要上传账号密码、令牌、原始个人截图、二维码、未经脱敏的参与者资料或会议录音；本地原始材料放在被忽略的目录中。
- Agent 走查用于整理证据与提出设计假设。课程要求的真人参与和 Maze 评估按 [项目简述](docs/project-brief.md) 执行。

当前任务：[Room 查询 Computer Use 取证 #1](https://github.com/12bitsD/comp3423-hci-project/issues/1)、[收集 Web 备选 #2](https://github.com/12bitsD/comp3423-hci-project/issues/2)。任务认领和讨论在 Issues 中进行，达成的决定更新 [决策记录](docs/decisions.md)。完整步骤见 [协作说明](CONTRIBUTING.md)。

本仓库未复制课程原始文件和私人会议材料。正式要求以课程最新发布内容为准。
