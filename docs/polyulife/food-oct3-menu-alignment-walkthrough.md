# Food October3：Online Order行省略号位置修正

本批修正当前28条连续Food列表中H Café和U Garden的省略号位置，并在实际Figma Present复查两张卡片及滚动往返。依据是此前原生列表采样E-FOOD-REV-07/E-FOOD-REV-10和[营业时间稿检查](food-oct3-hours-import-walkthrough.md)发现的重建间距问题；本批没有新增原生会话、状态、动作或HCI问题。

[18次实际编辑器/Present采样清单](../../evidence/2026-10-03-food-menu-alignment/manifest.json)、[读数与比较结果](../../evidence/2026-10-03-food-menu-alignment/readback.json)、[H Café实际显示](../../evidence/2026-10-03-food-menu-alignment/10-present-hcafe-corrected.png)和[U Garden实际显示](../../evidence/2026-10-03-food-menu-alignment/11-present-ugarden.png)可复查此次修改。

## 修改与实际核对

旧源稿增加Online Order按钮时，为行高增加60px，但省略号居中计算遗漏了这段高度。本批将两个实际菜单组下移30px，其透明选择区域、三个点、宽高和X不变。

| 当前列表菜单组 | 实际Figma节点 | 修正前Y读数 | 修正后Y读数 | 实际尺寸 |
| --- | --- | --- | --- | --- |
| H Café VenueMenu05 | 954:3783 | 903 | 933 | X516，48×46 |
| U Garden VenueMenu10 | 954:3978 | 1876 | 1906 | X516，48×46 |

Figma自带Find结果明确显示菜单所属`[FOOD-OCT3:LIST28]`，并将H Café列表菜单与营业时间展开稿菜单区分。先前图层Return操作误将265项选中，目标选择未完成，期间未改几何；[失败采样](../../evidence/2026-10-03-food-menu-alignment/01-layer-selection-failure.png)保留。随后单独找到正确菜单、核对读数，再执行位置修改。

根954:3580仍为X0/Y94000、576×1024；内容954:3589为0/0、576×5581及Left/Top；视口954:3588为0/147、576×823、Clip content且Overflow Vertical。即时导航采样06尚在加载，没有尺寸证据；稳定采样07及15–17补齐实际读数。

源稿[food-oct3-full-list-local.svg](../../design/polyulife/food-oct3-full-list-local.svg)仅两个菜单组改变，其余XML保持相同。旧源稿、旧元数据和映射存入[修正前快照](../../design/polyulife/food-oct3-full-list-pre-menu-alignment-layout.json)及`reconstruction_versions`；既有运行与失败记录保持。

营业时间稿已在导入时自行加入H Café的30px修正。本批把其生成器基础源稿固定为旧快照，避免未来重生成重复修正；四张已导入营业时间SVG字节保持不变。两份生成器重新运行后，实际导入和回放元数据均完整保留。

## Present 回放结果与边界

从已有独立Food参考起点开始，第一步下滚一页越过H Café，实际采样09显示LibCafé等及U Garden，保留该过冲；上滚0.3页后显示H Café。随后下滚0.6页显示U Garden、上滚0.6页返回H Café，再下滚返回U Garden，最后回到列表顶部。两张目标卡片的品牌、时间、标签和Online Order仍可见。

三项原始应用裁片`(267,60,623,691)`比较全部相等：H Café10/12、U Garden11/13、顶部08/14。六项标题/地图条/手柄裁片`(267,60,623,151)`比较全部相等。这支持本次有限视口的显示和滚动恢复，不证明原生全几何、任意数据、长时稳定性或完整App保真。此前底部区域的严格纯白比较失败仍保留，没有重新归为通过。

新增一个`partial`运行记录，正式Figma204映射画板、436控件、19滚动区域、142次运行，未映射草稿19个。证据2780条、70份公开清单含2498PNG。原生27会话、212状态、395动作（308 observed、78 not_attempted、9 attempted_unverified）保持，完整应用与视觉保真仍`not_verified`。

菜单、订餐、营业时间、调用者/Back等新列表导航仍待配置和回放。既有Action下拉框的URL协议安全拒绝未重试或绕过，本批仅改位置并使用已有滚动能力。原生连接恢复尚未验证；Agent回放不替代真人或真机触控评价。
