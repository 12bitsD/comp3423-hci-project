# Room 剩余日期栏阶段存档

2026-09-30，应用户要求先提交并推送当前进度。本批为阶段存档，尚未完成 Present 回放、公开截图归档及正式覆盖台账更新。

## 已配置的 Figma 日期栏

此前 Computer Use 操作日志记录了以下四个画板的替换与配置。日志副本见[阶段配置记录](room-remaining-date-bars-checkpoint.json)，素材来源见[日期条来源目录](../../design/polyulife/room-date-context-strip-sources.json)。

| 上下文 | 画板 | 新视口 | 内容层 | 日期连接 |
| --- | --- | --- | --- | --- |
| Today ALL | `412:19` | `463:19` | `463:21` | 本批未新增 |
| Today Available | `412:216` | `465:19` | `465:21` | Thu `465:26` → `412:317`，替代 `C-ROOM-DATES-01` |
| Thursday Available | `412:317` | `466:19` | `466:21` | 本批未新增 |
| Thursday ALL | `412:400` | `467:19` | `467:21` | Fri `467:30` → `412:551`，替代 `C-ROOM-DATES-04` |

四个日期视口的位置均为 (30, 100)，尺寸 516 × 84，内容宽度 658。已配置横向滚动，并使用 After delay 1ms → Scroll to DatesHorizontalContent、X/Y offset 0、Instant 设置初始位置。这是原型显示初始化，不是原生 App 的动作或延迟测量。

本批状态为 `configured_horizontal_not_replayed`。配置日志不证明连续日期路径、筛选连接、滚动边界或重新进入行为已经通过回放。

## 中断与恢复

Friday ALL 替换时曾误选整个画板；通过七次 Figma 撤销恢复了原画板 `412:551`。随后已选中原日期遮罩 `412:559`，其位置与尺寸为 (30, 100)、516 × 84，但在后续工具超时及运行时重置前未执行新的替换。Friday ALL 的既有筛选连接仍需回放检查；Friday Available 也尚未处理。

本轮原生 Preview 复查仍未取得完整网页视觉证据：部分 AX 文字可读，截图区域空白，后续出现窗口捕获失败和超时。没有确认成功关闭 Preview 或退出全屏，也没有确认视觉捕获问题已经恢复。原始截图与诊断日志仅保留在本地忽略目录，尚未作为新增公开观察归档。

## 接力事项

1. 在修改前核对选中的日期遮罩及其位置、尺寸，完成 Friday ALL、Friday Available 横向日期栏；Friday Available 的 Sat 连接应指向 `412:827`。
2. 回放 Today ALL → Available → Thu → ALL → Fri → Available → Sat → Sun → Mon → Tue → Today，并检查六个上下文的双向滚动、筛选连接、结果区保持及重新进入位置。
3. 保存脱敏截图、配置依据和比较结果，更新正式来源、连接历史、滚动区域及覆盖台账。
4. 原生 Preview 后续按真实捕获结果继续复查，区分 AX 可读与视觉呈现；不把原型回放作为新增原生证据或真人评估。

[正式覆盖台账](coverage.json)和已归档回放仍对应此前提交 `643b838` 的基线，尚未反映上述四个日期栏的新配置。全应用范围仍为 `not_verified`。
