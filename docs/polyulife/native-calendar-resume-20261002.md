# PolyULife 连接恢复与 Calendar 原生补查

2026-10-02 15:49–15:59 UTC（Asia/Shanghai 23:49–23:59），通过本次发现的 Wrapper 路径取得实际 PolyULife 窗口。版本 3.0.0 从本轮 AX 重新确认。保存26个截图状态及对应原始AX；公开版只包含脱敏画面和安全AX子集。应用沿用已有登录状态，没有重启、输入凭据、提交业务或分享数据。

[公开截图及清单](../../evidence/2026-10-02-native-calendar-resume/manifest.json)和[总览](../../evidence/2026-10-02-native-calendar-resume/contact-sheet.png)保留实际顺序。首次两个记录都曾使用序号02，但文件名不同、时间和步骤均保留；台账按实际顺序归一化为01–26，没有覆盖截图。`evidence/raw/2026-10-02-native-resume/`中的原始截图、完整AX、步骤JSON均被Git忽略。

## 实际操作和结果

| 保存步骤 | 动作和反馈 | 已确认范围 |
| --- | --- | --- |
| 01 | 恢复到 AG206 Room。日期栏显示Today02-Oct，结果标题仍为30-Sep (Today) | 恢复时两处日期并存；没有重新查询，不能判定底层结果日期或刷新后的行为 |
| 02–03 | Room Back→保留原Home位置，Home Calendar→October，选中Friday October2、全部类别和课程卡片 | 本次保留模式进入月视图；此前进入Week的记录仍有效，不能推断固定默认模式 |
| 04 | Filter弹层全部勾选 | AX的无名图标57首次点击只落在类别说明，没有界面变化；随后按截图点击可见Filter才打开，定位修正保留 |
| 05–07 | Select All清空全部；X关闭；重新打开 | X撤销本次草稿，返回原全部类别/课程卡片，重开仍全部勾选 |
| 08–10 | 再次全不选→Apply→重开Filter | 显示No Selected Event、No event、提醒启用全部筛选；点阵消失；重开仍全不选 |
| 11–13 | 单独Class→Apply→课程卡省略号 | 保留Class类别和课程卡；省略号进入课程详情，不是操作菜单 |
| 14–18 | Class Notice→加载标识→空白正文→More→Cancel→X | 网页容器地址栏显示校方域名的AR路径前缀。标识消失后正文仍空白；菜单含系统浏览器、Share via、Copy link。仅Cancel和X执行，X返回详情 |
| 19–23 | 详情Back→Class筛选保留；重开、清Class、选Exam、Apply | 返回October2 Class状态；Exam-only在这个日期显示No event |
| 24–26 | 重开Exam→清Exam→单选Payment草稿 | 已应用背景仍为Exam，Payment只在草稿中勾选 |
| 后续未保存 | 请求Payment Apply时工具报告Mac锁定 | 点击是否发出、结果和当前停留页面均未确认；动作标为attempted_unverified，先重新读取窗口，不能直接重复或写成成功 |

这里只验证10月2日样例，不代表其他日期没有考试/缴费事件。Notice文件名15中保留历史标签“loaded”，它的事实分类是**空白快照，成功加载未确认**；未提供原因判断。17/18的安全AX子集没有可用控件文本，返回判断依靠保存的截图与随后实际读取的详情AX。

## HCI事实、解释与验证

| 观察事实 | 问题假设与原则 | 下一步验证 |
| --- | --- | --- |
| Room恢复时日期栏Today02-Oct与结果30-Sep (Today)同时存在（01） | 可见系统状态的日期语义可能不清楚；也可能是保留旧查询。尚未验证实际数据或用户误解 | 重新查询、重新进入、跨日恢复；让真人解释当前查询日期 |
| Calendar实际Class卡片存在，但选中2日AX仍写“You have no entries for this day”；3日位于Sat列而AX称Sunday（03、09、12安全AX） | 状态/日期标签可能无法为辅助技术提供一致信息；不能直接推断普通视觉用户困难或所有读屏器结果 | 真机VoiceOver与读屏顺序、类别切换后事件播报，修正文案前复查 |
| 全不选会清掉卡片和点阵，并显示No Selected Event及提醒启用全部类别（09） | 筛选状态可见；空状态警示是否能让用户恢复查询，需要真人测试 | 测试用户能否辨认筛选导致的空状态、重开Filter并恢复类别 |
| Class Notice标识消失后页面空白，但X仍能返回（14–18） | 状态反馈可能不足；可能涉及网页/文档渲染或网络，原因未知 | 重新观察、Reload、内容可达性和系统浏览器对照；不以工具或一次空白定性App缺陷 |

已补入覆盖台账的20个日期/草稿/背景/详情状态。新增可见地图和网页菜单控件仍列为未尝试。旧“全部类别课程省略号”和Acad草稿X没有被本次Class-only、省略号及None-X执行替代为全覆盖。私人课程值、教师、时间地点及个人点阵已遮盖；原型使用合成DEMO。

## 接力

1. 先按skill发现当前运行路径并读取实际窗口。Payment结果未知，不能默认仍在草稿或已Apply。
2. 补Payment Apply及恢复原筛选；再验证Acad-X、全部类别省略号和完整类别组合。
3. 补课程地图、Notice正文/Reload和可逆菜单边界；Share不因分析任务自动获得发送授权。
4. 将Class/Exam/Payment与详情接入主Figma，并验证Calendar保留模式的Home/More调用者。当前新增[None参考原型](calendar-none-oct2-prototype-walkthrough.md)只覆盖一条分支。
