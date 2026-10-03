# Notification Search 详情加载草稿与入口复查

2026-10-03 继续补查VA210详情控件。实际原生采样6次：普通键盘输入没有显示文字；AX设值后`workshop`及VA210结果可见；结果叶节点、右箭头及随后无输入复查均仍是Search。本批没有进入详情，没有确认图片、标签或地图的新行为。既有已成功动作保留历史状态，追加本次失败/未确定执行记录，不将过去成功改成从未验证。

[公开清单](../../evidence/2026-10-03-search-detail-controls/manifest.json)、[联系表](../../evidence/2026-10-03-search-detail-controls/contact-sheet.png)、[输入轨迹](../../evidence/2026-10-03-search-detail-controls/input-trace.json)与[安全AX](../../evidence/2026-10-03-search-detail-controls/05-result-followup.safe-ax.txt)区分原生尝试与编辑器证据。6组实际保存截图和完整AX核对一致；当前样本不再依赖工具显示文字判断页面。普通输入失败与AX设值成功不能证明输入等价、焦点原因或完整搜索正确。

## 已导入、未配置的 Figma 草稿

前一批保存的[VA210地图加载截图](../../evidence/2026-10-03-search-detail-observation/12-result-chevron-check.png)与`E-SEARCH-OBS-12-AX`支持通知Search来源的加载视口。按该来源制作[可编辑SVG](../../design/polyulife/notification-search-detail-loading.svg)，导入同一Observed UI页：

| 项目 | 实际状态 |
| --- | --- |
| 节点 | [946:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=946-19) |
| 名称 | `[NS:LOADING] VA210 — Search map pending` |
| 几何 | 576×1024；X0、Y86000，编辑器字段已读回 |
| 图层 | 原生Frame/Group/Text/Vector；公开插图和校徽为图片填充，编辑器采样可见 |
| 原型 | 新建交互行仍为`On click → None`，没有目标；未连接、未Present回放 |
| 正式统计 | 不加入`state_node_mappings`或`action_connection_mappings`；另列`source_preparation_imports` |

[编辑器截图](../../evidence/2026-10-03-search-detail-controls/06-figma-loading-draft.png)和[安全字段读回](../../evidence/2026-10-03-search-detail-controls/figma-safe-readback.txt)证明导入草稿，不证明连接成功。[来源与素材](../../design/polyulife/notification-search-loading-sources.json)保存原生引用、裁片范围和哈希，[生成脚本](../../design/scripts/build_notification_search_loading.py)只生成本地文件，不操作Figma。

本次点击Figma的`Action`下拉框被浏览器安全策略拒绝，给出的理由是URL协议不被允许。随后只读URL和AX仍是HTTPS的Figma946:19页面；原因未隔离。没有切换输入机制、绕过拒绝、配置目标或运行Present。未把这一拒绝归为Figma或App业务故障。

## 后续接入条件

[连接计划](../../design/polyulife/notification-search-loading-plan.json)只有提议，没有配置记录。后续在可操作的合法编辑器上下文中，从Workshop结果改入加载画板，加载转已观察详情，并让Back返回原Workshop查询。800ms只能作为演示延时；该加载采样同一次访问的最终地图和原生时长没有确定证据，须保留推广标记。不要把未确定的坐标点击因果写成新原生成功动作。

接入后必须实际回放入口、加载、稳定详情和Back；还要检查在演示计时前返回会不会被再次导航，以及复入时图片是否丢失。当前没有执行这些验收，原型回放数量保持136。Call、图片展开/手势、标签、地图展开/缩放/位置及其它场所继续保留待查。

## 统计与验证

当前24次原生会话、181状态、351动作（263 observed、81 not_attempted、7 attempted_unverified）；2462条证据引用，59份公开清单含2265个PNG。Figma正式201画板、436控件、136次运行，另有本次1张未配置加载草稿。完整应用与视觉保真保持`not_verified`。

新增公共截图已目视检查。原生副本裁掉57px标题栏并归一化576×1024；光标/光晕及底部捕获形状保留，其来源未隔离。编辑器SDK字节实际为1211×750，账户/协作者头像块已遮盖；失败的高度断言在任何台账修改前停止，核对字节尺寸后完成归档，不覆盖已完成历史批次。完整AX隐藏身份不公开。

引用/哈希/PNG尺寸/SVG结构/链接校验、公开文字敏感模式和`git diff --check`通过。既有原生状态、动作状态、历史执行及证据、正式Figma映射/连接/回放均保留；仅追加本批执行、证据、会话与草稿记录。校验不能证明全应用覆盖或连接完成。
