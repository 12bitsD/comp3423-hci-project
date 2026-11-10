# Maze 测试执行包（Food + Apps）

更新：2026-11-11。本包是**执行模板**，不含任何真人数据。正式提交课程的数据必须来自真人参与者（≥5 位非组员）。第 8 节的 Pilot 记录是 Agent 试跑，用于验证任务可行性，**不计入五人**。

## 0. 流程总览

> **2026-11-11 已建并发布**：研究 `PolyULife Maze 2026-11 (Food + Apps)`（Maze 项目 PolyULife COMP3423）。
> **测试链接：https://t.maze.co/609474600** （Track responses 开、每设备限一次）
> 已含 5 个 Mission（Food×4 + Apps×1）+ Opinion Scale + Open Question。
> 注意：Maze 不允许同一 Figma 文件导入两个 study（报 unexpected error），Food 和 Apps 合并在同一研究。


```
建 Maze 项目（本包 §1）→ 发链接给 ≥5 位真人（§5 招募文案）→ 参与者自己完成（无需主持）
→ 你在 Maze 后台收报告（§6）→ 按 §7 模板写进课程报告
```

## 1. Maze 项目设置（step by step）

1. maze.co 注册/登录（免费档即可）。
2. **New project → Prototype test → Import from Figma**，粘贴下方 Present 链接。
3. 按 §2/§3 建 Mission（任务），每个任务设置**起点画框**和**终点画框**（Maze 自动判定成功/放弃）。
4. 按 §4 挂问卷题。
5. 用 Preview 自查一遍：每个任务从起点能走到终点、措辞没有歧义。
6. 复制测试链接，发给参与者。

**原型链接（Food）**：https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=1109-12&scaling=scale-down&content-scaling=fixed
**原型链接（Apps）**：https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=1138-56&scaling=scale-down&content-scaling=fixed

## 2. Food 任务定义（4 个 Mission）

### F-T1 找咖啡馆并看位置

> You have a short break between classes and want a coffee near Block FGHJ. Find a café, check its opening hours today, and see where it is on the campus map.

- 起点：`F00 / Home`（node-id=1109-12）
- 成功终点：`Map / hcafe`（node-id=1109-461）
- 预期路径：F00 → Explore → F01 → Cafés chip → Filter/Cafés → View details → Detail/hcafe → View location map
- 观察点：能否发现 Cafés chip；能否找到 View details；地图是否找到

### F-T2 查营业时间

> You plan to have lunch at H Café tomorrow. Check when it opens on weekdays.

- 起点：`F01 / All`（node-id=1109-25）
- 成功终点：`Detail / hcafe`（node-id=1109-440）
- 观察点：是否注意到 Open now chip 与 Opening hours 的区别；是否读到周表

### F-T3 筛选

> You only want to see vending machines on campus. Show only those places.

- 起点：`F01 / All`
- 成功终点：`Filter / Vending`（node-id=1109:383 对应帧）
- 注意：**只用一个筛选条件**。原型只有单筛选状态帧，不要在任务里要求组合筛选（如 "open now vending"）
- 观察点：Vending chip 是否被理解；与 Open now chip 是否混淆

### F-T4 外部服务交接

> You decided to order food online from H Café. Try to order and see what the app tells you.

- 起点：`Detail / hcafe`
- 成功终点：`External prompt`（node-id=1109:569）
- 观察点：是否理解 handoff 提示文案；是否选择 Stay in PolyULife；是否误以为会真的下单

## 3. Apps 任务定义（1 个 Mission，已按现有画框修订）

### A-T1 访客 QR 服务

> A guest will visit you on campus tomorrow. Using the PolyULife prototype, find the service that lets you request a QR code for your guest, review what is needed to continue, and open the official service page. When you are finished, return to the service list so you could choose another service.

- 起点：`A01 · All services`（node-id=1138-56）
- 成功终点：`A05 · VRS loading`（**原计划终点 A06 尚未建帧，A05 为现有可达成终点**）
- 返回检查：Cancel → A04 → Back to results → A01；查询与列表状态应保留
- 观察点：是否直接找到 VRS 行；是否误解 NetID 交接提示；返回链是否顺畅
- 后续问题：`Which category or filter is active now?`、`What do you expect to happen before you can use this service?`
- 边界：不要求输入 NetID/密码，不提交真实申请

## 4. 问卷题（每个项目结尾各挂一次）

- 评分题：`How easy was it to find what you needed?`（so-so / easy / hard，或 1–5 分）
- 开放题：`Was anything confusing or unclear? Please describe in your own words.`

## 5. 参与者说明（可直接转发）

> 你好！我们在做 PolyU 一门 HCI 课程的原型测试，想邀请你花约 10 分钟点一个手机原型（Food 找餐厅 / Apps 找服务，二选一或都做）。没有对错答案，点错也没关系。全程匿名，我们只记录点击和时长，不收集姓名学号。你可以随时退出。链接：[MAZE_LINK]。谢谢！

> Hi! We're testing a mobile app prototype for an HCI course. It takes about 10 minutes — just tap through the prototype and think aloud if you like. There are no wrong answers. It's anonymous (we only record taps and time). You can stop anytime. Link: [MAZE_LINK]. Thanks!

## 6. 结果收集清单

- Dashboard 每任务：成功率、放弃率、误点率、平均用时
- 每屏热力图（哪些区域被误点最多）
- 问卷评分分布 + 开放题原话（逐字引用）
- 导出 PDF 报告存档（命名如 `polyulife-food-test_report_2026-11-XX.pdf`）
- 隐私：参与者用匿名编号；仓库不存姓名、学号、邮箱、身份映射或未脱敏录屏（沿用 Map 的证据约定）

## 7. 报告小节模板（照 Map 的结构）

1. **Method**：参与者数量与背景、任务列表、流程（非主持、远程、自备设备）
2. **Results**：数据表（任务 / n / 成功率 / 放弃率 / 误点率 / 平均用时）
3. **Verbatim quotes**：3 条以内原话，配英文翻译
4. **Heatmap findings**：2–3 个从热力图读出的问题
5. **Iteration after testing**：据此做的设计修改（对照修改前后）

## 8. Pilot 记录（Agent 试跑，2026-11-11，不计入五人）

- 执行者：Agent（非真人），目的仅为验证任务可行性
- 结果：F-T1/F-T2/F-T4 全路径 Present 走通，无阻断；F-T3 措辞已从组合筛选改为单筛选（原型只支持单筛选帧）
- 关键确认：F01 → Cafés chip → Filter/Cafés → View details → Detail/hcafe → Map/hcafe → 返回链全部可达
- 教训：Maze 导入链接应指向 Flow 起点；同一 Figma 文件不能导入两个 study（合并不是一个坏选择，参与者一次做完 Food+Apps 也更连贯）
- 待人工确认：CUA 无法点击 Maze 内嵌的跨域 Figma iframe（自动化限制），正式发布后请人工点第一个任务确认原型可交互
- Apps 任务终点从 A06 修订为 A05（A06 未建帧）
