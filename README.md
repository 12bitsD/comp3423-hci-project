# COMP3423 HCI Project

本仓库记录 COMP3423 小组项目的研究、界面证据、设计决策与评估过程。当前**暂定 PolyULife 为研究对象，并行收集 Web 备选**；选题、具体功能和分工仍由小组讨论确认。

协作入口为公开仓库 [12bitsD/comp3423-hci-project](https://github.com/12bitsD/comp3423-hci-project)，任何人都可以读取和克隆。用 GitHub Issues 记录任务和待讨论问题，Pull Request 审阅改动，仓库文件保存研究材料与重要决策。

## 当前进展

2026-09-28 已通过原生 Mac App Store 安装并运行官方 PolyULife 3.0.0，通过 **Codex Computer Use** 连接应用，取得首页可访问性控件树（AX）信息。实际路线为：

**iPhone App on Apple Silicon Mac → Computer Use 连接真实窗口 → 观察画面/控件 → 执行动作并确认反馈。**

无需先搭建 Xcode 或 iOS Simulator。现已取得真实窗口截图，并走通 Room 查询、筛选、Preview、教室地图和返回首页的流程；More 中的恶劣天气详情及网页入口也已有取证。全部功能的覆盖与边界检查仍在进行，详见 [观察台账](docs/polyulife/README.md)。

已建立 [PolyULife Figma 文件](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)，正在依照实测截图制作原应用复现。文件存在不代表全应用复现完成；可编辑节点、交互连线和 Present 运行结果逐项登记于台账。

2026-10-03新增 [五项Food查询参考](docs/polyulife/food-oct3-query-alignment-walkthrough.md)：Asian、Taiwanese、Cake / Dessert、Salad分别独立展示已观察结果，Western沿用有限滚动参考。搜索栏位置已修正并保存实际Figma截图；查询输入、结果详情及返回调用者仍待连接，完整应用未完成。

## Figma 原型链接

- **[从首页开始体验（推荐）](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=67-569&scaling=scale-down&content-scaling=fixed&starting-point-node-id=67%3A569&show-proto-sidebar=1)**：包含日期、日程及功能入口，适合演示进入功能后返回首页的流程。
- **[打开 Figma 设计文件](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)**：当前复现位于 `01 · Observed UI` 页面。

| 功能入口 | 可点击原型 |
| --- | --- |
| Room：输入 A → AG206 查询 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-198&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A198&show-proto-sidebar=1) |
| Room：September30 七日选择与筛选 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=412-19&scaling=scale-down&content-scaling=fixed&starting-point-node-id=412%3A19&show-proto-sidebar=1) |
| Room：Available 时段参考 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-105&scaling=scale-down&content-scaling=fixed&starting-point-node-id=12%3A105&show-proto-sidebar=1) |
| More：天气与虚拟助手 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-435&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A435&show-proto-sidebar=1) |
| Calendar：公共校历与筛选 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=42-165&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=42%3A165&show-proto-sidebar=1) |
| Food：餐厅与营业时间 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=50-1911&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=50%3A1911&show-proto-sidebar=1) |
| Food：Western Cuisine 11条结果滚动参考（导航待接） | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=954-59&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=954%3A59&show-proto-sidebar=1) |
| Food：当前28条连续列表参考（导航待接） | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=954-3580&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=954%3A3580&show-proto-sidebar=1) |
| Apps：分类与 VRS | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI---Interaction-Atlas?node-id=61-2&t=Ohxzpdr7gRXrVgsv-0&scaling=scale-down&content-scaling=fixed&starting-point-node-id=61%3A2&show-proto-sidebar=1) |
| Home：Study、Courses 与 Campus QR | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=67-820&scaling=scale-down&content-scaling=fixed&starting-point-node-id=67%3A820&show-proto-sidebar=1) |
| Map：设施与分类筛选 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=70-1064&scaling=scale-down&content-scaling=fixed&starting-point-node-id=70%3A1064&show-proto-sidebar=1) |
| 菜单：Profile、Settings 与 Mac 页面 | [打开原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=42-1617&scaling=scale-down&content-scaling=fixed&starting-point-node-id=42%3A1617&show-proto-sidebar=1) |

原型仍在制作中，当前链接用于已复现的样例流程；完整覆盖与未完成项见 [观察台账](docs/polyulife/README.md)。需要演示返回首页时，请从上方推荐首页进入；部分独立功能入口没有首页返回上下文。个人信息采用合成 DEMO，房间可用性为历史观察数据。

## 从哪里开始

| 内容 | 入口 |
| --- | --- |
| 课程交付、截止时间与待确认事项 | [项目简述](docs/project-brief.md) |
| 全应用观察覆盖、真实截图与 Figma 复现进度 | [PolyULife 观察台账](docs/polyulife/README.md) |
| 选题和工具路线的决策记录 | [决策记录](docs/decisions.md) |
| 为什么选 Mac 路线、备选方案和下一轮验收 | [接入研究](docs/research/ios-computer-use.md) |
| 可复用的应用操作与 HCI 分析流程 | [PolyULife skill](.agents/skills/polyulife-ui-analysis/SKILL.md) |
| 新机器安装、权限配置和验收 | [安装与配置](.agents/skills/polyulife-ui-analysis/references/setup.md) |
| 截图、步骤记录和隐私处理约定 | [证据目录说明](evidence/README.md) |
| 克隆仓库、写入权限与 PR 协作 | [协作说明](CONTRIBUTING.md) |

## 在 Codex 中使用嵌入的 skill

1. 克隆 `https://github.com/12bitsD/comp3423-hci-project.git`，在 Codex 中将仓库根目录打开为项目；读取和克隆无需协作者邀请。
2. 本仓库已包含 `.agents/skills/polyulife-ui-analysis/`，无需依赖某位组员的全局 skill。首次运行先按 [安装与配置](.agents/skills/polyulife-ui-analysis/references/setup.md) 完成 Mac 应用和 Computer Use 配置。
3. 在项目聊天中输入：

   > 用 $polyulife-ui-analysis 分析 PolyULife 的 Room 查询流程，把实际操作和脱敏证据保存在 evidence/ 下，区分观察事实、问题假设与待验证事项。

4. 若当前客户端未列出项目 skill，可明确要求 Agent 先读取 `.agents/skills/polyulife-ui-analysis/SKILL.md`。skill 是操作说明；真实界面的观察与交互仍通过 Computer Use 完成。

## 协作方式

- 仓库公开可读、可克隆。需要直接推送工作分支的组员，将 GitHub 用户名或个人主页 URL 提供给仓库 owner `12bitsD`，接受协作者邀请后获得写入权限；不需要 Google 邮箱。尚无写入权限时可通过 fork 和 PR 提交改动。
- 工作分支使用 `feat/` 前缀，例如 `feat/room-enquiry-analysis`。按一次可复查的研究或修改提交，发起 Pull Request 并注明证据和未完成项。
- 一次流程分析至少记录运行环境、起点、实际动作、页面反馈及证据位置。已观察与未观察的内容分别标注，具体格式见 [证据约定](evidence/README.md)。
- 仓库只提交适合公开的材料。不要上传账号密码、令牌、原始个人截图、二维码、未经脱敏的参与者资料或会议录音；本地原始材料放在被忽略的目录中。
- Agent 走查用于整理证据与提出设计假设。课程要求的真人参与和 Maze 评估按 [项目简述](docs/project-brief.md) 执行。

当前任务：[Room 查询 Computer Use 取证 #1](https://github.com/12bitsD/comp3423-hci-project/issues/1)、[收集 Web 备选 #2](https://github.com/12bitsD/comp3423-hci-project/issues/2)。任务认领和讨论在 Issues 中进行，达成的决定更新 [决策记录](docs/decisions.md)。完整步骤见 [协作说明](CONTRIBUTING.md)。

本仓库未复制课程原始文件和私人会议材料。正式要求以课程最新发布内容为准。
