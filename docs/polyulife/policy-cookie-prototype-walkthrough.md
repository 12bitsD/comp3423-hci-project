# 政策页 cookie 关闭原型复验

2026-09-29（本地时间；下表 UTC）。本轮依据既有原生 Computer Use 证据实现关闭提示；Mac 仍锁屏，没有新增原生观察。完整应用保持 `not_verified`。

## 依据和实现

原生 [Privacy 关闭后](../../evidence/2026-09-28-full-audit/native-menu-192925-privacy-no-cookie-01.png) 和 [Terms 关闭后](../../evidence/2026-09-28-full-audit/native-menu-193003-terms-no-cookie-01.png) 显示提示消失、第二段露出。原生既有走查还确认：关闭 Privacy 后首次进入 Terms，仍出现其自身的提示。仅补录截图中可见的第二段片段；未从网络抓取正文或编造不可见部分。

Figma 保留 Privacy `50:2058` 与 Terms `50:1862` 画板，使用独立的交互组件集：Privacy `93:3`、Terms `102:12`。实例分别为 `98:7`、`95:2`，位置均为43,902.5、尺寸499×100。Close 将各自 `Property 1` 从 Default 切换为 Dismissed，后者隐藏内容；不新增导航历史。完整节点及源稿映射见 [组件元数据](../../design/polyulife/policy-cookie-components.json)。两个关闭状态属于既有画板内部状态，不虚增全屏 Frame 数。

初版共用组件时，关闭 Privacy 会使首次进入 Terms 的提示也消失；重启流程后仍复现。分开组件集后重新从通知页回放，Privacy 关闭、直接返回菜单、Terms 独立提示、关闭、直接返回菜单、最后关闭菜单回通知页均通过。新加2个关闭控件，现为76个全屏映射画板、2个画板内关闭状态、110个控件。该结果不证明连续滚动或完整应用已实现。

## 实际回放（包含失败与暂态）

| UTC | 观察 | 实际 Present 截图 |
| --- | --- | --- |
| 20:28:08 | 通知页打开抽屉 | [E-POLICY-COOKIE-P-01](../../evidence/2026-09-28-full-audit/figma-policy-cookie-drawer-start.png) |
| 20:28:16 | Privacy 提示可见 | [E-POLICY-COOKIE-P-02](../../evidence/2026-09-28-full-audit/figma-policy-cookie-privacy-visible.png) |
| 20:28:25 | Privacy 关闭提示并露出第二段 | [E-POLICY-COOKIE-P-03](../../evidence/2026-09-28-full-audit/figma-policy-cookie-privacy-dismissed.png) |
| 20:28:34 | Privacy Back 回抽屉 | [E-POLICY-COOKIE-P-04](../../evidence/2026-09-28-full-audit/figma-policy-cookie-privacy-back.png) |
| 20:28:43 | 失败：Privacy 关闭后 Terms 提示也消失 | [E-POLICY-COOKIE-P-05](../../evidence/2026-09-28-full-audit/figma-policy-cookie-terms-visible.png) |
| 20:29:17 | Restart 首次点击未生效，仍在 Terms | [E-POLICY-COOKIE-P-06](../../evidence/2026-09-28-full-audit/figma-policy-cookie-restarted.png) |
| 20:29:30 | 按 Enter 激活 Restart，回通知页 | [E-POLICY-COOKIE-P-07](../../evidence/2026-09-28-full-audit/figma-policy-cookie-restart-confirmed.png) |
| 20:29:50 | 重启复验：Privacy 提示可见，但学校标志缺失 | [E-POLICY-COOKIE-P-08](../../evidence/2026-09-28-full-audit/figma-policy-cookie-replay-privacy-visible.png) |
| 20:30:00 | 重启复验：Privacy 关闭，学校标志仍缺失 | [E-POLICY-COOKIE-P-09](../../evidence/2026-09-28-full-audit/figma-policy-cookie-replay-privacy-dismissed.png) |
| 20:30:20 | 重启复验失败：Terms 提示仍被串联关闭，学校标志缺失 | [E-POLICY-COOKIE-P-10](../../evidence/2026-09-28-full-audit/figma-policy-cookie-replay-terms-visible.png) |
| 20:33:52 | 独立组件修复后重启：转场暂空 | [E-POLICY-COOKIE-P-11](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-start.png) |
| 20:34:00 | 加载完成：通知页 | [E-POLICY-COOKIE-P-12](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-start-loaded.png) |
| 20:34:20 | 独立组件：Privacy 提示可见 | [E-POLICY-COOKIE-P-13](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-privacy-visible.png) |
| 20:34:30 | 独立组件：Privacy 关闭成功 | [E-POLICY-COOKIE-P-14](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-privacy-dismissed.png) |
| 20:34:42 | 独立组件：Privacy Back 直接回抽屉 | [E-POLICY-COOKIE-P-15](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-privacy-back.png) |
| 20:34:51 | 独立组件：Terms 提示独立显示 | [E-POLICY-COOKIE-P-16](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-terms-visible.png) |
| 20:35:00 | 独立组件：Terms 关闭成功 | [E-POLICY-COOKIE-P-17](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-terms-dismissed.png) |
| 20:35:08 | 独立组件：Terms Back 直接回抽屉 | [E-POLICY-COOKIE-P-18](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-terms-back.png) |
| 20:35:21 | 关闭抽屉返回通知来源 | [E-POLICY-COOKIE-P-19](../../evidence/2026-09-28-full-audit/figma-policy-cookie-independent-notification-return.png) |
| 20:37:31 | 更新后的流程说明保存并在 Present 读回 | [E-POLICY-COOKIE-P-20](../../evidence/2026-09-28-full-audit/figma-policy-cookie-final-context.png) |

## 验证边界与接力

- `PROTO-POLICY-COOKIE-V1-001` 保留失败；`V2` 的关闭与返回链路通过，整体仍为 partial。
- 重启初版回放时学校标志从 Privacy 和 Terms 消失；后续重载又可见。`D-POLICY-WORDMARK-RENDER` 保持 open，不能以最新一次截图有图判定稳定。
- 字体使用近似 Roboto，第二段位置为手工还原；Terms 片段下移以避免从提示上缘露字。没有声明逐像素一致。
- 原生政策连续滚动及中间正文、Terms 加载态、站内搜索/菜单、重复进入时 cookie 是否保留仍未完成。需要 Mac 解锁后继续取证；原型内重复进入行为不能代替原生结论。
- 原型图均为实际浏览器截图；共享副本只遮盖右上账号头像 `[1017,0,1075,49]`，其余像素保留。无私人业务字段；合成抽屉标明 DEMO。截图与遮盖转换逐像素核对，原始 JPEG 留在被忽略目录。

源码：[生成脚本](../../design/scripts/build_policy_cookie_svg.py)、[Privacy 无提示](../../design/polyulife/privacy-policy-no-cookie.svg)、[Terms 无提示](../../design/polyulife/terms-of-use-no-cookie.svg)。SVG 是设计还原，真实原生截图才是行为依据。Agent 回放不是 Maze 真人测试。
