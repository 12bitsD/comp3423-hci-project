# 让 Codex 观察 PolyULife：接入路线与当前证据

更新：2026-09-28。本文把最初的路线研究与后续安装验证合并为当前状态，供团队接着实验。项目范围见 [项目简述](../project-brief.md)，后续问题和实验任务在 [GitHub Issues](https://github.com/12bitsD/comp3423-hci-project/issues) 讨论。

## 当前选择与实测范围

采用 **官方 iPhone App 直接在 Apple Silicon Mac 运行 → Codex Computer Use 连接真实应用窗口**。Computer Use 提供截图、可访问性控件信息（AX）、点击和输入等能力；skill 只规定使用流程，不替代底层 Computer Use。

当日官方 App Store 页面列出 PolyULife 的 Mac 条件为 macOS 12.5+、Apple M1 或更新芯片，同时注明“专为 iPhone 设计，未针对 macOS 验证”。兼容声明支持尝试安装，具体流程仍需实测。[1][2]

| 能力 | 当前证据与结论 |
| --- | --- |
| 安装和运行 | 原生 App Store 获取后显示“打开”；应用已运行，版本 3.0.0 |
| 首页结构化读取 | Computer Use 通过实时发现的 Wrapper 路径连接，取得首页 AX，读到 Home/Calendar/Notification/More、Room/Food 等入口 |
| 应用画面截图 | 尚未留存 PolyULife 窗口截图作为验收证据；已有商店截图不代替 App 页面截图 |
| 业务操作闭环 | Room 查询的点击、反馈、返回尚未留下验收记录 |
| PolyU 登录 | 初次读取已是登录后首页，本会话未独立复现登录过程 |
| HCI 分析有效性 | 接入可行性得到部分验证；具体问题、设计方案及用户效果仍待研究 |

上述实测状态来自本次接入会话及已沉淀的 [连接记录](../../.agents/skills/polyulife-ui-analysis/references/connection.md)，不是本仓库初始化时再次复测的结果。新会话连接后以实时窗口为准。AX 有重复父容器、私用区图标字符和可能未显示的菜单文字，视觉结论仍需截图确认。

## 为什么不先配置模拟器

Apple Silicon Mac 可以运行开发者允许分发的 iPhone/iPad App；这与 iOS Simulator 是不同路线。[3] Simulator 需要源码或面向 Simulator 的构建。真机和 Simulator 即便都使用 arm64，也不是相同构建目标；装好 Xcode 不能自动让 App Store 真机安装包在 Simulator 中运行。[4]

当前 Mac 路线已进入应用并读到首页，优先把一条真实流程验证完整，再决定是否引入其他工具。

| 路线 | 适用条件 | 当前判断 |
| --- | --- | --- |
| iPhone App on Mac + Computer Use | App 允许 Mac 分发，系统兼容 | 当前首选；运行和首页 AX 已验证 |
| iPhone Mirroring | 兼容的 Mac/iPhone、同一 Apple Account 等官方条件 | 真机备选；此项目未实测，摄像头/麦克风等受限 [5] |
| 真机截图、录屏或 QuickTime | 人能在手机完成目标流程 | 可以提供旧界面证据；实时操作能力需另行验证 [6] |
| Xcode Device Hub | 已有完整 Xcode 和配对真机 | 可查看并交互设备；本项目未测，配置成本较高 [7] |
| iOS Simulator | 源码或 Simulator build、runtime | 获得构建条件后再评估 [4] |
| Appium / WebDriverAgent | 重复自动化需求、Xcode、签名和设备准备 | 后续规模化测试再评估；当前无需引入 [8] |
| 官方 Web 版本或另选 Web case | 可用的网站和合适研究问题 | 保留备选；网页证据须明确标为对应网页，不能代替 iOS 旧界面 |

## 下一轮最小验收

候选路径为 **首页 → Room / 房间查询 → 选择条件 → 查看结果 → 返回**。真实入口和筛选步骤以当前页面为准。先按 [安装与配置](../../.agents/skills/polyulife-ui-analysis/references/setup.md) 检查现有环境，再使用 [分析 skill](../../.agents/skills/polyulife-ui-analysis/SKILL.md) 操作。

1. 记录 App 版本、macOS 版本、运行方式、登录状态及起点；取得可读的真实应用截图。
2. 每次操作后读取新状态，确认入口点击、输入/筛选、查询结果及返回的实际反馈，记录失败点。
3. 保存关键状态的脱敏截图与步骤；在同样条件下复走，注明缓存、日期或登录状态造成的差异。
4. 按“观察事实 → 问题假设 → HCI 原则与建议 → 待验证事项”整理发现，每条关联证据；未发现的问题不凑数。

共享材料保存在 [evidence/](../../evidence/README.md)。普通查询与导航属于界面走查；预约提交、取消记录或资料修改需对应的业务操作授权。

## 分析边界

Mac 观察能支持信息层级、入口文案、导航与状态反馈的分析；触控误触、单手可达性、手势和设备功能需回到真实手机验证。Mac 适配、网络状态或 Computer Use 定位失败不直接归因于 App 设计。Agent 对页面的疑惑只能形成待验证假设，不能作为目标用户已遇到问题的证明。

课程要求的至少 5 位真实参与者 Maze 测试仍须完成。Agent 路径、耗时和成功率不能替代人类测试指标。

## 官方来源

以下资料在 2026-09-28 原始研究中核查；本次归档未重新读取在线页面。产品条件可能变化，新机器配置时以实时提示为准。

- [1] [OpenAI：Computer use](https://learn.chatgpt.com/docs/computer-use)
- [2] [Apple App Store：PolyULife](https://apps.apple.com/cn/app/polyulife/id6444471174)
- [3] [Apple：Running your iOS apps in macOS](https://developer.apple.com/documentation/apple-silicon/running-your-ios-apps-in-macos)
- [4] [Apple TN3117：真机与 Simulator 构建平台区别](https://developer.apple.com/documentation/technotes/tn3117-resolving-build-errors-for-apple-silicon)
- [5] [Apple：iPhone Mirroring](https://support.apple.com/en-us/120421)
- [6] [Apple：QuickTime 录制影片](https://support.apple.com/guide/quicktime-player/record-a-movie-qtp356b55534/mac)
- [7] [Apple：Interacting with your app in Device Hub](https://developer.apple.com/documentation/xcode/interacting-with-your-app-in-device-hub)
- [8] Appium XCUITest Driver：[系统要求](https://appium.github.io/appium-xcuitest-driver/latest/getting-started/system-requirements/)、[真机准备](https://appium.github.io/appium-xcuitest-driver/latest/getting-started/device-setup/)
