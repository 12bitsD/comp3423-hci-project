# Calendar 全局默认视图与筛选循环

2026-10-02。本轮使用Computer Use编辑Figma。原生应用发现明确返回Mac锁定；没有新增原生操作、状态或动作。复现的是已有September28历史样例，私人事件值及日期点模式使用DEMO/省略；不是当前App默认日期或More重入普遍规则。全应用仍 `not_verified`。

## 新增路径

More→Calendar默认全选→打开筛选→取消全选→只选Acad→Apply→公共No event→重开筛选→恢复全选→Apply→默认DEMO。草稿保留尚未更改的已应用背景；重新打开Acad后背景仍为公共No event，不用默认Class示例冒充已应用校历。新增7个576×970画板、19个配置控件，详见 [连接及原配置](../../design/polyulife/calendar-global-connections.json) 与 [来源生成脚本](../../design/scripts/build_calendar_global_filters.py)。

X退出、未改Acad再次Apply、两个Home出口和公共Acad→Notification为action_id:null的原型推广。取消会回固定已应用页，不证明原生取消/提交规则。Apply None、单独Class/Exam/Payment、其它日期/月份/模式、课程省略号及QR未生成推测成功路径。More的独立起点无Home调用栈，不在本批接受范围。

## 图标和定位修复

11恢复默认页时通用Class图标缺失。默认图标以同一公开PNG重新载入；三个草稿初始SVG使用ns1前缀，实际导入卡片图层未含Image Rectangle。修改源稿为xlink前缀，并用同样文字/几何的525×123卡片片段替换后出现图像层；再重传同PNG。记录源命名空间与实际层差异，不把它笼统归为原生App缺陷。卡片值始终合成，字体/几何近似。

UI展开操作曾误触卡片锁定，已对选中项调整并替换卡片；控件连接在卡片外，19条连接保留。首次返回的URI曾为page12:104，随后实际选中图层确认Acad-D为757:526；没有拿页面ID充当画板。

## 以实际保存像素纠正结果

28–31实际PNG仍是Figma初始加载，原拟Monday Calendar标签撤回，没有把未加载时的点击当路径通过。33实际头部确认Tuesday，34–38完成已确认Tuesday的通知交接与滚动位置返回。

42/43、52、54的保存PNG显示Monday Home。工具即时getScreenshot曾显示黑色，我曾据此推断直接Home失败；**该推断已撤回**，没有保存的原型黑屏支持它。临时Back实验47/48保存图仍为Acad，未到Home；最终恢复Close overlay。本輪未取得外部產品說明正文，不據此診斷返回或工具預覽的原因；驗收依據是實際保存的截图字节与可見内容。

## 有限样例

旧Home完成筛选循环及Calendar→Notification→More→Home；默认Calendar直接Home亦保存。Monday重置后，公共校历直接Home的保存图通过，换新Present标签再次保留。Tuesday由头部确认后滚到功能区，再走Calendar公共校历→Notification→More→Home恢复同一功能区。各分段并非独立重置。没有登录、预约、修改日历/资料、真实缴费或扫描QR；仅Figma热点和DEMO内容。

## 实际证据

| UTC | 记录 | PNG |
| --- | --- | --- |
| 2026-10-02T11:10:58.688Z | Legacy Home before new Calendar sample. | [E-CALENDAR-GLOBAL-00](../../evidence/2026-10-02-calendar-global/00-legacy-home.png) |
| 2026-10-02T11:10:58.955Z | Home More entry; caller preserved. | [E-CALENDAR-GLOBAL-01](../../evidence/2026-10-02-calendar-global/01-more.png) |
| 2026-10-02T11:10:59.211Z | More Calendar opens historical Sep28 all-category DEMO sample. | [E-CALENDAR-GLOBAL-02](../../evidence/2026-10-02-calendar-global/02-default.png) |
| 2026-10-02T11:11:36.516Z | Default filter opens all checked draft, default body retained. | [E-CALENDAR-GLOBAL-03](../../evidence/2026-10-02-calendar-global/03-all-draft.png) |
| 2026-10-02T11:11:36.789Z | Apply all restores default historical sample. | [E-CALENDAR-GLOBAL-04](../../evidence/2026-10-02-calendar-global/04-all-apply.png) |
| 2026-10-02T11:11:37.329Z | Select All clears every draft checkbox; applied default body unchanged. | [E-CALENDAR-GLOBAL-05](../../evidence/2026-10-02-calendar-global/05-none-draft.png) |
| 2026-10-02T11:12:27.610Z | Only academic calendar checked before Apply; default body still retained. | [E-CALENDAR-GLOBAL-06](../../evidence/2026-10-02-calendar-global/06-acad-draft.png) |
| 2026-10-02T11:12:27.910Z | Academic Apply changes applied body to recorded Sep28 No event. | [E-CALENDAR-GLOBAL-07](../../evidence/2026-10-02-calendar-global/07-acad-applied.png) |
| 2026-10-02T11:12:28.181Z | Reopen retains academic-only draft and academic background. | [E-CALENDAR-GLOBAL-08](../../evidence/2026-10-02-calendar-global/08-acad-reopen.png) |
| 2026-10-02T11:12:28.487Z | Restore All draft while academic applied background remains. | [E-CALENDAR-GLOBAL-09](../../evidence/2026-10-02-calendar-global/09-all-from-acad.png) |
| 2026-10-02T11:13:23.495Z | Prototype X cancels restored-All draft to academic applied sample; native cancel semantics not established. | [E-CALENDAR-GLOBAL-10](../../evidence/2026-10-02-calendar-global/10-all-draft-cancel.png) |
| 2026-10-02T11:13:24.264Z | Apply All restores default but generic Class icon missing; failure preserved. | [E-CALENDAR-GLOBAL-11](../../evidence/2026-10-02-calendar-global/11-restored-default.png) |
| 2026-10-02T11:13:24.536Z | Default Calendar bottom Notification opens recorded empty notification sample. | [E-CALENDAR-GLOBAL-12](../../evidence/2026-10-02-calendar-global/12-calendar-notification.png) |
| 2026-10-02T11:13:24.804Z | Notification More returns global More sample. | [E-CALENDAR-GLOBAL-13](../../evidence/2026-10-02-calendar-global/13-notification-more.png) |
| 2026-10-02T11:13:25.082Z | More Home restores original caller after full Calendar filter cycle. | [E-CALENDAR-GLOBAL-14](../../evidence/2026-10-02-calendar-global/14-legacy-return.png) |
| 2026-10-02T11:39:44.212Z | Default after same PNG reupload; inspect generic icon recovery. | [E-CALENDAR-GLOBAL-15](../../evidence/2026-10-02-calendar-global/15-default-icon-repair.png) |
| 2026-10-02T11:39:44.479Z | All draft after card-fragment namespace repair and PNG reupload. | [E-CALENDAR-GLOBAL-16](../../evidence/2026-10-02-calendar-global/16-all-card-repair.png) |
| 2026-10-02T11:39:44.721Z | Prototype All X restores applied default sample. | [E-CALENDAR-GLOBAL-17](../../evidence/2026-10-02-calendar-global/17-all-x-return.png) |
| 2026-10-02T11:39:45.232Z | None draft keeps default body; generic image repaired. | [E-CALENDAR-GLOBAL-18](../../evidence/2026-10-02-calendar-global/18-none-card-repair.png) |
| 2026-10-02T11:39:45.506Z | Prototype None X restores applied default; no Apply None executed. | [E-CALENDAR-GLOBAL-19](../../evidence/2026-10-02-calendar-global/19-none-x-return.png) |
| 2026-10-02T11:39:46.292Z | Academic draft keeps default body before Apply, image repaired. | [E-CALENDAR-GLOBAL-20](../../evidence/2026-10-02-calendar-global/20-acad-card-repair.png) |
| 2026-10-02T11:40:38.538Z | Prototype academic draft X restores default applied sample. | [E-CALENDAR-GLOBAL-21](../../evidence/2026-10-02-calendar-global/21-acad-draft-x.png) |
| 2026-10-02T11:40:39.530Z | Academic Apply after repaired draft still reaches public No event sample. | [E-CALENDAR-GLOBAL-22](../../evidence/2026-10-02-calendar-global/22-acad-reapply.png) |
| 2026-10-02T11:40:40.036Z | Prototype Apply on unchanged academic draft restores academic applied sample. | [E-CALENDAR-GLOBAL-23](../../evidence/2026-10-02-calendar-global/23-acad-nochange-apply.png) |
| 2026-10-02T11:40:40.546Z | Prototype X on retained academic draft restores academic applied sample. | [E-CALENDAR-GLOBAL-24](../../evidence/2026-10-02-calendar-global/24-acad-applied-x.png) |
| 2026-10-02T11:40:41.055Z | Second restored-All draft keeps academic background. | [E-CALENDAR-GLOBAL-25](../../evidence/2026-10-02-calendar-global/25-restore-all-second.png) |
| 2026-10-02T11:40:41.319Z | Second Apply All restores default with generic icon after repairs. | [E-CALENDAR-GLOBAL-26](../../evidence/2026-10-02-calendar-global/26-restored-icon-second.png) |
| 2026-10-02T11:40:41.590Z | Default Calendar Home closes to legacy Home caller. | [E-CALENDAR-GLOBAL-27](../../evidence/2026-10-02-calendar-global/27-direct-calendar-home.png) |
| 2026-10-02T11:43:33.529Z | Figma initial loading remains in saved capture; planned caller actions not established. | [E-CALENDAR-GLOBAL-28](../../evidence/2026-10-02-calendar-global/28-monday-start.png) |
| 2026-10-02T11:43:34.032Z | Figma initial loading remains in saved capture; planned caller actions not established. | [E-CALENDAR-GLOBAL-29](../../evidence/2026-10-02-calendar-global/29-monday-default.png) |
| 2026-10-02T11:43:35.024Z | Figma initial loading remains in saved capture; planned caller actions not established. | [E-CALENDAR-GLOBAL-30](../../evidence/2026-10-02-calendar-global/30-monday-acad.png) |
| 2026-10-02T11:43:35.299Z | Figma initial loading remains in saved capture; planned caller actions not established. | [E-CALENDAR-GLOBAL-31](../../evidence/2026-10-02-calendar-global/31-monday-home-return.png) |
| 2026-10-02T11:43:35.872Z | Tuesday caller scrolled before second source test. | [E-CALENDAR-GLOBAL-32](../../evidence/2026-10-02-calendar-global/32-tuesday-scrolled.png) |
| 2026-10-02T11:44:59.207Z | Actual header confirms Tuesday after loading sequence; corrected source label. | [E-CALENDAR-GLOBAL-33](../../evidence/2026-10-02-calendar-global/33-caller-date-recheck.png) |
| 2026-10-02T11:46:35.651Z | Confirmed Tuesday caller scrolled for recorded return test. | [E-CALENDAR-GLOBAL-34](../../evidence/2026-10-02-calendar-global/34-tuesday-baseline.png) |
| 2026-10-02T11:46:36.162Z | Tuesday More enters fixed Sep28 default sample. | [E-CALENDAR-GLOBAL-35](../../evidence/2026-10-02-calendar-global/35-tuesday-default.png) |
| 2026-10-02T11:46:37.151Z | Tuesday caller applies academic sample. | [E-CALENDAR-GLOBAL-36](../../evidence/2026-10-02-calendar-global/36-tuesday-acad.png) |
| 2026-10-02T11:46:37.421Z | Prototype academic Calendar Notification handoff, generalised from default native path. | [E-CALENDAR-GLOBAL-37](../../evidence/2026-10-02-calendar-global/37-acad-notification.png) |
| 2026-10-02T11:46:37.961Z | Notification More Home restores confirmed Tuesday scrolled caller. | [E-CALENDAR-GLOBAL-38](../../evidence/2026-10-02-calendar-global/38-tuesday-return.png) |
| 2026-10-02T11:48:04.795Z | Prototype Restart confirmed Monday caller before final sample. | [E-CALENDAR-GLOBAL-39](../../evidence/2026-10-02-calendar-global/39-monday-reset-confirmed.png) |
| 2026-10-02T11:48:27.336Z | Confirmed Monday More Calendar entry. | [E-CALENDAR-GLOBAL-40](../../evidence/2026-10-02-calendar-global/40-monday-default-confirmed.png) |
| 2026-10-02T11:48:28.305Z | Confirmed Monday academic apply. | [E-CALENDAR-GLOBAL-41](../../evidence/2026-10-02-calendar-global/41-monday-acad-confirmed.png) |
| 2026-10-02T11:48:28.579Z | Saved PNG shows correct Monday Home return; immediate tool-only screenshot was black. No saved black failure at this step. | [E-CALENDAR-GLOBAL-42](../../evidence/2026-10-02-calendar-global/42-monday-return-confirmed.png) |
| 2026-10-02T11:49:19.926Z | Saved PNG shows correct Monday Home return; immediate tool-only screenshot was black. No saved black failure at this step. | [E-CALENDAR-GLOBAL-43](../../evidence/2026-10-02-calendar-global/43-monday-return-settled.png) |
| 2026-10-02T11:57:29.605Z | Confirmed Monday start for direct Home Back experiment. | [E-CALENDAR-GLOBAL-44](../../evidence/2026-10-02-calendar-global/44-back-test-home.png) |
| 2026-10-02T11:57:30.096Z | Default reached from Monday More before direct return experiment. | [E-CALENDAR-GLOBAL-45](../../evidence/2026-10-02-calendar-global/45-back-test-default.png) |
| 2026-10-02T11:57:31.049Z | Academic applied before temporary Back return. | [E-CALENDAR-GLOBAL-46](../../evidence/2026-10-02-calendar-global/46-back-test-acad.png) |
| 2026-10-02T11:57:31.352Z | Temporary Back experiment remains academic view in saved PNG; expected Home not reached. | [E-CALENDAR-GLOBAL-47](../../evidence/2026-10-02-calendar-global/47-back-test-return.png) |
| 2026-10-02T11:59:08.721Z | Temporary Back experiment remains academic view in saved PNG; expected Home not reached. | [E-CALENDAR-GLOBAL-48](../../evidence/2026-10-02-calendar-global/48-back-apex-recheck.png) |
| 2026-10-02T12:03:17.333Z | Fresh Present tab confirms Monday start after final configuration. | [E-CALENDAR-GLOBAL-49](../../evidence/2026-10-02-calendar-global/49-fresh-monday.png) |
| 2026-10-02T12:04:02.726Z | Fresh tab More Calendar default sample. | [E-CALENDAR-GLOBAL-50](../../evidence/2026-10-02-calendar-global/50-fresh-default.png) |
| 2026-10-02T12:04:03.682Z | Fresh tab academic applied before direct Home. | [E-CALENDAR-GLOBAL-51](../../evidence/2026-10-02-calendar-global/51-fresh-acad.png) |
| 2026-10-02T12:04:03.994Z | Saved PNG shows correct Monday Home return; immediate tool-only screenshot was black. No saved black failure at this step. | [E-CALENDAR-GLOBAL-52](../../evidence/2026-10-02-calendar-global/52-fresh-home-return.png) |
| 2026-10-02T12:12:30.066Z | Short path default before direct Home, no filter transitions. | [E-CALENDAR-GLOBAL-53](../../evidence/2026-10-02-calendar-global/53-fresh-default-short.png) |
| 2026-10-02T12:12:30.371Z | Saved PNG shows correct Monday Home return; immediate tool-only screenshot was black. No saved black failure at this step. | [E-CALENDAR-GLOBAL-54](../../evidence/2026-10-02-calendar-global/54-fresh-default-short-home.png) |
| 2026-10-02T12:15:19.342Z | Final default Calendar deliverable. Saved direct Home captures pass; tool-only black previews remain a capture discrepancy. | [E-CALENDAR-GLOBAL-55](../../evidence/2026-10-02-calendar-global/55-delivery-default.png) |

56张实际PNG、1张拼图；24项裁片比较，17项相同，差异完整保留在 [manifest](../../evidence/2026-10-02-calendar-global/manifest.json)。比较不是原生全像素或完整交互验收。公开图只遮盖浏览器账号区域，与原截图逐像素核对；私人值始终DEMO。

当前147映射画板、339控件、101次运行；原生仍135状态/269动作（193 observed/76 not_attempted），完整范围未完成。Mac需要手动解锁才能继续新原生走查；本轮不重复发送解锁要求。
