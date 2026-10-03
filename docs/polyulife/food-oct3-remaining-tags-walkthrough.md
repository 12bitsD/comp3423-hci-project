# Block Y 余下五个标签与调用者返回

2026-10-03 用户解锁后，Computer Use 再次取得真实 PolyULife 截图及 AX，起点仍为已有 Block Y 顶部详情。沿用已记录的 App 3.0.0，本批没有重新打开版本页。保存24组实际截图/完整 AX；公开版本裁去标题栏，仅保留公共场所、查询和校园地图。没有凭据、订单、电话、定位权限或资料提交。

证据：[原生清单](../../evidence/2026-10-03-food-remaining-tags/manifest.json)、[首次采样联系表](../../evidence/2026-10-03-food-remaining-tags/contact-sheet.png)、[重复采样联系表](../../evidence/2026-10-03-food-remaining-tags/repeat-contact-sheet.png)、[首次输入轨迹](../../evidence/2026-10-03-food-remaining-tags/input-trace.json)、[重复轨迹](../../evidence/2026-10-03-food-remaining-tags/repeat-input-trace.json)。原始完整 AX 留在忽略目录；公开叶节点不证明屏外记录可见。

## 观察事实

| 标签与实际动作 | 截图 | 反馈与边界 |
| --- | --- | --- |
| Asian Cuisine、Back、重复 | 00→01→02；14→15 | 查询自动显示 Asian Cuisine，6条结果；返回顶部详情。没有任意文本输入或其它结果详情测试 |
| Western Cuisine、下滚、Back、重入 | 03→04→05；16→17 | 共11条结果；04显示末项 VA Café。16稳定重入显示同一结果次序。没有确认连续列表完整边界或推广滚动恢复规则 |
| Taiwanese Cuisine、自身结果、逐层返回 | 06→07→08→09；18→19 | 唯一结果是 Block Y；打开另一个详情实例，07内嵌地图显示加载标记。Back回保留 Taiwanese Cuisine 的搜索，再Back回原详情顶部。未保存嵌套详情地图加载完成样本，不能推断加载时长 |
| Cake / Dessert、Back、重复 | 10→11；20→21 | 查询文字含斜线，6条结果；返回详情顶部 |
| Salad、Back、重复 | 12→13；22→23 | 查询 Salad，7条结果；返回详情顶部 |

本批五个标签均从顶部详情触发，因此这些返回样本只证明当前调用者和位置。此前 Sandwich 从较低详情触发后回顶部、地图返回较低位置的记录仍分别保留，不能合并成统一恢复规则。Taiwanese 自身结果产生的嵌套详情与原始详情也不当作同一个调用层。

首次06、10等画面包含进入过程中的宽度变化，长标题暂时折行；07内嵌地图仍显示加载标记。另行读取AX后重复进入五个标签，补采14、16、18、20、22稳定画面，没有手工等待或测量加载延时。首批14张图原样保留，不以稳定图覆盖。七项原始正文像素比较全部不等，记录保留光标、地图与过渡差异；不据此认定产品缺陷或完整视觉一致。

## Figma 实际导入

[生成器](../../design/scripts/build_food_oct3_remaining_tags.py)依据稳定原生样本生成五份有限查询源稿，再通过 Figma UI 剪贴板导入。每个根 Frame 的576×1024及X/Y均读取，节点链接通过根层菜单复制。仅导入可编辑结构，没有配置标签跳转、结果行或Back，没有新增Present回放。

| 查询 | 实际根节点 | 位置 |
| --- | --- | --- |
| Asian Cuisine | [954:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=954-19) | 0,92000 |
| Western Cuisine | [954:59](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=954-59) | 700,92000 |
| Taiwanese Cuisine | [954:119](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=954-119) | 1400,92000 |
| Cake / Dessert | [954:139](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=954-139) | 2100,92000 |
| Salad | [954:179](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=954-179) | 2800,92000 |

证据：[实际编辑器清单](../../evidence/2026-10-03-food-tag-import/manifest.json)、[六次实际截图](../../evidence/2026-10-03-food-tag-import/contact-sheet.png)、[节点与文字核验](../../evidence/2026-10-03-food-tag-import/readback.json)、[来源](../../design/polyulife/food-oct3-remaining-tags-sources.json)、[未配置连接计划](../../design/polyulife/food-oct3-remaining-tags-plan.json)。截图中下方“Zoom to selection”是编辑器提示，不是App控件。

Salad查询文字已直接选择为独立 Text954:191，Typography 显示 Inter Regular23px。查看子层时 Right 键将查询组x12移到13，已明确恢复12并读取x12/y112/w552/h74；菜单定位失败及 Text 没有“Copy link to selection”选项的情况保留在readback。其它结果文字未逐一做编辑测试；字体、图标及间距仍有近似。五个查询固定样本不代表可任意搜索。

此前浏览器安全策略拒绝Action下拉框的操作仍未解决，本批没有重试，也没有通过其它表面完成被拒绝的跳转配置。导入和文字检查属于其它正常编辑操作。新增五张图登记为未配置草稿，不增加正式可回放映射或控件数。

## HCI 假设与接力

Taiwanese标签返回自身结果并允许再次进入详情，可能产生用户不易察觉的嵌套调用层；需要真人任务观察其返回预期，不能仅凭Agent路线断言混乱。首次过渡折行和地图加载可能影响页面稳定感，但需真实手机、重复采样与人类体验验证，不能把Mac截图时机等同于缺陷。

当前原生27会话、212状态、395动作（308 observed、78 not_attempted、9 attempted_unverified），12项正式候选问题、2664证据；65份公开清单共2388PNG。正式Figma保持202映射画板、436控件、17滚动区域、137次运行；另有16个未配置草稿。本批先前锁定的Asian输入仍保留attempted_unverified历史，新的成功执行单独登记。

后续继续：重建当前28条Food连续列表；补查其它场所/结果详情、LibCafé标签及未观察控件；在安全拒绝得到解释后配置这批实际关系并用Present回放。嵌套地图加载完成、自由地图平移/缩放边界和完整搜索能力仍未验证。完整应用与视觉保真保持`not_verified`；Agent回放不替代手机触控和真人Maze测试。
