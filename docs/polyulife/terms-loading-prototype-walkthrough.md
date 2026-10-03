# Terms 加载状态接入与返回栈修复 — 2026-10-01

按既有原生[E-MENU-N-21](../../evidence/2026-09-28-full-audit/native-menu-192948-terms-loading-01.png)重建空白嵌入正文、灰遮罩、中央白卡与校徽。原生状态S-TERMS-LOADING引用该截图，原截图记录state_ids为空的历史元数据未重写。新画板621:20为576×970、Clip content、位置0,58500；标题、遮罩、白卡可编辑，校徽为56×56原图裁片。字体/几何近似，捕获指针未复制；没有新增条款接受动作。

## 最终连线

菜单Terms75:1700改为Open overlay→621:20；加载根After delay800ms Swap overlay→50:1862；已加载条款Back50:1908改为Close overlay。覆盖层保持原菜单调用栈，仅为Figma实现，不能推断原生架构。800ms仅演示延时，原生截图时间差不是加载时长。新增1个控件、替换2个既有控件，共132映射画板、303控件、71次原型运行。

初版Navigate→加载→正文，再显式Navigate回菜单时，菜单Close Back重新打开条款；08–13保存失败，13确认循环。改为覆盖层后，17–22实际通知→菜单→加载→正文→菜单→通知；23–29实际Tuesday DEMO Home→菜单→加载→正文→关闭cookie→菜单→Home，两个来源恢复。加载图19/25为实际短暂状态截图，非本地渲染。30/31核对最终根无额外起点、After delay800ms/Swap overlay/Instant读回。旧连接作为superseded保留。

八项裁片比较7项相等、1项差异，见[清单](../../evidence/2026-10-01-terms-loading/manifest.json)和[截图对照](../../evidence/2026-10-01-terms-loading/contact-sheet.png)。唯一差异是初版Navigate加载10与最终覆盖层加载19，全裁片范围不同，原因未确定；最终两个调用者加载19/25相等。仅为原型一致性；学校标志当前可见，既有D-POLICY-WORDMARK-RENDER仍open。06/07记录More菜单未连接的尝试，随后改从已有通知入口回放，不将未连接归因原生App。

## 仍需完成

原生清单显示PolyULife运行，当前bundle ID歧义解析后的Wrapper绑定再次超时；没有重启或新增原生动作。加载中Back/取消、政策连续正文和滚动、站内菜单/搜索、原生重复进入cookie状态、其它来源与独立settled参考的返回仍未确认或实现。原生135状态/268动作数组保持不变。全应用 `not_verified`，Agent回放不作为真人Maze评估。

源码：[生成脚本](../../design/scripts/build_terms_loading_svg.py)、[SVG](../../design/polyulife/terms-loading.svg)、[资产来源](../../design/polyulife/terms-loading-assets.json)、[连接清单](../../design/polyulife/terms-loading-connections.json)。
