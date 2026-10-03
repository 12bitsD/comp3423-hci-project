# Food详情实际导入与连续滚动

2026-10-03 使用当前 Codex In-app Browser，通过 Figma UI/剪贴板导入此前真实原生走查的11份SVG。原生事实见[上一批详情记录](food-oct3-detail-walkthrough.md)，本批没有新增原生动作或把原型回放当成原生执行。页面导入、设计尺寸和Overflow设置是本次实际操作；没有重试或绕过此前被URL协议安全策略拒绝的Action下拉框，也没有配置页面跳转。

保存[29张实际编辑器/Present截图及一张联系表](../../evidence/2026-10-03-food-detail-import/manifest.json)、[节点与几何记录](../../evidence/2026-10-03-food-detail-import/imports.json)、[尺寸/文字/约束读回](../../evidence/2026-10-03-food-detail-import/readback.json)、[操作和比较轨迹](../../evidence/2026-10-03-food-detail-import/input-trace.json)。编辑器截图实际为1211×750，Present为890×750，按各自实际像素尺寸遮盖头像；没有按预览尺寸误套遮盖框。

## 实际画板

各根Frame的576×1024和X/Y均从UI读回。上排Y88000，下排Y90000；没有用文件生成成功代替实际导入。

| 页面 | Figma节点 | X | 当前验证 |
| --- | --- | --- | --- |
| Block Y初始详情 | [949:63](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-63) | 0 | 标题Text/样式直接检查；有限垂直滚动回放，其它控件未配置 |
| Block Y较低视口 | [949:128](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-128) | 700 | 编辑器图片/文字可见；独立静态草稿，未回放 |
| Block Y图片 | [949:193](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-193) | 1400 | 品牌图/X组导入；X未配置 |
| Coffee搜索 | [949:201](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-201) | 2100 | 八个固定结果；未配置输入/结果/Back |
| LibCafé详情 | [949:248](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-248) | 2800 | 当前无头图布局/地图可见；未配置 |
| LibCafé地图 | [949:308](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-308) | 3500 | 编辑器截图地图可见；未配置 |
| Sandwich搜索 | [949:319](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-319) | 0 | 下排固定结果；未配置 |
| Block Y地图加载 | [949:366](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-366) | 700 | 下排校徽可见；没有延时连接 |
| Block Y地图 | [949:378](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-378) | 1400 | 下排初始地理视图可见；未配置 |
| Block Y放大地图 | [949:389](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-389) | 2100 | 下排放大样本可见；未配置输入代理 |
| Block Y缩小地图 | [949:400](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=949-400) | 2800 | 下排缩小样本可见；未配置 |

[实际导入联系表](../../evidence/2026-10-03-food-detail-import/contact-sheet.png)只展示这些编辑器像素，部分底部黑色片段属于编辑器Zoom to selection提示，保留原采样而不归为App控件；10个未回放草稿不计入正式映射画板。Block Y根949:63新增一项有限映射，其垂直滚动已实际回放。946:19旧加载草稿仍保留；当前共有11个未配置草稿（旧1、新10），不等于全应用已完成。

## 失败、纠正与滚动证据

快速粘贴时URL曾暂时为页面12:104，初始日志错误地把它当成较低详情节点。保留该次守卫停止事实，通过单个对象的Copy link to selection核对为949:128；图片949:193在守卫停止之前已导入，随后只重命名，没有重复粘贴。对根图层按Return曾进入三个子层，纠正为单根选中后再复制链接。另有两次精确图层名定位超时，画板仍在画布；后续从实际Select layer菜单核对Frame/Text/Group，未把定位失败归为页面丢失。

11号截图直接检查Block Y标题为Text，右侧Typography为Bold22px。其它子层没有逐一编辑验证；地图地理标签、图钉及地图内按钮图形仍为栅格，不能宣称全地图可编辑。

将DetailViewport组转换为Frame后，设高度924时原有Scale约束把1013高的内容也缩短到924。14号Present保留了压缩布局。恢复内容1013后，17号滚动生效，但底部多出21像素留白；原生较低视口支持更短的有限构图。随后只把两块背景向量高度设992，不改变文字、品牌图和地图位置，内容约束改Left/Top。

最终[布局源](../../design/polyulife/food-oct3-blocky-scroll.svg)与[几何来源](../../design/polyulife/food-oct3-blocky-scroll-layout.json)记录：949:65视口位于0/100，576×924、Clip content、Vertical；949:66内容高992，推导范围68。Header在滚动Frame之外。原11份导入源和旧本地渲染保持为历史基线；新布局源本身不是可运行的滚动原型，实际运行依据是Present截图。

Present由UI的Present按钮打开，最初Actual size导致画面底部裁切；旧Room流在侧栏仍被选中，但实际可见帧是949:63，不是Room回放。关闭侧栏并选择Fit width and height后，保存11次Present样本，其中19–25为最终滚动往返。没有新建Home调用者流或从原生Food入口跳进详情的原型链。

| 最终回放 | 证据 | 结果 |
| --- | --- | --- |
| 顶部→向下滚动 | 19→20 | Header固定；品牌图部分裁切，完整下方地图可见 |
| 额外下滚 | 20→21 | 保存的应用裁片像素相等，支持当前原型有限下边界 |
| 向上回顶部与额外上滚 | 20→22→23 | 22/23均与19的应用裁片相等 |
| 第二次下移及回顶 | 23→24→25 | 24与20、25与19的应用裁片相等 |

七项实际Present裁片比较五等两不等：两项不等是压缩/修正以及89/68范围的前后差异，原图保留。比较范围为890×750截图中的267/60/623/691半开应用区域，不扩大容差。相等只支持这些有限原型像素，不证明原生全范围、长期图片稳定性或完整保真。

## 后续范围

图片X、标签/结果/Back、内嵌地图/缩放/返回、加载延时和当前Food调用者都未配置；其它五个Block Y标签与其它场所交互仍待真实观察。原生AX在末尾重新返回PolyULife窗口信息，本批未再保存页面截图或新增原生执行；下一次输入前仍需重新确认当前界面。

本批当前统计：原生26会话、205状态、382动作（295 observed、78 not_attempted、9 attempted_unverified）保持；Figma202映射画板、436配置控件、17滚动区域、137次运行；2604证据、63份公开清单含2355PNG。完整应用/视觉保真`not_verified`。结构校验、截图相等和Agent回放不替代手机真机或真人Maze评价。
