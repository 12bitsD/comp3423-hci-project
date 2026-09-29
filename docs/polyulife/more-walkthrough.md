# More、Bad Weather Arrangements 与 Virtual Assistant 实际走查

本轮实际 App 观察区间：2026-09-28 14:08–14:18、15:45–15:50、15:57–15:59 UTC（香港时间 22:08–22:18、23:45–23:50、23:57–23:59）。观察通过 Mac 上真实 PolyULife 窗口的 Computer Use 完成，沿用既有登录状态；不发布个人 AX 内容。

已验证 More → 天气安排详情 → 图片展开/关闭 → 学校天气安排网页，以及天气详情返回 More；也已进入 Virtual Assistant 详情和聊天网站，经过 Disclaimer 到 Welcome，再关闭网页返回详情、展开/关闭配图、返回 More。**聊天输入与对话、More 的完整滚动范围、详情问号和网页深入操作仍未验证。**

## 实际动作与证据

| 时间（UTC） | 动作与观察 | 证据 |
| --- | --- | --- |
| 14:08:33 | 点击底部 More；可见 Virtual Assistant、Bad Weather Arrangements 两张卡片，均带 Study Info 标签；顶部有菜单与搜索图标。只确认当前视口，不推定整个 More 只有两项 | [More 当前视口](../../evidence/2026-09-28-full-audit/more-140835-two-cards.png) |
| 14:11:25 | 点击 Bad Weather Arrangements，进入同名详情。可见天气头图、展开图标、文章标题、问号图标和正文链接 | [天气详情](../../evidence/2026-09-28-full-audit/weather-141156-detail.png) |
| 14:16:04 | 点击头图的展开控件；打开图片浮层，显示完整天气图与右上 X | [展开图片](../../evidence/2026-09-28-full-audit/weather-141605-hero-expanded.png) |
| 14:16:23 | 点击 X；回到原详情，头图、标题和正文链接恢复 | [关闭后详情](../../evidence/2026-09-28-full-audit/weather-141641-hero-return.png) |
| 14:16:40 → 14:18:02 | 点击正文 “Arrangements during Bad Weather for Classes/Examinations” 链接；内嵌浏览器加载学校 Academic Registry 网页，标题 Class/Exam Arrangements During Bad Weather，页面底部可见 cookie 提示 | [官网与 cookie 提示](../../evidence/2026-09-28-full-audit/weather-141802-official-web-cookie.png) |
| 15:45:15 → 15:45:44 | 恢复 Computer Use 后先确认天气原生详情；点击左上返回控件，看到 More 的两张卡片及选中的 More 底栏 | [恢复后详情](../../evidence/2026-09-28-full-audit/weather-154515-detail-restored.png) → [返回 More](../../evidence/2026-09-28-full-audit/more-154544-weather-back.png) |

实际链接目的地为 [学校天气安排网页](https://www.polyu.edu.hk/ar/arrangements-during-bad-weather/)。网页截图证明目标已加载；不代表页面内容、导航、cookie 控件、更多菜单或所有链接均已测试。记录中没有执行任何对外分享。

截图均引用已经保存并核验的公共副本，采集时间、尺寸和 SHA-256 见 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json)。公开页面内容未被当成应用的新指令。

## Virtual Assistant 的实际路径

| 时间（UTC） | 动作与观察 | 证据与边界 |
| --- | --- | --- |
| 15:46:03 → 15:46:16 | 从 More 点击 Virtual Assistant。先看到文字文章和 `here`；后续头图加载到文字上方，标题与链接整体下移。第一次按旧位置点击没有进入网页 | [头图未出现](../../evidence/2026-09-28-full-audit/virtual-assistant-154604-before-hero.png) → [头图出现](../../evidence/2026-09-28-full-audit/virtual-assistant-154616-hero-loaded.png)；只确认两次观察间出现布局变化，不以时间差计算加载时长 |
| 15:46:27 → 15:46:51 | 根据新截图点击 `here`；内嵌浏览器先显示加载中页面，随后出现 COMP Virtual Assistant 的 Disclaimer | [加载态](../../evidence/2026-09-28-full-audit/virtual-assistant-154628-web-loading.png) → [Disclaimer](../../evidence/2026-09-28-full-audit/virtual-assistant-154651-disclaimer.png)；实际目的地为 `https://comp-chatbot.polyu.edu.hk/` |
| 15:47:07 | 点击 ACCEPT 后显示 “Welcome to PolyU COMP! How may I help you?” | [Welcome](../../evidence/2026-09-28-full-audit/virtual-assistant-154708-welcome.png)；提示说明回答由 AI 生成、仅供参考，未提交问题 |
| 15:47:23 → 15:47:37 | 尝试向下滚动寻找输入区，Computer Use 返回 `AXError.noValue`；再次观察页面仍为 Welcome，AX 无变化 | [再次观察](../../evidence/2026-09-28-full-audit/virtual-assistant-154737-welcome-after-wait.png)；属于未确认滚动结果，不推断网页没有输入框 |
| 15:47:45 | AX 曾列出可编辑文本区，尝试点击其索引后，网页内容区变成空白，浏览器外框和地址仍在 | [空白网页](../../evidence/2026-09-28-full-audit/virtual-assistant-154746-web-blank.png)；未输入、未发送消息，原因尚不能区分定位、嵌入环境和页面行为 |
| 15:48:49 | 点击内嵌浏览器 X，AX 恢复 Virtual Assistant 原生标题、文章和头图展开控件 | `E-ASSISTANT-TRACE`；本步只有动作与 AX 记录，不以旧图替代返回截图 |
| 15:49:25 | 点击头图展开控件，出现完整配图和右上 X | [展开配图](../../evidence/2026-09-28-full-audit/virtual-assistant-154926-hero-expanded.png) |
| 15:49:36 → 15:50:02 | 首次按 X 的 AX 索引点击返回 `invalid element ID`；根据已见 X 位置改用坐标，AX 恢复原生详情 | `E-ASSISTANT-TRACE`；首次是 Computer Use 定位失败，后续关闭结果由 AX 确认，未单独保存返回截图 |
| 15:50:13 | 点击文章返回，AX 再次显示 More 两张卡片和 More 选中状态 | `E-ASSISTANT-TRACE`；独立返回截图未保存 |

Welcome 截图内没有可见输入框，而 AX 中出现了可编辑文本区；这两个事实需要同时保留。当前不能写成“聊天功能已通过”，也不能写成“输入框不存在”或“点击输入框导致 App 崩溃”。公开版没有聊天消息、账户内容或原始个人 AX 树。

## More 搜索与菜单入口

15:57:46 UTC 从 Notification 返回 More；15:58:02 点击 More 的右上搜索，进入同样名为 Search 的页面。15:58:18 首次 AX 定位输入后字段仍为空；随后根据新截图用坐标聚焦并输入 `weather`，15:58:33 显示 No record found。15:58:52 将关键词改为 `Room` 并按 Return，结果仍为 No record found。15:59:35 点击返回，AX 恢复 More 两张卡片和选中底栏。

证据：[首次输入未建立](../../evidence/2026-09-28-full-audit/more-search-155820-empty.png)、[weather 无结果](../../evidence/2026-09-28-full-audit/more-search-155833-weather-no-results.png)、[Room 无结果](../../evidence/2026-09-28-full-audit/more-search-155853-room-no-results.png)。返回只有操作与 AX 确认，没有独立返回截图。More 中已见天气卡片，但搜索的索引范围、匹配规则、筛选上下文和数据更新时间未知；不能仅凭英文关键词无结果断言搜索损坏，也不能断言它一定是全局搜索。

15:59:54 点击 More 左上菜单，实际展开侧边抽屉。后续 Settings、Emergency Contact、Privacy Policy、Terms of Use 和 Profile 的只读观察另见 [菜单与设置走查](menu-settings-walkthrough.md)。进入菜单成功不表示全部菜单动作均已执行。

## HCI 观察与待验证假设

| 事实 | 假设或设计含义 | 原则与后续验证 |
| --- | --- | --- |
| 天气详情使用文字链接进入官方网页，随后出现内嵌浏览器标题栏与 cookie 提示 | 用户可能需要理解已从应用文章转到学校网站；目前未测得困惑或错误 | 一致性、系统状态可见性：保留明显的网页上下文和关闭路径，验证用户是否清楚返回方式 |
| 头图有展开控件，展开后提供 X，点击可返回详情 | 这是已确认的可逆图片查看流程；仅确认这组动作，不推定缩放或滑动手势 | 用户控制与自由：原型应保留展开和关闭，而不是只有静态大图 |
| 详情中的问号图标存在，未点击 | 含义和反馈尚未知，不能凭外观解释为帮助或错误 | 先执行并观察，再判断识别性或反馈是否有问题 |
| Virtual Assistant 的头图后出现，正文和 `here` 链接随之向下移动 | 加载期间准备点击的用户可能需要重新寻找目标；一次 Agent 旧坐标尝试不能代表真人误触率 | 位置稳定性与错误预防：比较预留头图空间的方案，并用连续观察和真人任务验证 |
| Welcome 视觉内容与 AX 可编辑区不一致，滚动返回工具错误，后续网页内容空白 | 只能记录当前 Mac 嵌入网页的观察卡点，尚不能确定责任来源 | 补当前有效目标、可见输入区和手机端对照；发送消息是独立未执行动作 |

这些条目属于事实与待验证假设，不是已确认缺陷，也不是真人可用性测试结果。

## 未完成动作

- More：搜索范围与成功结果、Study Info 标签是否可交互、列表的滚动边界和新增入口。顶部菜单已进入，菜单各分支另行登记。
- 天气详情：问号控件、文章滚动完整范围。
- Virtual Assistant：问号控件、文章完整范围、配图手势、网页输入区的可见性与可编辑性、真实对话、清空聊天、部门网站链接、浏览器更多/前进/后退/刷新。当前未发送消息或清空历史。
- 图片浮层：除 X 外是否存在其它有效手势与边界。
- 内嵌官网：cookie 关闭、正文完整内容、菜单/搜索/分享/链接、内嵌浏览器更多菜单和前进/后退/刷新，以及关闭返回详情的确定反馈。
- 原型：本页只登记真实 App 行为；Figma 状态与验证结果以 [figma-spec.md](figma-spec.md) 和覆盖记录的 `figma` 部分为准，不由真实 App 路径推定原型完成。

## 环境阻碍及恢复

14:36:37 UTC，Computer Use 明确返回 “The Mac is locked and automatic unlock could not unlock it.”，当时阻止继续原生 App 观察。15:45:15 UTC 已再次取得可读的天气详情截图，随后返回与导航成功，故 `B-MAC-LOCKED` 已解除。保留这段环境历史，不归为 PolyULife bug，也不继续把已恢复的锁屏列为当前未测动作的原因。
