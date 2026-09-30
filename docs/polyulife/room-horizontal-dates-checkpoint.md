# Tuesday 日期条阶段存档

> 后续已完成 Today 连接和本批证据归档，见[连续日期条回放](room-horizontal-dates-prototype-walkthrough.md)。以下保留先推送版本的阶段状态。

2026-09-30，应用户要求先提交当前进度。本批次为未完成的工作存档，尚未纳入正式覆盖统计或完成证据归档。

## 已保存的材料

- [生成脚本](../../design/scripts/build_room_horizontal_dates_svg.py) 从已有日期 SVG 生成完整的七日日期条。
- [日期条素材](../../design/polyulife/room-dates-tuesday-strip.svg)：658 × 84，日期固定为已观察的 30-Sep 至 06-Oct，Tuesday 选中。
- [Tuesday 初始位置参考](../../design/polyulife/room-dates-tuesday-horizontal.svg)及[反向滚动位置参考](../../design/polyulife/room-dates-tuesday-reversed-horizontal.svg)：576 × 1026。两个完整 SVG 是来源参考，当前只将日期条素材导入原有画板。

## 当前 Figma 进度

此前 Computer Use 操作记录显示：画板 `412:1120` 中的日期条已替换为 `436:32` 横向滚动容器，位置 (30, 100)、视口 516 × 84、内容 658 × 84。使用 After delay 1ms → Scroll to DatesHorizontalContent、X offset 142、Instant 定位 Tuesday 初始位置。这是 Figma 内部显示初始化，不是原生 App 的动作或延迟测量。

原有有限 On Drag 连接 `C-ROOM-DATES-12` 随旧日期组移除。阶段回放记录包含双向滚动、稳定中间位置和两个端点；这些属于原型回放，未新增原生观察或真人评估。公开截图、哈希、结果区比较和正式映射更新尚待完成。

## 接力事项

1. 新日期条的 Today 点击返回尚未连接，需要连接到 `412:216` 并回放验证。
2. 检查重新进入时的初始位置、结果区保持及既有日期/筛选路径。
3. 脱敏归档本批次截图与配置依据，更新来源、连接、滚动区域、别名和回放记录；保留旧回放历史。
4. 更新正式覆盖台账，明确旧 `C-ROOM-DATES-12` 被替代。目前 [coverage.json](coverage.json) 和上一批[日期回放记录](room-dates-prototype-walkthrough.md)对应此前已归档版本，尚不代表此处最新的 Figma 编辑。

全应用范围仍为 `not_verified`。本次提交仅保存阶段材料，不表示日期路径或全应用复刻已经完成。
