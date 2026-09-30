# Calendar 周选择器与返回 — 2026-09-30

本批通过 Computer Use 接入两张画板和四条控件，保存两组原型运行。累计118张映射画板、274条控件、53次运行；全应用仍为 `not_verified`。

## 原生观察与复现范围

来源是2026-09-28的既有记录：E-CALENDAR-WEEK-PICKER-HEADER显示Week4/5/6和三个学期；E-CALENDAR-WEEK-WHEEL-SCROLLED显示滚轮13、标题仍Week5；E-CALENDAR-WEEK-COLLAPSED显示收起后仍Week5。A-CALENDAR-WEEK-SELECT点击下一周未建立成功选择，不可写成Week6已应用。本批按当前发现的Wrapper运行路径连接仍超时，没有重启或新增原生执行。

新增[选择器558:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=558-19)和[滚轮558:126](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=558-126)，尺寸576×970，位置0/700,50500，Clip content开启。标题、学期、滚轮数字、日期及图形可编辑，字体和图标近似，原生指针/阴影省略。源图只公开上方576×384；下方课表是原有合成DEMO移下186px并裁切，不是观察到的私人课表。[生成脚本](../../design/scripts/build_calendar_week_picker_svg.py)和[来源哈希](../../design/polyulife/calendar-week-picker-assets.json)可复查。

## 连接

Week视图70:973的WeekSelector70:977：On click Open overlay到558:19，对应A-CALENDAR-WEEK-PICKER。选择器WeekWheelInputProxy558:37：On drag Swap overlay到558:126，代理原生A-CALENDAR-WEEK-SCROLL-ATTEMPT的向下滚动。Figma默认Smart animate300ms仅是原型表现，拖动任何方向都可触发；不是连续滚轮、方向限制、完整周范围或原生时序。

滚轮状态WeekSelector558:133：Close overlay返回原来的70:973，对应A-CALENDAR-WEEK-COLLAPSE。初始选择器WeekSelector558:26也可Close overlay，是提前收起的推广恢复路径，action_id为null。已有Week视图Home历史返回保留，未新增此连接。详见[连接清单](../../design/polyulife/calendar-week-picker-connections.json)。

## 实际回放与差异

07–13从Week5独立起点展开、点击Week6、拖动到滚轮13、收起及重入。Week6没有配置，点击只显示Figma交互提示，未生成不同周结果；这是原型限制，不能代替原生选择结论。10的实际留存文件已显示稳定滚轮13，不把立即工具画面中的渐隐旧Week6当作最终内容。

14–20从Tuesday Home底部Calendar进入，展开、拖动、收起、Home返回，再次进入滚轮13。Week标题和日期未改变，Home内容、Tuesday日期和导航保留，但底部图片从14的可见变成19的空白。这是实际保存的Figma视觉失败，原因未确定，未宣称整条路线视觉通过。

六项同原型裁片比较四项相等：收起Week视图、提前收起、选择器重入、Home来源Week返回；两项差异保留：Week6交互提示和Home底部缺图。比较不证明原生像素保真或真人可用性。20个真实截图及contact sheet见[公开清单](../../evidence/2026-09-30-calendar-week-picker/manifest.json)。

## 尚未验证

不同周成功应用、学期更改、连续滚轮和边界、周选择器内月视图切换、课表详情及完整课表滚动均未实现或验证。原生A-CALENDAR-WEEK-APPLY-RECHECK保持not_attempted。还需恢复原生观察并验证Home图片稳定性；Agent回放不替代真人Maze测试。
