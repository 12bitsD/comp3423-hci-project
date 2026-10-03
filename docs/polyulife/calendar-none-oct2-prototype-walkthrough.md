# Oct2 Calendar 全不选分支 — Figma 原型回放

依据[本轮真实原生记录](native-calendar-resume-20261002.md)，新增5个可编辑画板、7个控件和3组有限Present回放。它补入先前未实现的全不选Apply及重开结果，保留草稿前后的两种已应用背景。完整Calendar和PolyULife仍 `not_verified`。

原生截图来自10月2日23:49–23:59（Asia/Shanghai）；本次Figma导入/回放日志为10月2日16:19–16:34 UTC，对应Asia/Shanghai的次日凌晨。因此目录标记为`2026-10-03-calendar-none-prototype`，页面仍是历史固定October2样例，不是实时日期或课程数据。

## 来源、尺寸与编辑器记录

[SVG生成脚本](../../design/scripts/build_calendar_none_oct2.py)复用已有公开月份/过滤/空状态结构，按新原生截图将日期选中2、类别设为全部或No Selected Event。私人卡片值全部是DEMO，私人点阵省略；通用课堂图标改为可编辑矢量近似。字体和图标几何是近似，未取得完整像素保真。

五个Frame均576×1024、Clip content开启、y68500，x分别0/700/1400/2100/2800。1024是本次Mac全屏画面按576宽归一化的尺寸，不是iPhone视口；旧970高来源继续保留。日期28颜色曾随复用源变成黑色，已在源稿纠正相邻月份颜色并用Paste to replace更新未连线的首帧（791:19→791:177）。全部草稿导入的第一瞬间URL仍是Page12:104，随后实际导入791:335；没有重复粘贴或把Page计作Frame。两个导航中断分别读取实际位置后恢复，未重复配置连接。

| Frame | 节点 | 真实来源 |
| --- | --- | --- |
| OCT2:ALL Calendar all — DEMO | 791:177 | E-NATIVE-OCT2-03 |
| OCT2:ALL-D All draft — applied all | 791:335 | E-NATIVE-OCT2-04 |
| OCT2:NONE-D None draft — applied all | 791:529 | E-NATIVE-OCT2-05/08 |
| OCT2:NONE No Selected Event — applied | 791:713 | E-NATIVE-OCT2-09 |
| OCT2:NONE-R None draft — applied none | 791:873 | E-NATIVE-OCT2-10 |

实际重新加载编辑器后，五个命名Frame重新出现在图层列表。完整来源哈希、尺寸/位置读回和节点见[来源清单](../../design/polyulife/calendar-oct2-none-sources.json)及[连接清单](../../design/polyulife/calendar-oct2-none-connections.json)。

## 7条连接及范围

| 源控件 | 行为和目标 | 原生对应 |
| --- | --- | --- |
| ALL Filter 791:286 | Navigate to ALL-D | A-NATIVE-OCT2-04 |
| ALL-D SelectAll 791:500 | Navigate to NONE-D | A-NATIVE-OCT2-05 |
| NONE-D X 791:690 | Navigate to ALL | A-NATIVE-OCT2-06 |
| NONE-D Apply 791:709 | Navigate to NONE | A-CALENDAR-APPLY-NONE |
| NONE Filter 791:822 | Navigate to NONE-R | A-NATIVE-OCT2-10 |
| NONE-R X 791:1036 | Navigate to NONE | null；保留已应用none的原型取消推广 |
| ALL-D X 791:496 | Navigate to ALL | null；未变更草稿取消推广 |

所有连接On click/Instant。使用完整合成Frame间Navigate实现有限状态，没有原生overlay架构或普遍持久化的结论。两条推广出口已在Figma起点说明和JSON明确标注，不写成原生执行。

新增独立起点 **Reference · Oct2 None filters — partial**。它尚未接到主Home/More调用者；底部导航、月份/其他日期、未配置类别和省略号不是已实现功能。Class/Exam/Payment与课程详情虽然取得部分原生证据，本轮没有据此宣称已复现。

## 实际回放与验证

[保存截图、像素比较和时间](../../evidence/2026-10-03-calendar-none-prototype/manifest.json)含14张实际Present截图、1张重新加载后的编辑器截图及拼图。00是初始Actual size视图，页面下部被裁切；菜单选Fit width and height并关闭flows栏后才建立01基线。第一次文字定位未匹配，随后按真实menuitemcheckbox选择，没有将未执行的设置当作成功。

- 01–04：Filter→全不选草稿→X，恢复原全部类别和DEMO卡片。
- 04–10：Filter→全不选→Apply空状态→重开全不选→推广X→再次重开。
- 11–13：Figma Restart回到起点，再检验未修改ALL草稿的推广X。

7项应用区域裁片比较全部相等：X恢复、重开ALL、重复NONE草稿、推广X保持NONE、重复NONE重开、Restart和未改草稿X。裁片为viewport中的`[470,60,808,661]`。**比较的是原型重复状态，不是原型与原生的像素一致，也不是全应用或真人测试成功率。**全屏尺寸、合成内容、独立起点和未配置控件限制仍保留。
