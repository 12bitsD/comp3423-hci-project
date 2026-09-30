# Calendar 节假日详情与调用者返回 — 2026-09-30

当前Home→Week→月视图上下文已补接Sep26公共节假日详情及返回。Monday重复进入/返回、Tuesday详情后继续模式循环均实际回放。累计122个映射画板、284条控件、61次原型运行，全应用仍 `not_verified`。

## 原生依据和本轮连接

原生A-CALENDAR-EVENT-OPEN在Sep26节假日省略号进入详情（E-CALENDAR-EVENT），A-CALENDAR-EVENT-BACK返回相同日期和事件（E-CALENDAR-EVENT-BACK）。[原生详情](../../evidence/2026-09-28-full-audit/calendar-155243-public-holiday-detail.png)是公共事件，不含私人课表。此前独立详情42:479保留。本轮发现列表仍显示PolyULife运行，当前Wrapper路径连接再次超时；没有重启应用，也没有把发现结果当成可观察窗口或新增原生成功动作。

新增[详情591:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=591-19)，尺寸576×970、Clip content开启、位置2100,52000。源自已有公开calendar-holiday-detail.svg，文字/日期/边框/箭头可编辑，字体/图标近似，原生截图里的指针与背景边缘未复制。Back增加52×56透明点击区，为原型点击区域推广，不声称原生具有同样命中区域。[生成脚本](../../design/scripts/build_calendar_detail_context_svg.py)及[素材哈希](../../design/polyulife/calendar-detail-context-assets.json)可复查。

月视图573:19的EventMenu573:151 On click Swap overlay到591:19；详情Back591:29 Swap overlay回573:19，两者Instant，分别映射上述原生动作。详情替换原有month overlay，返回替换回同一个月视图，保持Week底层和Home调用者历史；这是Figma实现方式，不是原生架构证据。根检查显示Add flow starting point，没有新增独立Flow。[两条连接清单](../../design/polyulife/calendar-detail-context-connections.json)保存实际配置。

## 实际回放与检查

04–11从Monday Home进入Week、展开周选择器、转Sep26月视图，省略号进入详情，Back回月视图，再次进入详情并返回，最后走既有月视图Home恢复出口。12–18切Tuesday，重复进入月视图/详情/返回，随后Month→Events→History→Week→Home。进入与返回的日期、公共事件及Home调用者得到保存画面支持；模式Home恢复出口仍是原生未验证的推广动作。

八项原型裁片比较六项相等：Monday第一次和第二次月视图返回、重复详情、Tuesday月视图返回、两调用者详情及两调用者月视图。两个Home起点/终点不等，均在应用裁片内(22,588,358,613)；照片仍可见，但底部局部差异未解释，不能宣称完整视觉一致。[19张截图和比较清单](../../evidence/2026-09-30-calendar-detail/manifest.json)、[对照图](../../evidence/2026-09-30-calendar-detail/contact-sheet.png)记录实际文件。这些是原型一致性检查，不是原生像素保真或真人评估。

## 未完成范围

目前只有固定历史Sep26公共节假日详情，未接事件列表其它省略号，不能从此推断其它事件的标题、字段或返回逻辑。其它日期/筛选/空结果、Hide History、连续列表与边界、其他调用者、长期状态和完整手机操作仍未完成。Home局部差异保持开放。原生135状态/268动作（193 observed、75 not_attempted）保持不变；其中observed也包含未建立成功结果的尝试。
