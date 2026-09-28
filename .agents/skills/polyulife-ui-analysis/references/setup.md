# 安装与配置

目标链路：**官方 iPhone App 在 Apple Silicon Mac 运行 → Codex Computer Use 连接应用窗口 → 读取截图和控件信息 → 操作后确认反馈。**

首次安装、换机器或权限缺失时使用本页。已运行成功的机器保留现有安装与权限，不重复配置。下面的官方要求核查于 2026-09-28，设置名称和商店可用性以当前版本为准。

## 1. 确认运行条件

- 使用 Apple Silicon Mac。PolyULife 当时的官方商店页面列出最低要求为 **Apple M1 或更新芯片、macOS 12.5 或更高版本**；这只是 App 的最低要求，Codex 桌面客户端也需满足自身当前要求。
- 原生 Mac App Store 应能找到 PolyULife。页面标注“专为 iPhone 设计，未针对 macOS 验证”时，说明仍需验证实际运行与功能；不把这句提示直接当作禁止安装。
- 此路线直接使用 App Store 分发的 iOS App on Mac，无需配置 Xcode、Simulator、Appium、开发者签名或 iPhone 配对。

**完成条件**：当前 Mac 满足要求，原生商店显示目标应用及可用的获取或打开按钮。若商店不可用，记录地区/系统/账户等实际提示，不猜测原因。

## 2. 准备 Computer Use

按当前 Codex/ChatGPT 桌面应用界面检查：

1. 在 **Plugins → Computer Use** 安装或启用插件；若显示相应控件，启用其 server 和 skill。先复用已启用的配置。
2. 按 macOS 提示，由用户在 **系统设置 → 隐私与安全性** 中为提示指定的 Computer Use 组件开启：
   - **屏幕录制 / 屏幕与系统音频录制**：获取应用画面。
   - **辅助功能**：点击、输入和导航。
   官方文档当时将组件称为 `Codex Computer Use`；以本机实际提示的项目为准。若系统要求重启对应组件，按提示处理后重试观察。
3. 在桌面应用的 **Settings → Computer use** 检查应用访问。系统权限与单个应用访问授权是两层设置；按任务需要允许 App Store 和 PolyULife。是否保存为 Always allow 由用户选择，skill 不要求永久授权。
4. 确认本会话可调用 `mcp__cua_repl`。缺少工具时先解决插件/环境问题；不要把 shell 截图或其他自动化方式描述成已跑通 Computer Use。

操作系统的安全与隐私授权需要用户在系统界面完成。出现阻塞时指出具体权限项和当前提示，避免笼统要求“重新配置所有权限”。

**完成条件**：Computer Use 工具可选中已允许的原生应用，取得窗口状态；截图和输入能力在后面的实际验收中分别确认。

## 3. 在原生 App Store 安装

用户已授权安装时，通过 `mcp__cua_repl` 直接选择原生 App Store。新会话第一次调用只做这个入口调用，先阅读其返回文档与状态：

```javascript
var appStore = await cua.getApp("App Store");
```

然后根据实时界面逐步操作，每次动作后取新状态：

1. 在搜索框搜索 **PolyULife**。若 Mac App 分类无结果，查看 **iPhone 与 iPad App** 分类。
2. 核对应用名和开发者 **The Hong Kong Polytechnic University**，避免选中 PolyU Library 或 iPolyU。
3. 点击该应用的 **获取 / 安装**。若已显示“打开”，直接复用现有安装。
4. 如出现 Apple 账户登录、Touch ID、密码或其他认证提示，按当前工具规则与可用认证方式处理；需要用户参与时停在该提示。认证信息不写入 skill、日志或共享证据。若出现新的条款确认，按其实际审批要求处理，不自动代为接受。
5. 观察下载结果；以目标按钮变为 **打开** 作为商店阶段的完成证据，再点击打开。

使用搜索框或按钮时从新状态取得索引，不抄用历史索引。无需浏览器跳转来完成上述原生商店流程。若某个工具明确拒绝操作，遵守该拒绝的实际范围；skill 不构成绕过限制的授权，也不把单次跳转失败扩大成“应用无法在 Mac 运行”。

**完成条件**：目标应用在商店显示“打开”，随后实际应用窗口可被发现；只有下载进度或获取按钮变化时，不宣称运行成功。

## 4. 连接 PolyULife 并处理其登录状态

先尝试实际安装位置，例如本机观察到的：

```javascript
var polyuLifeApp = await cua.getApp("/Applications/polyuLife.app");
```

出现“找不到运行应用”或同 bundle ID 多副本时，使用 [连接与恢复](connection.md) 动态发现当前 Wrapper 路径。不要把临时容器路径写死为固定配置。

App Store 的 Apple 账户认证负责下载应用；PolyULife 内的 PolyU/NetID 登录决定能否访问个人功能。两者分别处理。先读取当前应用状态，保留已有登录；若目标流程要求登录而当前是游客态，再按实际提示完成必要的用户步骤。不要为了复现安装过程主动退出登录。

**完成条件**：已取得属于 PolyULife 的窗口，能判明当前页面及登录/游客状态；登录受阻则明确停在哪一层。

## 5. 按能力逐项验收

| 能力 | 可复核证据 |
| --- | --- |
| 已安装 | 原生商店目标按钮为“打开” |
| 已运行并连接 | Computer Use 返回 `polyuLife` 的实际窗口状态 |
| 可读取控件信息 | `getAXState()` 返回页面文字/控件；乱码或缺失如实记录 |
| 可观察视觉界面 | `getScreenshot()` 返回可辨识的当前应用画面；与控件信息对照 |
| 可操作 | 在已授权范围内点一个普通入口、观察结果，再返回；每一步以新状态/截图确认 |

若本次只需准备环境，至少报告已经验证到哪一项。若用户要界面分析，再按主 skill 继续指定流程；无需在配置阶段扩展成完整应用测试。

## 本次配置事实与证据边界

2026-09-28 本机为 Apple Silicon/macOS 27.0，Computer Use 已经可用。**本会话没有从零安装 Computer Use 插件，也没有重新配置 macOS 系统权限**；第 2 节是官方配置指引，不是本次逐步执行记录。

本次通过原生 App Store 搜索并获取 PolyULife，按钮随后变为“打开”。期间出现过 Apple 账户认证界面，随后回到下载状态；记录不声称 Agent 输入过密码。应用已运行，最终通过实时发现的 Wrapper 路径取得首页 AX 状态，版本为 3.0.0。首次读取时已显示登录后的首页，**本会话未独立复现 PolyU 登录过程**。

本次留有商店截图及 PolyULife 首页 AX 输出；尚未留存 PolyULife 窗口截图和具体功能“点击—反馈—返回”的验收证据。详细运行身份问题及已验证范围见 [连接与恢复](connection.md)。

## 官方依据

- [OpenAI：Computer Use 的插件、系统权限和应用访问设置](https://learn.chatgpt.com/docs/computer-use)
- [Apple App Store：PolyULife 兼容性与开发者信息](https://apps.apple.com/cn/app/polyulife/id6444471174)
- [Apple：在 macOS 运行 iOS App](https://developer.apple.com/documentation/apple-silicon/running-your-ios-apps-in-macos)
