# Room Preview 原生控件补查 · 2026-09-30

本轮使用 `polyulife-ui-analysis` 和原生 Computer Use，从 Home 进入 Room，查询 AG206，再补查 Preview。App 版本3.0.0已通过私有 Home AX重核；公开材料不包含身份或课表。现有 App 登录保留，网页认证表单未输入或提交。

## 实际步骤

| 步骤 | 观察事实与限制 | 证据 |
| --- | --- | --- |
| 01-room-empty | Home Room opens initial Today30-Sep empty field. | [截图](../../evidence/2026-09-30-room-preview-controls/01-room-empty.png) |
| 02-room-all | Entered AG206 via setValue/Search then focused retyping; eventual screenshot confirms Today30-Sep ALL. Early AX still initial; invalid stale index attempted once, corrected using fresh AX. | [截图](../../evidence/2026-09-30-room-preview-controls/02-room-all.png) |
| 03-preview-opening | Preview from ALL opens wrapper. Source screenshot is blank web area; saved full AX already contains AG206 webpage and disabled history controls. No visual loaded-page claim. | [截图](../../evidence/2026-09-30-room-preview-controls/03-preview-opening.png) |
| 04-preview-top | AG206 official page present in AX; saved screenshot still blank. Back and Forward disabled. | [截图](../../evidence/2026-09-30-room-preview-controls/04-preview-top.png) |
| 05-preview-menu | More opens menu from embedded Preview. | [截图](../../evidence/2026-09-30-room-preview-controls/05-preview-menu.png) |
| 06-copy-link-feedback | Copy link click dismisses menu. No visible copied toast in sampled screenshot and clipboard content not read or validated. | [截图](../../evidence/2026-09-30-room-preview-controls/06-copy-link-feedback.png) |
| 07-share-inspection | Share via click dismisses menu; neither a share sheet nor recipients appear in sampled AX/screenshot. No sharing submitted; share capability unresolved. | [截图](../../evidence/2026-09-30-room-preview-controls/07-share-inspection.png) |
| 08-preview-reload | Reload reconstructs AG206 webpage AX; source screenshot remains blank. Not proof of visual recovery or measured latency. | [截图](../../evidence/2026-09-30-room-preview-controls/08-preview-reload.png) |
| 09-open-system-result | Menu dismisses. Subsequent live native Chrome handle reports Room Search at polyu.edu.hk/learningspaces/AG206/. Handoff proven by live AX; follow-up browser capture interrupted by user interaction and not archived. | [截图](../../evidence/2026-09-30-room-preview-controls/09-open-system-result.png) |
| 11-preview-pdf | Actual AX AirMedia_Manual.pdf link clicked. Immediate sample still AG206. Subsequent login boundary proves navigation reached authentication, not readable PDF. | [截图](../../evidence/2026-09-30-room-preview-controls/11-preview-pdf.png) |
| 14-login-boundary | PolyU login is visible in screenshot; AX Sign in with your NetID and NetPassword, empty placeholder fields. Back enabled, Forward disabled. No credentials entered. | [截图](../../evidence/2026-09-30-room-preview-controls/14-login-boundary.png) |
| 15-browser-back | Back returns Room Search AX, with Back disabled and Forward enabled. Sampled web screenshot is blank. | [截图](../../evidence/2026-09-30-room-preview-controls/15-browser-back.png) |
| 16-browser-forward | Forward returns login AX, Back enabled and Forward disabled. Sampled webpage is blank; this does not prove the visual login rendered in this sample. | [截图](../../evidence/2026-09-30-room-preview-controls/16-browser-forward.png) |
| 17-room-after-external-change | User changed app before intended Back. Fresh AX/screenshot confirms Room AG206 Today30-Sep ALL. Not an Agent close/back execution. | [截图](../../evidence/2026-09-30-room-preview-controls/17-room-after-external-change.png) |
| 18-preview-reopen | Agent reopens Preview: Room Search and both history buttons disabled. Loading mark visible in screenshot; final page rendering not verified. | [截图](../../evidence/2026-09-30-room-preview-controls/18-preview-reopen.png) |
| 20-photo-previous-attempt | Previous button click changed AX Slide 3 to Slide 1. Screenshot remains blank; exact one-step sequence/autoplay/visual identity/endpoints unknown. Earlier scroll failed noWindowsAvailable; same handle revalidated before click. | [截图](../../evidence/2026-09-30-room-preview-controls/20-photo-previous-attempt.png) |
| 21-photo-next-current | Next button click changed AX Slide 1 to Slide 3. Screenshot remains blank; exact photo order/autoplay/endpoints not proven. | [截图](../../evidence/2026-09-30-room-preview-controls/21-photo-next-current.png) |
| 22-preview-close-room | Agent X closes Preview; screenshot confirms AG206, Today30-Sep and ALL retained. | [截图](../../evidence/2026-09-30-room-preview-controls/22-preview-close-room.png) |

[结构化步骤](room-preview-controls-20260930.json)、[脱敏 AX 摘录](room-preview-controls-20260930-ax.json)、[截图处理清单](../../evidence/2026-09-30-room-preview-controls/manifest.json)分别记录动作、控件状态和图像来源。

## 证据边界与失败

- 同一原生句柄恢复响应，全屏截图能呈现 Room 和一次登录页。原始3024×1898截图裁切 `[978,0,2046,1898]` 后缩放为576×1024；这是取证转换，不是手机设备截图。普通窗口和窗口缩放仍返回104×194或128×238缩略图，结束时已退出全屏，正常窗口视觉连接仍未恢复。
- Preview 的 AG206 页面 AX可读，但本轮该页面截图始终为空白或加载标记。不能把它当成已呈现网页，也不能把 Computer Use/渲染差异归为 App 业务缺陷。登录截图14则实际呈现了表单，前进回来的截图16仍空白。
- Copy link 只确认菜单关闭；未读系统剪贴板，也未看到可复查复制反馈。Share via只确认菜单关闭，未出现可确认的分享面板；未选择接收者、未分享。
- 系统浏览器交接通过实时原生 Chrome AX的标题和公开 URL确认。用户正在操作 Chrome阻止了后续捕获，未伪造截图或把私有浏览器标签归档。
- 使用指南链接最终进入 PolyU认证边界。没有证明 PDF内容可读，也没有登录。后退和前进的历史按钮启用状态与网页标题往返得到 AX证明。
- Previous/Next 后 Slide3→1、Slide1→3标签变化得到确认。由于网页截图为空白，自动轮播或精确一步照片顺序、端点、图片对应关系仍未验证。
- 早期过期索引失败、查询初始采样、一次 noWindowsAvailable以及人工页面变化均保留。人工返回 Room不算 Agent的关闭动作；之后 Agent实际 X关闭的步骤22才确认返回及 AG206/Today/ALL保留。

## HCI 解释与下一步

观察事实是菜单动作后没有可复查的复制提示，分享面板也未确认。可提出“系统状态可见性”假设，但尚不能认定实际复制或分享失败；需在可稳定截图的环境及真实手机验证反馈。

公开指南进入认证页面，需在 Figma表达这一边界，不能用已登录 App假设网页也自动登录。当前历史返回对可逆导航提供有限事实；仍需覆盖其它指南、重新加载的视觉反馈、更多历史、完整照片和网页范围。完整 PolyULife和 Figma仍为 `not_verified`，Agent操作也不是真人 Maze评估。
