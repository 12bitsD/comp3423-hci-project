# Room 原生补查：地图返回、无匹配查询与清空

2026-09-29，真实已安装PolyULife通过Computer Use重新可读；未改登录、资料或设置，未提交预约。16张公开图均从576×1082窗口截图裁除顶部112px得到576×970应用内容；原始AX和截图留在忽略目录。实际查询使用AX setValue，不能等同真实逐字键入体验。

## 确认的行为

- Today ALL直接选择Sun04-Oct后保持ALL，并自动移动日期条，使Sun和Mon可见。
- Sunday ALL下滚至14:30开头的完整行后，进入AG206地图、AX Increment一次、Decrement一次、Back；日期、ALL、列表滚动位置保留。两块排除指针区域的像素比较均不完全相同，故只按可见标签与裁剪位置确认滚动保持，不宣称逐像素一致。
- 再下滚仍停在同一视口，21:00–21:30下一行仍被裁切；未证明列表真正末端。
- 将输入改为ZZZZ9999后，旧AG206结果继续显示，直到点击搜索才变成No room found。
- 清空控件成功清除文本后，No room found仍保留；再次点击搜索才恢复Find an available classroom提示。与历史清空行为一致，本次补充Sunday上下文。

输入/选择/清空有一次点击无变化或焦点错位，失败尝试保留。未将这些工具行为判为App缺陷。完整AG206输入稍后出现联想；截图记录的是已加载联想，不能以更早AX断言联想不存在。地图加载徽标只在实时查看时出现，保存的地图截图已经加载完成。

## 对Figma的影响与未完成项

地图返回应保留列表滚动；编辑输入、无匹配结果、清空后的旧空态、重新搜索的初始提示需要分别表达。已有地图六个控件完成配置，Present尚未通过；查询新增状态尚未绘制。此轮3个新状态只是输入内容/结果的已观察状态，不是完整输入等价类覆盖。

原生台账现为124状态、265动作，其中181 observed /84 not_attempted；observed包含无变化的尝试，不能视作成功计数。12次原生会话。正式Figma映射仍86帧、217控件、32次运行，另有地图WIP3帧/6控件未并入。完整应用仍not_verified。

[机器可读步骤与比较](room-recheck-20260929.json) · [地图接力](room-map-work-in-progress.md)

| 步骤 | 实际结果 | 截图 |
| --- | --- | --- |
| 01 | Room reopened from Home with Today29-Sep and empty query. | [E-ROOM-RECHECK-01](../../evidence/2026-09-28-full-audit/room-recheck-01-empty.png) |
| 02 | Plain click/typeText had no visible effect; AX setValue AG206 succeeded. Saved screenshot shows AG206 suggestion and initial instructions. Input method difference retained. | [E-ROOM-RECHECK-02](../../evidence/2026-09-28-full-audit/room-recheck-02-query-filled.png) |
| 03 | AX suggestion click did not dismiss popup; coordinate correction selected AG206. Saved screenshot has already settled to ALL results, not a loading frame. | [E-ROOM-RECHECK-03](../../evidence/2026-09-28-full-audit/room-recheck-03-selection.png) |
| 04 | Follow-up stable ALL capture, not an additional suggestion-click execution. | [E-ROOM-RECHECK-04](../../evidence/2026-09-28-full-audit/room-recheck-04-today-all.png) |
| 05 | Direct Today ALL→Sun keeps ALL. Date strip automatically shifts to show Sun and Mon. | [E-ROOM-RECHECK-05](../../evidence/2026-09-28-full-audit/room-recheck-05-sunday-all.png) |
| 06 | List scrolled: clipped preceding row then14:30 onward, final visible complete label21:00–21:30, next row clipped. | [E-ROOM-RECHECK-06](../../evidence/2026-09-28-full-audit/room-recheck-06-list-before-map.png) |
| 07 | Initial UI briefly showed logo loading; saved screenshot is settled map, not proof of the loading layout. | [E-ROOM-RECHECK-07](../../evidence/2026-09-28-full-audit/room-recheck-07-map-opening.png) |
| 08 | Native AX slider Increment once; zoomed campus map visible. | [E-ROOM-RECHECK-08](../../evidence/2026-09-28-full-audit/room-recheck-08-map-increment.png) |
| 09 | Native AX slider Decrement once; campus map visible. | [E-ROOM-RECHECK-09](../../evidence/2026-09-28-full-audit/room-recheck-09-map-decrement.png) |
| 10 | Back preserves Sunday, ALL and list position with the same14:30 first complete row. This scoped native return now confirms scroll retention. | [E-ROOM-RECHECK-10](../../evidence/2026-09-28-full-audit/room-recheck-10-map-return.png) |
| 11 | Additional downward scroll made no visible list progress. Last row remains clipped; true list end still unverified. | [E-ROOM-RECHECK-11](../../evidence/2026-09-28-full-audit/room-recheck-11-list-further-down.png) |
| 12 | AX setValue ZZZZ9999 changes input while old AG206 Sunday ALL scrolled results remain. | [E-ROOM-RECHECK-12](../../evidence/2026-09-28-full-audit/room-recheck-12-unmatched-query.png) |
| 13 | Explicit Search with ZZZZ9999 replaces old result with No room found / Please search another room. | [E-ROOM-RECHECK-13](../../evidence/2026-09-28-full-audit/room-recheck-13-unmatched-search.png) |
| 14 | Coordinate clear attempt after dismissing text context menu leaves query unchanged; targeting/focus failure retained. | [E-ROOM-RECHECK-14](../../evidence/2026-09-28-full-audit/room-recheck-14-clear-query.png) |
| 15 | Fresh AX clear element click succeeds: field empty; prior No room found body remains; Sun stays selected. | [E-ROOM-RECHECK-15](../../evidence/2026-09-28-full-audit/room-recheck-15-cleared-stale-empty.png) |
| 16 | Search with empty input restores Find an available classroom / Enter room number to begin search; Sun remains selected. | [E-ROOM-RECHECK-16](../../evidence/2026-09-28-full-audit/room-recheck-16-empty-search.png) |
