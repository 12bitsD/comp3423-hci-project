# Assistant 中间状态素材与接入边界 — 2026-09-30

补齐已有原生证据中的三种中间状态，完成可编辑SVG和本地渲染检查。**尚未导入Figma、未连线、未回放**，Figma仍为128映射画板、299配置控件、64次运行，全应用 `not_verified`。素材准备不增加原生观察或原型成功数。

| 原生状态与证据 | 新设计源码 | 已确认内容与限制 |
| --- | --- | --- |
| S-ASSISTANT-BEFORE-HERO / E-ASSISTANT-BEFORE-HERO | [头图出现前](../../design/polyulife/virtual-assistant-before-hero.svg) | 原生文字位于顶部，头图和展开图标尚未出现；根据已加载版可编辑正文向上移动203px重建。没有预留空头图，不把两次截图间隔当成延迟测量 |
| S-ASSISTANT-WEB-LOADING / E-ASSISTANT-WEB-LOADING | [网页加载中](../../design/polyulife/virtual-assistant-web-loading.svg) | 内嵌浏览器标题为空、正文中央有校徽、底部地址栏可见。校徽为原生公开截图的56×58裁片；没有编造spinner动画、成功时间或错误反馈 |
| S-ASSISTANT-WEB-BLANK / E-ASSISTANT-WEB-BLANK | [原因未明的空白网页](../../design/polyulife/virtual-assistant-web-blank.svg) | 顶部COMP Virtual Assistant与浏览器控件可见，正文空白。没有添加AX中提及但截图未见的输入框；该状态不证明输入功能不存在或App崩溃 |

原始公开截图及动作见[More走查](more-walkthrough.md)。[生成脚本](../../design/scripts/build_assistant_transient_svg.py)沿用已有可编辑header/正文/浏览器图层，保留文字、Back、here、X、More、地址栏和刷新等分组；除加载校徽之外没有栅格内容。字体、矢量图标、正文换行、底部边框和背景仍为近似，鼠标指针/光晕未复制。[素材与来源哈希](../../design/polyulife/virtual-assistant-transient-assets.json)及[渲染清单](../../evidence/2026-09-30-assistant-source-preparation/manifest.json)可复查。本地Sharp渲染图用于检视素材，不是Computer Use截图或Figma导入证明。

## 接入顺序及不能推定的行为

1. 用Computer Use恢复现有编辑器的有效点击和截图，核对当前文件与页面。导入三份SVG并检查576×970、可编辑图层及Clip content；取得实际节点ID后才能新增state_node_mappings。
2. More卡片的原生入口先到BeforeHero，再出现Detail；当前直接到Detail的连接省略了布局变化。准备替换入口并添加加载转换；Figma演示延时必须单独标为代理，不能当作原生延迟测量。正文here在加载前的位置和移动后的位置分别检查。
3. Detail→here的原生链路先有WebLoading，再到Disclaimer。接入中间状态并保留原有Disclaimer/Welcome后续连接；原生浏览器loading阶段的X没有独立验证，任何提前退出若配置，应 `action_id:null` 标注为推广。
4. WebBlank暂作为观察参考。A-ASSISTANT-FOCUS-INPUT是真实工具尝试，责任来源未明，不能直接把“点击可见输入框→空白”当作产品行为来连线。该参考状态的X→Detail有原生AX关闭证据，但没有独立返回截图；接入后仍需实际Figma回放和原生补查。
5. 从More和Home来源回放加载、布局变化、Disclaimer/Welcome、原型恢复和图片返回；保留原先缺图失败及新旧连接历史。待验证聊天/问号/文章滚动/网页controls仍在Q-MORE-REMAINING，不由这三张素材关闭。

## 本次环境与待续

现有Present同一句柄的AX+截图和浏览器screenshot均返回采集失败；DOM仍能读到原型controls，不能读取实际画布内容。编辑器DOM可读到筛选图层，点击None行后仍选中原Sep28 Filter，不能声称目标已切换；未继续按旧坐标修改。

实时发现列表仍有运行中的PolyULife与同bundle非运行安装项。按bundle发现当前Wrapper完整路径后连接超时，未重启应用。只确认运行项和可读DOM，不确认原生窗口或Figma画布可操作。本次没有新的原生动作、Figma修改或原型运行。筛选最后Home返回、Tuesday及Flow3清理检查仍待恢复后继续，见[筛选检查点](calendar-filter-context-prototype-walkthrough.md)。
