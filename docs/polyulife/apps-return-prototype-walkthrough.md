# Apps 分类与嵌套页面返回

2026-09-29（本地时间；截图时间为UTC）。本批只修改和回放 Figma。用户回复恢复后，原生 Computer Use 再次明确返回 Mac locked，未取得新的真实页面。原生台账仍为121个状态、265个动作（179 observed / 86 not_attempted），完整应用保持 `not_verified`。

## 已解决的具体问题

上一版 Apps All 的 history Back 只能处理 Home 直接进入。分类使用 Navigate to 会累积历史，分类绕行后 Back 可能退回上个分类。现在 Home 将 Apps 打开为全屏覆盖层，分类使用 Swap overlay，VRS详情和空登录另开嵌套层；各层关闭时恢复底层，不重建首页，因此保留日期和滚动位置。

依据是[原生Apps走查](apps-walkthrough.md)的分类与VRS返回，以及[Home补测](home-study-map-walkthrough.md)的Apps返回Home。为其它七个分类状态补Back属于对这条观察的原型推广；本批逐一验证的是Figma，不能称各分类原生Back全部已实测。

从Tuesday首页功能区实跑 All → Campus → VRS详情 → 空登录 → 关闭登录 → 详情 → Campus → Study → IT Tips → Health → Wellness → Job → 拖分类条 → All → 首页，返回保留原Tuesday根节点和滚动位置。Monday直接往返及七个分类状态各自Back均回原Monday位置；历史Home功能区经Campus返回也通过。

另将Present中的应用区域 `(581,60)–(938,661)` 做像素比较：Tuesday分类链前后、Monday直接往返和七个分类Back、历史Home往返共10对画面完全一致。这支持本批截图中的位置保留，不证明未测来源或原生App行为。

## 配置读回

共修改16个既有控件，新增7个分类Back，当前138个配置控件；未增Frame，仍76个映射Frame、2个内部cookie状态和2个滚动区域。Open overlay居中、不点击外部关闭、无背景遮罩。分类拖动仍为On drag / Smart animate / Ease out / 300ms；其它转换Instant。详见[完整配置读回](../../design/polyulife/apps-overlay-layout.json)。

| 来源Frame | 触发节点 | 当前动作 | 目标 |
| --- | --- | --- | --- |
| 67:694 | 113:31 | Open overlay | 61:2 |
| 61:2 | 61:129 | Close overlay | 关闭一层 |
| 61:2 | 61:109 | Swap overlay | 61:135 |
| 61:135 | 61:192 | Swap overlay | 61:215 |
| 61:215 | 61:324 | Swap overlay | 61:344 |
| 61:344 | 61:458 | Swap overlay | 61:475 |
| 61:475 | 61:568 | Swap overlay | 61:585 |
| 61:585 | 61:649 | Swap overlay | 61:663 |
| 61:663 | 61:688 | Swap overlay | 61:721 |
| 61:721 | 61:749 | Swap overlay | 61:2 |
| 61:135 | 61:155 | Open overlay | 61:778 |
| 61:778 | 61:791 | Open overlay | 61:843 |
| 61:843 | 61:855 | Close overlay | 关闭一层 |
| 61:778 | 61:799 | Close overlay | 关闭一层 |
| 67:569 | 113:76 | Open overlay | 61:2 |
| 67:820 | 67:890 | Open overlay | 61:2 |
| 61:135 | 61:209 | Close overlay | 关闭一层 |
| 61:215 | 61:338 | Close overlay | 关闭一层 |
| 61:344 | 61:469 | Close overlay | 关闭一层 |
| 61:475 | 61:579 | Close overlay | 关闭一层 |
| 61:585 | 61:657 | Close overlay | 关闭一层 |
| 61:663 | 61:715 | Close overlay | 关闭一层 |
| 61:721 | 61:772 | Close overlay | 关闭一层 |

## 实际回放证据

| UTC | 观察 | 截图 |
| --- | --- | --- |
| 21:37:33.781 | Apps覆盖层入口 | [E-APPS-STACK-P-01](../../evidence/2026-09-28-full-audit/figma-apps-stack-overlay-entry.png) |
| 21:37:44.233 | 直接返回周二原滚动位置 | [E-APPS-STACK-P-02](../../evidence/2026-09-28-full-audit/figma-apps-stack-overlay-direct-return.png) |
| 21:42:02.925 | 周二重新进入All | [E-APPS-STACK-P-03](../../evidence/2026-09-28-full-audit/figma-apps-stack-chain-all.png) |
| 21:42:19.388 | Campus分类 | [E-APPS-STACK-P-04](../../evidence/2026-09-28-full-audit/figma-apps-stack-campus.png) |
| 21:42:30.605 | VRS详情嵌套层 | [E-APPS-STACK-P-05](../../evidence/2026-09-28-full-audit/figma-apps-stack-vrs-detail.png) |
| 21:42:39.723 | VRS空登录嵌套层 | [E-APPS-STACK-P-06](../../evidence/2026-09-28-full-audit/figma-apps-stack-vrs-login.png) |
| 21:42:50.256 | 关闭登录回详情 | [E-APPS-STACK-P-07](../../evidence/2026-09-28-full-audit/figma-apps-stack-vrs-close-login.png) |
| 21:43:01.181 | 详情返回Campus且保留选中 | [E-APPS-STACK-P-08](../../evidence/2026-09-28-full-audit/figma-apps-stack-vrs-back-campus.png) |
| 21:43:12.537 | Study分类 | [E-APPS-STACK-P-09](../../evidence/2026-09-28-full-audit/figma-apps-stack-study.png) |
| 21:43:25.008 | IT Tips分类 | [E-APPS-STACK-P-10](../../evidence/2026-09-28-full-audit/figma-apps-stack-it.png) |
| 21:43:38.650 | Health分类 | [E-APPS-STACK-P-11](../../evidence/2026-09-28-full-audit/figma-apps-stack-health.png) |
| 21:43:48.552 | Wellness分类 | [E-APPS-STACK-P-12](../../evidence/2026-09-28-full-audit/figma-apps-stack-wellness.png) |
| 21:46:55.672 | Job分类 | [E-APPS-STACK-P-13](../../evidence/2026-09-28-full-audit/figma-apps-stack-job.png) |
| 21:47:03.213 | Job分类条拖至左端 | [E-APPS-STACK-P-14](../../evidence/2026-09-28-full-audit/figma-apps-stack-job-left.png) |
| 21:47:07.946 | 切回All | [E-APPS-STACK-P-15](../../evidence/2026-09-28-full-audit/figma-apps-stack-all-return.png) |
| 21:47:16.947 | 完整分类链返回周二原滚动位置 | [E-APPS-STACK-P-16](../../evidence/2026-09-28-full-audit/figma-apps-stack-home-return.png) |
| 21:47:48.781 | Restart后周一起点 | [E-APPS-STACK-P-17](../../evidence/2026-09-28-full-audit/figma-apps-stack-monday-start.png) |
| 21:47:56.485 | 周一滚至功能区 | [E-APPS-STACK-P-18](../../evidence/2026-09-28-full-audit/figma-apps-stack-monday-features.png) |
| 21:48:03.332 | 周一Apps入口 | [E-APPS-STACK-P-19](../../evidence/2026-09-28-full-audit/figma-apps-stack-monday-apps.png) |
| 21:48:11.066 | 周一直接返回原滚动位置 | [E-APPS-STACK-P-20](../../evidence/2026-09-28-full-audit/figma-apps-stack-monday-return.png) |
| 21:52:15.694 | Campus返回前 | [E-APPS-STACK-P-21](../../evidence/2026-09-28-full-audit/figma-apps-stack-campus-before-back.png) |
| 21:52:23.252 | Campus直接返回周一原滚动位置 | [E-APPS-STACK-P-22](../../evidence/2026-09-28-full-audit/figma-apps-stack-campus-back-home.png) |
| 21:52:34.171 | Study返回前 | [E-APPS-STACK-P-23](../../evidence/2026-09-28-full-audit/figma-apps-stack-study-before-back.png) |
| 21:52:42.051 | Study直接返回周一原滚动位置 | [E-APPS-STACK-P-24](../../evidence/2026-09-28-full-audit/figma-apps-stack-study-back-home.png) |
| 21:52:51.524 | IT Tips返回前 | [E-APPS-STACK-P-25](../../evidence/2026-09-28-full-audit/figma-apps-stack-it-before-back.png) |
| 21:52:59.293 | IT Tips直接返回周一原滚动位置 | [E-APPS-STACK-P-26](../../evidence/2026-09-28-full-audit/figma-apps-stack-it-back-home.png) |
| 21:53:09.421 | Health返回前 | [E-APPS-STACK-P-27](../../evidence/2026-09-28-full-audit/figma-apps-stack-health-before-back.png) |
| 21:53:16.069 | Health直接返回周一原滚动位置 | [E-APPS-STACK-P-28](../../evidence/2026-09-28-full-audit/figma-apps-stack-health-back-home.png) |
| 21:53:27.193 | Wellness返回前 | [E-APPS-STACK-P-29](../../evidence/2026-09-28-full-audit/figma-apps-stack-wellness-before-back.png) |
| 21:53:35.308 | Wellness直接返回周一原滚动位置 | [E-APPS-STACK-P-30](../../evidence/2026-09-28-full-audit/figma-apps-stack-wellness-back-home.png) |
| 21:53:45.389 | Job返回前 | [E-APPS-STACK-P-31](../../evidence/2026-09-28-full-audit/figma-apps-stack-job-before-back.png) |
| 21:53:53.547 | Job直接返回周一原滚动位置 | [E-APPS-STACK-P-32](../../evidence/2026-09-28-full-audit/figma-apps-stack-job-back-home.png) |
| 21:54:05.084 | Job分类条左端返回前 | [E-APPS-STACK-P-33](../../evidence/2026-09-28-full-audit/figma-apps-stack-job-left-before-back.png) |
| 21:54:15.363 | Job分类条左端直接返回周一原滚动位置 | [E-APPS-STACK-P-34](../../evidence/2026-09-28-full-audit/figma-apps-stack-job-left-back-home.png) |
| 21:54:26.795 | 历史Home功能区入口 | [E-APPS-STACK-P-35](../../evidence/2026-09-28-full-audit/figma-apps-stack-legacy-start.png) |
| 21:54:34.548 | 历史Home经Apps到Campus | [E-APPS-STACK-P-36](../../evidence/2026-09-28-full-audit/figma-apps-stack-legacy-campus.png) |
| 21:54:47.724 | Campus返回历史Home | [E-APPS-STACK-P-37](../../evidence/2026-09-28-full-audit/figma-apps-stack-legacy-return.png) |
| 21:56:53.093 | 新版Home流程说明已读回 | [E-APPS-STACK-P-38](../../evidence/2026-09-28-full-audit/figma-apps-stack-home-description.png) |
| 21:57:03.184 | Apps独立入口限制说明已读回 | [E-APPS-STACK-P-39](../../evidence/2026-09-28-full-audit/figma-apps-stack-standalone-description.png) |

## 限制与后续

- 已验证的返回必须从Home进入。独立Apps流程仍保留作参考入口，没有Home调用来源；其退出语义未验证，不能作为完整往返验收。Home与Apps说明均已在Present重载后读回。
- 分类只接通上述固定链及对应Back，任意分类互跳、完整列表滚动和VRS之外服务尚未接入。拖动只对应一段已观察位置转换。
- VRS加载帧仍为静态参考，回放跳过加载，不模拟登录提交。
- 其它十个新复制Home入口仍未逐个回放，模块返回、原生完整滚动边界和既有视觉缺陷仍未解决。
- 39张真实Present截图仅遮盖右上账号区域 `[1017,0,1075,49]`，转为PNG后按像素校验；原始JPEG留在忽略目录。截图不替代原生取证或Maze真人评估。

后续更新：[可见分类互跳验证](apps-category-prototype-walkthrough.md)已新增并回放33个连接；本页的固定链限制作为历史记录保留。
