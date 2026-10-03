# Calendar Payment：原生补查与 Figma 检查点（2026-10-03）

真实 PolyULife 已重新可观察。Payment-only 草稿的 Apply 得到 **Payment / No event**，选中日期仍是 October 2，Today 标签为 October 3。新增可编辑结果画板和 Apply 连接，并在实际 Figma Present 中回放两次。完整应用仍 `not_verified`。

## 原生事实与边界

本次版本为 3.0.0，运行方式为安装的 iPhone App on Mac，使用 Computer Use。从已有登录状态和 Payment-only 草稿继续；没有支付交易。Finder 对已安装应用执行 Open，再选本次发现的 Wrapper 路径后得到实际窗口。此前连接超时与这次恢复分别保留；没有退出、强制重启或修改配置。这个恢复样例不保证所有机器适用。

| 动作 | 实际结果 | 公开证据 |
| --- | --- | --- |
| Payment-only Apply | 草稿关闭，显示 Payment 与 No event；October2 仍选中 | [01截图](../../evidence/2026-10-03-calendar-payment-native/01-payment-applied.png) / [安全AX](../../evidence/2026-10-03-calendar-payment-native/01-payment-applied.safe-ax.txt) |
| 重新打开筛选 | 多次 AX 定位未建立弹层；坐标路径报 noWindowsAvailable，未确认输入执行 | [03留存页面](../../evidence/2026-10-03-calendar-payment-native/03-payment-reopen-confirmed.png) / [05留存页面](../../evidence/2026-10-03-calendar-payment-native/05-payment-reopen-after-raise.png) |
| Payment → Home | 正常进入 Home；原有滚动位置显示 My Exam，私人字段已遮罩 | [06截图](../../evidence/2026-10-03-calendar-payment-native/06-payment-home-attempt.png) / [安全AX](../../evidence/2026-10-03-calendar-payment-native/06-payment-home-attempt.safe-ax.txt) |
| Home → Calendar | 月视图仍为 October，October2 和 Payment 保留，显示 No event | [07截图](../../evidence/2026-10-03-calendar-payment-native/07-calendar-payment-reentry.png) / [安全AX](../../evidence/2026-10-03-calendar-payment-native/07-calendar-payment-reentry.safe-ax.txt) |

文件名中的 attempt/confirmed/black 保留采集时标签，不能据此判定成功或黑屏。06 的 Home 结果实际已确认；03 未确认重开；04 保存的像素仍是正常 Payment 页面，CUA 即时黑图是另一条工具观察。安全 AX 只保留必要公开控件，是派生子集。原始身份、考试/课程与账户聚合信息仅在忽略的 raw 目录。

历史 Oct2 Payment Apply 仍为 `attempted_unverified`，因为当时输入与结果未知。本次新增独立的 Oct3 observed Apply，不改写历史。Payment 重开也是 `attempted_unverified`。工具点击失效没有足够依据归为 App 缺陷。

## Figma 实际成果

- [Payment 结果画板 823:21](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=823-21)：576×1024，文本、图形和控件来自可编辑 SVG；几何与字体近似，个人日期标记省略。
- Apply：已有草稿 800:1610 的控件 800:1793 → 823:21，On click / Navigate to / Instant。连接依据为本次原生 Apply。
- [连接及属性读回](../../design/polyulife/calendar-oct3-payment-connections.json)；[来源与哈希](../../design/polyulife/calendar-oct3-payment-sources.json)。
- 参考分支说明已更新为19个有限画板；主 Home/More 调用者尚未整合，没有虚构 Payment 重开弹层。

[实际 Present 拼图](../../evidence/2026-10-03-calendar-payment-prototype/contact-sheet.png)包含草稿→Apply→结果两次样例。第二次使用 Figma 的 Previous frame 回到草稿，**不是原生 Back、Cancel 或重新打开筛选**。结果页两次应用裁片相等；草稿比较不等，底部差异来自可见 Figma 播放提示浮层。比较不证明原生像素保真或真人可用性。

## HCI 解释与后续

已观察的这个 Home 往返保留了日期、模式和分类，为检查导航上下文连续性提供证据；尚不能推导所有调用者都保留状态，也不能认定有统一固定 Week/月入口。重开筛选失败目前只支持工具定位限制，不新增应用可用性问题。

下一步把这个有限 Home 调用上下文接入原型并回放，再补筛选重开/X、其它日期/组合与模式边界、Notice/地图剩余控件。完整视觉验收、手机触控和真人 Maze 评估仍未完成。

当前台账：16次原生会话、157状态、303动作（220 observed /81 not_attempted /2 attempted_unverified）；Figma166映射画板、363配置控件、109次运行。数量不是覆盖率或成功率。[完整台账](coverage.json)、[分离来源的追踪记录](calendar-payment-oct3-trace.json)、[原生清单](../../evidence/2026-10-03-calendar-payment-native/manifest.json)、[原型清单](../../evidence/2026-10-03-calendar-payment-prototype/manifest.json)。
