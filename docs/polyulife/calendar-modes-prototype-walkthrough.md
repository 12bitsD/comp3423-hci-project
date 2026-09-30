# Calendar 模式切换、调用者与漏接修复 — 2026-09-30

本批通过 Computer Use 补入三个公共日历上下文画板和八条控件，保存三组原型运行。累计121个映射画板、282条控件、56次运行；全应用仍 `not_verified`。上一轮周选择器已有画板，本批没有重做。

## 原生证据和状态

既有A-CALENDAR-VIEW-MONTH在周选择器内进入September26月视图（E-CALENDAR-MONTH-RETURN）；A-CALENDAR-VIEW-EVENTS进入公共事件列表（E-CALENDAR-EVENTS）；A-CALENDAR-SHOW-HISTORY显示历史（E-CALENDAR-HISTORY）；A-CALENDAR-VIEW-WEEK回Week5（E-CALENDAR-TRACE）。这些来自2026-09-28观察，不是本批新的原生执行。最近按当前发现的Wrapper连接超时，本批未重启应用或增加原生动作。

实际画板为[月视图573:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=573-19)、[事件573:174](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=573-174)、[历史573:293](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=573-293)。尺寸576×970、Clip content开启，位置0/700/1400,52000。它们从原有公开SVG复制，文字/日期/图标为可编辑近似；[生成脚本](../../design/scripts/build_calendar_mode_context_svg.py)和[哈希](../../design/polyulife/calendar-mode-context-assets.json)可复查。September26和公共事件保持历史固定样例，不是当前数据。周视图和Home私人课表仍为合成DEMO。

## 同层模式循环

周选择器558:30的MonthView Swap overlay到月视图573:19；月视图ViewMode573:28 Swap到事件573:174；事件HistoryToggle573:178 Swap到历史573:293；历史ViewMode573:300 Close overlay回原来的Week5根70:973。均On click，三个Swap使用Instant。四条分别对应上述原生动作。这一层用来保留Home进入Week前的历史上下文；只证明所回放样例，没有宣称原生内部也采用overlay。

月/事件/历史的NavHome573:157/573:276/573:401设置Back，分别在Monday和Tuesday调用者中测试。它们是原型恢复出口，action_id为null；不能把这些原型返回写成已观察的原生跨模式Home结果。通过原有Week NavHome的Back可返回调用者。[连接清单](../../design/polyulife/calendar-mode-context-connections.json)区分观察动作和推广出口。

## 实际路线、失败与修复

11–24从Tuesday Home底部Calendar进入Week、展开、转月视图、事件、历史、回Week、回Home，并测试三个模式直接Home出口。12与17周视图相等，Home日期/内容保留；11到18的底部图片变为空白。20/22/24与已空白的18相等，只证明返回一致，不证明图片恢复。

25–30第一次Monday路线失败：底部Calendar入口漏接，26–29实际仍停在Monday Home。文件名按原始尝试保留，记录已改成真实Home状态；后续连点无效，不算完成模式切换，也不能通过开始/结束Home相同宣称返回成功。

在实际Monday NavCalendar67:678新增On click Navigate to Week70:973，31保存配置；它推广了已观察Tuesday A-HOME-EP002到Monday上下文，action_id仍null。重载后32–45再次回放：33确实进入Week，35/36/37为月/事件/历史，38回Week，39回Monday；40–45三个直接出口均回Monday。原始失败不删除。32到39底部图片仍丢失，未虚称整体视觉通过。标题图层定位时第一次点中了Events标题，发现没有HistoryToggle后改到Show History文字，未在错误图层写入动作。

十二项原型裁片比较十项相等、两项不等（Monday、Tuesday底部图片丢失），详见[45个截图与清单](../../evidence/2026-09-30-calendar-modes/manifest.json)。这些是原型内部一致性检查，不是原生像素保真、实时数据、真人测试或全覆盖证明。

## 剩余范围

新上下文中的日期切换、筛选、事件详情、连续列表滚动和Hide History未接入；原有独立日历样例保持原配置。周根/滚轮13直接转月视图、其它周/学期/日期/滤镜组合、More调用者及长会话行为未验证。原生不同周成功应用、Home图片稳定性与完整可编辑保真仍待补，课程Maze评估需要真人完成。
