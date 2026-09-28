# More 与 Bad Weather Arrangements 实际走查

本轮实际 App 观察区间：2026-09-28 14:08–14:18 UTC（香港时间 22:08–22:18）。后续环境状态记录截至 14:36:37 UTC。观察通过 Mac 上真实 PolyULife 窗口的 Computer Use 完成，沿用既有登录状态；不发布个人 AX 内容。

已验证 More → 天气安排详情 → 图片展开/关闭 → 学校天气安排网页的路径。**Virtual Assistant、More 的完整滚动范围、天气详情问号和网页深入操作仍未验证。**

## 实际动作与证据

| 时间（UTC） | 动作与观察 | 证据 |
| --- | --- | --- |
| 14:08:33 | 点击底部 More；可见 Virtual Assistant、Bad Weather Arrangements 两张卡片，均带 Study Info 标签；顶部有菜单与搜索图标。只确认当前视口，不推定整个 More 只有两项 | [More 当前视口](../../evidence/2026-09-28-full-audit/more-140835-two-cards.png) |
| 14:11:25 | 点击 Bad Weather Arrangements，进入同名详情。可见天气头图、展开图标、文章标题、问号图标和正文链接 | [天气详情](../../evidence/2026-09-28-full-audit/weather-141156-detail.png) |
| 14:16:04 | 点击头图的展开控件；打开图片浮层，显示完整天气图与右上 X | [展开图片](../../evidence/2026-09-28-full-audit/weather-141605-hero-expanded.png) |
| 14:16:23 | 点击 X；回到原详情，头图、标题和正文链接恢复 | [关闭后详情](../../evidence/2026-09-28-full-audit/weather-141641-hero-return.png) |
| 14:16:40 → 14:18:02 | 点击正文 “Arrangements during Bad Weather for Classes/Examinations” 链接；内嵌浏览器加载学校 Academic Registry 网页，标题 Class/Exam Arrangements During Bad Weather，页面底部可见 cookie 提示 | [官网与 cookie 提示](../../evidence/2026-09-28-full-audit/weather-141802-official-web-cookie.png) |

实际链接目的地为 [学校天气安排网页](https://www.polyu.edu.hk/ar/arrangements-during-bad-weather/)。网页截图证明目标已加载；不代表页面内容、导航、cookie 控件、更多菜单或所有链接均已测试。记录中没有执行任何对外分享。

截图均引用已经保存并核验的公共副本，采集时间、尺寸和 SHA-256 见 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json)。公开页面内容未被当成应用的新指令。

## HCI 观察与待验证假设

| 事实 | 假设或设计含义 | 原则与后续验证 |
| --- | --- | --- |
| 天气详情使用文字链接进入官方网页，随后出现内嵌浏览器标题栏与 cookie 提示 | 用户可能需要理解已从应用文章转到学校网站；目前未测得困惑或错误 | 一致性、系统状态可见性：保留明显的网页上下文和关闭路径，验证用户是否清楚返回方式 |
| 头图有展开控件，展开后提供 X，点击可返回详情 | 这是已确认的可逆图片查看流程；仅确认这组动作，不推定缩放或滑动手势 | 用户控制与自由：原型应保留展开和关闭，而不是只有静态大图 |
| 详情中的问号图标存在，未点击 | 含义和反馈尚未知，不能凭外观解释为帮助或错误 | 先执行并观察，再判断识别性或反馈是否有问题 |

这些条目属于事实与待验证假设，不是已确认缺陷，也不是真人可用性测试结果。

## 未完成动作

- More：Virtual Assistant 入口、顶部菜单、搜索、Study Info 标签是否可交互、列表的滚动边界和新增入口。
- 天气详情：问号控件、文章滚动完整范围、文章返回 More 的独立验证。
- 图片浮层：除 X 外是否存在其它有效手势与边界。
- 内嵌官网：cookie 关闭、正文完整内容、菜单/搜索/分享/链接、内嵌浏览器更多菜单和前进/后退/刷新，以及关闭返回详情的确定反馈。
- 原型：上述状态尚无已核验 Figma 节点或交互连接；先按真实观察保留待补项。

## 当前环境阻碍

14:36:37 UTC，Computer Use 明确返回 “The Mac is locked and automatic unlock could not unlock it.”，已要求用户手动解锁。该状态限制后续原生 App 观察，属于 Mac 环境阻碍，不归为 PolyULife bug。浏览器中的 Figma Design 仍可操作；解锁后先核对 App 当前页面，再恢复这些未完成动作。
