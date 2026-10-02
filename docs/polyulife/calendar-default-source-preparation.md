# Calendar 默认月视图：历史来源补齐

2026-10-02。本轮Computer Use实时应用发现返回“Mac已锁定，自动解锁失败”；没有执行新的Calendar或QR原生动作，也没有重启应用。整体目标仍未完成。

## 取得的来源

先前 `S-CALENDAR-DEFAULT` 只有AX记录，公开截图因私人课程内容而暂未收录。本轮找到同一历史会话在2026-09-28 15:50:57.332 UTC保存的原始JPEG：576×1082，包括112px的Mac标题区。该来源对应已有More→Calendar操作后的September/2026-27 Semester1默认月历。没有把这次读旧截图计为新原生执行。

[脱敏原生视口](../../evidence/2026-10-02-calendar-default-source/native-calendar-default-redacted.png)裁掉Mac标题区，保留576×970内容。私人事件值（课程名/代码、时间及地点）以不透明遮盖删除；个人日程在日期格上形成的点标记也逐条遮盖。公开来源没有用合成值替换原像素，全部变换和原文件摘要记录在 [manifest](../../evidence/2026-10-02-calendar-default-source/manifest.json)。原图继续留在Git忽略目录。页面中的公共类别行和筛选按钮为全选状态，与Acad-only空态不同。

## 可编辑准备稿

[calendar-default-demo.svg](../../design/polyulife/calendar-default-demo.svg)使用原生来源支持的默认类别行、实色筛选按钮与卡片结构；已有公共校历稿只复用Month/Header/Grid基础层。个人点标记不复制，私人事件值替换成明确标注DEMO的合成示例。一张示例卡不是原生事件总数，也不表示其它事件不存在。通用Class图标只裁切原生公共UI元素；其它文字和几何可编辑。手工字体/几何近似仍未进行完整视觉验收。[本地SVG渲染预览](../../evidence/2026-10-02-calendar-default-source/calendar-default-demo-render.png)已检查布局；使用sips光栅化，不是原生截图或Figma回放。

源码及哈希见 [来源记录](../../design/polyulife/calendar-default-source.json) 和 [生成脚本](../../design/scripts/prepare_calendar_default_source.py)。本轮只准备来源/SVG，尚未导入Figma、连线或Present回放；140画板、320控件、94次运行不变。

历史来源中可见Class事件省略号，新增 `A-CALENDAR-DEFAULT-CLASS-MORE` 为not_attempted，目标未知；不把公共节假日详情冒充私人课程详情。原生状态/会话数量仍135/14，动作现在269（193 observed、76 not_attempted）；新增的是历史控件登记，不是执行。

## 下一步

- 将准备稿作为带DEMO声明的默认视图接入More→Calendar、默认视图→Notification、打开全选筛选及ApplyAll返回；保留已有Home来源。
- 全选/Acad/None的提交、取消和背景不能直接复用不相符的公共日期截图；需要按来源逐个核验。
- 解锁Mac后补查默认事件详情、其它类别/边界、QR底部导航与实际返回。没有新的原生结果前不生成推测的成功分支，也不以文件数量判定完整应用完成。
