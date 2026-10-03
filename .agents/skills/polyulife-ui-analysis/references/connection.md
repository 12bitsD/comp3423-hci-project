# PolyULife 连接与恢复

仅在应用定位或启动出现问题时读取。首次安装及 Computer Use 权限配置见 [安装与配置](setup.md)。使用当前 `cua_repl` 返回的 API 和权限状态；下面是本机已观察到的行为，不是跨版本保证。

## 安装位置与运行身份不同

本机安装位置为 `/Applications/polyuLife.app`，bundle ID 为 `polyu.its.mobi.psma.prod`。iOS App on Mac 实际运行的副本可能位于系统临时目录下的 `…/Wrapper/polyuLife.app`。

因此可能同时出现：

- 用显示名称或安装路径连接，返回 `Running application not found`；
- `cua.listApps()` 显示同 bundle ID 的运行项和非运行项；
- 按 bundle ID 连接，返回 `Ambiguous app identifier`，并列出两个完整路径。

这些结果不能单独证明应用未安装或已崩溃。

恢复方法：

1. `await cua.listApps()`，确认当前 PolyULife 运行项。
2. 必要时用已发现的 bundle ID 调用 `cua.getApp(...)`。若返回歧义，读取这次结果中的完整路径。
3. 从结果中选择真实运行副本的完整路径，例如本次发现的 `Wrapper/polyuLife.app` 路径，再用 `cua.getApp(observedRuntimePath)` 连接；不要拼接或复用历史临时目录/UUID。
4. 以返回的 PolyULife 窗口与页面内容确认成功。若仍无法连接，保留具体错误，不无限重试。

绑定调用若中途失败，变量可能未建立。恢复时使用新的变量声明，而不是直接给未定义的绑定赋值：

```javascript
// observedRuntimePath 必须来自当前工具发现结果。
var polyuLifeApp = await cua.getApp(observedRuntimePath);
```

后续复用成功的 app 句柄。只有句柄失效或运行身份变化时才重新发现。

## 已验证范围：2026-09-28

本会话的原生 App Store 搜索结果出现 PolyULife；点击“获取”后按钮变为“打开”。随后应用清单显示其运行项。显示名称/安装路径定位曾失败，bundle ID 返回安装路径与临时 Wrapper 路径的歧义信息；选择当时返回的 Wrapper 路径后，工具取得 `polyuLife` 首页窗口的 AX 状态。

首页 AX 状态可读到版本 `3.0.0`、Home/Calendar/Notification/More，以及 Room/Food 等入口。部分图标为私用区字符，且父容器重复聚合子节点文字。

这证明安装、运行和首页结构化读取在当时环境中成功；用户随后确认链路已通。该会话在首页读取后转入 skill 收敛，**没有留下 Room 查询的点击—反馈—返回验收证据**。后续执行按实时结果报告，不把这份历史记录当作完整功能验证。

## 部分输入失效时的边界（2026-10-03）

本次实际窗口仍能通过AX和保存截图读取，但坐标输入返回 `noWindowsAvailable`。重新发现运行Wrapper并Raise也未恢复坐标输入；不能把这个错误直接解释为锁屏、退出或业务缺陷。不要重复索要解锁或无限重绑。

Calendar模式切换的无文字AX `element` 点击能产生Events/Week/Month变化，历史标题点击能切换Show/Hide History；同页筛选图标容器/按钮未建立弹层。必须根据实际截图与动作后状态判断，不能因角色不是button而排除可点击入口，也不能凭输入调用返回宣称成功。当前索引和私用字形不是固定标识，后续重新读取本次页面。

遇到历史/课程记录，原始截图和AX仅保存在忽略目录；共享截图遮盖记录值、日期与个人块位置，Figma使用明确的合成DEMO。模式切换观察不授权支付、记录变更或其它业务提交。

2026-10-03 Payment详情补查确认，插图会异步加载并将正文中的财务字段下移。不要沿用首帧逐字段遮罩；必要时遮盖整个私人正文，重新逐张检查并重建哈希/联系表。安全AX只保留公共控件，不复制聚合父容器中的私人值。单独公开插图前，裁片必须视觉检查，确保未带入相邻标题、日期或金额。遮罩后的像素一致不能用于证明私人正文或金额的保真。

2026-10-03 用户再次解锁后的复查：旧句柄截图返回Computer Use timeout；App清单仍有运行项。bundle歧义结果提供本次Wrapper路径，按该路径重连仍超时。一次针对性恢复后停止重复重绑，继续处理既有证据。不要把运行项、解锁回复或timeout单独当作成功窗口观察或锁屏/崩溃诊断。
