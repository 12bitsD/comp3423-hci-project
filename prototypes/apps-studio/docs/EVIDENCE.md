# Apps · 证据与演示边界

## 观察事实

来源为 2026-09-28 对官方 PolyULife 3.0.0 的实际 Mac 窗口走查，完整动作见 `docs/polyulife/apps-walkthrough.md` 和截图清单。原图只复制并改名，没有重绘内容：

| 本地素材 | 原始证据 | 证明范围 |
| --- | --- | --- |
| `assets/original-apps-all.png` | `evidence/2026-09-28-full-audit/apps-171359-all.png` | Apps 初始 All、横向分类栏、服务卡片和入口 |
| `assets/original-apps-category-dragged.png` | `apps-171722-category-bar-dragged.png` | 分类栏拖动后 Job 内容/选择仍保留，但选中 Job 标签在视口外 |
| `assets/original-vrs-detail.png` | `apps-171424-vrs-detail.png` | VRS 内部详情、用途和 Open VRS 链接 |
| `assets/original-vrs-login.png` | `apps-171522-vrs-login-empty-fields.png` | 本次 VRS 内嵌网页出现空 NetID/NetPassword 登录表单 |

已观察路径包括 Campus → VRS 详情 → 内嵌网页 → 关闭 → 详情 Back → Campus，返回保留 Campus。没有输入凭证、登录或提交访客申请。

## 问题假设而非用户结论

- `H-APPS-CATEGORY-VISIBILITY`：选中分类离开视口后，用户可能难以确认当前列表属于哪个分类。这是与系统状态可见性有关的待验证假设，不是已测得的错误率、困惑或任务失败。
- 原 VRS 详情可继续优化服务目的、目的地和登录要求的可理解性。现有证据不证明原链接失效，也不证明所有服务都需要重复登录或 SSO 有缺陷。
- 搜索是新增的设计提案。它用于比较“浏览分类”和“按名称/任务词查找”两条路径，不宣称原 App 用户一定要求搜索。

## 设计响应

- 分类 chips 换行显示，并以结果标题、`Current filter` 和结果数量重复表达当前状态。
- 查询匹配服务名、描述、分类和常见任务词；结果保持可扫描的名称和用途。
- 详情页先说明用途、NetID 可能性和官方目的地，再进入加载与外部登录演示。
- 加载可取消，网页可关闭，返回恢复查询、分类和滚动位置；无结果提供明确恢复动作。
- 具名原则：Visibility of system status、Recognition rather than recall、User control and freedom。设计效果必须经真人评估，不能由实现检查推出。

## 演示内容与限制

- 本地 10 条服务来自已观察名称和说明，构成核心任务演示集，不代表完整或实时线上目录；A01 的 10 results 因而只是演示数据。
- 外部域名来自 VRS 观察；其他服务统一写 Official PolyU service，不猜造网址。
- 外部登录页是安全静态演示，不可输入凭证、不会联网认证或提交访客申请。
- 浏览器计时只是原型过渡，不是原 App 或改版的真人/网络性能数据。
- 导出截图和 Agent 走查证明实现行为，不是真人 Maze 结果。当前尚无可编辑 Apps Figma 页面、真人结果或效果提升结论。
