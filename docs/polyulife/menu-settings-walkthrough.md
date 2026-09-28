# 侧边菜单、Settings 与信息页实际走查

观察区间：2026-09-28 15:59:54–16:05:58 UTC，即香港时间 2026-09-28 23:59:54 至 2026-09-29 00:05:58。使用真实 PolyULife Mac 窗口的 Computer Use。只读查看设置和个人页结构，没有更改开关、呼叫电话、退出登录或修改资料。

## 实际动作与结果

| 时间（UTC） | 动作与结果 | 证据与边界 |
| --- | --- | --- |
| 15:59:54 | 从 More 左上菜单展开抽屉，列出 Profile、Settings、Emergency Contact、Log Out、Privacy Policy、Terms of Use 和 version: 3.0.0 | [菜单条目裁切](../../evidence/2026-09-28-full-audit/drawer-155955-menu-items-only.png)；账户区排除 |
| 16:00:10 | 打开 Settings，显示 Location Service OFF、Push Notification OFF，各附前往系统设置的文字说明；下面还可见一个没有文字标题的开关样式控件 | [Settings](../../evidence/2026-09-28-full-audit/settings-160011-initial.png)；第三项 AX 只有无描述 element，功能与值语义未知 |
| 16:01:06 | 点击返回，AX 恢复菜单条目 | `E-MENU-TRACE`；无独立返回截图 |
| 16:01:28 → 16:01:54 | 打开 Emergency Contact，弹窗先提示遇危险应撤离至安全地点，再向 Campus Control Centre 报告；提供 Call 27667666 和 Close。只点 Close，AX 恢复菜单 | [公共紧急提示](../../evidence/2026-09-28-full-audit/emergency-160129-public-contact-dialog.png) 与 `E-MENU-TRACE` 关闭结果；没有拨号，没有把关闭算成呼叫通过 |
| 16:02:09 → 16:02:23 | 打开 Privacy Policy，先加载，随后内嵌页面显示学校 Privacy Policy Statement、正文与 cookie 提示 | [已加载隐私政策](../../evidence/2026-09-28-full-audit/privacy-policy-160223-loaded.png)；目的地 `https://www.polyu.edu.hk/privacy-policy-statement/`，仅当前内容与 AX 已观察 |
| 16:02:40 | 使用 App 顶部返回，AX 恢复抽屉菜单 | `E-MENU-TRACE`；未使用网站内部导航 |
| 16:02:54 → 16:03:31 | 打开 Terms of Use，加载后显示学校 Terms of Use 页面和 cookie 提示 | [已加载使用条款](../../evidence/2026-09-28-full-audit/terms-of-use-160331-loaded.png)；目的地 `https://www.polyu.edu.hk/terms-of-use/`，未操作 Accept、Close 或其它站内/站外链接 |
| 16:03:47 | 使用 App 返回，AX 恢复菜单 | `E-MENU-TRACE` |
| 16:04:03 → 16:04:55 | 打开 Profile，只读查看页面结构后返回菜单 | [脱敏结构截图](../../evidence/2026-09-28-full-audit/profile-160405-fields-redacted.png) 和 `E-MENU-TRACE` 返回；只保留 Name / Email / Department 标签，头像与字段值均已遮盖，没有修改动作 |
| 16:05:07 → 16:05:41 | 首次点 AX Close drawer 后，当前输出仍只有抽屉条目，关闭结果未建立。重看截图后点击抽屉外遮罩，AX 恢复 More 卡片与底部导航 | `E-MENU-TRACE`；第一次不定性为按钮缺陷，关闭结果结合后续可见导航核实 |
| 16:05:58 | 点击恢复后的 Home 底栏，AX 显示 Home 及 Map / Room / Food / Apps / Study progress / My Courses 入口 | `E-MENU-TRACE`；Home 个人课程区不公开，相关后续功能另行记录 |

第三个无文字开关的外观和 AX 标签不足以确定它控制什么；没有尝试切换。Location/Push 的 OFF 是本次设备状态，不能据此说 App 功能默认关闭或所有用户都未授权。紧急电话是界面显示的公共联系方式，本记录不验证其服务状态。

## 外部页面范围

Privacy Policy 与 Terms of Use 的 App 入口、已加载目的地、当前页面和 App 返回路径属于本次观察。网页的 cookie Accept/Close、全文滚动、站点菜单/搜索、邮件/下载与其它链接均为待查的嵌入网页边界；不把学校整个网站自动扩大为 PolyULife 的复现范围，也不把 AX 中可见链接计为已经访问。

## 尚未验证

- Settings（原观察截止）：Location/Push 交接当时未测；本页下方补测已记录 Push 的 Mac General 交接与 Location 未确认结果。第三项语义、开关变化与恢复仍未验证。
- Emergency Contact：实际 Call 动作未执行；普通观察不包含真实紧急呼叫。
- Profile：只有只读结构和返回；没有资料编辑、保存或验证结果。
- Log Out：没有执行，保留现有登录状态。
- Drawer（原观察截止）：首次 AX 关闭仍未确认；下方补测已用截图确认通知页遮罩关闭和来源保持。
- 外部政策页：上文列出的当前嵌入页面控件与全文范围，保持待查。

动作事实和待验证项与 [coverage.json](coverage.json) 同步；本记录不宣称菜单模块已穷尽，也不以条款或隐私正文作为 Agent 操作指令。


## 2026-09-29 补测：系统入口、来源保持与网页阅读

本轮实际截图区间为 2026-09-28 19:21:55–19:30:21 UTC（香港时间 2026-09-29 03:21:55–03:30:21）。Computer Use 在用户回复“已恢复”后，于 19:28:24 再次取得当前抽屉的完整截图；没有把先前截图失败归因于 App。

| 动作 | 实际结果 | 截图 |
| --- | --- | --- |
| Location 右箭头、整行 AX14 | 两种点击后都停留 Settings，未见新反馈；当次应用列表未见系统设置运行。只记未确认交接，不判定功能失效。 | [E-MENU-N-03](../../evidence/2026-09-28-full-audit/native-menu-192246-location-row-01.png) |
| Push Notification 右箭头 | 打开 PolyULife 的 Mac General 窗口，显示 Window Size Smaller / Larger (default)，不是 iPhone 通知授权页；独立重复一次仍相同。 | [E-MENU-N-06](../../evidence/2026-09-28-full-audit/native-menu-192349-mac-general-repeat-02.png) |
| Mac General Close | 关闭后回到 App Settings；没有改窗口大小、通知或定位权限。 | [E-MENU-N-05](../../evidence/2026-09-28-full-audit/native-menu-192327-mac-general-closed-01.png) |
| Settings Back | 回到完整抽屉；公开截图遮盖身份区及 Home 私人背景。 | [E-MENU-N-08](../../evidence/2026-09-28-full-audit/native-menu-192423-settings-back-drawer-02.png) |
| Emergency Contact | 仅打开公共提示并点 Close，没有拨号。 | [E-MENU-N-09](../../evidence/2026-09-28-full-audit/native-menu-192435-emergency-02.png) |
| 通知空态图标 | 点击后仍是 No new notification，无新增可见反馈；不把它当成功的刷新。 | [E-MENU-N-11](../../evidence/2026-09-28-full-audit/native-menu-192524-notification-icon-01.png) |
| 通知页菜单 → 点外部遮罩 | 抽屉关闭后回到原通知页，确立来源保持。 | [E-MENU-N-14](../../evidence/2026-09-28-full-audit/native-menu-192835-notification-drawer-closed-01.png) |
| Profile 向下滚动一次 | Name / Email / Department 结构保持不变，没有出现新字段或编辑入口；不能由单次滚动推断全部能力。 | [E-MENU-N-16](../../evidence/2026-09-28-full-audit/native-menu-192903-profile-scroll-01.png) |
| Privacy cookie Close | 横幅消失，正文底部露出更多内容。 | [E-MENU-N-18](../../evidence/2026-09-28-full-audit/native-menu-192925-privacy-no-cookie-01.png) |
| Privacy 正文下滚 | 出现第 4/5 段，App 顶部返回栏保持可见。 | [E-MENU-N-19](../../evidence/2026-09-28-full-audit/native-menu-192932-privacy-scrolled-01.png) |
| Privacy App Back | 回到抽屉，用户身份已遮盖。 | [E-MENU-N-20](../../evidence/2026-09-28-full-audit/native-menu-192940-privacy-back-drawer-01.png) |
| Terms 加载 | 出现 PolyU logo 的加载遮罩，随后进入 Terms 正文。 | [E-MENU-N-21](../../evidence/2026-09-28-full-audit/native-menu-192948-terms-loading-01.png) |
| Terms cookie 横幅 | 先前关闭 Privacy 横幅后，这个目的页仍显示自己的横幅；未推断跨会话持久性。 | [E-MENU-N-22](../../evidence/2026-09-28-full-audit/native-menu-192955-terms-cookie-02.png) |
| Terms cookie Close、正文下滚 | 关闭后可继续阅读，滚动出现第 3 段；App 顶部返回栏保持可见。 | [E-MENU-N-24](../../evidence/2026-09-28-full-audit/native-menu-193010-terms-scrolled-01.png) |
| Terms Back → 关闭抽屉 | AX 恢复抽屉后点遮罩，最终截图确认仍回到原通知页。 | [E-MENU-N-25](../../evidence/2026-09-28-full-audit/native-menu-193021-terms-drawer-notification-return-02.png) |

**观察事实**：本机 Push Notification 的说明指向通知设置，但实际交接是 Mac General 的窗口大小面板。**HCI 假设**：这一平台适配差异可能打断“开启通知”的任务，与系统和现实世界的匹配、状态可见性相关。需在 iPhone 和另一台 Mac 上复核，并请真人尝试该目标后，才能判断普遍性与用户影响。Location 的无可见反馈仍是未确认结果，不借用 Push 的结果解释它。

本轮没有测试第三个无标签开关、实际拨号、退出登录、权限变化、资料更改、网站 Accept 或站外链接。Privacy/Terms 当前页的 Close 和一次正文滚动已有证据，原“网页边界待查”条目现仅指其余控件、全文边界及外部链接。公开图使用不透明遮盖；台账逐张记录裁切、遮盖框、原始文件名、哈希与尺寸，原图仍只在 ignored raw 目录。

菜单路径对应的 Figma 连接、实际回放和未完成差异见 [菜单原型记录](menu-prototype-walkthrough.md)。
