# 全局导航与调用者返回回放

本批跨中断继续，2026-10-02归档。时间以各步UTC为准。使用Computer Use修改既有Figma并保存实际回放；原生Wrapper读取超时，本批没有新增原生状态/动作。全应用与完整视觉仍为 `not_verified`。

## 依据和实现

原生台账确认 More→Menu、More→Home、Notification→More，以及菜单/天气/Assistant的部分进出。原生截图/记录：`E-DRAWER`、`E-MENU-TRACE`、`E-MORE-SEARCH-TRACE`、`E-HOME-STUDY-MAP-TRACE` 和 `E-MENU-N-04/06`。这些不证明全部调用者日期/滚动位置组合。此次使用Open/Swap/Close覆盖层复现有限调用者返回；它是Figma架构，不推断原生架构。

补入More Home/Menu、Notification More、Monday Menu/More/Notification和Tuesday More入口，调整相关子页、加载、图片、网页和菜单关闭。配置36项净变化：新增8控件、替换28；另外原Mac Close临时改为Close overlay后恢复既有Back，不计净变化。原画板保留，新增一个缩放参考画板 `753:39`，关闭控件 `753:41`。明细、原配置和历史读回见 [连接记录](../../design/polyulife/global-navigation-connections.json)。

## 失败和修复

- 中断前Home→More一条连接已读回Open overlay；Figma报ERR_NETWORK_IO_SUSPENDED，原标签消失。更换同一浏览器中的标签后重新读回该设置，未重复创建文件。加载中的旧Present能进入More，但其Home/Menu当时尚未连接；4张失败截图保留。
- 构造Notification More时空心图标中心的右键选中背景42:1639，留下未完成Click None；复查后撤销，并在真正NavMore42:1653配置Swap overlay。没有把背景误绑留作完整导航。
- 原1382×320的Mac参考直接作覆盖层时，关闭控件在应用视口外（07）。改回独立宽画板后，Back直接回Home而不是Settings（10）。11实际是点击Home菜单打开抽屉，已纠正原拟标签Settings Back。
- 以同一原稿 [mac-general.svg](../../design/polyulife/mac-general.svg) 生成 [等比例参考](../../design/polyulife/mac-general-overlay-fit.svg)，576×133.37适配原型内展示，不是原生尺寸。新弹层Close能返回Settings→Drawer→原调用者；13/51两个来源样例保留。原始宽Mac画板仍在。参考文字变小，完整视觉不验收为通过。没有修改真实系统设置。
- 39的Tuesday坐标667未命中文字，保持Monday；673处命中后43显示Tuesday。**36实际保存图已显示Notification**，不能把随后的工具截图/定位猜测说成Notification中心点击失败。
- 旧Home返回时瞬时工具画面为空，但68、69实际保存文件均已恢复Home；没有补造一张已保存的全黑失败图。

## 有限回放

Monday从Home→More→Home、菜单Profile/Settings/紧急提示关闭，以及天气图片/公共网页、Assistant图片/演示网页返回均保存。Notification→More→Home保留Monday。Tuesday先滚到功能区，然后Notification→Menu→Notification→More→Settings→缩放Mac参考逐层返回，最后恢复Tuesday功能区；直接More及其政策菜单也回到同一来源。旧Home的More和Notification往返回归保留。各分段延续前一状态，08为明确原型Restart测试重置，64为旧Home独立起点；不是所有分段都独立重置。

Assistant Accept只点击Figma模拟热点，没有在真实服务接受条款、发送聊天。没有呼叫、退出登录、预约或更改权限/资料。私人资料和课程保持DEMO。Calendar默认内容、Calendar/QR跨页导航、独立起点关闭、其它调用者和全部输入/边界仍待完成。

## 原生来源关联校验

缩放参考复用 `S-SETTINGS-MAC-GENERAL`，context_variant明确区分。其真实截图E-MENU-N-04/06在该原生state的screenshot_evidence_ids中，但历史evidence记录自身state_ids为空。校验器现在同时承认已有state→evidence和evidence→state两种明确关联；仍要求真实native session，不能靠设计稿或任意截图代替。没有补写原生记录来通过校验。

## 实际截图索引

| UTC | 记录 | 图 |
| --- | --- | --- |
| 2026-09-30T17:43:28.421Z | Loaded Present Home before navigation; network interruption means version freshness unknown. | [E-GLOBAL-NAV-CHECKPOINT-00](../../evidence/2026-10-01-global-navigation-checkpoint/00-home-before.png) |
| 2026-09-30T17:43:28.719Z | Home More click opens More in loaded Present; overlay configuration persistence/freshness not established. | [E-GLOBAL-NAV-CHECKPOINT-01](../../evidence/2026-10-01-global-navigation-checkpoint/01-more-after-entry.png) |
| 2026-09-30T17:43:48.244Z | More Home click produces no destination in loaded Present; known missing app control, not native behavior. | [E-GLOBAL-NAV-CHECKPOINT-02](../../evidence/2026-10-01-global-navigation-checkpoint/02-more-home-no-change.png) |
| 2026-09-30T17:43:48.520Z | More Menu click also leaves More in loaded Present; new connection not yet configured. | [E-GLOBAL-NAV-CHECKPOINT-03](../../evidence/2026-10-01-global-navigation-checkpoint/03-more-menu-no-change.png) |
| 2026-10-02T09:14:15.478Z | Monday Home before new global navigation. | [E-GLOBAL-NAV-00](../../evidence/2026-10-02-global-navigation/00-monday-home.png) |
| 2026-10-02T09:14:15.782Z | Monday bottom More entry. | [E-GLOBAL-NAV-01](../../evidence/2026-10-02-global-navigation/01-monday-more.png) |
| 2026-10-02T09:14:37.310Z | More Home restores Monday caller. | [E-GLOBAL-NAV-02](../../evidence/2026-10-02-global-navigation/02-monday-home-return.png) |
| 2026-10-02T09:14:37.860Z | More Menu opens full DEMO drawer. | [E-GLOBAL-NAV-03](../../evidence/2026-10-02-global-navigation/03-more-drawer.png) |
| 2026-10-02T09:14:56.587Z | Drawer Profile opens synthetic read-only sample. | [E-GLOBAL-NAV-04](../../evidence/2026-10-02-global-navigation/04-profile.png) |
| 2026-10-02T09:14:56.837Z | Profile Back returns same drawer. | [E-GLOBAL-NAV-05](../../evidence/2026-10-02-global-navigation/05-profile-drawer-return.png) |
| 2026-10-02T09:14:57.155Z | Drawer Settings opens reference view, no preference modified. | [E-GLOBAL-NAV-06](../../evidence/2026-10-02-global-navigation/06-settings.png) |
| 2026-10-02T09:15:12.388Z | FAILED: wide overlay crops Close outside application viewport. | [E-GLOBAL-NAV-07](../../evidence/2026-10-02-global-navigation/07-mac-reference.png) |
| 2026-10-02T09:27:35.714Z | Prototype reset for Mac handoff repair; test reset is not an app action. | [E-GLOBAL-NAV-08](../../evidence/2026-10-02-global-navigation/08-restart-for-mac-recheck.png) |
| 2026-10-02T09:27:52.858Z | Mac reference uses its own wide viewport after clipping failure. | [E-GLOBAL-NAV-09](../../evidence/2026-10-02-global-navigation/09-mac-separate-frame.png) |
| 2026-10-02T09:28:06.573Z | FAILED: wide-reference Back returns Home instead of Settings. | [E-GLOBAL-NAV-10](../../evidence/2026-10-02-global-navigation/10-mac-settings-return.png) |
| 2026-10-02T09:28:06.957Z | After wrong Mac return, Home Menu opens Home drawer; not Settings Back. | [E-GLOBAL-NAV-11](../../evidence/2026-10-02-global-navigation/11-settings-drawer-return.png) |
| 2026-10-02T09:32:33.361Z | Settings reentry from Home drawer after wide-reference failure. | [E-GLOBAL-NAV-12](../../evidence/2026-10-02-global-navigation/12-settings-before-fit.png) |
| 2026-10-02T09:32:33.638Z | Uniformly fitted Mac reference popup; native window size not represented. | [E-GLOBAL-NAV-13](../../evidence/2026-10-02-global-navigation/13-mac-fit-popup.png) |
| 2026-10-02T09:32:49.099Z | Fitted reference Close returns Settings. | [E-GLOBAL-NAV-14](../../evidence/2026-10-02-global-navigation/14-fit-settings-return.png) |
| 2026-10-02T09:32:49.371Z | Settings Back returns retained Home drawer. | [E-GLOBAL-NAV-15](../../evidence/2026-10-02-global-navigation/15-fit-drawer-return.png) |
| 2026-10-02T09:32:49.675Z | Drawer close restores Monday Home after fitted reference. | [E-GLOBAL-NAV-16](../../evidence/2026-10-02-global-navigation/16-fit-home-return.png) |
| 2026-10-02T09:33:21.362Z | Open public emergency notice only; no call. | [E-GLOBAL-NAV-17](../../evidence/2026-10-02-global-navigation/17-emergency.png) |
| 2026-10-02T09:33:39.159Z | Emergency Close returns drawer without calling. | [E-GLOBAL-NAV-18](../../evidence/2026-10-02-global-navigation/18-emergency-drawer.png) |
| 2026-10-02T09:33:39.427Z | Drawer closes to More caller. | [E-GLOBAL-NAV-19](../../evidence/2026-10-02-global-navigation/19-drawer-more-return.png) |
| 2026-10-02T09:33:39.700Z | Weather article opened as nested overlay. | [E-GLOBAL-NAV-20](../../evidence/2026-10-02-global-navigation/20-weather.png) |
| 2026-10-02T09:33:53.165Z | Weather image expanded. | [E-GLOBAL-NAV-21](../../evidence/2026-10-02-global-navigation/21-weather-expanded.png) |
| 2026-10-02T09:34:11.767Z | Expanded weather image Close restores article. | [E-GLOBAL-NAV-22](../../evidence/2026-10-02-global-navigation/22-weather-image-return.png) |
| 2026-10-02T09:34:12.073Z | Weather public webpage prototype opened; full website not implemented. | [E-GLOBAL-NAV-23](../../evidence/2026-10-02-global-navigation/23-weather-web.png) |
| 2026-10-02T09:34:29.660Z | Web X closes to weather article. | [E-GLOBAL-NAV-24](../../evidence/2026-10-02-global-navigation/24-weather-web-return.png) |
| 2026-10-02T09:34:29.931Z | Weather Back restores More. | [E-GLOBAL-NAV-25](../../evidence/2026-10-02-global-navigation/25-weather-more-return.png) |
| 2026-10-02T09:34:30.200Z | Assistant before-hero sample after entry; inspect saved timing. | [E-GLOBAL-NAV-26](../../evidence/2026-10-02-global-navigation/26-assistant-loading.png) |
| 2026-10-02T09:34:40.525Z | Assistant article after demo delay. | [E-GLOBAL-NAV-27](../../evidence/2026-10-02-global-navigation/27-assistant-settled.png) |
| 2026-10-02T09:35:02.444Z | Assistant hero expands. | [E-GLOBAL-NAV-28](../../evidence/2026-10-02-global-navigation/28-assistant-expanded.png) |
| 2026-10-02T09:35:02.716Z | Hero Close restores article overlay. | [E-GLOBAL-NAV-29](../../evidence/2026-10-02-global-navigation/29-assistant-image-return.png) |
| 2026-10-02T09:35:02.985Z | Assistant embedded web loading sample, demo timing. | [E-GLOBAL-NAV-30](../../evidence/2026-10-02-global-navigation/30-assistant-web-loading.png) |
| 2026-10-02T09:35:15.489Z | Disclaimer sample after demo delay. | [E-GLOBAL-NAV-31](../../evidence/2026-10-02-global-navigation/31-assistant-disclaimer.png) |
| 2026-10-02T09:35:35.526Z | Figma Accept hotspot only opens recorded Welcome sample; no live website agreement or chat submission. | [E-GLOBAL-NAV-32](../../evidence/2026-10-02-global-navigation/32-assistant-welcome.png) |
| 2026-10-02T09:35:35.810Z | Welcome X closes to article. | [E-GLOBAL-NAV-33](../../evidence/2026-10-02-global-navigation/33-assistant-web-return.png) |
| 2026-10-02T09:35:36.079Z | Article Back returns More. | [E-GLOBAL-NAV-34](../../evidence/2026-10-02-global-navigation/34-assistant-more-return.png) |
| 2026-10-02T09:35:36.380Z | More Home returns Monday after menu/weather/Assistant. | [E-GLOBAL-NAV-35](../../evidence/2026-10-02-global-navigation/35-monday-full-return.png) |
| 2026-10-02T09:36:48.947Z | Monday Notification entry. | [E-GLOBAL-NAV-36](../../evidence/2026-10-02-global-navigation/36-monday-notification.png) |
| 2026-10-02T09:36:49.217Z | Notification More swaps top global page. | [E-GLOBAL-NAV-37](../../evidence/2026-10-02-global-navigation/37-notification-more.png) |
| 2026-10-02T09:36:49.475Z | Cross-page Notification More Home restores Monday. | [E-GLOBAL-NAV-38](../../evidence/2026-10-02-global-navigation/38-cross-nav-monday-return.png) |
| 2026-10-02T09:36:49.758Z | Date coordinate667 misses T; stays Monday with hotspot hints. Later673 succeeds. | [E-GLOBAL-NAV-39](../../evidence/2026-10-02-global-navigation/39-tuesday-home.png) |
| 2026-10-02T09:38:47.485Z | Notification retarget sample; saved36 already proves initial center click succeeded. | [E-GLOBAL-NAV-40](../../evidence/2026-10-02-global-navigation/40-notification-target-recheck.png) |
| 2026-10-02T09:39:19.854Z | Notification More click on visible glyph opens More. | [E-GLOBAL-NAV-41](../../evidence/2026-10-02-global-navigation/41-notification-more-recheck.png) |
| 2026-10-02T09:39:20.094Z | Notification More Home restores Monday caller. | [E-GLOBAL-NAV-42](../../evidence/2026-10-02-global-navigation/42-cross-nav-monday-recheck.png) |
| 2026-10-02T09:39:20.365Z | Tuesday selected using actual T glyph. | [E-GLOBAL-NAV-43](../../evidence/2026-10-02-global-navigation/43-tuesday-selected.png) |
| 2026-10-02T09:40:09.237Z | Tuesday Home scrolled before cross-page return. | [E-GLOBAL-NAV-44](../../evidence/2026-10-02-global-navigation/44-tuesday-scrolled.png) |
| 2026-10-02T09:40:09.477Z | Tuesday bottom Notification opens. | [E-GLOBAL-NAV-45](../../evidence/2026-10-02-global-navigation/45-tuesday-notification.png) |
| 2026-10-02T09:40:09.743Z | Notification menu opens drawer. | [E-GLOBAL-NAV-46](../../evidence/2026-10-02-global-navigation/46-notification-drawer.png) |
| 2026-10-02T09:40:10.010Z | Drawer closes to Notification caller. | [E-GLOBAL-NAV-47](../../evidence/2026-10-02-global-navigation/47-notification-drawer-return.png) |
| 2026-10-02T09:40:10.280Z | Notification More swaps global page while Home remains caller. | [E-GLOBAL-NAV-48](../../evidence/2026-10-02-global-navigation/48-tuesday-notification-more.png) |
| 2026-10-02T09:40:49.577Z | More Menu from Tuesday cross-page caller. | [E-GLOBAL-NAV-49](../../evidence/2026-10-02-global-navigation/49-tuesday-more-drawer.png) |
| 2026-10-02T09:40:49.842Z | Settings opens above Tuesday More drawer. | [E-GLOBAL-NAV-50](../../evidence/2026-10-02-global-navigation/50-tuesday-settings.png) |
| 2026-10-02T09:40:50.115Z | Second fitted reference sample, nested under More caller. | [E-GLOBAL-NAV-51](../../evidence/2026-10-02-global-navigation/51-tuesday-mac-fit.png) |
| 2026-10-02T09:40:50.352Z | Fitted popup closes to Settings. | [E-GLOBAL-NAV-52](../../evidence/2026-10-02-global-navigation/52-tuesday-settings-return.png) |
| 2026-10-02T09:40:50.622Z | Settings Back restores More drawer. | [E-GLOBAL-NAV-53](../../evidence/2026-10-02-global-navigation/53-tuesday-settings-drawer.png) |
| 2026-10-02T09:40:50.892Z | Drawer closes to More, not Home. | [E-GLOBAL-NAV-54](../../evidence/2026-10-02-global-navigation/54-tuesday-drawer-more.png) |
| 2026-10-02T09:40:51.160Z | More Home preserves Tuesday and scrolled feature region. | [E-GLOBAL-NAV-55](../../evidence/2026-10-02-global-navigation/55-tuesday-caller-return.png) |
| 2026-10-02T09:41:14.133Z | Tuesday direct More entry independent of Notification. | [E-GLOBAL-NAV-56](../../evidence/2026-10-02-global-navigation/56-tuesday-direct-more.png) |
| 2026-10-02T09:41:14.607Z | Privacy entry from nested More drawer. | [E-GLOBAL-NAV-57](../../evidence/2026-10-02-global-navigation/57-more-privacy.png) |
| 2026-10-02T09:41:14.880Z | Privacy Back restores drawer caller. | [E-GLOBAL-NAV-58](../../evidence/2026-10-02-global-navigation/58-privacy-more-drawer.png) |
| 2026-10-02T09:41:15.115Z | Terms loading mark after nested menu entry. | [E-GLOBAL-NAV-59](../../evidence/2026-10-02-global-navigation/59-more-terms-entry.png) |
| 2026-10-02T09:41:36.098Z | Terms settled in nested menu path. | [E-GLOBAL-NAV-60](../../evidence/2026-10-02-global-navigation/60-more-terms-settled.png) |
| 2026-10-02T09:41:36.368Z | Terms Back restores same More drawer. | [E-GLOBAL-NAV-61](../../evidence/2026-10-02-global-navigation/61-terms-more-drawer.png) |
| 2026-10-02T09:41:36.638Z | Drawer closes to More after both policy entries. | [E-GLOBAL-NAV-62](../../evidence/2026-10-02-global-navigation/62-policies-more-return.png) |
| 2026-10-02T09:41:36.913Z | More Home restores Tuesday scrolled caller after policies. | [E-GLOBAL-NAV-63](../../evidence/2026-10-02-global-navigation/63-policies-tuesday-return.png) |
| 2026-10-02T09:42:01.793Z | Existing Home feature flow reopened for regression. | [E-GLOBAL-NAV-64](../../evidence/2026-10-02-global-navigation/64-legacy-home.png) |
| 2026-10-02T09:42:02.095Z | Existing Home More now opens retained overlay. | [E-GLOBAL-NAV-65](../../evidence/2026-10-02-global-navigation/65-legacy-more.png) |
| 2026-10-02T09:42:02.366Z | More Home restores existing Home sample. | [E-GLOBAL-NAV-66](../../evidence/2026-10-02-global-navigation/66-legacy-more-home.png) |
| 2026-10-02T09:42:02.635Z | Existing Home Notification entry. | [E-GLOBAL-NAV-67](../../evidence/2026-10-02-global-navigation/67-legacy-notification.png) |
| 2026-10-02T09:42:02.905Z | Saved return shows Home; immediate tool-only screenshot was blank, actual saved PNG recovered. | [E-GLOBAL-NAV-68](../../evidence/2026-10-02-global-navigation/68-legacy-notification-home.png) |
| 2026-10-02T09:42:34.493Z | Re-observe legacy Notification Home return after blank capture; actual pixels reviewed. | [E-GLOBAL-NAV-69](../../evidence/2026-10-02-global-navigation/69-legacy-return-settled.png) |
| 2026-10-02T09:46:59.327Z | Editor root fit reference with editable text/vector and576x133.37 dimensions; prototype adaptation only. | [E-GLOBAL-NAV-70](../../evidence/2026-10-02-global-navigation/70-editor-mac-fit.png) |

共75张实际截图（旧检查点4、新Present70、编辑器1）和2张拼图。新批33项应用区域比较中27项相同、6项差异，5项差异在右边缘最后2px，另1项为日期定位错误/正确状态；这些差异均保留，不据此宣称全像素一致。不能将等同比例当原生视觉通过。清单保留哈希、尺寸、账号遮盖和差异框：[旧检查点](../../evidence/2026-10-01-global-navigation-checkpoint/manifest.json)、[新批](../../evidence/2026-10-02-global-navigation/manifest.json)。公开图与原图除账号遮盖外逐像素一致。

当前140映射画板、320配置控件、94次原型运行；原生仍135状态/268动作（193 observed、75 not_attempted）。全范围与完整视觉未完成；图片/控件数量不代表覆盖率。
