# Figma 复现与证据对应约定

本页定义从真实 PolyULife 观察到可编辑、可点击 Figma 的对应关系。实际覆盖由 [coverage.json](coverage.json) 记录。本页同时记录已经确认的文件状态和后续制作、验证方法；实际存在文件不等于节点和交互已经完成。

## 当前真实文件与验证状态

- 文件：[PolyULife — Observed UI & Interaction Atlas](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)。真实 Figma Design 文件已创建、重命名并生成首批 Room 页面。
- [可运行原型入口](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI---Interaction-Atlas?node-id=2-50&starting-point-node-id=2%3A50)。14:55–14:57 UTC 已实际点击三条连接并核对节点 URL：联想 `2:50` → ALL `2:98` → Available `2:211` → ALL `2:98`。
- 原生 Agents 完成报告列出 **4 frames、7 components、3 connections**。其中三条连接已独立运行；`room-suggest-a` 在编辑器中确认是 576×970 的 Frame，Auto layout 已启用。随后通过 Return 选出 Header、DaySelector、SearchRowContainer、Line、EmptyState 五个子图层；15:03:27 UTC 进一步选中原生 [Text 2:55](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-55)，右栏确认 Inter Bold 18 px、111×22。这个 frame 的原生结构与标题可编辑属性已核对，其余 frame 和全部组件仍需逐项检查。
- **视觉核验未通过**：生成稿在标题高度、字号/控件比例、日期边框、搜索图标与清空外观、Available 时段排列和背景颜色上偏离来源。下面逐项列出；可运行原型不等于忠实复现。
- Figma 原生 Agents 已提示免费 Starter 计划的 **daily credits** 用尽，后续提示生成受限；没有付费或升级。现有文件及编辑器仍可核验/修改。主线另外验证普通 SVG 粘贴可生成原生 Frame、Vector、Text，检查测试 Text 12:5 后已删除临时 Frame 12:2；忠实 SVG 设计源码正在准备，后续导入现有 Figma 并重连。这条替代制作路线不受 Agents 提示额度影响。
- 当前路线为浏览器 Computer Use 操作 Figma Design 与其原生 Agents。Codex Figma 插件连接仍未确认；该连接不影响当前浏览器路径。

### 来源与真实节点

| 观察状态 | 来源截图 | 已核对 Figma 节点 |
| --- | --- | --- |
| `S-EMPTYQUERY` | [初始空查询](../../evidence/2026-09-28-full-audit/room-135521-empty-query.png) | 生成报告称已创建 `room-empty`；节点 ID 与内部结构待核验 |
| `S-SUGGESTION` | [A 联想](../../evidence/2026-09-28-full-audit/room-135612-a-suggestion.png) | [room-suggest-a · 2:50](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-50) |
| `S-ALL` | [AG206 ALL](../../evidence/2026-09-28-full-audit/room-135628-ag206-all.png) | [room-all · 2:98](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-98) |
| `S-AVAILABLE` | [AG206 Available](../../evidence/2026-09-28-full-audit/room-135653-ag206-available.png) | [room-available · 2:211](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=2-211) |

### 原型实际运行

公开运行截图：[联想页](../../evidence/2026-09-28-full-audit/figma-present-145546-room-suggest-a.png)、[ALL 稳定状态](../../evidence/2026-09-28-full-audit/figma-present-145617-room-all.png)、[Available 稳定状态](../../evidence/2026-09-28-full-audit/figma-present-145645-room-available.png)。[帧属性与额度提示](../../evidence/2026-09-28-full-audit/figma-145434-frame-properties-and-credits.png)证明编辑器状态，不能代替视觉验收。最后一次 ALL 返回依据 URL/AX，没有单独的返回截图。

| 动作时间（UTC） | 点击 | 实际结果 | 判定范围 |
| --- | --- | --- | --- |
| 14:56:01 | 联想页 AG206 项 | URL 从 `2:50` 变为 `2:98`，进入 ALL 状态 | 该点击连接通过；不证明输入框有真实联想逻辑 |
| 14:56:31 | ALL 页 Available | URL 从 `2:98` 变为 `2:211`，显示六个可用时段 | 该连接通过；时段排列视觉不通过 |
| 14:57:31 | Available 页 ALL | URL 从 `2:211` 返回 `2:98` | 该返回连接通过；真实 App 的同日期这一步仍需与既有观察精确对应 |

本轮真实 App 已观察在 Sun 04-Oct 的 Available 空结果切换 ALL；原型第三条使用 Tue 29-Sep 的有结果版本。二者操作机制相近，仍须补做同日期数据状态的精确复核，不能修改原始 App 记录来迁就原型。

### 已发现的复现偏差

| 偏差 | 来源与生成稿差异 | 状态与修复要求 |
| --- | --- | --- |
| `D-ROOM-HEADER-SCALE` | 生成稿标题区约 60 px，来源截图约 100 px；整体字体及控件偏小 | 未解决；在相同 576×970 比例核对尺寸并重排，不用整体放大掩盖局部差异 |
| `D-ROOM-DATE-BORDER` | 生成稿给日期增加了来源中未观察到的边框 | 未解决；按来源恢复未选日期外观 |
| `D-ROOM-SEARCH-DECORATION` | 生成稿输入区增加 leading magnifier，并出现不应有的模糊 clear 外观 | 未解决；区分 App 真实控件与截图中的 Computer Use 指针/高亮，不把工具覆盖物做进设计 |
| `D-ROOM-SLOT-ORDER` | Available 来源前两行是 `08:30 / 09:00`、`11:30 / 12:00`；生成稿是 `08:30 / 11:30`、`09:00 / 12:00`。ALL 第一行也从来源 `08:30 / 09:00` 变成生成稿 `08:30 / 12:30` | 未解决；保持时间与行列对应，修复后在 Present 再看六个时段 |
| `D-ROOM-BACKGROUND` | 生成稿部分背景使用灰白，与来源的白色背景不同 | 未解决；分别核对页面、容器与卡片填充 |

这些是 Figma 草稿的复现偏差，不是 PolyULife 新发现的缺陷。

下一步先检查并修正现有原生图层，保留真实节点映射，复验视觉偏差和三条原型连接；再补完所有已观察状态与待观察模块。此前 Processing 记录只是生成期间的历史状态，不能作为当前状态继续引用。

## 文件组织

当前免费计划最多三个工作页。先在现有一个页面内按 **sections** 组织 Room Finder，后续新增模块继续使用 sections，整个文件保持不超过三个工作页。下表是后续组织方案，不声称这些页已经创建：

| 工作页（最多三页） | 其中的 sections |
| --- | --- |
| `01 · Observed UI & Flows` | Index、各功能模块的已观察状态、可运行原型起点、待补覆盖说明；组件实例复用同一批状态 |
| `02 · Components` | 已观察的文字、颜色、间距、导航、按钮、日期/筛选/时段及变体 |
| `03 · Analysis & Evidence` | 事实、截图索引、HCI 假设、待验证事项和独立改进建议 |

先按真实 UI 完成复现；用户尚未批准的改进建议保留为分析或独立方案，不能覆盖原应用证据。课程后续 redesign 可复用组件并建立独立版本。

## 从状态到节点

每个 `state` 对应一个可定位的 Figma frame、overlay 或 component variant。节点命名使用 `[state_id] 实际页面/状态名`，名称来自观察记录。`state_node_mappings` 记录：

- `state_id`、`node_id`、`node_url`、Figma 工作页及节点类型。
- `source_evidence_ids`：真实截图和辅助 AX 引用。
- `viewport`：截图内容区域尺寸、缩放及 Figma frame 尺寸；窗口装饰与应用内容边界分开记录。
- `content_policy`：真实界面中的个人字段在共享版替换为明确的示例值；保留文案长度、层级和交互作用。
- `visual_review`：检查时间、证据、结果和未解决差异；真实核对前为 `not_run`。

截图用作对照来源。可编辑文字、图形、组件和布局承载正式页面内容；整页截图加少量热点只能作为临时取证或对照层，不能满足完整可编辑复现。控件样式由已观察截图量取；尚未出现的颜色、字体、状态和页面结构保持待补，不用惯例当成原应用事实。

加载、空状态、错误提示、弹窗、筛选、展开菜单和键盘相关变化在实际观察到后分别建模；共享组件可使用 variant，出现/退出方式由实际动作决定。多种数据内容若交互等价可采用脱敏示例，但记录所依据的状态及差异。

## 从动作到连接

每个已经实际执行并得到反馈的 `action` 对应 Figma 连接或组件交互。`action_connection_mappings` 记录：

- `action_id`、起点 `source_node_id`、目标 `target_node_id` 或明确目标 URL。
- `trigger`、`behavior`、`transition`、必要前置条件，以及关联的反馈状态。
- 返回、关闭、取消、清空等恢复路径对应的动作 ID。
- `implementation_status` 与 `prototype_run_ids`；只配置连线而未运行不能记为验证通过。

普通导航使用实际目标；弹层使用 overlay/关闭交互；滚动与固定导航按真实截图和操作复现。文本输入、日期、搜索、筛选等按实际反馈表现，用变量、组件或明确样例实现。Figma 能力不足时登记 `reconstruction_deviations`，写明原应用行为、当前实现、影响范围和补齐方式；静态画面不能证明输入流程完整。

外部网页、系统权限、登录和设备能力在原型中标明入口及真实观察到的交接结果。展示示例成功反馈时必须是原型模拟并有来源状态，不得执行真实预约或伪装成真实业务完成。无法观察的分支在台账保留缺口。

## 验证和交付

1. 在 Figma 编辑界面打开真实节点，核对文字、图标、布局、比例、可见状态和个人字段处理。保存节点 URL 和核对证据后，才更新相应视觉检查状态。
2. 打开 Figma Present，从每个流程起点按台账动作操作。每次运行登记 `id`、时间、起点节点、动作序列、预期状态、实际结果、证据和失败项。
3. 检查导航、弹层、选择、输入反馈、滚动、外部跳转说明和返回路径。页面是否可达、控件是否响应、结束后是否可继续操作分别验证。
4. 失败关联到原动作，修复后新增复验记录。共享链接以实际可访问性检查为准；URL 存在不证明成员可以查看或使用。
5. 将节点和动作映射与全应用台账逐条比对。任何尚未观察、缺截图、缺节点、缺连线、未复验或仍有阻碍的项均保持未完成；全应用完成判定见 [README](README.md#完成判定)。

交付包含真实 Figma 文件及原型链接、状态/动作映射、证据索引、HCI 分析及明确的剩余缺口。Agent 对原型的走查是功能验证记录；课程真人可用性评估另按 [项目说明](../project-brief.md) 执行。
