# 首页连续滚动与 Apps 直接返回

2026-09-29（本地时间；下表UTC）。原生Computer Use再次报告Mac锁定，无新增原生观察。基于[既有Home取证](home-study-map-walkthrough.md)与合成DEMO内容，改造现有Figma Monday67:569、Tuesday67:694；完整应用保持 `not_verified`。

## 改动和依据

既有原生证据显示首页功能区及向上滚到日期区的动作。原型现在用真实垂直滚动区域连接这两段内容，而非用点击切换固定滚动截图。中间位置、反向滚动和固定导航都在Present实际验证。此结果只证明原型滚动，不证明新原生状态；原生全列表末端、其它日期、卡片详情和底部面板展开尚未确认。

每页原有正文Clip path group转换为Frame，去掉旧遮罩，保留Clip content与Vertical overflow；视口位于0,100、尺寸576×735。Header、BottomSheet和BottomNavigation留在区域外。Features复制自已有功能区，位置为视口内78,909、尺寸454×178。其布局偏移353单位来自原有顶部/功能区样例；总滚动范围352为该合成内容算出的范围，不是新测得的原生完整边界。

首次缩小Frame时，子层原有Scale约束压缩了正文；恢复原尺寸后改为Top约束，再缩小视口，顶部回放已恢复原布局。公开源稿保留这种约束说明；SVG只描述可编辑内容，单独导入并不会创建Figma滚动行为。

Apps初次返回点击无效，保留失败截图。补接All页Back61:129后，分别从周一/周二滚动功能区进入Apps并返回，均保留来源Frame和滚动位置；周一返回后再滚回顶部仍显示周一。该Back只支持直接从Home进入；Apps分类之间现为导航帧，其历史栈与各分类Back仍须改造，不能据此认定完整Apps返回通过。

## 实际 Present 回放

| UTC | 观察 | 截图 |
| --- | --- | --- |
| 21:18:33.815 | 周二顶部，恢复内容原尺寸后 | [E-HOME-SCROLL-P-01](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-top.png) |
| 21:18:42.551 | 周二连续下滚至功能区 | [E-HOME-SCROLL-P-02](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-first.png) |
| 21:19:06.381 | 周二反向滚至中间位置 | [E-HOME-SCROLL-P-03](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-middle.png) |
| 21:19:20.771 | 周二滚回顶部 | [E-HOME-SCROLL-P-04](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-restored-top.png) |
| 21:20:33.789 | Restart后的暂态黑屏 | [E-HOME-SCROLL-P-05](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-top.png) |
| 21:20:43.855 | 周一加载完成 | [E-HOME-SCROLL-P-06](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-loaded.png) |
| 21:20:53.160 | 周一中间滚动位置 | [E-HOME-SCROLL-P-07](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-middle.png) |
| 21:21:03.480 | 周一连续滚至功能区 | [E-HOME-SCROLL-P-08](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-features.png) |
| 21:21:27.212 | 周一功能区进入Apps | [E-HOME-SCROLL-P-09](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-apps-entry.png) |
| 21:21:39.442 | 失败：Apps Back未接线，点击后仍在Apps | [E-HOME-SCROLL-P-10](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-apps-return.png) |
| 21:25:43.834 | 补线后Apps Back回周一，保留滚动位置 | [E-HOME-SCROLL-P-11](../../evidence/2026-09-28-full-audit/figma-home-scroll-apps-return-connected.png) |
| 21:26:30.957 | 周一返回后滚回顶部 | [E-HOME-SCROLL-P-12](../../evidence/2026-09-28-full-audit/figma-home-scroll-monday-return-top.png) |
| 21:26:39.979 | 回归：Monday日期切到Tuesday | [E-HOME-SCROLL-P-13](../../evidence/2026-09-28-full-audit/figma-home-scroll-date-change-regression.png) |
| 21:26:49.022 | 回归：My Class打开Week5 | [E-HOME-SCROLL-P-14](../../evidence/2026-09-28-full-audit/figma-home-scroll-myclass-regression.png) |
| 21:26:58.402 | 回归：Week5 Home回周二顶部 | [E-HOME-SCROLL-P-15](../../evidence/2026-09-28-full-audit/figma-home-scroll-myclass-return-regression.png) |
| 21:27:08.352 | 周二滚至功能区准备Apps回放 | [E-HOME-SCROLL-P-16](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-apps-start.png) |
| 21:27:17.705 | 周二功能区进入Apps | [E-HOME-SCROLL-P-17](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-apps-entry.png) |
| 21:27:28.130 | Apps Back回周二并保留滚动位置 | [E-HOME-SCROLL-P-18](../../evidence/2026-09-28-full-audit/figma-home-scroll-tuesday-apps-back.png) |
| 21:28:00.492 | 说明已保存但Present仍显示缓存旧说明 | [E-HOME-SCROLL-P-19](../../evidence/2026-09-28-full-audit/figma-home-scroll-final-context.png) |
| 21:29:15.050 | 重载后新说明可见 | [E-HOME-SCROLL-P-20](../../evidence/2026-09-28-full-audit/figma-home-scroll-description-reloaded.png) |
| 21:29:26.592 | 最新说明下滚到功能区 | [E-HOME-SCROLL-P-21](../../evidence/2026-09-28-full-audit/figma-home-scroll-final-features-context.png) |

## 新增功能实例

六个入口在两张首页中各复制一份，目标配置逐项从UI读回；本批只实际回放Apps两份入口，其余10份明确为未回放。另增加1个Apps Back，共131个配置控件。2个滚动区域单独登记，不增加全屏Frame数量；仍为76个映射Frame、2个画板内cookie状态。

| 日期页 | 入口图层 | Figma节点 | 验证 |
| --- | --- | --- | --- |
| Monday | FeatureMyCourses | 113:90 | 配置已读回，尚未回放 |
| Monday | FeatureStudyProgress | 113:84 | 配置已读回，尚未回放 |
| Monday | FeatureApps | 113:76 | 已回放直接入口 |
| Monday | FeatureFood | 113:71 | 配置已读回，尚未回放 |
| Monday | FeatureRoom | 113:64 | 配置已读回，尚未回放 |
| Monday | FeatureMap | 113:58 | 配置已读回，尚未回放 |
| Tuesday | FeatureMyCourses | 113:45 | 配置已读回，尚未回放 |
| Tuesday | FeatureStudyProgress | 113:39 | 配置已读回，尚未回放 |
| Tuesday | FeatureApps | 113:31 | 已回放直接入口 |
| Tuesday | FeatureFood | 113:26 | 配置已读回，尚未回放 |
| Tuesday | FeatureRoom | 113:19 | 配置已读回，尚未回放 |
| Tuesday | FeatureMap | 113:13 | 配置已读回，尚未回放 |

源稿：[生成脚本](../../design/scripts/build_home_scroll_svg.py)、[Monday](../../design/polyulife/home-demo-monday-scroll.svg)、[Tuesday](../../design/polyulife/home-demo-tuesday-scroll.svg)、[原生Figma布局参数](../../design/polyulife/home-scroll-layout.json)。旧固定位置源稿仍保留为历史。My Class及Monday→Tuesday原连接在改造后回归通过。

## 明确保留的缺口

- 未观察完整原生滚动末端，范围与间距为合成样例推导；Mac锁屏恢复后需补查。
- 新复制的其它功能入口未逐个回放，已有业务页返回可能指向旧固定Home功能区；这些路径不能宣称保留当前日期或滚动状态。
- Apps分类绕行与直接起于Apps的返回语义未实现；其它日期、自由输入、周选择器、考试卡横向滚动和面板展开仍缺失。
- 装饰图本次可见，但间歇缺失未修复；字体、图标和DEMO日程仍不代表私人真实数据或逐像素还原。
- 21张实际Present截图仅遮盖右上账号区域 `[1017,0,1075,49]`，转码与遮盖逐像素校验；原始JPEG留在忽略目录。Agent回放不替代Maze真人评估。
