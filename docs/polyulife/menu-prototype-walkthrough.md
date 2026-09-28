# 菜单与 Mac 设置交接：Figma 实际回放

当前 [菜单原型入口](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=42-1617&scaling=scale-down&content-scaling=fixed&starting-point-node-id=42%3A1617&show-proto-sidebar=1)，流程名 `Menu · Profile, Settings and Mac handoff`。原生 App 依据见 [实际菜单走查](menu-settings-walkthrough.md)。

本批用完整 576×970、明确 DEMO 身份的抽屉 75:1669 替代当前菜单映射；旧 489×642 公开菜单裁片 50:1846 留作历史参考，不再作为 Home 的当前目标。新增 Mac General 75:1710（1382×320），保持其独立 Mac 窗口形态，不画成 iPhone 权限页。Settings/Profile/政策/条款/紧急提示复用已有可编辑文字和向量页面。

## 连接与返回语义

共 15 个控件已在 Present 实际执行，其中 HomeMenu 是更改既有目标，其余为本批新增连接；当前台账合计 76 个映射画板、108 个控件。Back 使用原型历史返回，实测从 Notification 和 Home 打开抽屉后，关闭会分别返回各自来源。公开抽屉用中性灰背景条保留遮罩点击范围；没有复制真实 Home 私人课程内容。

| 动作 | 来源 frame | 控件节点 | 目标 / 行为 |
| --- | --- | --- | --- |
| `A-NOTIFICATION-MENU` | `42:1617` | `42:1622` | `75:1669` / Navigate to |
| `A-HOME-MENU` | `67:820` | `67:921` | `75:1669` / Navigate to |
| `A-DRAWER-SETTINGS` | `75:1669` | `75:1684` | `50:1794` / Navigate to |
| `A-DRAWER-PROFILE` | `75:1669` | `75:1680` | `50:1818` / Navigate to |
| `A-DRAWER-EMERGENCY` | `75:1669` | `75:1688` | `50:1778` / Navigate to |
| `A-DRAWER-PRIVACY` | `75:1669` | `75:1696` | `50:2058` / Navigate to |
| `A-DRAWER-TERMS` | `75:1669` | `75:1700` | `50:1862` / Navigate to |
| `A-DRAWER-CLOSE` | `75:1669` | `75:1671` | Back；来源由实际历史决定 |
| `A-SETTINGS-PUSH` | `50:1794` | `50:1808` | `75:1710` / Navigate to |
| `A-MAC-GENERAL-CLOSE` | `75:1710` | `75:1712` | Back；来源由实际历史决定 |
| `A-SETTINGS-BACK` | `50:1794` | `50:1798` | Back；来源由实际历史决定 |
| `A-PROFILE-BACK` | `50:1818` | `50:1822` | Back；来源由实际历史决定 |
| `A-PRIVACY-BACK` | `50:2058` | `50:2104` | Back；来源由实际历史决定 |
| `A-TERMS-BACK` | `50:1862` | `50:1908` | Back；来源由实际历史决定 |
| `A-EMERGENCY-CLOSE` | `50:1778` | `50:1791` | Back；来源由实际历史决定 |

## 回放证据

运行 `PROTO-MENU-V2-001`：2026-09-28 19:42:04–19:47:30 UTC。以下为真实浏览器 Computer Use 截图，保留 Figma 周边上下文并遮盖右上账户头像。它们证明记录中的导航，不代表真人可用性指标。

| UTC | 实际动作与结果 | 证据 |
| --- | --- | --- |
| 19:42:04 | 通知空态起点 | [E-MENU-P-01](../../evidence/2026-09-28-full-audit/figma-menu-194204-01.png) |
| 19:42:14 | 通知页打开完整抽屉 | [E-MENU-P-02](../../evidence/2026-09-28-full-audit/figma-menu-194214-02.png) |
| 19:42:22 | 抽屉进入 Settings | [E-MENU-P-03](../../evidence/2026-09-28-full-audit/figma-menu-194222-01.png) |
| 19:42:31 | Push Notification 进入 Mac General | [E-MENU-P-04](../../evidence/2026-09-28-full-audit/figma-menu-194231-02.png) |
| 19:42:38 | 关闭 Mac General 返回 Settings | [E-MENU-P-05](../../evidence/2026-09-28-full-audit/figma-menu-194238-01.png) |
| 19:42:51 | Settings 返回抽屉 | [E-MENU-P-06](../../evidence/2026-09-28-full-audit/figma-menu-194251-01.png) |
| 19:43:00 | Profile DEMO | [E-MENU-P-07](../../evidence/2026-09-28-full-audit/figma-menu-194300-01.png) |
| 19:43:07 | Profile 返回 | [E-MENU-P-08](../../evidence/2026-09-28-full-audit/figma-menu-194307-01.png) |
| 19:43:15 | 紧急联系提示：首次点击未跳转，记为失败 | [E-MENU-P-09](../../evidence/2026-09-28-full-audit/figma-menu-194315-01.png) |
| 19:45:43 | 打开紧急联系提示 | [E-MENU-P-10](../../evidence/2026-09-28-full-audit/figma-menu-194543-01.png) |
| 19:45:57 | 仅 Close 返回抽屉 | [E-MENU-P-11](../../evidence/2026-09-28-full-audit/figma-menu-194557-01.png) |
| 19:46:09 | 隐私政策 | [E-MENU-P-12](../../evidence/2026-09-28-full-audit/figma-menu-194609-01.png) |
| 19:46:20 | 隐私政策返回 | [E-MENU-P-13](../../evidence/2026-09-28-full-audit/figma-menu-194620-01.png) |
| 19:46:27 | 使用条款 | [E-MENU-P-14](../../evidence/2026-09-28-full-audit/figma-menu-194627-01.png) |
| 19:46:38 | 使用条款返回 | [E-MENU-P-15](../../evidence/2026-09-28-full-audit/figma-menu-194638-01.png) |
| 19:46:48 | 多次子页往返后关闭菜单回通知页 | [E-MENU-P-16](../../evidence/2026-09-28-full-audit/figma-menu-194648-02.png) |
| 19:46:59 | 从 Home 流程验证另一来源：转场时画面暂空，下一张才是加载完成 | [E-MENU-P-17](../../evidence/2026-09-28-full-audit/figma-menu-194659-01.png) |
| 19:47:10 | 等待 Home 流程渲染后的菜单起点 | [E-MENU-P-18](../../evidence/2026-09-28-full-audit/figma-menu-194710-01.png) |
| 19:47:21 | Home 打开完整抽屉 | [E-MENU-P-19](../../evidence/2026-09-28-full-audit/figma-menu-194721-01.png) |
| 19:47:30 | 关闭抽屉回到 Home | [E-MENU-P-20](../../evidence/2026-09-28-full-audit/figma-menu-194730-02.png) |

紧急入口首次失败是本次原型配置问题：多选状态下误加了拖动连接。检查单个图层后移除这一共同误连接，给 DrawerEmergency 75:1688 加独立 Click；同时移除紧急提示正文的误返回，只给 Close 50:1791 加 Back。修正后实际打开、关闭均成功；未把首次失败删除或计为通过。

## 仍未完成

- **导航样例通过，视觉只部分通过。** Privacy/Terms 的初始视口右侧裁切已在后续字体修复中消除（见下）；字体仍为近似。cookie Close 已在后续独立组件增量中接入并回放；正文滚动和 Terms 加载状态仍未接入。
- 抽屉的来源背景使用灰色条，尚未重建真实内容覆盖效果。Emergency 以独立 frame 展示，尚未实现原生 sheet overlay 的位置和背景。Mac General 图标近似，只有关闭路径，没有实现其它标签页或偏好变更。
- Location 无反馈属于原生观察中的未确认结果；没有编造权限页。无标签开关、Log Out、Call 都不提供伪造的成功结果。
- 旧菜单裁片保留在画布历史参考中；完整应用仍是 `not_verified`。其它模块未尝试动作、图片缺失与输入/滚动边界继续沿用台账。

源文件：[完整 DEMO 抽屉](../../design/polyulife/drawer-full-demo.svg)、[Mac General](../../design/polyulife/mac-general.svg)、[生成脚本](../../design/scripts/build_menu_svg.py)。共享 screenshot 与设计稿分别索引，设计稿不替代原生证据。

[19:56:00 最终菜单流程上下文](../../evidence/2026-09-28-full-audit/figma-menu-195600-02.png)确认流程名称、DEMO 抽屉和可见的未完成范围说明；额外自动起点 Flow 1 已移除。


## 政策页字体修复复验（2026-09-29 本地时间）

通过 Computer Use 在 Figma 编辑器中只选择 `VisiblePolicyText` 和 `CookieNotice` 的文本子层，将导入后实际显示的 Inter 改为可用的 Roboto。正文保持 21.7 px，cookie 保持 20.3 px；Terms 的 Website Contents 仍为粗体。没有改变文案、字号、控件位置或原型连接。同步修改两个 SVG 中相同文本层的字体声明。

- [Privacy 实际 Present 截图](../../evidence/2026-09-28-full-audit/figma-privacy-typography.png)：正文及 cookie 首行右侧完整显示。
- [Terms 实际 Present 截图](../../evidence/2026-09-28-full-audit/figma-terms-typography.png)：正文、粗体小标题及 cookie 首行右侧完整显示。

两张图均是 Figma 重建结果的实际浏览器截图，完整保留 1280×720 视口；画面没有账号栏或私人字段，因此无需遮挡。它们不作为原生应用证据。Roboto 是近似字体，并未识别出原生网页确切字体；底部 cookie 内容仍按初始视口高度截断，关闭和滚动交互仍未实现。

本轮尝试恢复原生观察时 Computer Use 仍返回 Mac 锁屏，因此没有新增原生状态或已观察动作。完整应用仍为 `not_verified`。

后续完成情况：[政策 cookie 独立组件复验](policy-cookie-prototype-walkthrough.md)。以下新增结果不改写上文历史回放；初始同源组件失败和图片缺失均保留。
