# Room Preview 网页、菜单与照片原型

2026-09-29。本批继续既有原生证据的 Figma 重建。收到恢复回复后，Computer Use 仍返回 Mac 锁定；没有新增原生 App 状态、动作或真人评估。完整应用仍为 `not_verified`。

## 来源与实现

以 [Room 原生走查](room-walkthrough.md)中的 E-PREVIEWLOAD、E-PREVIEWTOP、E-MENU、E-PHOTO1、E-PHOTO2、E-RETURN 为布局和顺序依据。补充打开[官方 AG206 网页](https://www.polyu.edu.hk/learningspaces/AG206/)，用浏览器公开素材导出获得照片、横幅和标志。此网页会自动轮播，AX 标签和画面有时间差；本地检查导出字节后确认官方3.jpg对应第一张椅子/白板照片，1.jpg对应第二张显示器/红桌照片，不能由文件名或网页轮播时间推断原生行为。[素材来源与哈希](../../design/polyulife/room-preview-assets.json)独立登记；[网页截图](../../evidence/2026-09-28-full-audit/room-preview-official-web-source.png)仅为补充网页证据，精确截图时间未保留。

新增三个576×970画板：网页310:12、加载312:95、菜单312:153，Y=33000。网页内310:14为561×726竖向滚动区域，位于(8,152)，内容高度1809，只做到原生已观察照片视口。菜单为透明底加70%遮罩与菜单，Cancel关闭叠层而保留下面的页面状态。照片是组件集312:257的两态实例314:12，位于滚动内容(18,1389)，大小526×394.5；第一态312:256，第二态312:258。只连接一次Next。S-PHOTO1用滚动状态登记，S-PHOTO2用组件状态登记，S-RETURN复用已有Available12:105，均不虚增完整画板。

新增6个连接：Available Preview打开加载、After delay800ms交换为网页、网页菜单打开、Cancel关闭、Next切换组件、X关闭网页。800ms是演示参数，不是原生加载耗时；加载标记仅静态采样。加载阶段X和菜单未连接。SVG文本/形状可编辑，五份图片为栅格；[生成器](../../design/scripts/build_room_preview_svg.py)生成源码，滚动Frame/约束、组件和连接在Figma UI中配置。

## 回放、修复与比较

32张实际Present截图记录四次Tuesday Home入口。首轮完整走通Home→Room→A→AG206→Available→Preview→菜单/Cancel→滚动→照片Next→X→Available→Back→Home。初始截图记录了加载帧，随后进入Room Search。第二轮证实原型重新打开保留之前的滚动和第二张照片；这是Figma的当前表现，原生重新打开的重置/保留规则尚未观察。

上滚途中曾出现横幅和标志空白，重复加载帧也曾缺少加载标记。全部保留失败截图，然后通过图片填充对话框重新上传三份PNG。修复后的页顶及反向滚动页顶逐像素一致，加载标记再次可见。导入后字体实际为Inter，两行正文右侧裁切，已从25px改为24px；电话号码相对正文起点调整为180px。修复截图可读，但不代表完整视觉验收或长期图片稳定性通过。组件的两个照片填充在本批前段也已独立上传。

四次关闭Preview后的Available，与进入前基线应用区域(461,60,818,661)逐像素一致；四次返回Home亦与原始Tuesday Home基线逐像素一致。菜单在页顶和中间滚动位置取消后，各自底层视口逐像素一致。反向滚动到顶在修复后通过同区域像素比较。中间滚动、反向滚动、不同位置关闭是原型检查，不新增原生动作。

## 保留缺口

下方完整网页、PDF、真实滚动边界、Previous/更多Next/轮播边界、原生重新打开语义均未验证。浏览器刷新/前进/后退和菜单系统浏览器/分享/复制未连接。仅Tuesday Home来源测试了新分支；其它来源及独立Room入口缺口保留。字体、图标、加载动画与完整视觉一致性未完成，整个Room及完整应用都未完成。

[节点、配置读回、修复与像素比较](../../design/polyulife/room-preview-connections.json)

| 步骤 | 结果 | 证据 |
| --- | --- | --- |
| 01-home-baseline | recorded | [E-ROOM-PREVIEW-P-01](../../evidence/2026-09-28-full-audit/room-preview-proto-01-home-baseline.png) |
| 02-room-entry | recorded | [E-ROOM-PREVIEW-P-02](../../evidence/2026-09-28-full-audit/room-preview-proto-02-room-entry.png) |
| 03-suggestion | recorded | [E-ROOM-PREVIEW-P-03](../../evidence/2026-09-28-full-audit/room-preview-proto-03-suggestion.png) |
| 04-all | recorded | [E-ROOM-PREVIEW-P-04](../../evidence/2026-09-28-full-audit/room-preview-proto-04-all.png) |
| 05-available-baseline | recorded | [E-ROOM-PREVIEW-P-05](../../evidence/2026-09-28-full-audit/room-preview-proto-05-available-baseline.png) |
| 06-preview-entry | recorded | [E-ROOM-PREVIEW-P-06](../../evidence/2026-09-28-full-audit/room-preview-proto-06-preview-entry.png) |
| 07-preview-loaded | recorded | [E-ROOM-PREVIEW-P-07](../../evidence/2026-09-28-full-audit/room-preview-proto-07-preview-loaded.png) |
| 08-menu | recorded | [E-ROOM-PREVIEW-P-08](../../evidence/2026-09-28-full-audit/room-preview-proto-08-menu.png) |
| 09-menu-cancel | menu_cancel_preserved_underlying_view_pixel_equal | [E-ROOM-PREVIEW-P-09](../../evidence/2026-09-28-full-audit/room-preview-proto-09-menu-cancel.png) |
| 10-scroll-partial | recorded | [E-ROOM-PREVIEW-P-10](../../evidence/2026-09-28-full-audit/room-preview-proto-10-scroll-partial.png) |
| 11-photo-two | recorded | [E-ROOM-PREVIEW-P-11](../../evidence/2026-09-28-full-audit/room-preview-proto-11-photo-two.png) |
| 12-return-available | available_return_pixel_equal | [E-ROOM-PREVIEW-P-12](../../evidence/2026-09-28-full-audit/room-preview-proto-12-return-available.png) |
| 13-return-home | home_return_pixel_equal | [E-ROOM-PREVIEW-P-13](../../evidence/2026-09-28-full-audit/room-preview-proto-13-return-home.png) |
| 14-reenter-loading | loading_mark_blank_before_reupload | [E-ROOM-PREVIEW-P-14](../../evidence/2026-09-28-full-audit/room-preview-proto-14-reenter-loading.png) |
| 15-reenter-top | reopen_retains_photo_two_and_scroll_native_semantics_unverified | [E-ROOM-PREVIEW-P-15](../../evidence/2026-09-28-full-audit/room-preview-proto-15-reenter-top.png) |
| 16-intermediate-scroll | reopen_retains_photo_two_and_scroll_native_semantics_unverified | [E-ROOM-PREVIEW-P-16](../../evidence/2026-09-28-full-audit/room-preview-proto-16-intermediate-scroll.png) |
| 17-reverse-intermediate | recorded | [E-ROOM-PREVIEW-P-17](../../evidence/2026-09-28-full-audit/room-preview-proto-17-reverse-intermediate.png) |
| 18-scrolled-menu | recorded | [E-ROOM-PREVIEW-P-18](../../evidence/2026-09-28-full-audit/room-preview-proto-18-scrolled-menu.png) |
| 19-scrolled-cancel | menu_cancel_preserved_underlying_view_pixel_equal | [E-ROOM-PREVIEW-P-19](../../evidence/2026-09-28-full-audit/room-preview-proto-19-scrolled-cancel.png) |
| 20-reverse-top | banner_and_wordmark_blank_before_reupload | [E-ROOM-PREVIEW-P-20](../../evidence/2026-09-28-full-audit/room-preview-proto-20-reverse-top.png) |
| 21-second-return-available | available_return_pixel_equal | [E-ROOM-PREVIEW-P-21](../../evidence/2026-09-28-full-audit/room-preview-proto-21-second-return-available.png) |
| 22-second-return-home | home_return_pixel_equal | [E-ROOM-PREVIEW-P-22](../../evidence/2026-09-28-full-audit/room-preview-proto-22-second-return-home.png) |
| 23-fixed-entry | loading_mark_blank_before_reupload | [E-ROOM-PREVIEW-P-23](../../evidence/2026-09-28-full-audit/room-preview-proto-23-fixed-entry.png) |
| 24-fixed-top | recorded | [E-ROOM-PREVIEW-P-24](../../evidence/2026-09-28-full-audit/room-preview-proto-24-fixed-top.png) |
| 25-fixed-body | two_clipped_lines_and_hotline_spacing_fixed | [E-ROOM-PREVIEW-P-25](../../evidence/2026-09-28-full-audit/room-preview-proto-25-fixed-body.png) |
| 26-fixed-reverse-top | reverse_scroll_top_pixel_equal_after_reupload | [E-ROOM-PREVIEW-P-26](../../evidence/2026-09-28-full-audit/room-preview-proto-26-fixed-reverse-top.png) |
| 27-fixed-return-available | available_return_pixel_equal | [E-ROOM-PREVIEW-P-27](../../evidence/2026-09-28-full-audit/room-preview-proto-27-fixed-return-available.png) |
| 28-fixed-return-home | home_return_pixel_equal | [E-ROOM-PREVIEW-P-28](../../evidence/2026-09-28-full-audit/room-preview-proto-28-fixed-return-home.png) |
| 29-loading-fixed | loading_mark_visible_after_reupload | [E-ROOM-PREVIEW-P-29](../../evidence/2026-09-28-full-audit/room-preview-proto-29-loading-fixed.png) |
| 30-final-top | recorded | [E-ROOM-PREVIEW-P-30](../../evidence/2026-09-28-full-audit/room-preview-proto-30-final-top.png) |
| 31-final-available | available_return_pixel_equal | [E-ROOM-PREVIEW-P-31](../../evidence/2026-09-28-full-audit/room-preview-proto-31-final-available.png) |
| 32-final-home | home_return_pixel_equal | [E-ROOM-PREVIEW-P-32](../../evidence/2026-09-28-full-audit/room-preview-proto-32-final-home.png) |
