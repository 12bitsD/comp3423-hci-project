# 政策页已观察滚动视口与重入复验

2026-10-01（本地；步骤时间为 UTC）。使用 `polyulife-ui-analysis` 和 Computer Use 在既有 Figma 中继续复现。原生 Wrapper 本轮连接超时，未新增原生状态/动作；以下是设计还原及 Agent 原型回放，不是原生新观察或真人测试。全应用保持 `not_verified`。

## 原生依据和范围

Privacy [E-MENU-N-19](../../evidence/2026-09-28-full-audit/native-menu-192932-privacy-scrolled-01.png) 和 Terms [E-MENU-N-24](../../evidence/2026-09-28-full-audit/native-menu-193010-terms-scrolled-01.png) 显示关闭 cookie 后滚动到两个后续视口。Privacy 可见段落4/5，Terms 可见段落3；顶部/底部被裁的文字不是完整正文。仅逐行转录能读出的文字，省略光标；字体、几何近似，Terms顶部不可辨的字形及底部下一段小片段未补造。初始和后续截图不连续，不能推导完整中间正文、滚动量或边界。公开 `dpo.email@polyu.edu.hk` 来自截图中的学校业务联系地址。

生成稿见 [脚本](../../design/scripts/build_policy_scrolled_svg.py) 与 [来源哈希](../../design/polyulife/policy-scrolled-sources.json)。Figma 新增 Privacy `655:19`、Terms `655:62` 两个576×970画板，位置分别0/700,63000。文字、表头、滚动条用可编辑层重建，尚未逐像素验收。

## 原型操作

从 Home 打开菜单 → Privacy/Terms → Close cookie → **键盘 ↓** → 已观察滚动视口 → Back → 菜单 → 灰色区域关闭菜单回 Home。↓ 是原型输入代理，不表示原生支持键盘；目前在整个初始画板上可用，关闭 cookie 是回放约定而非条件门控。未实现连续/反向滚动、拖动条、完整正文或政策正文链接。没有点击 Accept 或模拟接受条款。

两条根代理使用 Swap overlay；滚动后 Back 使用 Close overlay。Privacy 入口从 Navigate to 改为 Open overlay，初始 Back 从 Back 改为 Close overlay，从而直接保留菜单调用者。覆盖层是 Figma 架构，原生架构未知。Privacy滚动后返回菜单有原生执行依据；Terms滚动后返回仅从初始 Back 推广，action_id为null。既有独立 cookie 组件保留，未换成新的全屏关闭状态。新增4控件、替换2既有控件，节点和读回见 [连接记录](../../design/polyulife/policy-scrolled-connections.json)。

## 失败与同素材复验

首次重入 Privacy 的实际保存图11丢失校名标志；同一PNG通过图像上传对话框重传到50:2065，位置64,168、尺寸246×49及STRETCH保留，imageShouldColorManage从false读回为true。随后14和17连续重入可见，差异仅在校名区域。原型同会话保留关闭 cookie，不是原生重复进入规则。

Terms重入的实际保存图19加载卡片缺校徽，后续20正文标志可见。同一加载PNG重传621:34，位置261,486、56×56及STRETCH保留，色彩管理读回true；24、27连续加载均有图，25、28正文及返回正常。这些变化不能单独确定缺图根因；长期稳定性与完整保真仍未验证。两个失败图保留，原生 App 未归为有此缺陷。

05、06仍是加载状态，06原拟标签“visible”经实际保存像素检查改正；11正确登记为关闭cookie内部状态。没有将暂态误计为加载成功完成。

## 实际保存步骤

| UTC | 记录 | 截图 |
| --- | --- | --- |
| 2026-09-30T17:22:13.497Z | Home opens drawer before policy replay. | [E-POLICY-SCROLL-SCREEN-00](../../evidence/2026-10-01-policy-scroll/00-home-drawer.png) |
| 2026-09-30T17:22:21.212Z | Privacy entry displays initial policy and cookie banner. | [E-POLICY-SCROLL-SCREEN-01](../../evidence/2026-10-01-policy-scroll/01-privacy-visible.png) |
| 2026-09-30T17:22:30.444Z | Close cookie before using scroll proxy. | [E-POLICY-SCROLL-SCREEN-02](../../evidence/2026-10-01-policy-scroll/02-privacy-dismissed.png) |
| 2026-09-30T17:22:30.695Z | Down proxy displays observed finite viewport. | [E-POLICY-SCROLL-SCREEN-03](../../evidence/2026-10-01-policy-scroll/03-privacy-scrolled.png) |
| 2026-09-30T17:22:30.976Z | Privacy scrolled Back closes overlay directly to drawer. | [E-POLICY-SCROLL-SCREEN-04](../../evidence/2026-10-01-policy-scroll/04-privacy-drawer-return.png) |
| 2026-09-30T17:22:38.652Z | First Terms entry shows loading mark; not settled content. | [E-POLICY-SCROLL-SCREEN-05](../../evidence/2026-10-01-policy-scroll/05-terms-entry.png) |
| 2026-09-30T17:22:38.711Z | Capture labelled visible originally still shows loading; corrected after saved-pixel inspection. | [E-POLICY-SCROLL-SCREEN-06](../../evidence/2026-10-01-policy-scroll/06-terms-visible.png) |
| 2026-09-30T17:22:48.737Z | Terms after demo timer. | [E-POLICY-SCROLL-SCREEN-07](../../evidence/2026-10-01-policy-scroll/07-terms-settled.png) |
| 2026-09-30T17:22:49.041Z | Close Terms cookie before proxy. | [E-POLICY-SCROLL-SCREEN-08](../../evidence/2026-10-01-policy-scroll/08-terms-dismissed.png) |
| 2026-09-30T17:22:49.343Z | Down proxy opens observed Terms finite viewport. | [E-POLICY-SCROLL-SCREEN-09](../../evidence/2026-10-01-policy-scroll/09-terms-scrolled.png) |
| 2026-09-30T17:22:49.614Z | Terms scrolled Close overlay returns drawer. | [E-POLICY-SCROLL-SCREEN-10](../../evidence/2026-10-01-policy-scroll/10-terms-drawer-return.png) |
| 2026-09-30T17:22:59.808Z | Reentry retains dismissed cookie in this prototype session, but public wordmark disappears; failure preserved. | [E-POLICY-SCROLL-SCREEN-11](../../evidence/2026-10-01-policy-scroll/11-privacy-reentry.png) |
| 2026-09-30T17:23:00.113Z | Initial Privacy Back now Close overlay; regression return. | [E-POLICY-SCROLL-SCREEN-12](../../evidence/2026-10-01-policy-scroll/12-privacy-initial-back.png) |
| 2026-09-30T17:23:00.411Z | Close drawer to original Home caller. | [E-POLICY-SCROLL-SCREEN-13](../../evidence/2026-10-01-policy-scroll/13-home-return.png) |
| 2026-09-30T17:23:56.621Z | Same PNG reuploaded; reentry and wordmark inspected. | [E-POLICY-SCROLL-SCREEN-14](../../evidence/2026-10-01-policy-scroll/14-privacy-after-image-reupload.png) |
| 2026-09-30T17:24:08.764Z | Second Privacy proxy sample after image reupload. | [E-POLICY-SCROLL-SCREEN-15](../../evidence/2026-10-01-policy-scroll/15-privacy-scrolled-recheck.png) |
| 2026-09-30T17:24:09.034Z | Second scrolled Privacy Back. | [E-POLICY-SCROLL-SCREEN-16](../../evidence/2026-10-01-policy-scroll/16-privacy-drawer-recheck.png) |
| 2026-09-30T17:24:09.344Z | Consecutive reentry after same PNG reupload; finite visual check. | [E-POLICY-SCROLL-SCREEN-17](../../evidence/2026-10-01-policy-scroll/17-privacy-image-second-entry.png) |
| 2026-09-30T17:24:09.597Z | Second initial Back closes to drawer. | [E-POLICY-SCROLL-SCREEN-18](../../evidence/2026-10-01-policy-scroll/18-privacy-initial-back-recheck.png) |
| 2026-09-30T17:24:17.705Z | Terms second entry loading card has no mark; saved-pixel failure preserved. | [E-POLICY-SCROLL-SCREEN-19](../../evidence/2026-10-01-policy-scroll/19-terms-reentry-transition.png) |
| 2026-09-30T17:24:28.879Z | Terms reentry after timer; inspect wordmark and independent dismissed state. | [E-POLICY-SCROLL-SCREEN-20](../../evidence/2026-10-01-policy-scroll/20-terms-reentry-settled.png) |
| 2026-09-30T17:24:29.128Z | Second Terms finite proxy. | [E-POLICY-SCROLL-SCREEN-21](../../evidence/2026-10-01-policy-scroll/21-terms-scrolled-recheck.png) |
| 2026-09-30T17:24:29.389Z | Second Terms scrolled return. | [E-POLICY-SCROLL-SCREEN-22](../../evidence/2026-10-01-policy-scroll/22-terms-drawer-recheck.png) |
| 2026-09-30T17:24:29.630Z | Drawer closes to Home after second Terms run. | [E-POLICY-SCROLL-SCREEN-23](../../evidence/2026-10-01-policy-scroll/23-home-final.png) |
| 2026-09-30T17:25:37.471Z | Same Terms loading PNG reupload; first subsequent entry. | [E-POLICY-SCROLL-SCREEN-24](../../evidence/2026-10-01-policy-scroll/24-terms-reupload-loading.png) |
| 2026-09-30T17:25:49.710Z | Settled Terms after loading-image reupload. | [E-POLICY-SCROLL-SCREEN-25](../../evidence/2026-10-01-policy-scroll/25-terms-reupload-settled.png) |
| 2026-09-30T17:25:49.989Z | Initial Terms Back returns caller. | [E-POLICY-SCROLL-SCREEN-26](../../evidence/2026-10-01-policy-scroll/26-terms-reupload-drawer.png) |
| 2026-09-30T17:25:50.239Z | Second consecutive entry after same PNG reupload. | [E-POLICY-SCROLL-SCREEN-27](../../evidence/2026-10-01-policy-scroll/27-terms-reupload-second-loading.png) |
| 2026-09-30T17:30:55.123Z | Second settled Terms after mark reupload. | [E-POLICY-SCROLL-SCREEN-28](../../evidence/2026-10-01-policy-scroll/28-terms-reupload-second-settled.png) |
| 2026-09-30T17:30:55.389Z | Second initial Terms Back after mark reupload. | [E-POLICY-SCROLL-SCREEN-29](../../evidence/2026-10-01-policy-scroll/29-terms-reupload-second-drawer.png) |
| 2026-09-30T17:30:55.633Z | Final caller restored after finite repair tests. | [E-POLICY-SCROLL-SCREEN-30](../../evidence/2026-10-01-policy-scroll/30-home-delivery.png) |

本批31张实际 Present 截图加1张拼图。18项应用裁片比较中16项相等、2项差异（Privacy标志及Terms加载校徽失败/恢复）；比较不证明原生视觉保真。清单、尺寸、哈希、遮盖范围与完整差异框见 [manifest](../../evidence/2026-10-01-policy-scroll/manifest.json)。只遮盖浏览器右上账号区域，正文不含私人账户数据；身份/课程为DEMO。原始截图位于被忽略目录，公開PNG逐像素验证除遮盖区域外相同。

4次运行分别记录首轮视觉失败、Privacy重传、Terms重入视觉失败和Terms加载校徽重传；后续运行连续沿用前一菜单/来源，不是四次独立重置。当前139映射画板、312控件、86次运行、16滚动区域、3个内部组件状态；原生仍135状态/268动作。新增的有限键盘代理不计作连续滚动区域。完整范围与视觉保真仍 `not_verified`。

下一步需原生连续取证补齐正文/边界/反向滚动与重复进入状态，再核验网站搜索、菜单和公开链接。当前只完成有证据的两个视口及有限返回样例，不关闭模块发现队列。
