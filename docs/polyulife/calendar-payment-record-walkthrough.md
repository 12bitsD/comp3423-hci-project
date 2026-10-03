# Payment 第一条历史记录与 Portal 原生走查

2026-10-03 使用已安装的 iPhone App on Mac，经 Computer Use 读取真实窗口并按最新 AX 操作。沿用当前登录状态，从 October 2 / Payment 月历开始，最后返回同一起点。本批只观察第一条历史记录，没有付款、输入凭证、分享或修改记录。

## 已观察路径

Month → Events → Show History → 第一条记录 → 金额显示 → 金额隐藏 → Back。再次打开记录后，Student Account Portal 链接进入 App 内嵌浏览器：加载标志 → 有标题的空白页 → More → Cancel → X → 详情 → Back → 历史列表。最后隐藏历史并经 Week 返回 Month。

[公开截图和安全 AX 索引](../../evidence/2026-10-03-payment-record-native/manifest.json)包含 17 个采样画面。首次详情采样没有插图，后续插图加载后将字段整体下移；没有连续录像或受控缓存实验，不能量化加载时间或频率。关闭 Portal 后的一次 Back 使用了暂未就绪的元素索引；重新读取 AX 后成功返回。这是工具定位的暂态，不能据此认定 App 返回故障。

Portal 菜单显示 Open in system browser、Share via…、Copy link、Cancel，本批仅执行 Cancel 和 X。有标题的空白页不能证明服务成功、登录成功或服务器故障。刷新、前进后退、外部浏览器和分享分支均未执行。

## 隐私与证据边界

真实财务标题、记录编号、日期和金额不进入公开材料。详情插图异步加载会移动字段，逐字段固定遮罩不可靠；公开截图遮盖整个详情正文和私人标题，安全 AX 仅保留公共控件。脱敏草稿曾漏掉移动后的字段，已在提交前整区重做，并更新哈希及联系表；未公开未脱敏草稿。

公开遮罩后的像素一致只支持可见非私人区域，不能证明金额、正文布局或插图完全一致。后续 Figma 将使用明确标注的合成 DEMO 数据。本批尚未导入详情与 Portal 画板；原型覆盖仍为 175 个映射画板、378 个控件和 121 次运行，全应用完成状态为 `not_verified`。

新增金额眼睛控件名称假设见 [HCI 分析](hci-findings.md)。Mac AX 的字形名称不能代表已验证的 iPhone VoiceOver 行为或真人错误。
