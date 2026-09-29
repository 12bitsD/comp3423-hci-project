# AG206 地图复现检查点（尚未回放）

2026-09-29。三个地图 Frame 已导入 Figma；本批仍是 **work in progress**，未计入 `coverage.json` 的正式映射和原型运行统计。完整应用仍为 `not_verified`。本批没有新增原生观察或真人评估。

## 依据与实现

| 原生状态 / 证据 | Figma 节点 | 源码 |
| --- | --- | --- |
| S-MAP / E-MAP | [338:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=338-19) | [initial](../../design/polyulife/room-map-initial.svg) |
| S-MAPZOOM / E-MAPZOOM | [339:30](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=339-30) | [zoomed](../../design/polyulife/room-map-zoomed.svg) |
| S-MAPOUT / E-MAPOUT | [339:41](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=339-41) | [out](../../design/polyulife/room-map-out.svg) |

每个画板576×970，Y=36000，X依次0/700/1400。标题与Back为可编辑图层，底图从公开原生截图裁取(0,100,576,970)，保留原截图中的光标与光晕，不补造被遮像素。地图地理、标签及标记仍为栅格图片，不是实时地图。

已配置：339:47（缩小画面的Back）Close overlay，对应A-ROOM-MAP-BACK；339:36（放大画面的Back）Close overlay，为原型推断；339:30的Key(↓) Swap overlay至339:41，对应A-ROOM-MAP-DECREMENT的结果。最后一项已在重新打开的编辑器中读回确认。↓只是原型输入代理，原生执行的是AX Slider Decrement，未观察原生方向键行为。

放大与缩小画面的图片此前已通过上传对话框重传。初始画面的额外重传尝试因点击定位与file chooser超时没有完成；SVG导入的底图在编辑器可见，仍需Present确认。浏览器出现截图/点击坐标不一致，重新打开后台标签后可以读回配置，但未完成路径回放。没有将工具异常归为App缺陷。

![编辑器中的三个地图画面及缩小连接](../../design/polyulife/assets/room-map-editor-checkpoint.png)

## 2026-09-29 后续配置与原生复查

原生连接恢复后完成[16张截图的复查](room-recheck-20260929.md)：已确认地图缩放后Back保留Sunday ALL与列表滚动位置。此结论只限记录的路径，不等于所有入口都保留。

另补齐三个Figma连接：338:19的↑ Swap overlay→339:30；初始Back338:25 Close overlay（推断出口）；Sunday ALL的Location327:251 Open overlay→338:19。现有地图共六个控件，均有编辑器读回；339:30临时Flow 3已移除。↑/↓仍是原生AX操作的代理。

Present已尝试从Tuesday Home下滚并点击Room，但未成功打开Room，伴随视口尺寸和点击落点不一致。两次截图保留在[回放尝试](../../design/polyulife/room-map-replay-attempts.json)，**没有记作通过或正式prototype run**。当前截图仅支持首页与失败尝试。

## 从这里继续

1. 从Tuesday Home进入Room，完整回放Sun ALL → 下滚 → Location → ↑ → ↓ → Back → Home；补测初始/放大画面Back。
2. 验证三张底图在Present中显示；初始图额外重传此前失败，先确认是否确有缺图再修复。
3. 比较返回日期、ALL和列表视口，并验证Home返回。原生已新增该样例滚动保持证据，原型尚未通过。
4. 回放成功后把三张地图、六个控件和证据加入正式Figma台账。不要把WIP直接视为通过，也不要重跑历史归档脚本。

自由平移、真实缩放边界、Google Maps交接均未实现；A-ROOM-MAP-DRAG没有证明成功平移。S-MAPRETURN可对应既有Sunday ALL的滚动状态，无需造重复全屏画板。

[机器可读接力记录](../../design/polyulife/room-map-work-in-progress.json) · [素材来源与哈希](../../design/polyulife/room-map-assets.json) · [生成脚本](../../design/scripts/build_room_map_svg.py) · [原生Room走查](room-walkthrough.md)
