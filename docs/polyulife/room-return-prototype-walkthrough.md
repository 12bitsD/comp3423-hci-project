# Room 样例路径保留 Home 来源

2026-09-29。原生 Computer Use 仍为 Mac locked。本批只有 Figma 修改与回放；原生保持 121 状态 / 265 动作（179 observed、86 not_attempted），完整应用保持 `not_verified`。

## 修改及验证

此前 Room 初始 Back 只证明直接往返，查询与筛选使用 Navigate to，内部路径不能稳定退出到原 Home。现将三个 Home 入口改为 Open overlay，A 键样例、AG206 建议及两项筛选切换改为 Swap overlay，初始 Back 改为 Close overlay，并给建议、All、Available 三个页面补返回。共更新 8 个已有控件，新增 3 个，当前 192 个配置控件。

Monday 和 legacy Home 分别验证 Home→Room→键 A→AG206→Available→All→Back；Tuesday 分别从 Empty、Suggestion、All、Available 四个状态退出。六次返回与各自 Home 基线应用区域 `(581,60,938,661)` 像素完全一致。Tuesday 日期来源在进入前确认是29/TUE。

## 原生依据与未完成项

[原生 Room 记录](room-walkthrough.md)支持模块返回 Home，但本次新增的三个确切来源未逐一原生观察，属于原型推广，action_id=null。原有 Tuesday Available→All 曾错误关联 Sunday 的 A-ROOM-SUN-ALL；当前关联纠正为 null、保留历史配置，依然不代表 Sunday 流程完成。Home Monday 进入的是固定 Tuesday 查询样例，未实现动态日期继承。

键 A 仍是固定样例，非自由输入。日期切换、清空/搜索、其它房间、Preview、槽位、完整列表及地图尚未补齐。Food 内部绕行也仍未完成。

独立 Room 起点没有 Home 调用层：选中侧栏后直接按 A 没有变化；点击应用区域取得焦点后按 A 可以进入建议及结果。因此第一次无变化是焦点准备问题。独立 Available 的 Back 实跑无效果，记录为 `D-ROOM-STANDALONE-EXIT`，需要从 Home 进入才能使用本次验证的退出路径。

legacy 起点刚切换时有一张黑屏截图，随后渲染完成才保存有效基线并执行路径；黑屏与焦点准备记录均保留，不计为导航通过。四份流程说明已更新，独立 Room 说明在 Present 重载后读回。

## 配置和证据

[控件配置与六项像素比较](../../design/polyulife/room-return-connections.json)。27 张实际 Present 截图遮盖账号区域，公开 PNG 转码与遮盖逐像素核对。它们不是原生观察或 Maze 真人结果。

| 步骤 | 结果 | 证据 |
| --- | --- | --- |
| Monday Home feature-area baseline | recorded | [E-ROOM-STACK-P-01](../../evidence/2026-09-28-full-audit/room-stack-mon-baseline.png) |
| Home Monday opens Room empty sample | recorded | [E-ROOM-STACK-P-02](../../evidence/2026-09-28-full-audit/room-stack-mon-empty.png) |
| Key A sample trigger while Room is open from Home | recorded | [E-ROOM-STACK-P-03](../../evidence/2026-09-28-full-audit/room-stack-mon-suggestion.png) |
| Select AG206 suggestion | recorded | [E-ROOM-STACK-P-04](../../evidence/2026-09-28-full-audit/room-stack-mon-all.png) |
| Available filter after AG206 query | recorded | [E-ROOM-STACK-P-05](../../evidence/2026-09-28-full-audit/room-stack-mon-available.png) |
| All filter uses existing Tuesday sample; native Sunday action mismatch retained | recorded | [E-ROOM-STACK-P-06](../../evidence/2026-09-28-full-audit/room-stack-mon-all-return.png) |
| After query and All/Available detour, Back restores Monday Home | return_pixel_equal | [E-ROOM-STACK-P-07](../../evidence/2026-09-28-full-audit/room-stack-mon-full-home-return.png) |
| Confirmed Tuesday 29 home | recorded | [E-ROOM-STACK-P-08](../../evidence/2026-09-28-full-audit/room-stack-tue-top.png) |
| Tuesday feature-area baseline | recorded | [E-ROOM-STACK-P-09](../../evidence/2026-09-28-full-audit/room-stack-tue-baseline.png) |
| Tuesday direct Room entry | recorded | [E-ROOM-STACK-P-10](../../evidence/2026-09-28-full-audit/room-stack-tue-empty.png) |
| Empty Room Back restores Tuesday | return_pixel_equal | [E-ROOM-STACK-P-11](../../evidence/2026-09-28-full-audit/room-stack-tue-empty-home-return.png) |
| Tuesday sample suggestion before exit | recorded | [E-ROOM-STACK-P-12](../../evidence/2026-09-28-full-audit/room-stack-tue-suggestion.png) |
| Suggestion Back restores Tuesday | return_pixel_equal | [E-ROOM-STACK-P-13](../../evidence/2026-09-28-full-audit/room-stack-tue-suggest-home-return.png) |
| Tuesday All result before exit | recorded | [E-ROOM-STACK-P-14](../../evidence/2026-09-28-full-audit/room-stack-tue-all.png) |
| All Back restores Tuesday | return_pixel_equal | [E-ROOM-STACK-P-15](../../evidence/2026-09-28-full-audit/room-stack-tue-all-home-return.png) |
| Tuesday Available before exit | recorded | [E-ROOM-STACK-P-16](../../evidence/2026-09-28-full-audit/room-stack-tue-available.png) |
| Available Back restores Tuesday | return_pixel_equal | [E-ROOM-STACK-P-17](../../evidence/2026-09-28-full-audit/room-stack-tue-available-home-return.png) |
| Legacy flow selected but canvas still black; not used as baseline | not_yet_rendered | [E-ROOM-STACK-P-18](../../evidence/2026-09-28-full-audit/room-stack-legacy-baseline.png) |
| Legacy Home visibly rendered before testing | recorded | [E-ROOM-STACK-P-19](../../evidence/2026-09-28-full-audit/room-stack-legacy-ready-baseline.png) |
| Legacy Home chain reaches Available | recorded | [E-ROOM-STACK-P-20](../../evidence/2026-09-28-full-audit/room-stack-legacy-available.png) |
| Legacy Home chain returns to All | recorded | [E-ROOM-STACK-P-21](../../evidence/2026-09-28-full-audit/room-stack-legacy-all.png) |
| Room internal detour returns original legacy Home | return_pixel_equal | [E-ROOM-STACK-P-22](../../evidence/2026-09-28-full-audit/room-stack-legacy-full-home-return.png) |
| Standalone key A while sidebar link focused left Room empty | no_change | [E-ROOM-STACK-P-23](../../evidence/2026-09-28-full-audit/room-stack-standalone-key-a.png) |
| After canvas focus, standalone key A displays suggestion | recorded | [E-ROOM-STACK-P-24](../../evidence/2026-09-28-full-audit/room-stack-standalone-suggestion-focused.png) |
| Standalone sample reaches Available | recorded | [E-ROOM-STACK-P-25](../../evidence/2026-09-28-full-audit/room-stack-standalone-available.png) |
| Standalone Available Back has no effect; no Home caller exists | standalone_exit_failed | [E-ROOM-STACK-P-26](../../evidence/2026-09-28-full-audit/room-stack-standalone-close-empty.png) |
| Room standalone description persisted after reload | recorded | [E-ROOM-STACK-P-27](../../evidence/2026-09-28-full-audit/room-stack-standalone-description.png) |
