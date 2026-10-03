# Room Preview：登录边界与复制菜单反馈 · 2026-09-30

[本轮原生控件证据](room-preview-controls-20260930.md)确认使用指南进入认证边界、历史按钮启用状态往返，以及 Copy link菜单关闭。本轮在真实 Figma中导入该空登录页面，另在历史 Preview网页样例中补入复制菜单关闭；两部分不是连续认证流程。

## 画板和连接

- [登录画板452:19](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=452-19)为576×1024，位置0,43000。文字、字段、按钮与浏览器图标可编辑，校徽为原生截图14的公开栅格裁片。未输入凭据，字段与提交、忘记密码、Close/More/Reload/Back均未连线；真实历史往返待合适网页视觉证据后接入。
- `312:242` Copy link文字：On click → Close overlay，位于菜单312:153。只复现菜单关闭，不写剪贴板，也未扩大为整行点击区域。顶部和中间滚动位置各回放一次，关闭后画面分别与基线像素一致。
- 原有 Preview310:12仍依据旧原生网页截图；本轮当前原生网页截图空白，未用该空白替代已观察网页，也未虚构当前照片顺序或下方指南布局。

## 实际渲染与失败

[公开清单](../../evidence/2026-09-30-preview-prototype-controls/manifest.json)保存10张实际截图及拼图。初次仍在Figma加载；随后登录内容组被图层检查误隐藏，截图02只剩外框。通过 Show可见性控件恢复后，截图03确认校徽、提示、空字段、登录按钮及链接实际呈现。失败保留，不归因于原生 App。

[连接配置](../../design/polyulife/room-preview-controls-connections.json)、[登录源码与来源](../../design/polyulife/room-preview-login-source.json)和 [覆盖台账](coverage.json)登记实际节点。Menu原型URL会保持父节点310:12，菜单显示和关闭以截图证明，不能只看URL判定弹层。

当前正式Figma为109个映射画板、245个配置控件、40次原型运行。完整应用仍 `not_verified`：当前网页视觉连接、PDF/历史、整行复制热区、剪贴板、分享面板、更多指南、任意查询/日期与其它功能边界未完成。原型回放不增加原生观察或真人评估数量。
