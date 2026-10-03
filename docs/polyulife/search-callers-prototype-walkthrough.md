# More / Notification 搜索原型回放 — 2026-09-30

本批通过 Computer Use 在实际 Figma 中补入两个独立调用者的搜索流程，复用既有原生截图和动作证据。新增六个可编辑画面、十五条配置连接；已有原生动作台账不变。完整 PolyULife 仍为 `not_verified`。

## 来源与复现

More 原生空页、weather 无结果、Room 无结果对应 E-MORE-SEARCH-EMPTY / WEATHER / ROOM；Room 搜索 Back 返回 More 已由原生 AX 确认。Notification 的空搜索、weather 无结果、Return 保持无结果、Clear 清空和空页 Back 返回由既有原生截图及动作台账支持。当前原生 App 身份发现仍显示运行，但重新连接超时，未新增原生观察。

五个 SVG 画面位于 Y47000，节点依次为527:19、527:34、527:65、527:96、527:111。Return 后同样的无结果画面使用实际 Figma 副本538:20，位置3500,47000、576×970、Clip content，文本和向量可编辑。它是原型内部状态，不是新的原生状态。源文件、哈希、上下文和节点见 [画面清单](../../design/polyulife/search-caller-contexts.json)，连接见 [连接清单](../../design/polyulife/search-caller-connections.json)。

W 固定替代 weather 输入，R 固定替代 Room 替换输入。这是 Figma 输入代理；任意查询、真实文本输入、成功搜索、其它入口组合、连续状态规则和精确视觉均未实现。More 空/weather 直接返回、Notification weather/提交后直接返回、提交后 Clear 与重复 Return 是未被单独原生观察的原型推广，action_id 为 null。对应原生输入和查询反馈之间的未观察加载/键盘状态没有补造。

## 实际回放与失败修复

- More：14–24 截图涵盖 Search→空→W weather→R Room→Back More，以及空/weather 直接返回；53–57 补查 weather 返回并无输入复查。保存的返回截图均呈现 More。少数立即返回的工具输出出现黑屏，后来无输入截图恢复；保存图20本身已是 More，文件原名保留，不把它虚称为黑屏证据。
- Notification 初次：25–28；Search 与 W 通过，Return 错误到菜单75:1669，失败保留。
- 修复：编辑器读回显示 Enter 实际写在空根527:96，移除错连。原weather根527:111不能 Swap overlay 到自身（菜单选项disabled），于是复制出538:20，原根 Enter→副本，副本 Enter→原根。副本 Clear/Back 沿用源控件并单独读回。09/29为错误配置、30为自身目标禁用、31/32/33/34/35为副本及修复证据。
- Notification 修复后：36–52；空→W weather→Return 相同无结果→Clear 空→Back Notification；另跑原weather Clear、weather直接Back、重复Return及副本Back。返回仍为 Notification。

Present overlay 的 URL 保留 underlying caller，不用 URL 把527:19等画面误认作More或Notification。见 [脱敏截图清单及像素比较](../../evidence/2026-09-30-search-callers/manifest.json)。画面身份由实际视觉、配置读回及已执行路径共同确认；同视觉的提交前/后副本不能仅靠截图区分。副本 Prototype 面板显示 Add flow starting point，未生成新起点。

十七项原型裁片比较中十四项完全相等。提交前/后weather差异为783个像素，最大单通道差27、超过10的像素18个；两个跨调用者比较的最大差分别为4和7。差异原因未建立，不据此宣称原生像素保真。所有已保存的调用者返回比较相等。

## 可复现操作

从 [More Present](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-435&starting-point-node-id=12%3A435&scaling=scale-down&content-scaling=fixed) 点 Search，按 W、R 后点 Back。从 [Notification Present](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=42-1617&starting-point-node-id=42%3A1617&scaling=scale-down&content-scaling=fixed) 点 Search，按 W、Return，点查询框右侧 X，再点 Back。W/R 不是普通输入框。

## 观察事实、假设与后续

事实：既有原生样例的查询不匹配时显示相同 No record found 文案，Notification Return 没有建立成功结果；本原型只重放这些固定样例。假设：通用空结果信息可能不足以解释当前搜索范围或帮助用户修正关键词，需以原生搜索范围、成功查询和真人理解验证；不能根据固定无结果样例推断整个搜索失效。HCI 关联为错误恢复与状态可见性，设计改进应在确认范围后提供更具体的修正提示。

工具限制：一条现有 Present 标签导航/AX/截图超时，同一标签检查并保留，另一个现有标签可完成回放；未重启App或浏览器。配置时还有临时ERR_ABORTED和层标签定位失败，均按新状态核对后修正。这些不归为App缺陷。公开截图遮盖账户/协作头像，AX全文与未经脱敏截图继续保存在被忽略的本地raw目录。

下一步继续原生搜索输入/范围/结果与未观察入口，再补Home Search内部控件、其它调用者与界面视觉。真人课程测试仍需真人执行；本批不形成用户成功率、耗时或Maze数据。
