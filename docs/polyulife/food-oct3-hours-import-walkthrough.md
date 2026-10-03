# Food October3：四种营业时间展开状态导入

本批通过 Computer Use 在实际 Figma 编辑器导入四张可编辑画板，保存12次实际编辑器采样及联系表：[公开清单](../../evidence/2026-10-03-food-hours-import/manifest.json)、[实际界面概览](../../evidence/2026-10-03-food-hours-import/11-four-hours-overview.png)、[读数与修正记录](../../evidence/2026-10-03-food-hours-import/readback.json)。没有新增原生会话、状态、动作或 Present 回放。用户回复解锁后，本次原生截图读取仍返回 Mac locked；不能据此评价 App 或宣称连接恢复。

依据是[此前营业时间往返观察](food-oct3-reverse-walkthrough.md)的四张真实原生截图，沿用28条列表的独立行文字、向量及公共品牌素材。公共截图已由原始750×1390窗口裁切后规范化为576×1024，本批坐标均为重建坐标，不等于原始窗口或完整原生滚动范围。

| 既有原生状态与证据 | 本批实际 Figma 节点 | 展开的公开营业时间 |
| --- | --- | --- |
| Block Y半展开面板，E-FOOD-REV-04 | [967:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=967-19) | Mon–Fri08:00–20:00；Sat09:00–18:00；Sun/public holiday Closed |
| Open Now H Café，E-FOOD-REV-08 | [967:178](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=967-178) | Mon–Fri08:00–22:00；Sat08:00–18:00；Sun/public holiday10:00–18:00 |
| 红色品牌、Chinese Soup标签的VA210，E-FOOD-REV-14 | [967:382](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=967-382) | Mon–Sun/public holiday00:00–23:59；不推广到同名的其它机器 |
| Closed Gourmet Shop Further information，E-FOOD-REV-19 | [967:741](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=967-741) | Mon–Fri08:00–19:30；Sat–Sun/public holiday Closed |

四张根画板均实际读回576×1024，位置X0/700/1400/2100、Y100000。每张分别选择一个时间文字层，确认独立 Text、Inter Regular14px；公共品牌图标、地图条和Block Y半面板校园地图为截图素材。字体、图标、间距为近似重建，不作逐像素保真承诺。源稿与素材依据见[源稿元数据](../../design/polyulife/food-oct3-hours-sources.json)和[生成器](../../design/scripts/build_food_oct3_hours.py)。生成器本身不操作 App 或 Figma。

## 检查发现及修正

H Café正常行含Online Order按钮，旧连续列表源稿的省略号未计入该按钮的60px附加行高，位置约偏高30px。本批只在新展开源稿加入30px居中修正和34.5px营业时间展开修正；实际 VenueMenu05读回X516、Y419.5、48×46，中心442.5。原生采样点约441.5，仍有差异；现有连续列表的H Café/U Garden菜单尚未修改，不能称整张列表已修复。

Gourmet初稿加54px后，已观察到的底部标签碎片消失，省略号也偏低。[初稿截图](../../evidence/2026-10-03-food-hours-import/06-gourmet-root.png)和[初稿源文件](../../design/polyulife/food-oct3-gourmet-hours-before-spacing.svg)保留。改为42px重建间距后，通过实际 Paste to replace替换967:577为967:741，根尺寸/位置不变，标签上移12px、菜单上移6px。[修正截图](../../evidence/2026-10-03-food-hours-import/07-gourmet-spacing-repair.png)保留标签的可见碎片；VenueMenu28实际Y838.5、48×46，中心861.5。末项全高、原生精确裁切边界仍未知，不能以954px可见内容遮罩推出滚动视口边界。

记录了两项工具问题：读取AX差异行时解析前缀失败，没有额外执行UI动作；H Café根图层因左侧列表虚拟化未匹配，改用已核实节点的编辑器URL恢复选择。这是编辑器定位，未配置或绕过曾被拒绝的原型页面跳转连接。

## 完成边界与接力

本批是四个实际导入、局部编辑性和布局已检查的有限视口草稿。未配置营业时间展开/收起、Home/Back调用者、菜单、详情、标签、订餐连接，也未做新 Present 回放。它们加入`source_preparation_imports`，不提升正式映射、控件或运行数量。此前Action下拉框的URL协议安全拒绝仍未解除，本批未重试或绕过该动作。

当前正式Figma仍204映射画板、436控件、19滚动区域、141次运行；未正式映射的导入草稿增至19个。原生27会话、212状态、395动作（308 observed、78 not_attempted、9 attempted_unverified）保持；证据2760条，69份公开清单含2479个PNG。完整应用及视觉保真保持`not_verified`，Agent编辑器检查不替代真人Maze评价。

下一步恢复原生窗口后继续核查余下场所控件；对本批四种状态补调用者及展开/收起的实际原型回放，修正连续列表Online Order行菜单位置，并检查与已映射列表的整合。任何未完成导航和精确范围均保留缺口。
