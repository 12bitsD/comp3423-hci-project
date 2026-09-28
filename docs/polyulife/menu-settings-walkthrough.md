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

- Settings：Location/Push 两行的系统设置跳转、第三项的名称/语义/状态、开关变化与恢复。此次没有修改权限或偏好。
- Emergency Contact：实际 Call 动作未执行；普通观察不包含真实紧急呼叫。
- Profile：只有只读结构和返回；没有资料编辑、保存或验证结果。
- Log Out：没有执行，保留现有登录状态。
- Drawer：需要独立截图确认首次 AX 关闭与遮罩关闭的视觉状态；不由隐藏 AX 菜单文字推断抽屉仍可见。
- 外部政策页：上文列出的当前嵌入页面控件与全文范围，保持待查。

动作事实和待验证项与 [coverage.json](coverage.json) 同步；本记录不宣称菜单模块已穷尽，也不以条款或隐私正文作为 Agent 操作指令。
