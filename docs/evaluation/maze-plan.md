# PolyULife · 全组 Maze 测试计划

更新：2026-11-09。负责人 E 组织；A–E 各自提供功能任务、招募至少一位不同的真实目标用户，并分析自己的功能。当前是**计划，不是测试结果**。

## 1. 目标与参与者

目标是检查五项改版任务能否被真实用户理解、完成和恢复，并收集支持迭代的证据，而不是验证 Agent 的操作能力。

- 至少 **5 位不同的真实 PolyU 学生**；尽量覆盖对 PolyULife 熟悉与不熟悉的人。记录与任务相关的经验，不收集无关身份信息。
- 每位参与者尽量完成全部五条任务；未完成或中止也保留记录，不能只保留成功样本。
- 先由 E 做一次试测，确认链接、起点、任务措辞和结果记录可用。试测发现阻断问题后须冻结新版本，并说明是否将试测者计入正式五人。
- 向参与者说明目的、预计时长、记录内容、可随时退出和公开材料的匿名化方式；不在公开仓库存放姓名、学号、邮箱、账号、身份映射或未经处理的屏幕录像。

## 2. 冻结版本与执行

1. C 从共同首页验收五条往返，D 验收样式，E 检查可访问性与任务；各负责人确认边界状态。
2. 保存带日期的 Figma 测试副本，例如 `PolyULife-Maze-2026-11-10-v1`。同一轮所有参与者使用相同版本和任务。
3. Maze 使用实际 Figma 原型链接。Agent 生成的 HTML 仅作实现检查，不能冒充课程 Figma 测试。
4. 不在任务文字中泄露点击路径。参与者操作时只使用统一说明，不临场提示；协助和中止都写入备注。
5. 保留 Maze 原始导出和 dashboard 截图，按匿名编号整理。任何阻断修复记录时间、版本及受影响结果。

## 3. 五条任务

### Apps（A，可直接录入）

**English task wording**

> A guest will visit you on campus tomorrow. Using the PolyULife prototype, find the service that lets you request a QR code for your guest, review what is needed to continue, and open the official service page. When you are finished, return to the service list so you could choose another service.

**Success and observation**

- Maze 成功终点：到达 `A06 / Official sign-in`，且服务为 Visitor Registration System。
- 返回检查：关闭外部页并回到进入前列表；查询、分类和滚动位置应保留。若 Maze 只能设一个终点，将返回行为作为后续观察/追加任务记录，不改写主任务成功数据。
- 记录直接/间接成功、耗时、错误入口、查询词、是否误解 NetID 交接、返回是否顺利及原话。
- 不要求输入 NetID/NetPassword，不提交真实访客申请。
- 后续理解问题：`Which category or filter is active now?` 与 `What do you expect to happen before you can use this service?`

### Calendar（B，待功能负责人确认）

- English task wording：**待 B 提供**。应要求找指定日期的课程或事件并查看详情，不写出 Calendar、筛选或按钮路径。
- Success：**待 B 提供目标 frame、正确日期/事件和返回状态。**

### Room（C，待功能负责人确认）

- English task wording：**待 C 提供**。应要求找指定房间/时段，并处理一次无可用或无结果恢复，不提示搜索、日期或 Available 控件。
- Success：**待 C 提供目标 frame、正确房间/日期和恢复条件。**

### Food（D，待功能负责人确认）

- English task wording：**待 D 提供**。可围绕寻找餐厅、核对营业时间并返回，不把历史演示时间写成当前真实营业状态。
- Success：**待 D 提供目标 frame、正确餐厅/信息和返回状态。**

### Map（E，待功能负责人确认）

- English task wording：**待 E 提供**。应要求按需求找一类校园设施并查看位置，不直接提示分类或地图按钮。
- Success：**待 E 提供目标 frame、正确地点和返回状态。**

## 4. 指标与反馈

每个任务记录：

| 数据 | 统一含义 |
| --- | --- |
| Direct success | 未走错误路径即到达预定义成功终点 |
| Indirect success | 经回退或额外路径最终到达成功终点 |
| Failure / abandon | 未到终点、错误完成或中止；保留原因，不删除样本 |
| Time | Maze 记录的任务耗时；不与 Agent 操作时间混用 |
| Errors / wrong turns | 错入模块、错误返回、误解状态、重复尝试等具体行为 |
| Participant quotation | 尽量逐字记录能解释行为的原话，附匿名编号和任务 |
| Single Ease Question | 每任务 `Overall, how easy or difficult was this task?`，1 = Very difficult，7 = Very easy |

本轮只测试改版，没有同一批参与者的原界面基线，因此报告可描述完成情况和发现，不能仅凭此声称相对原 App 提升了多少百分比。

## 5. 结果保存与迭代

建议公开证据目录使用 `evidence/YYYY-MM-DD-maze/`，仅保存匿名聚合数据、Maze 导出/dashboard、任务版本和迭代记录；身份映射与原始私人材料保留在本地忽略目录。

每位功能负责人提交：实际样本与未完成项 → 数据图表/原话 → 对具体设计的解释 → 修改前后 frame 和日期 → 仍需验证的问题。E 汇总方法、整体结果和限制，不能把少数参与者的反馈推成统计普遍结论。

同伴复核重点：数字能否追溯到原始导出；原话是否对应匿名参与者；失败样本是否保留；每个“因此修改”是否确有前后版本；报告、PPT、视频和最终 Figma 是否使用同一迭代版本。
