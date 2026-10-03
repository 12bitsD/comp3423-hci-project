# Calendar 月份、无事件日期与调用者返回 — 2026-09-30

当前Home→Week→月视图上下文补接已观察的月份/日期循环：Sep26→Oct1→Sep1→Sep28无事件→Sep26。增加三个公开日期画板和七条控件，Monday/Tuesday两组实际回放，累计125个映射画板、291条控件、63次原型运行。完整PolyULife仍 `not_verified`。

## 原生语义及素材

既有A-CALENDAR-NEXT-MONTH进入October并选中1、显示National Day（E-CALENDAR-OCT1）；A-CALENDAR-PREV-MONTH返回September并选中1、显示No event（E-CALENDAR-SEP1），并不是恢复之前的26。A-CALENDAR-DATE-SEP28选择28、保持academic-only No event（E-CALENDAR-SEP28）；A-CALENDAR-DATE-SEP26选择26并显示公共节假日（E-CALENDAR-SEP26）。本轮没有新的原生操作。上一轮按当前发现的Wrapper连接超时，不把发现列表中的运行状态当成可观察窗口或原生流程完成。

三个画板分别为[Oct1 596:20](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=596-20)、[Sep1 596:174](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=596-174)、[Sep28 596:335](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=596-335)，尺寸576×970、Clip content开启，位置0/700/1400,53500。由已有公开SVG复制，Sep28来源E-CALENDAR-ACAD-EMPTY，与后续Sep28截图的同一公共日期/过滤状态对应。月份/日期/标题/无事件提示/事件卡/图标为可编辑近似，光标和光晕未复制；历史固定数据，不是当前实时日历。Home/Week私人内容保持合成DEMO。[生成脚本](../../design/scripts/build_calendar_date_context_svg.py)与[哈希记录](../../design/polyulife/calendar-date-context-assets.json)保留来源。

## 七条连接

| 源与控件 | Figma行为与目标 | 原生对应 |
| --- | --- | --- |
| Sep26 573:19 NextMonth573:26 | Swap overlay→Oct1 596:20 | A-CALENDAR-NEXT-MONTH |
| Oct1 596:20 PreviousMonth596:25 | Swap overlay→Sep1 596:174 | A-CALENDAR-PREV-MONTH |
| Sep1 596:174 Day28 596:270 | Swap overlay→Sep28 596:335 | A-CALENDAR-DATE-SEP28 |
| Sep28 596:335 Day26 596:425 | Swap overlay→Sep26 573:19 | A-CALENDAR-DATE-SEP26 |
| Oct1 NavHome596:157 | Back→测试的Home调用者 | null，原型恢复推广 |
| Sep1 NavHome596:318 | Back→测试的Home调用者 | null，原型恢复推广 |
| Sep28 NavHome596:479 | Back→测试的Home调用者 | null，原型恢复推广 |

四个Swap均On click/Instant，替换同一层month overlay并保留Week底层；这描述Figma实现，不证明原生使用overlay。三个Home恢复入口分别从Monday和Tuesday采样；原生在这些日期上下文的Home返回仍未观察。[配置清单](../../design/polyulife/calendar-date-context-connections.json)明确区分原生动作和推广。

## 实际回放、编辑器修正和差异

11–19实际重载后仍是Tuesday Home，按保存画面记为Tuesday起点。12–16完成四步日期循环，17–18回归已有节假日详情/Back，19回Tuesday。20–25分别从Oct1、Sep1和Sep28直接Home返回。26直接重开Monday；27–31完成同一循环，32–34继续Month→Events→History→Week→Home，35–40测试三个直接恢复出口，均保留Monday。

十五项裁片比较十三项相等，包含日期跨调用者/返回/详情回归，以及相对于已返回Home基线的三个日期恢复出口。11→19和26→34的Home初始/最终不等，差异都在应用裁片内(22,588,358,613)，照片仍可见但局部原因未明。以已返回基线相等不能消除这两个失败，不能作为全视觉保真证明。[44张保存截图及比较](../../evidence/2026-09-30-calendar-dates/manifest.json)、[对照图](../../evidence/2026-09-30-calendar-dates/contact-sheet.png)可复查。

流程根检查时第一次定位命中右侧连接文字，选中URL仍为原来的NextMonth控件；选择守卫发现后停止，没有新增或覆盖动作。随后图层列表虚拟化导致Sep1文字未找到，当前编辑器仍可读取，没有重建浏览器或改动配置。通过折叠/滚动及直接定位恢复。41为Oct1 Prototype根检查；42虽然文件名写flow-check，实际是Sep1 Design面板，已修正文案，不作为流程起点证明；43、44才是Sep28和Sep1的Prototype根检查，均显示Add flow starting point，没有新增独立Flow。保留这些尝试与实际结果的区别。

## 未完成范围

日期循环只有上述四条边；其他日格、Month/semester边界、Sep1/28下一月、Oct1下一月、其它事件详情/筛选/列表、More调用者和长期状态未实现。源图保留的其它箭头及图标是近似显示；不能从未配置控件推断原生没有该行为，也不宣称Oct1下一月箭头的可见性/边界已验证。无事件图的右侧滚动条是重建图形，未实现连续滚动。Home局部差异仍开放。没有新增原生状态或成功动作，也不替代真人课程评估。
