# Payment 日期与月份循环（2026-10-03）

通过真实 PolyULife Computer Use，已观察 **October2 → October3 → October4 → November1 → October1 → October2**，Payment 分类一直保留并显示 No event。四个新日期/月份状态已在 Figma 复现，五条连接实际回放两轮；恢复 October2 后还检查了既有 Home 往返。完整应用仍 `not_verified`。

## 原生记录

运行方式为已安装的 iPhone App on Mac，继续已有登录与 Payment 筛选；本次未重新核对版本，最近版本依据为前一原生会话的 3.0.0。没有输入凭证、执行支付或更改配置。当前起点及结束点均为 October2 / Payment。

| 动作 | 真实反馈 | 公开截图 / 安全AX |
| --- | --- | --- |
| 点击 October3 | Saturday, October3 被选中；Payment / No event | [01](../../evidence/2026-10-03-calendar-payment-dates-native/01-payment-oct3.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/01-payment-oct3.safe-ax.txt) |
| 点击 October4 | Sunday, October4 被选中；分类不变 | [02](../../evidence/2026-10-03-calendar-payment-dates-native/02-payment-oct4.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/02-payment-oct4.safe-ax.txt) |
| 月份标题 `Increment` | 留在 October4，没有确认 November | [03](../../evidence/2026-10-03-calendar-payment-dates-native/03-payment-november.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/03-payment-november.safe-ax.txt) |
| 新状态列出的 `increment` | November / November1；Payment / No event | [04](../../evidence/2026-10-03-calendar-payment-dates-native/04-month-increment-correction.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/04-month-increment-correction.safe-ax.txt) |
| 新状态列出的 `decrement` | October / October1；没有恢复先前 October4 | [05](../../evidence/2026-10-03-calendar-payment-dates-native/05-payment-october-return.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/05-payment-october-return.safe-ax.txt) |
| 点击 October2 | 回到起点日期，Payment 保留 | [07稳定截图](../../evidence/2026-10-03-calendar-payment-dates-native/07-payment-oct2-stable.png) / [AX](../../evidence/2026-10-03-calendar-payment-dates-native/07-payment-oct2-stable.safe-ax.txt) |

03 文件名中的 november 是尝试标签，不是成功结果。大写动作后保存状态未变化，随后小写动作后得到 November；没有隔离大小写、时序等因素的贡献，不能推导所有控件只能用小写。后续操作仍应以新 AX 列出的动作和实际反馈为准。

这一次跨月正反向都选中目标月1日，同时保留 Payment，只证明这个有限上下文。月份、年度、学期边界、其它模式及调用者规则未完成。首尾两张真实归一化 October2 图像逐像素相等，这是原生起点恢复证据，不是 Figma 比较或真人评估。

公开截图只保留应用内容，空状态中没有身份、私人课程、个人二维码或支付内容；AX 文件是明确派生的安全子集。[原生清单](../../evidence/2026-10-03-calendar-payment-dates-native/manifest.json)列出8张真实截图、来源、时间、哈希、裁切及状态/动作。原始完整 AX 只存于忽略的 raw 目录。

## HCI 事实与假设

October3 可见页面位于 Sat 列，选中标题是 `Saturday, October 3`，而对应 AX 日期控件名称是 `Today Sunday 3 October 2026 ...`。这在当前 Mac 上再次复现了已有 `F-CALENDAR-AX-DATE-LABEL`，并非新增加一个重复问题。辅助访问名称与可见日期语义应一致；它可能影响依赖控件名称的日期判断，但没有实测 iOS VoiceOver、真人困惑或误操作。需要在真实手机、读屏与语言设置下复核；原型视觉仍照可见日期复现，不把候选修复当成原 App 行为。

月份返回选中1日属于当前观察到的行为，不直接写成数据错误。若用户希望返回之前的日期，是否需要额外操作，应通过真实任务与参与者验证。[候选分析与边界](hci-findings.md)。

## Figma 实际结果

| 对应状态 | 可编辑画板 |
| --- | --- |
| October3 | [828:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=828-19) |
| October4 | [829:178](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=829-178) |
| November1 | [829:337](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=829-337) |
| October1 | [829:510](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=829-510) |

四张576×1024原生Frame/Text/Vector画板没有整页截图填充；November的六行日期和下移内容按观察组织。字体、通用图标与几何近似，个人标记省略，完整视觉验收未完成。[来源及哈希](../../design/polyulife/calendar-payment-dates-sources.json)、[五条连接与属性读回](../../design/polyulife/calendar-payment-dates-connections.json)。连接为 On click / Navigate to / Instant，日期/箭头热点表示已观察控件；没有把初始无变化尝试模拟成延时。

实际编辑器曾因同名目标文字与未关闭弹窗选错根图层，放大旧日期文字；失败步骤没有登记为新连接。修正为弹窗内 Close、唯一根图层、图层列表滚动与选中读回后，五个控件全部配置。

[Present清单](../../evidence/2026-10-03-calendar-payment-dates-prototype/manifest.json)保存13张实际截图、1张范围说明和拼图，3组运行：两个完整日期/月循环，以及恢复 October2 后的 Home 往返回归。7项重复画面裁片比较全部相等。即时 AX URL 有时仍显示来源页，保存的实际像素已确认目标；不凭URL滞后断言导航失败。比较不证明原生像素保真、任意日期行为或真人可用性。

## 剩余工作

后续[October3 Home返回上下文](calendar-payment-day3-home-walkthrough.md)已补原生观察和两条连接；其它新日期Home、筛选和视图模式尚未连线，未观察控件没有泛化到其它日期。Payment 重开/X、任意日期/组合、年度学期边界、其它 Home/More 调用者及全应用覆盖继续保持未完成。

当前台账：17次原生会话、161状态、308动作（225 observed /81 not_attempted /2 attempted_unverified）；Figma171映射画板、370配置控件、115次运行。数量不代表完成率。原生分析、原型功能回放、手机手势和真人 Maze 测试仍分开记录。
