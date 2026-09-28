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
