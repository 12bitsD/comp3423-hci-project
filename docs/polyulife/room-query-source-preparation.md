# Room 查询状态：源码与 Figma 导入检查点

2026-09-30。以[9月29日原生复查](room-recheck-20260929.md)为依据，六个576×970可编辑SVG已通过Computer Use导入[Figma文件](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)的`01 · Observed UI`页面（12:104）。Figma编辑器已读回Frame、文字/矢量图层和四条原型连接；独立Present回放尚未成功，因此这批仍不计入正式覆盖台账的已验证画板、控件或运行数量。

| 源码 | 真实状态与证据 | 需要表达的行为 |
| --- | --- | --- |
| [AG206联想](../../design/polyulife/room-query-ag206-suggestion.svg) | S-ROOM-QUERY-AG206 / E-ROOM-RECHECK-02 | 完整房间号、一个联想项及原始提示并存 |
| [修改输入后旧结果](../../design/polyulife/room-query-dirty-results.svg) | S-ROOM-QUERY-DIRTY / E-ROOM-RECHECK-12 | ZZZZ9999与旧AG206列表并存，Sunday/ALL及已观察滚动位置保留 |
| [无匹配结果](../../design/polyulife/room-query-no-result.svg) | S-ROOM-QUERY-NONE / E-ROOM-RECHECK-13 | 点击搜索后出现No room found |
| [无匹配结果聚焦](../../design/polyulife/room-query-focused-no-result.svg) | S-ROOM-QUERY-NONE / E-ROOM-RECHECK-14 | 点击输入框，查询内容保持、光标出现；清空图标形状参照相邻聚焦态推断 |
| [清空后的旧空态](../../design/polyulife/room-query-cleared-stale.svg) | S-CLEARED的Sunday上下文 / E-ROOM-RECHECK-15 | 输入为空、光标可见，No room found尚未消失 |
| [空查询恢复提示](../../design/polyulife/room-query-empty-sunday.svg) | S-EMPTYQUERY的Sunday上下文 / E-ROOM-RECHECK-16 | 再次搜索后恢复初始提示，Sunday仍选中 |

本批保留9月29日实际日期条：Today29-Sep、Wed30-Sep至Mon05-Oct。不会把历史9月28日原型的日期含义覆盖掉；导入时须用清楚的日期/上下文别名。后两张复用已有原生状态ID，不制造新的观察计数。

源码保留独立Header、SearchButton、ClearInput、AG206Suggestion、NoRoomFound等图层。dirty-results列表是固定已观察偏移，不提供连续滚动或实时可用性。输入目前是静态文本，尚未实现任意字符串或真实键盘；Figma的点击跳转只是观察到的查询路径代理，不能当作原生输入实现。

六个实际Frame节点分别为AG206联想`381:265`、修改后旧结果`381:72`、无匹配`381:19`、聚焦无匹配`383:19`、清空后旧空态`381:327`、空查询恢复`381:383`。编辑器读回四条On click → Navigate to：旧结果SearchButton`381:113`→无匹配、无匹配RoomInput`381:60`→聚焦、聚焦ClearInput`383:67`→清空后旧空态、清空后SearchButton`381:369`→空查询恢复。对应E-ROOM-RECHECK-13至16。Present仍从旧默认Flow启动，未能进入这条孤立路径；未建立可回放起点前，不声称交互测试通过。

本地使用resvg-py0.5.0渲染并逐列与截图对照：最初五张的结构、日期、查询/空态区别和列表行位置已检查；新增聚焦无匹配源码也已单独渲染检查。字体宽度/字重、图标、滚动指示条仍有差异，未做Figma视觉验收。下图上排为最初五张源码渲染，下排为真实截图；光标光晕和窗口输入边缘未复制进源码。

![源码与真实截图对照](../../design/polyulife/assets/room-query-source-comparison.png)

## 接力步骤

1. 为孤立的查询路径建立可回放起点，在Present中逐步验证四条连接和视觉状态。
2. AG206联想属于Today上下文。选择结果不能直接跳到Sunday结果；需准备对应Today状态或保留为单独待连路径。
3. 继续实现实际输入和其他查询分支；ZZZZ9999样例不代表全部异常输入覆盖。
4. 实际Present回放和视觉比较后，才更新正式覆盖台账。地图WIP另见[地图检查点](room-map-work-in-progress.md)。

[生成器](../../design/scripts/build_room_query_svg.py) · [来源、哈希及本地渲染记录](../../design/polyulife/room-query-sources.json)
