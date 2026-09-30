# Search caller reconstruction checkpoint — 2026-09-30

本次提交保存 More 与 Notification 两个搜索入口的未完成原型，供团队和后续 Agent 接力。原生证据沿用现有走查；本批没有新增原生观察，也尚未进行 Present 回放。全应用完成状态仍为 `not_verified`。

## 已配置

五个独立的可编辑搜索画面已通过 Computer Use 导入 [Figma](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=527-19)。节点、源文件及证据引用见 [画面清单](../../design/polyulife/search-caller-contexts.json)；七条连接的编辑器配置读回已完成，见 [连接清单](../../design/polyulife/search-caller-connections.json)。这两份清单是阶段记录，尚未并入正式覆盖统计。

- More Search 打开空搜索；W 切换到固定 weather 查询；R 切换到固定 Room 查询；三个状态的 Back 关闭 overlay。
- Notification Search 打开该入口独立的空搜索画面。

W/R 是 Figma 的固定查询输入代理，不代表原生键盘行为，也不支持任意文本。More 的 Room 查询返回有原生证据；空查询和 weather 查询直接返回是原型推广，未宣称已在原生观察。

## 接力位置

Notification 空搜索根节点为 `527:96`，weather 无结果根节点为 `527:111`。还需配置五条连接：空搜索 W 到 weather、weather Return 保持无结果、Clear 到空搜索、空搜索 Back 返回 Notification、weather Back 返回 Notification。最后一条是未观察的原型推广，其余按既有原生动作台账引用。

之后检查新增 flow 起点并回放两个入口的完整返回路径，保存脱敏截图，再归档覆盖表及正式 walkthrough。页面采用现有近似 SVG 几何；像素保真、任意输入和成功搜索结果均未验证。

## 本地证据与限制

编辑器截图和完整 AX 配置读回保存在被忽略的 `evidence/raw/2026-09-30-search-callers/`，不包含在公开提交中。原始 AX 可能含账户信息，后续必须脱敏后共享。本批原生 AX 获取超时，编辑器也出现短暂定位失败及一次执行超时；已从保存的连接清单恢复，工具失败不归为 App 缺陷。

正式归档基线仍为 109 个画面、251 个控件、43 次原型运行。本提交只保存五个新画面的源文件与七条配置记录，不把待回放的工作计为新增已验证覆盖。
