# Room 日期条、周日过渡与时段列表原型

2026-09-29。本轮原生 Computer Use 仍返回 Mac 锁定，因此继续重建既有原生证据，没有新增 App 状态、动作或真人评价。完整应用保持 `not_verified`。

## 已观察来源与实现

以 [Room 原生走查](room-walkthrough.md)的 E-DATEDRAG、E-SUNTRANSITION、E-SUNEMPTY、E-SUNALL、E-SUNSCROLLED 为依据：拖出Sun，选择后先显示新选中日期与旧Tue结果，随后无需再次搜索而自动出现Sun空态；切ALL后全红时段，下滚到约14:30–21:30和下一行局部。截图间隔不代表App响应时长。

新增三个576×970可编辑Frame：过渡325:19、空态327:121、ALL327:202，Y=34500。现有Available12:105保留其它控件，只把日期裁剪组换成DatesHorizontalViewport328:19，位置(30,100)、尺寸516×84，内部658px内容含七个已观察日期，水平滚动范围142px。Sunday画板仍是已观察的右移日期裁片，其反向日期滚动和其它日期选择没有完成。构建参考日期Frame327:387不计为全屏状态。

Sunday ALL的SlotsScrollContent327:278位于(26,426)，尺寸524×544，内部940px，配置Vertical并裁剪。26个半小时时段标签从08:30到21:30，另保留截图最下方下一行的22px上沿；没有补造未见标签。范围396px由已观察视口推导，**不是已验证的真实列表末端**。原生滚动指示条尚未复现。两个滚动终点S-DATEDRAG与S-SUNSCROLLED登记为现有画板的滚动状态，不另外造全屏Frame。

新增7个连接：Sun→过渡→自动空态→ALL；ALL→Available，以及三个新画板的Back。后四项是原型推断，action_id为空：原生只观察过从地图回Sun ALL再回Home，不能冒称已独立观察每个新出口或反向筛选。过渡采用Figma默认800ms演示延时，不是网络模拟或测量值。

## 实际回放结果

24张Present截图确认Tuesday Home→Room→A→AG206→Available→拖日期→Sun→旧结果过渡→自动空态→ALL→列表中间/已观察末段→上滚→空态→Home。另复测Sunday ALL直接Back，以及过渡期间立即Back；最后一次关闭后过了演示定时器，仍停在Home，没有再次打开Room。

三个新出口和定时器后Home均与初始Home应用区域(461,60,818,661)逐像素一致；ALL列表上滚回原视口、反向筛选回空态也分别与各自基线一致。日期反向拖回起点时可见日期恢复，但与首次Available截图在日期区域内存在像素差异，两个不等比较保留，未推断原因。用反向拖动后的稳定视口为基线，Preview加载/打开/X返回后逐像素一致。合计9项比较，7项相等、2项日期基线差异；不把所有比较写为通过。

重复进入Available时，原型保留日期条上次滚动位置。原生重新进入的滚动重置规则尚未观察。两个日期拖动即时截图与稳定截图分开，避免把过渡位置当作稳定布局。

## 剩余范围与接力

Room自由输入/清空/搜索、其它日期/范围、Sunday日期条反向滚动、Sunday Preview、地图与缩放、真实时段末端、其它来源/独立起点及完整视觉验收仍待完成。已观察AG206地图下一批可继续重建，但Google Maps跳转、平移有效动作和缩放边界仍需原生观察。原型固定历史数据，不提供实时可用性。Agent回放与人类Maze评价分别记录。

[SVG生成器](../../design/scripts/build_room_sunday_svg.py) · [节点、连接读回、旧Available映射与像素比较](../../design/polyulife/room-sunday-connections.json)

| 步骤 | 结果 | 证据 |
| --- | --- | --- |
| 01-home-baseline | recorded | [E-ROOM-SUNDAY-P-01](../../evidence/2026-09-28-full-audit/room-sunday-proto-01-home-baseline.png) |
| 02-available-before | recorded | [E-ROOM-SUNDAY-P-02](../../evidence/2026-09-28-full-audit/room-sunday-proto-02-available-before.png) |
| 03-date-drag | immediate_drag_view_before_settling | [E-ROOM-SUNDAY-P-03](../../evidence/2026-09-28-full-audit/room-sunday-proto-03-date-drag.png) |
| 04-date-drag-settled | drag_settled_at_observed_sunday_position | [E-ROOM-SUNDAY-P-04](../../evidence/2026-09-28-full-audit/room-sunday-proto-04-date-drag-settled.png) |
| 05-sunday-transition | sun_selected_old_tuesday_result_visible | [E-ROOM-SUNDAY-P-05](../../evidence/2026-09-28-full-audit/room-sunday-proto-05-sunday-transition.png) |
| 06-sunday-empty | sunday_empty_result_updated_without_search | [E-ROOM-SUNDAY-P-06](../../evidence/2026-09-28-full-audit/room-sunday-proto-06-sunday-empty.png) |
| 07-sunday-all-top | recorded | [E-ROOM-SUNDAY-P-07](../../evidence/2026-09-28-full-audit/room-sunday-proto-07-sunday-all-top.png) |
| 08-list-intermediate | recorded | [E-ROOM-SUNDAY-P-08](../../evidence/2026-09-28-full-audit/room-sunday-proto-08-list-intermediate.png) |
| 09-list-observed-bottom | recorded | [E-ROOM-SUNDAY-P-09](../../evidence/2026-09-28-full-audit/room-sunday-proto-09-list-observed-bottom.png) |
| 10-list-top-return | original_list_or_empty_view_pixel_equal | [E-ROOM-SUNDAY-P-10](../../evidence/2026-09-28-full-audit/room-sunday-proto-10-list-top-return.png) |
| 11-filter-available-return | original_list_or_empty_view_pixel_equal | [E-ROOM-SUNDAY-P-11](../../evidence/2026-09-28-full-audit/room-sunday-proto-11-filter-available-return.png) |
| 12-empty-home-return | home_return_pixel_equal | [E-ROOM-SUNDAY-P-12](../../evidence/2026-09-28-full-audit/room-sunday-proto-12-empty-home-return.png) |
| 13-available-reentry | reentry_retains_date_scroll_position_native_reentry_unverified | [E-ROOM-SUNDAY-P-13](../../evidence/2026-09-28-full-audit/room-sunday-proto-13-available-reentry.png) |
| 14-date-reverse-immediate | recorded | [E-ROOM-SUNDAY-P-14](../../evidence/2026-09-28-full-audit/room-sunday-proto-14-date-reverse-immediate.png) |
| 15-date-reverse-settled | dates_visually_return_to_start_pixels_differ_from_first_baseline | [E-ROOM-SUNDAY-P-15](../../evidence/2026-09-28-full-audit/room-sunday-proto-15-date-reverse-settled.png) |
| 16-preview-regression-loading | recorded | [E-ROOM-SUNDAY-P-16](../../evidence/2026-09-28-full-audit/room-sunday-proto-16-preview-regression-loading.png) |
| 17-preview-regression-loaded | recorded | [E-ROOM-SUNDAY-P-17](../../evidence/2026-09-28-full-audit/room-sunday-proto-17-preview-regression-loaded.png) |
| 18-preview-return-date-top | preview_return_pixel_equal_to_stable_reversed_date_baseline | [E-ROOM-SUNDAY-P-18](../../evidence/2026-09-28-full-audit/room-sunday-proto-18-preview-return-date-top.png) |
| 19-second-transition | sun_selected_old_tuesday_result_visible | [E-ROOM-SUNDAY-P-19](../../evidence/2026-09-28-full-audit/room-sunday-proto-19-second-transition.png) |
| 20-second-list-scrolled | recorded | [E-ROOM-SUNDAY-P-20](../../evidence/2026-09-28-full-audit/room-sunday-proto-20-second-list-scrolled.png) |
| 21-list-home-return | home_return_pixel_equal | [E-ROOM-SUNDAY-P-21](../../evidence/2026-09-28-full-audit/room-sunday-proto-21-list-home-return.png) |
| 22-transition-before-close | sun_selected_old_tuesday_result_visible | [E-ROOM-SUNDAY-P-22](../../evidence/2026-09-28-full-audit/room-sunday-proto-22-transition-before-close.png) |
| 23-transition-home-return | home_return_pixel_equal | [E-ROOM-SUNDAY-P-23](../../evidence/2026-09-28-full-audit/room-sunday-proto-23-transition-home-return.png) |
| 24-post-timer-home | home_remains_after_demo_timer_pixel_equal | [E-ROOM-SUNDAY-P-24](../../evidence/2026-09-28-full-audit/room-sunday-proto-24-post-timer-home.png) |
