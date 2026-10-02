# October3 Payment 的 Home 返回上下文（2026-10-03）

真实 Computer Use 已观察 **October3 Payment → Home → Calendar**，返回后仍选中 October3，保留 October/月视图、Payment 和 No event。Figma 已补对应的可编辑 Home DEMO 与两条导航，Present 回放两次；完整应用仍 `not_verified`。

## 原生事实与边界

从既有 October2 Payment 起点选择 October3，再通过 Home 和 Calendar 导航。原生返回前后的归一化截图逐像素相等；结束时恢复 October2，与起点截图相等。这仅支持本次日期和调用者上下文的连续性，不能推出任意日期、模式、分类或调用者都保留状态。没有输入凭证、支付、修改用户配置或重新登录。本记录没有重新核对版本，3.0.0 来自前一原生会话。

| 操作 | 实际结果 | 证据 |
| --- | --- | --- |
| October3 → Home | Home 保留既有 My Exam/功能区的滚动位置；个人信息遮盖 | [02截图](../../evidence/2026-10-03-payment-day3-navigation-native/02-home-after-day3.png) / [安全AX](../../evidence/2026-10-03-payment-day3-navigation-native/02-home-after-day3.safe-ax.txt) |
| Home → Calendar | October3 / Payment / No event，日期未回到 October2 | [03截图](../../evidence/2026-10-03-payment-day3-navigation-native/03-calendar-after-home3.png) / [安全AX](../../evidence/2026-10-03-payment-day3-navigation-native/03-calendar-after-home3.safe-ax.txt) |
| 筛选图标 AX click | 输入调用返回，保存截图仍为原页面，没有确认筛选面板 | [04](../../evidence/2026-10-03-payment-day3-navigation-native/04-filter-reopen-day3-attempt.png) |
| 按新截图定位筛选 | 坐标输入返回 noWindowsAvailable；随后同句柄可读取原页面。没有确认输入执行，不归因于 App | [05](../../evidence/2026-10-03-payment-day3-navigation-native/05-filter-coordinate-day3.png) |
| 恢复 October2 | 回到原生起点 | [06](../../evidence/2026-10-03-payment-day3-navigation-native/06-oct2-restored.png) |

[原生清单](../../evidence/2026-10-03-payment-day3-navigation-native/manifest.json)含7张真实截图、安全AX派生子集及2项原生像素比较。Home 身份、数量、考试课程/日期/时间/地点及底部内容全部遮盖；完整原始截图和AX只在忽略的 raw 目录。视图切换图标尚缺可执行的定位，本批没有记录为已尝试或已观察。

本批不新增 HCI 缺陷：状态保留是事实；筛选定位失败目前只能作为工具限制。是否符合参与者预期、是否影响操作效率，仍需真实任务测试。

## Figma 重建与回放

[Home 832:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=832-19)为576×1024可编辑 Frame/Text/Vector/分组，位于画布0,75700。沿用已有合成 DEMO 模板表达观察到的滚动位置；所有个人字段为虚构示例。静态 Home 的连续滚动、卡片与其它功能尚未接入。完整图形和字体保真未验收。

| 已观察动作 | 实际连接 |
| --- | --- |
| A-NATIVE-PAYNAV-HOME3 | October3 Payment 828:19 / NavHome 828:157 → Home 832:19 |
| A-NATIVE-PAYNAV-CALENDAR3 | Home 832:19 / NavCalendar 832:126 → October3 Payment 828:19 |

连接均 On click / Navigate to / Instant。[连接与实际属性读回](../../design/polyulife/calendar-payment-day3-home-connections.json)、[可编辑来源](../../design/polyulife/calendar-payment-day3-home-sources.json)。独立画板表达这一日期的固定返回上下文；尚未实现通用状态模型，未把返回泛化到其它日期。

[Present清单](../../evidence/2026-10-03-payment-day3-navigation-prototype/manifest.json)保存10张实际截图、1张编辑器范围说明及拼图。两次 October3 → Home → Calendar 均返回正确日期；随后执行 October4 → November1 → October1 → October2，既有下游目标仍可到达。7项原型比较全部相等，包括重复Home/October3、起点恢复及三个下游目标与上一批截图的比较；不证明原生视觉保真或真人成功率。

编辑器导入成功后，最初在 Prototype 页检查尺寸，未得到尺寸字段；切到 Design 复核并继续同一画板，没有重复导入。图层行命中锁定与目标同名文本冲突已纠正；随后通过分组选择、连接属性和真实 Present 核对。编辑器定位事件与原生失败分开记录。

## 接力与剩余工作

参考 Flow 当前25个有限画板、33个控件。全台账18次原生会话、162状态、312动作（228 observed /81 not_attempted /3 attempted_unverified）；Figma172映射画板、372配置控件、118次回放。数量不等于完整覆盖。

继续解决原生筛选重开与视图切换定位，再观察其它日期/分类/调用者；将有限返回上下文收敛为通用状态模型、补连续Home与尚未观察功能。手机手势/设备能力与真人课程评估需独立完成。
