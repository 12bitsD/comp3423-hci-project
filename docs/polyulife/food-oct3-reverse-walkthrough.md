# Food October3：营业时间往返与完整列表采样

2026-10-03 通过 Mac Computer Use，从`workshop` Search返回已读Notification，再从Home进入Food。当前列表首项为Block Y，H Café显示Open Now，与历史夜间VA210首项/Closed H Café样本不同；原因和排序机制未隔离，不替换历史证据或直接推断排序规则。

保存26次实际原生采样：[清单](../../evidence/2026-10-03-food-reverse-controls/manifest.json)、[联系表](../../evidence/2026-10-03-food-reverse-controls/contact-sheet.png)、[输入与像素比较轨迹](../../evidence/2026-10-03-food-reverse-controls/input-trace.json)。两张Home只公开下方导航裁片，私人上半页和完整AX不公开。以下编号是公开截图前缀。

## 已观察的路径

| 路径 | 证据 | 实际结果与边界 |
| --- | --- | --- |
| Workshop Search Back → Notification → Home → Food | 00–03 | 从通知调用者退回并进入Food。Home下方Food入口/选中Home可见，不证明私人日期、日程或完整Home保真 |
| Block Y营业时间展开 → 收起 | 03–05 | 展开显示Mon–Fri、Sat、Sun/public holiday三行；收起移除三行并恢复后续卡片位置 |
| Food手柄向上拖 | 05–06 | 面板上移至标题下，更多列表卡片出现。06与后来稳定首项视口有位置差异，保留采样，不声称逐像素复位 |
| H Café Open Now营业时间展开 → 收起 | 07–09 | 显示当前Mon–Fri/Sat/Sun时段，再收起。历史Closed H Café的反向动作仍未验证 |
| 列表持续下移 | 06–07、10–13、16–17 | 从Block Y穿过餐厅、咖啡店和售货机至Gourmet Shop。28个条目标题均有可见截图依据，具体卡片功能没有全部操作 |
| 指定VA210营业时间展开 → 收起 | 13–15 | 用红色原味品牌图标及Chinese Soup/Snacks/Bottled Herbal Tea标签识别该条目；展开Mon–Sun/public holiday00:00–23:59，再收起。补查`A-FOOD-HOURS-COLLAPSE`，不推广到其它同名机器 |
| 最后卡片后再次下移 | 17–18 | Gourmet Shop仍为末项，两张完整原始截图像素相等。支持当前列表的有限下边界，不证明其它数据/窗口/手势也相同 |
| Gourmet Shop Further information展开 → 收起 | 18–20 | Closed状态下显示Mon–Fri08:00–19:30、Sat–Sun/public holiday Closed；再收起。没有打开外站或订单 |
| 反向滚动与上边界检查 | 20–22 | 回到Block Y首项；额外上滚保持同一内容。21/22原始正文差异限于小块光标区域，仍保存完整差异；不宣称整图相等 |
| 手柄向下拖及无输入复查 | 22–24 | 面板仍保持展开，无已确认收起结果。`A-FOOD-SHEET-COLLAPSE`记`attempted_unverified`，不能归为确定业务缺陷 |
| Food Back → Home | 24–25 | 返回Home导航区域；共享证据只有公共下方裁片，用户登录与业务记录未改动 |

8项原始正文裁片比较保留在轨迹中；只有17/18相等。营业时间往返的内容恢复有截图和AX依据，其像素比较仍可能包含光标差异。06/21的位置差异原因未隔离；不用扩大容差掩盖失败，也不以像素比较代替状态判定。

## 28条当前场所记录与交互发现

[可见依据目录](../../evidence/2026-10-03-food-reverse-controls/venue-catalogue.json)逐条保存标题、公共AX描述、实际可见截图和研究编号。研究编号用当前行顺序区分，不是App或后台业务ID。AX聚合头像文字会把H/L加在Homantin Hall Canteen/LibCafé前；可见名称单独核对，不把头像字母当场所名称。

| 当前记录组 | 可见截图 |
| --- | --- |
| Block Y、Communal Staff/Student Canteen、Communal Student Restaurant | 06 |
| H Café、Homantin Hall Canteen、LibCafé | 07 |
| Theatre Lounge、The Forest、U Garden、V Café | 10 |
| VA Café、VA Kiosk、VA Staff Canteen | 11 |
| VA Student Canteen、W Kiosk、X Café | 12 |
| Z Canteen、Z Café、前两条VA210 | 13 |
| 其余三条VA210、Global Student Hub售货机 | 16 |
| 两条Block R、Gourmet Shop | 17 |

5条VA210同名同地址，品牌插图与标签不同；2条Block R同名同地址，也有不同图标/标签。后续详情、菜单、标签及素材不能仅按标题合并。列表上的营业时间箭头、无文字省略号和横向截断标签是独立入口；H Café和U Garden的Online Order可见。除本页明确执行的时间/信息动作外，其余条目控件仍待查，没有因为列表末端到达就宣称Food交互完整。

## HCI 事实、假设与待验证

| 观察事实 | 问题假设 | 待验证 |
| --- | --- | --- |
| 多张卡片的标题与地址相同，品牌图标/标签不同 | 按标题寻找具体机器时可能需要额外辨认；关联“识别而非回忆”与信息辨别。当前差异也可能足够，不能直接定为缺陷 | 真机中可见品牌/商品是否足以识别；Search结果如何区分这些条目；真人选择任务 |
| Closed Gourmet Shop使用Further information，展开后是营业时间 | 标签是否让用户预期其它详情，尚无用户证据；关联入口文案与结果匹配 | 真人对文案的理解、其它Closed场所、下一次开放时间的任务 |
| 同一手柄上移有效，下移尝试没有确认结果 | 原因可能与输入/手势/面板状态有关，未隔离；只保留失败事实 | 明确当前交互能力后做一次针对性恢复，必要时手机真机验证；不能把Agent失败当触控可用性指标 |

这些是本批假设，未增加正式候选问题数量。Mac鼠标、Agent采样和等待不能替代手机触控/真人Maze评价。

## Figma 接力与完成边界

Figma本轮未改动，正式仍201映射画板、436控件、136次运行，另有前一轮946:19加载草稿未配置。上轮Action下拉框的浏览器安全拒绝没有新的解除证据，本轮未重试或绕过。已有历史Food页面与Closed H Café保存原调用者与数据；当前28条列表、Block Y/Open H Café/Gourmet Shop的状态和滚动应建立明确的新数据上下文，不能覆盖旧证据。

下一步按目录和原生截图重建可编辑行组件、公共图片裁片、标签裁切和连续滚动；所有省略号/详情/标签先取真实行为证据，再配置连接。面板收起未验证，不构造必然成功返回。需要回放当前Food入口、三组营业时间往返、末端/反向滚动、Gourmet信息和Home返回，并单独标记原型能力差异。

新增13个当前原生视口状态、13个有反馈动作；追加既有Search Back、面板展开、VA210展开/收起执行。当前25会话、194状态、364动作（277 observed、78 not_attempted、9 attempted_unverified）；2517条证据，60份公开清单含2292个PNG。聚合`A-FOOD-LIST-BOUNDS`虽有有限上下边界证据，仍因其它场所/手柄范围未完成而保留`attempted_unverified`。新发现队列记录28条卡片的剩余控件；完整应用及视觉保真保持`not_verified`。

哈希、尺寸、引用、公开文字敏感模式、旧证据/状态/历史执行保存及`git diff --check`通过。结构校验只验证记录一致性，不能证明全应用、全部数据或Figma完成。
