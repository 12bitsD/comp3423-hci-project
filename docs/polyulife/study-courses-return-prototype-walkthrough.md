# Study / Courses 样例返回原首页

2026-09-29。本批只通过 Computer Use 修改和回放 Figma。收到用户“已恢复”后原生工具仍提示 Mac locked，未取得新原生状态；原生台账保持 121 状态 / 265 动作（179 observed / 86 not_attempted），完整应用保持 `not_verified`。

## 问题与实现

[前一批直接返回](home-feature-return-prototype-walkthrough.md)只补了历史 Back；模块内部 Navigate to 会累积历史，不能保证退出整个模块。本批让三个 Home 来源（Monday、Tuesday、legacy）打开 Study/Courses overlay，八条既有内部路径切换 overlay，八个外层 Back 关闭 overlay，保留调用首页及其滚动位置。更新17个既有控件，新增5个，当前181个配置控件；76个映射Frame、2个内部cookie状态及2个垂直滚动区域不变。

## 验证范围

- 三个 Home 来源各回放 Study（Completed、标题展开/收起、Requirements、Offerings、外层 Back）和 Courses（Canvas、标题展开/收起、Blackboard、空登录、外层 Back）路径，共六组。
- Tuesday 另从 Completed、展开 Completed、Requirements、Canvas、展开 Canvas、Blackboard 分别退出，加上完整路径的 Offerings/登录出口，覆盖全部八个外层 Back。
- 12张返回截图与各来源基线在应用区域 `(581,60,938,661)` 像素完全相同。Monday/legacy组合主要保存末页和返回图，标题中间步骤的逐状态截图来自Tuesday，不扩充原生覆盖率。
- 两条 Home 流程说明已修改并在 Present 重载后读回。切换日期流程曾短暂黑屏，随后首页渲染完成；两张截图都保留。

## 原生依据与仍未完成的范围

[原生 Study/Courses 记录](home-study-map-walkthrough.md)支持标题展开/收起、前向页签路径及空Blackboard登录外层Back回Home；五个新增中间状态外层Back是原型推广，原生相同来源并未独立观察。Completed/Canvas根页Back同样仍有此来源限制。

Study blank保留为独立未解释状态，原有固定返回legacy Home未动，没有虚构Offerings搜索到blank的连接。Offerings内层返回、逆向页签、其它课程行、完整列表、搜索、独立模块起点仍未完成。加载被跳过，课程/日程使用明确DEMO。Map/Room/Food内部绕行与既有缺图问题仍保留；`D-HOME-MODULE-RETURN`仅部分解决。Agent回放不能替代原生观察或Maze真人评估。

## 配置读回

[完整配置与像素比较](../../design/polyulife/study-courses-return-connections.json)。旧配置保存在coverage映射的configuration_history中；新增Back的action_id为null。

| 来源Frame | 触发节点 | 行为 | 目的/返回 | 变更 |
| --- | --- | --- | --- | --- |
| 67:569 | 113:84 | Open overlay | 67:2 | 更新，保留旧配置 |
| 67:694 | 113:39 | Open overlay | 67:2 | 更新，保留旧配置 |
| 67:820 | 67:898 | Open overlay | 67:2 | 更新，保留旧配置 |
| 67:569 | 113:90 | Open overlay | 67:271 | 更新，保留旧配置 |
| 67:694 | 113:45 | Open overlay | 67:271 | 更新，保留旧配置 |
| 67:820 | 67:904 | Open overlay | 67:271 | 更新，保留旧配置 |
| 67:2 | 67:29 | Swap overlay | 67:71 | 更新，保留旧配置 |
| 67:71 | 67:99 | Swap overlay | 67:2 | 更新，保留旧配置 |
| 67:2 | 67:11 | Swap overlay | 67:141 | 更新，保留旧配置 |
| 67:141 | 67:157 | Swap overlay | 67:188 | 更新，保留旧配置 |
| 67:271 | 67:292 | Swap overlay | 67:360 | 更新，保留旧配置 |
| 67:360 | 67:382 | Swap overlay | 67:271 | 更新，保留旧配置 |
| 67:271 | 67:280 | Swap overlay | 67:450 | 更新，保留旧配置 |
| 67:450 | 67:465 | Swap overlay | 67:485 | 更新，保留旧配置 |
| 67:485 | 67:507 | Close overlay | Home caller | 更新，保留旧配置 |
| 67:271 | 67:351 | Close overlay | Home caller | 更新，保留旧配置 |
| 67:2 | 67:62 | Close overlay | Home caller | 更新，保留旧配置 |
| 67:71 | 67:132 | Close overlay | Home caller | 新增，原生来源待核 |
| 67:141 | 67:182 | Close overlay | Home caller | 新增，原生来源待核 |
| 67:188 | 67:253 | Close overlay | Home caller | 新增，原生来源待核 |
| 67:360 | 67:441 | Close overlay | Home caller | 新增，原生来源待核 |
| 67:450 | 67:476 | Close overlay | Home caller | 新增，原生来源待核 |

## 实际截图

时间为UTC，截图为实际Present输出；只遮盖Figma账号区域。原始JPEG在忽略目录，公开PNG逐像素核对遮盖和转码，哈希与尺寸校验。

| 时间 | 观察 | 截图 |
| --- | --- | --- |
| 2026-09-28T22:56:29.249Z | Tuesday feature-region baseline | [E-STUDY-STACK-P-01](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-baseline.png) |
| 2026-09-28T22:56:29.521Z | Tuesday opens Study overlay | [E-STUDY-STACK-P-02](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-completed.png) |
| 2026-09-28T22:56:41.405Z | Study title expanded within same overlay | [E-STUDY-STACK-P-03](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-expanded.png) |
| 2026-09-28T22:56:56.146Z | Study title collapsed without adding navigation history | [E-STUDY-STACK-P-04](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-collapsed.png) |
| 2026-09-28T22:56:56.412Z | Requirements selected | [E-STUDY-STACK-P-05](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-requirements.png) |
| 2026-09-28T22:57:07.590Z | Public offerings after expand/collapse and Requirements detour | [E-STUDY-STACK-P-06](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-offerings.png) |
| 2026-09-28T22:57:28.674Z | Offerings outer Back closes Study and restores Tuesday features | [E-STUDY-STACK-P-07](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-study-return.png) |
| 2026-09-28T22:57:28.911Z | Tuesday opens Courses overlay | [E-STUDY-STACK-P-08](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas.png) |
| 2026-09-28T22:57:40.889Z | Canvas title expanded | [E-STUDY-STACK-P-09](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-expanded.png) |
| 2026-09-28T22:57:55.890Z | Canvas title collapsed | [E-STUDY-STACK-P-10](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-collapsed.png) |
| 2026-09-28T22:57:56.162Z | Blackboard selected | [E-STUDY-STACK-P-11](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-blackboard.png) |
| 2026-09-28T22:58:07.699Z | Blackboard empty login preserves Tuesday caller | [E-STUDY-STACK-P-12](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-login.png) |
| 2026-09-28T22:58:20.200Z | Blackboard login Back returns original Tuesday feature scroll | [E-STUDY-STACK-P-13](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-courses-return.png) |
| 2026-09-28T22:58:46.624Z | Exit check before 67:62 | [E-STUDY-STACK-P-14](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-completed-exit-before.png) |
| 2026-09-28T22:58:46.891Z | Exit 67:62 returns caller after tue-completed-exit | [E-STUDY-STACK-P-15](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-completed-exit-return.png) |
| 2026-09-28T22:58:58.048Z | Exit check before 67:132 | [E-STUDY-STACK-P-16](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-expanded-exit-before.png) |
| 2026-09-28T22:58:58.291Z | Exit 67:132 returns caller after tue-expanded-exit | [E-STUDY-STACK-P-17](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-expanded-exit-return.png) |
| 2026-09-28T22:59:12.547Z | Exit check before 67:182 | [E-STUDY-STACK-P-18](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-requirements-exit-before.png) |
| 2026-09-28T22:59:12.818Z | Exit 67:182 returns caller after tue-requirements-exit | [E-STUDY-STACK-P-19](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-requirements-exit-return.png) |
| 2026-09-28T22:59:23.608Z | Exit check before 67:351 | [E-STUDY-STACK-P-20](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-exit-before.png) |
| 2026-09-28T22:59:23.883Z | Exit 67:351 returns caller after tue-canvas-exit | [E-STUDY-STACK-P-21](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-exit-return.png) |
| 2026-09-28T22:59:36.827Z | Exit check before 67:441 | [E-STUDY-STACK-P-22](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-expanded-exit-before.png) |
| 2026-09-28T22:59:37.090Z | Exit 67:441 returns caller after tue-canvas-expanded-exit | [E-STUDY-STACK-P-23](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-canvas-expanded-exit-return.png) |
| 2026-09-28T22:59:50.696Z | Exit check before 67:476 | [E-STUDY-STACK-P-24](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-blackboard-exit-before.png) |
| 2026-09-28T22:59:50.964Z | Exit 67:476 returns caller after tue-blackboard-exit | [E-STUDY-STACK-P-25](../../evidence/2026-09-28-full-audit/figma-study-stack-tue-blackboard-exit-return.png) |
| 2026-09-28T23:00:48.178Z | Monday feature-region baseline | [E-STUDY-STACK-P-26](../../evidence/2026-09-28-full-audit/figma-study-stack-mon-baseline.png) |
| 2026-09-28T23:01:10.206Z | Exit check before 67:253 | [E-STUDY-STACK-P-27](../../evidence/2026-09-28-full-audit/figma-study-stack-mon-study-chain-before.png) |
| 2026-09-28T23:01:10.477Z | Exit 67:253 returns caller after mon-study-chain | [E-STUDY-STACK-P-28](../../evidence/2026-09-28-full-audit/figma-study-stack-mon-study-chain-return.png) |
| 2026-09-28T23:04:20.442Z | Exit check before 67:507 | [E-STUDY-STACK-P-29](../../evidence/2026-09-28-full-audit/figma-study-stack-mon-courses-chain-before.png) |
| 2026-09-28T23:04:20.748Z | Exit 67:507 returns caller after mon-courses-chain | [E-STUDY-STACK-P-30](../../evidence/2026-09-28-full-audit/figma-study-stack-mon-courses-chain-return.png) |
| 2026-09-28T23:04:52.135Z | Legacy Home feature baseline | [E-STUDY-STACK-P-31](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-baseline.png) |
| 2026-09-28T23:05:12.395Z | Exit check before 67:253 | [E-STUDY-STACK-P-32](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-study-chain-before.png) |
| 2026-09-28T23:05:12.668Z | Exit 67:253 returns caller after legacy-study-chain | [E-STUDY-STACK-P-33](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-study-chain-return.png) |
| 2026-09-28T23:05:13.893Z | Exit check before 67:507 | [E-STUDY-STACK-P-34](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-courses-chain-before.png) |
| 2026-09-28T23:05:14.160Z | Exit 67:507 returns caller after legacy-courses-chain | [E-STUDY-STACK-P-35](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-courses-chain-return.png) |
| 2026-09-28T23:06:56.223Z | Reloaded legacy flow description; native limitations retained | [E-STUDY-STACK-P-36](../../evidence/2026-09-28-full-audit/figma-study-stack-legacy-description.png) |
| 2026-09-28T23:07:04.746Z | Dates flow description persisted; transient black app region immediately after flow change | [E-STUDY-STACK-P-37](../../evidence/2026-09-28-full-audit/figma-study-stack-dates-description.png) |
| 2026-09-28T23:07:13.179Z | Dates flow settled after transient loading | [E-STUDY-STACK-P-38](../../evidence/2026-09-28-full-audit/figma-study-stack-dates-ready.png) |
