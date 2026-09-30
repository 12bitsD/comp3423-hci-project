# PolyULife 全应用观察与 Figma 复现

本次工作目标是通过 Computer Use 分析 PolyULife 中的每一项交互，并在 Figma 中复现完整应用及可点击流程。范围从实际界面动态发现，不以课程最低功能数量、首页或少量示例流程作为完成边界。

## 接力入口

1. 执行真实观察前读 [PolyULife skill](../../.agents/skills/polyulife-ui-analysis/SKILL.md)，需要恢复连接时按其中指向的参考文件操作。
2. 以 [coverage.json](coverage.json) 为当前覆盖台账，优先处理 `discovery_queue` 和已有动作中的未确认结果。台账条目必须回链本次实际证据。
3. 按下方流程发现、记录和复查。准备建立 Figma 页面、组件或连接时读 [figma-spec.md](figma-spec.md)。
4. 新会话先核对实际 App 页面、版本和工具连接，再恢复台账。台账中的历史观察不能替代本次状态确认。

## 当前进度（2026-09-30）

Room查询和AG206地图样例已归入正式台账：**108个Figma画板、3个画板内组件状态、244个配置控件、10个滚动区域及39次原型运行**（包括失败记录）。查询新增七个日期/聚焦变体、五条连接和两条实际Present回放，见 [查询回放](room-query-source-preparation.md)；地图新增三个部分可编辑画板、六个控件及失败/修复后运行，见 [地图回放](room-map-prototype-walkthrough.md)。新增[七日选择、筛选保持与列表边界的原生实测](room-dates-20260930.md)后，当前原生为132个状态、268个动作（185 observed、83 not_attempted）。本批12张日期/筛选变体已导入、12个控件与Today连续列表已实跑，见[七日原型回放](room-dates-prototype-walkthrough.md)；Tuesday 已替换为连续横向滚动，并完成两次 Today 返回，见[连续日期条回放](room-horizontal-dates-prototype-walkthrough.md)；Saturday、Sunday、Monday也已补为连续条并实跑移动后按钮命中，见[三个日期上下文回放](room-date-contexts-prototype-walkthrough.md)；其余六个准备中的上下文、Home和其它交接待完成。变体和原型回放不增加原生观察数量。全应用完成状态保持 `not_verified`。

已通过 Computer Use 完成一轮 [Room Finder 实际走查](room-walkthrough.md)：输入与无结果、AG206 联想查询、ALL/Available 筛选、Preview 网页与照片轮播、日期异步更新、AG206 地图缩放以及返回 Home 的基本路径。Room 其它分支和边界仍在发现队列，不能称为全部交互已覆盖。

[HCI 候选问题](hci-findings.md) 将观察事实、相反证据、问题假设、设计建议与真人待验证事项分开记录；这些建议不会覆盖原应用复现。

[首页导航局部截图](../../evidence/2026-09-28-full-audit/home-134424-navigation-only.png)已确认 Map、Room、Food、Apps、Study progress、My Courses，以及底部 Home、Calendar、QR 图标、Notification、More 可见。首页完整内容和各目的页分别登记，入口可见不等于流程通过。实际动作、状态和未完成项见 [coverage.json](coverage.json)，截图清单见 [manifest.json](../../evidence/2026-09-28-full-audit/manifest.json)。

原生 App 已包含 [2026-09-29 Room补查](room-recheck-20260929.md)及[2026-09-30七日选择](room-dates-20260930.md)，已有132个状态、268个动作记录。185个 `observed` 表示真实尝试或反馈被记录，也包括未建立成功结果的工具定位尝试；不等于所有动作通过，仍有83个 `not_attempted` 动作。

- [More、天气与 Virtual Assistant](more-walkthrough.md)：天气图片展开/关闭和返回 More；虚拟助手详情、Disclaimer、Welcome 与返回；聊天输入仍未通过，没有发送消息。
- [Calendar 与 Notification](calendar-notification-walkthrough.md)：校历筛选、公共事件详情/返回、视图切换、月份、通知空态、搜索与清除。个人课表不公开。
- [侧边菜单与 Settings](menu-settings-walkthrough.md)：只读设置/Profile、紧急提示关闭、隐私/条款加载与返回。没有切换设置、呼叫或退出登录。
- [Food](food-walkthrough.md)：VA210 营业时间、标签搜索、地点详情、图片展开/关闭、全屏地图平移/返回；详情→Search→原详情→列表的返回栈、列表面板展开/滚动、H Café营业时间和Online Order外链提示关闭。外站未打开，其它地点和完整边界仍待查。
- [Apps](apps-walkthrough.md)：All及六个分类、VRS详情→内嵌网页→空NetID登录页→X→详情Back并保留Campus，以及拖动分类栏后Job保持选中，再点击All。后续Apps Back→Home也已补测。未输入凭证；其它服务、完整列表和登录后内容待查。11张Apps源码已导入，12个分类/VRS连接样例实跑；缺失中文已修复并复验，加载帧与其余边界未运行。

- [Study progress、My Courses、主 Map、QR 与 Home](home-study-map-walkthrough.md)：长名称展开/收起、Requirements公开目录、Canvas/Blackboard和空登录页返回、六个地图类别及多选/设施详情/返回、饮水站列表滚动、QR显示与Home返回、Home日期/My Class周历及选择器尝试。个人课程和日程不公开；二维码与身份整块遮盖。

Study搜索输入后空白、主地图平移/面板拖动/标记点击、周选择器应用新周数尚未确认成功；所有模块仍保留未测控件与边界。Apps中的Study分类与Home的Study progress分别记录。Home的Notification、Calendar、Search、Menu及各自返回已补测；底部Calendar实际落在Week5。当前108个画板已登记Figma映射（另保留旧检查点和菜单裁片等历史源码），个人课程和日程使用明确的DEMO资料，二维码不可扫描。

七份公开清单合计970个PNG文件（主清单836、查询回放8、地图回放26、七日选择20、七日原型20、连续日期条30、日期上下文30，含拼图），文件哈希和尺寸已校验；私人原始图不提交。图片数量不作为覆盖率或成功率。

真实 [Figma Design 文件](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/)已新增 `01 · Observed UI`：四张 576×970 Room SVG 设计源码已导入为原生可编辑图层，并建立[当前 Room 样例原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-198&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A198&show-proto-sidebar=1)。独立标签页已复验 **A 样例 → AG206 → Available → ALL** 四步。旧草稿已置于 `00 · Archive — initial AI draft`（原 `Page 1`），其三条旧连接记录保留为历史。

另一条[天气样例原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=12-435&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=12%3A435&show-proto-sidebar=1)已在独立标签页实跑 **More → 天气详情 → 图片展开 → 详情 → More** 四步。原生 App 天气返回也有独立证据；天气正文链接前排版仍稍挤，视觉保持近似，未称逐像素一致。

同一 More 原型的 Virtual Assistant 分支已跑通七条导航和“点免责声明正文不跳转”的负向检查；但从 Welcome 关闭网页返回详情后，头图重复变空白，重载恢复后再次重走仍复现。因此 **VA 导航样例通过，视觉验收未通过**，问题保持未解决；不把它归为原 App 的缺陷。具体步骤、图像证据和来源状态差异见 [Figma 验证记录](figma-spec.md)。

[Calendar 公共校历原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=42-165&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=42%3A165&show-proto-sidebar=1)已实跑 **13条连接、10张固定状态**，包含公共假期详情与返回、列表/历史、月份切换、Acad/All/None筛选选择和Acad Apply。分支间的 Figma Restart 只记为测试重置。其它日期、周视图、Hide History、All/None Apply与筛选关闭等尚未全部接入；筛选背景合成和整卡热点相对原生省略号的范围差异已保留。

[Food 原型](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/PolyULife-%E2%80%94-Observed-UI-and-Interaction-Atlas?node-id=50-1911&t=u9E3LqVQD7AiByx8-0&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=50%3A1911&show-proto-sidebar=1)的 **11个连接控件**已实测导航，包括图片/搜索/详情/地图四个按历史返回的Back。详情→搜索→原详情→营业时间列表的栈已复现；直接详情入口和返回也已独立复测。列表/详情的图片仍出现重复缺失与恢复，因此 **Food导航样例通过、整体视觉未通过**。未展开列表的原生详情入口及加载态差异保持待核实，地图平移帧尚未接入。

截至Room Sunday批次，`01 · Observed UI` 当前映射 **86个Frame、3个画板内组件状态、217个配置控件，另有4个垂直和1个水平滚动区域**；其中连续滚动批次复制的10个功能入口实例已逐一回放，五个模块初始页Back已补接并验证Monday/Tuesday直接返回；Study/Courses既有内部路径现已验证保留三个Home来源，Map既有样例内部绕行也已验证；Room/Food内部绕行及未实现分支仍待完成；新增菜单15个控件已回放，导航通过、视觉仍有缺口。Home/Study/Courses/QR此前22个连接样例已实跑；后补原生证据发现Home Calendar原先目标不符，现已改为Week5 DEMO，并验证Calendar往返两步，新增一个返回控件。Apps/Courses的中文缺字已修复并定向复验。Home装饰图仍有消失/恢复，VA和Food的缺图问题也保持open，不能称整体视觉通过。

[Home日期与返回](home-date-prototype-walkthrough.md)已验证Monday→Tuesday，以及My Class、Calendar、Menu、Search、Notification往返保留周二；既有功能区Calendar/Search返回已回归通过。Week/Notification Home当前使用Back，只覆盖实测Home来源，其它来源与直接起点行为未实现。[Home连续滚动](home-scroll-prototype-walkthrough.md)已在Monday/Tuesday两页实现并回放日期区与功能区之间的移动、中间位置和反向滚动；原生完整滚动边界未验证，范围由两段样例推导。[Apps返回栈](apps-return-prototype-walkthrough.md)已将分类改成同层切换，详情与登录逐层关闭；Tuesday完整分类/VRS链、Monday七个分类状态各自Back及历史Home往返均保留来源与滚动位置。[可见分类互跳](apps-category-prototype-walkthrough.md)已新增并实跑33个连接，VRS与Monday原滚动位置回归通过；完整分类条滚动、原生来源组合行为与独立Apps起点退出仍未完成；七个新增分类Back为基于已观察Apps返回行为的原型推广，未新增原生验证。Apps加载、Food平移地图及Home其它日期仍未运行；搜索输入/结果等内部控件仍待查。菜单已使用完整DEMO抽屉，紧急提示背景等仍有缺口，个人页面使用合成资料；具体边界见 [Figma节点与验证记录](figma-spec.md)。自由输入、其它日期、清空、Preview、地图、滚动及其余状态尚未全部连接，不能称Room或全应用完成。Agents免费每日额度用尽后没有付费；普通SVG导入和手动连线继续可用，总页数控制在三页以内。

早期捕获问题及 14:36:37 UTC 的 Mac 锁屏已经恢复：15:45:15 UTC 起重新取得真实 App 截图，随后多条原生导航成功。旧锁屏记录保留为环境历史。2026-09-29首页日期批次重新检查时，Computer Use再次提示Mac锁定，用户回复恢复后仍未取得新原生状态；该环境阻碍单独登记为B-MAC-LOCKED-HOME-DATE，不归为PolyULife缺陷。2026-09-30通过全屏切换及退出恢复正常原生截图并完成Room实测，该阻碍已标为resolved，历史根因仍未知。Figma独立工作继续；全应用覆盖与原型完成仍未获验证。

## 观察循环

1. **记录会话**：填写时间、App 版本、系统与运行方式、登录状态的概括和起始位置。仅存环境信息，不写个人姓名、学号、通知正文、账号或二维码内容。
2. **确认状态**：用 Computer Use 读取真实窗口和截图，按视觉内容登记 `state`。AX 用于补充文字与定位；只在 AX 中出现的文字先列为入口线索。每个独立页面、弹层、菜单、选中项变化、滚动分段、加载、空白或错误状态都以真实变化判断是否需要单独记录，不按想象补齐。
3. **枚举可操作项**：检查可见按钮、标签、链接、卡片、输入、筛选、滚动区域和返回方式；对观察到的每个控件登记 `action`，新目标加入发现队列。滚动后再检查新增入口，并保留与原状态的关系。
4. **操作并核对**：从最新状态定位，执行一步，记录实际反馈、目标状态、证据和返回路径。没有变化同样记录，不把工具定位失败直接当成 App 缺陷。预约、资料变更等有业务后果的提交以实际授权为前提；不能执行时记录准确阻碍与待补动作。
5. **扩展覆盖**：沿新发现的内部页面、内嵌 Web、外部跳转、登录或权限提示继续登记。应用内入口及跳转结果属于本次范围；外部独立产品的进一步研究边界必须显式记录。遇到账号、硬件或业务条件限制，保留未完成项，不静默排除。
6. **形成分析与复现**：把有证据的事实、问题假设及待验证事项分别写入 `findings`；在 Figma 按状态建立节点，按实际动作建立连接。回到原型实际运行，逐条复走并记录结果。
7. **回查入口**：对已访问状态复查菜单、各标签、滚动末端和返回路径。记录本次复查范围与新发现入口；持续迭代到未检查入口清零，且所有阻碍都有解决证据。

## 台账约定

`coverage.json` 保存结构化索引；共享证据遵循 [证据规范](../../evidence/README.md)。大段观察记录可以放入独立证据文档，通过相对路径引用，不把整段 AX 或个人原始截图嵌入 JSON。

| 集合 | 用途及最小记录 |
| --- | --- |
| `sessions` | `id`、`started_at`、`environment`、`starting_state_id`、`evidence_ids`；环境记录 App/系统版本、运行方式及非个人化登录状态 |
| `entry_points` | `id`、可见标签、发现来源、所在状态、复核状态、关联动作；未知状态用 `null`，保留原始历史来源 |
| `states` | `id`、会话、页面标题、状态说明、可见范围、前置条件、截图证据、AX 证据、控件动作列表、发现是否已检查；列出未确认事项 |
| `actions` | `id`、起始状态、控件/手势、输入概括、实际执行记录、观察反馈、目标状态、证据、返回路径、授权状态和阻碍；可重复执行但每次单独留执行记录 |
| `evidence` | `id`、类型、相对路径、会话、采集时间、所证实的状态/动作、脱敏说明；截图引用需对应真实文件 |
| `findings` | `id`、观察事实、关联状态/动作/证据、问题假设、HCI 原则及因果解释、建议、待真人或真机验证事项 |
| `figma` | 文件 URL、状态到节点和组件的映射、动作到连接的映射、复现偏差及验证记录；节点 URL 必须在实际创建并检查后填写 |
| `discovery_queue` | 入口线索或待检查状态、待执行动作、加入原因、处理状态和实际解决引用；只是队列清空不能证明完整覆盖 |
| `blockers` | 所影响状态/动作、已验证的条件、缺失依赖、下一步；存在阻碍时相关能力保持未完成 |
| `closure_reviews` | 真实复查的会话、状态/菜单/滚动范围、发现的新增入口、证据；初始空数组表示尚未复查 |

标识稳定且唯一，例如 `S001`（状态）、`A001`（动作）、`E001`（证据）、`F001`（分析）、`R001`（复查）；重新截图可新增证据并保留旧引用。`null` 表示未确认或未创建，空数组表示当前没有记录；两者都不能解释为已通过。

记录状态使用明确的阶段词：入口为 `pending_revalidation` / `confirmed_visible` / `confirmed_unavailable`；动作可为 `not_attempted` / `observed` / `blocked`；队列可为 `pending` / `in_progress` / `resolved`。`confirmed_unavailable` 和 `blocked` 需理由及证据，它们不计入成功覆盖。原型验证只能为 `not_run` / `passed` / `failed` / `blocked`，通过需指向实际运行记录。

## 完成判定

每项能力都需要以下独立证据，不能用文件存在或清单勾选代替：

| 能力 | 完成证据 |
| --- | --- |
| 实际观测 | 当前环境中的状态记录，及可定位到该状态的真实 Computer Use 观察证据 |
| 视觉证据 | 对应状态的可读、脱敏截图；AX 文字单独不能满足视觉验证 |
| 动作及反馈 | 实际起点、执行动作、结果和返回路径，含有条件可达的边界状态；每个发现控件均已处理 |
| HCI 分析 | 事实与假设分离，关联具体证据及适用原则，未知事项明确保留 |
| Figma 节点 | 真实文件中可查看、可编辑的节点，覆盖状态结构、内容与关键视觉关系；占位或导入计划不算节点完成 |
| Figma 连接 | 每个已观察交互对应可运行连接、组件交互或明确的复现限制；关键输入/反馈和返回路径可操作 |
| 原型验证 | 在实际 Figma Present 中按动作清单复走，记录起点、预期、实际结果与证据，失败已修复并复验 |
| 全应用覆盖 | 入口检查与滚动/菜单复查有记录，队列无未检查项，阻碍已解决，所有状态/动作均满足对应能力 |

完整交付仍受实际可观测性约束：未登录分支、特殊账号权限、硬件能力或不能安全触发的业务状态一旦发现，必须在台账中保持明确缺口。先完成可执行部分、持续补齐缺口；未经验证的部分不标为全应用完成。Mac 观察与原型不能替代手机触控体验或课程要求的真人 Maze 测试。

校园地图新增12帧、20控件，地图批次截止时总计75帧/94连接；导航样本逐条通过，图片显示仍有未解决项，详见[地图原型回放与分类栏补测](map-prototype-walkthrough.md)。初始底图直接PNG替换后两次返回可见，不能据此关闭其他图片问题。

## 菜单与设置增量

[菜单原型记录](menu-prototype-walkthrough.md)：完整 DEMO 抽屉、Mac General 交接、15 个菜单控件已实际回放，当前76个映射画板、110个控件，另登记2个画板内 cookie 关闭状态。通知页与Home的菜单关闭分别回到来源页。政策初始文字裁切与 cookie 关闭已修复并回放；滚动、加载、弹层背景及标志图片稳定性仍未完成；全应用目标保持 `not_verified`。

[政策 cookie 原型复验](policy-cookie-prototype-walkthrough.md)：记录共享组件串联失败、独立组件修复，以及关闭提示后保持菜单返回路径的实测证据。

[Home十个入口与直接返回](home-feature-return-prototype-walkthrough.md)：十组直接往返和首页像素比较通过；Tuesday Food缺图复现，视觉仍未通过。

[Study/Courses样例返回原首页](study-courses-return-prototype-walkthrough.md)：三来源六条链路、Tuesday八个外层出口和12次返回像素比较通过。原生中间状态出口仍待核；Map/Room/Food内部绕行及其它未实现分支保留。

[Map来源保留与逐层返回](map-return-prototype-walkthrough.md)：Tuesday全部十个外层出口、Monday/legacy代表路径通过；重复进入底图缺失复现，独立Map起点无Home调用层的退出失败已记录。

[Map底图重新上传](map-image-repair-walkthrough.md)：8个筛选页在连续两轮Monday首页路径中均可见；其它来源、长时稳定性、Home/Food图片及独立Map退出仍未完成。

[Room来源保留](room-return-prototype-walkthrough.md)：三个Home来源已验证，Tuesday四个出口通过；三个新出口仍为原型推广，独立起点退出、完整Room及Food绕行未完成。

[Food来源与分层返回](food-return-prototype-walkthrough.md)：三个Home返回像素一致；深层标签/重复详情返回通过。图片不稳定、独立出口和完整Food未完成。

[Food图片重新上传](food-image-repair-walkthrough.md)：14项填充保留原图内容；连续两轮Tuesday深层路径图片可见，问题部分解决，其它来源和长时稳定性未验证。

[Food H Café原型](food-hcafe-prototype-walkthrough.md)：新增4个已观察视口、11个控件。修复提示框内部误关闭，四侧遮罩关闭及三种Tuesday Home返回已复测；连续列表、其它来源、收起与外站Open未完成。

[Room Preview原型](room-preview-prototype-walkthrough.md)：新增3个Frame、1个照片组件状态、6个控件和1个竖向滚动区域。菜单取消、照片Next、四次Available及Tuesday Home返回已验证；完整网页、原生重开语义和完整视觉验收未完成。

[Room Sunday原型](room-sunday-prototype-walkthrough.md)：新增3个Frame、7个控件，Available日期条及Sunday ALL列表可连续滚动。过渡/空态/ALL与三个推断出口通过Tuesday来源样例回放，完整日期和列表边界、地图及查询仍未完成。9项像素比较中7项相等，2项日期基线差异保留。

### AG206 地图制作中的检查点

[三个地图画面及剩余连接/回放步骤](room-map-work-in-progress.md)已保存，尚未计入正式覆盖统计；没有新增原生观察或回放通过记录。

[2026-09-29 Room原生补查](room-recheck-20260929.md)：新增16张公开截图，确认地图返回的列表位置、无匹配查询及清空/再搜索反馈。地图WIP现有六个连接，Present仍未通过。最新原生124状态/265动作（181 observed、84 not_attempted），正式Figma统计不变。

[Room查询Figma样例回放](room-query-source-preparation.md)：七个有原生截图依据的可编辑SVG已导入Figma。AG206联想→Today ALL及无匹配搜索→聚焦→清空→再搜索两条Flow已在Present回放并保存七张公开截图，正式映射与运行已归档；静态输入、其余日期/房间、完整视觉和整App覆盖仍未验证。

2026-09-30连接复查：原生AX仍可读取首页，但截图仅返回倾斜缩略图，Window菜单选择当前窗口后仍未恢复正常图像；原因未确认，未新增原生状态或动作。Figma编辑器可读取本批七个画板，已有样例归档继续推进。

[AG206地图样例回放](room-map-prototype-walkthrough.md)：Tuesday Home→Sunday ALL下滚→Location→放大代理→缩小代理→Back→Home已实际走通，初始/放大Back亦已验证。25张裁片保留一次初始底图重入缺失；重传同一PNG后初始地图三次重入可见。11个像素检查8等、3不等，五个列表返回及Home返回全部相等。地图仍为截图素材和方向键代理，完整可编辑地图、自由平移、真实缩放边界及外部交接未完成。

[2026-09-30 Room七日实测](room-dates-20260930.md)：19张原生脱敏截图确认七日选择、筛选保持、日期条反向拖动、Today列表末行与反向返回。当前原生132状态/268动作，Figma仍96画板/228控件/36次运行；新增日期状态等待复现。全应用保持 `not_verified`。

[September30 Room日期原型](room-dates-prototype-walkthrough.md)：12张1026px画板、12个控件及Today连续列表已实际回放；独立末端画板仅作参考。当前108画板/240控件/37次运行，日期条连续滚动及完整来源/返回仍待完成。
