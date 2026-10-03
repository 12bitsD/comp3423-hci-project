# Room PQ604/PQ604B 历史查询链

2026-10-03 从既有 2026-09-28 原生证据补入七个可编辑状态：首次 Room 入口的 Today28-Sep 空输入；PQ604 输入/无结果；PQ604B 聚焦/无结果；Tue29-Sep 保留房号；Tue29-Sep 清空输入但保留旧无结果。来源对应 `S-EMPTY / S-PQ / S-PQNONE / S-PQB / S-PQBNONE / S-TUE / S-CLEARED`，详见[来源清单](../../design/polyulife/room-pq-query-sources.json)。清空后仍显示旧结果、再次空查询才恢复搜索指引，是既有原生观察事实；本批没有新增原生执行。

首次原生截图为1060×1898，其余为576×970。首次截图按宽度等比缩到576，再裁掉底部约61.37px空白，保留实际三日日期条与没有Search按钮的状态；这个捕获布局差异不能证明异步加载或响应式机制。SVG文字、图标与几何近似，指针、光晕及窗口底部黑色边缘省略。七个画板均是Frame/Group/Text/Vector，未使用整页截图背景。

## 连接与回放

将历史Home `67:820` 和September28 Monday连续Home `67:569` 的Room入口，从后续Tue空查询页 `12:198` 修正到初始Today28页 `846:19`；Tuesday Home原有上下文入口保留。本批新增14条控件：七步查询链与七个Back。完整读回与旧连接修改见[连接清单](../../design/polyulife/room-pq-query-connections.json)。

从这两个Home入口打开Room后，焦点留在画布，按P得到固定PQ604，点击Search，按B得到固定PQ604B，点击Search，选择Tue29，按Backspace清空整个房号，点击Search恢复指引。前三个键盘动作是原型的固定输入代理，不是原生键盘行为，也不是任意文本输入。链路使用Swap overlay；Back使用Close overlay保留调用Home。

三组实际Present运行包含历史Home完整链及已有A→AG206下游、初始页直接Back、连续Monday Home完整链后在清空页Back。保存[23张Present、3张编辑器截图与联系表](../../evidence/2026-10-03-room-pq-query/manifest.json)。逐张检查保存像素，页面日期、房号、聚焦及结果文案与目标状态一致。初始页与清空页两个新增出口实际回放，其余五个新增Back已配置、尚未回放；它们的逐状态原生出口也未确立。Home个人字段全部合成DEMO。

11项重复App裁片比较中4项相等：历史Home两次返回、初始页重开、连续Home清空后返回。两个Home来源之间七个相同Room状态比较均不完全相等；背景采样颜色相同但存在像素差异，原因未隔离，不宣称完全渲染一致。截图与URL读回独立保留，URL可能滞后，判定以实际保存画面为准。比较只证明本批原型样本，不能证明原生或全应用保真。

## 连接限制与下一步

用户解锁后，旧句柄截图仍返回Computer Use timeout；重新发现运行App、通过bundle歧义结果选择当次Wrapper后再连接也超时。清单中的运行状态不证明可观察；超时不证明继续锁屏、崩溃或业务故障。没有重启、退出或更改设置。

本批原生台账数组保持不变，Figma累计187映射画板、402配置控件、129次有限运行。任意输入、其它日期、未回放出口、Calendar主分支整合和未观察功能仍待完成；完整范围保持 `not_verified`。Agent回放不替代真实参与者评价。
