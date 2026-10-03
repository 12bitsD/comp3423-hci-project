# Notification 记录原生走查与来源准备

2026-10-03 用 Mac Computer Use 重新取得 PolyULife 3.0.0 的真实窗口，并走查一条 ITS 公共工作坊通知。新增 8 个状态、13 个动作，其中 12 个 observed、1 个 attempted_unverified；保存 26 张窗口截图、安全 AX 子集与联系表。当前原生共 21 次会话、178 状态、340 动作（254 observed、81 not_attempted、5 attempted_unverified）。完整应用仍 `not_verified`。

[原生清单](../../evidence/2026-10-03-notification-record-native/manifest.json)记录实际截图时间、裁切、尺寸与哈希；[联系表](../../evidence/2026-10-03-notification-record-native/contact-sheet.png)包含全部 26 张样本。[覆盖台账](coverage.json)记录动作与结果。以下编号均指公开截图文件名前缀。

## 已观察事实

| 路径 | 样本 | 结果与边界 |
| --- | --- | --- |
| Payment → Notification | 00–04 | 显示 Yesterday 下的一条工作坊通知；卡片绿色圆点和底部通知红点可见 |
| 打开第一条记录 | 05 | 首次详情未显示插图；标题、发布信息、正文及 Read more 可见 |
| Read more → 网页 → More → Cancel → X | 06–12 | 保存加载标识、有标题空白网页及菜单；关闭回到已显示插图的详情。空白截图时 AX 有网页内容，不能据此判断服务成功或故障 |
| 展开插图 → X | 13–14 | 插图展开，关闭返回详情 |
| 详情 Back → 列表 → 重开 → Back | 15–17 | 卡片保留，绿色圆点与页签红点消失；重开详情时插图已显示 |
| Calendar → Notification | 18–19 | 日历仍 October、选中 October2、分类 Payment；回通知后两种圆点仍未出现 |
| 再次详情/网页往返 | 20–25 | 再次保存详情、加载、网页空白及关闭；最终回到已读列表 |

这是一条通知的有限样本。没有确认通知已读变化的精确触发时刻、跨进程持久化、所有通知类型或完整列表边界。首次无图与后来有图是采样事实；不能把关闭网页解释为图片加载原因，也没有测量加载时长。

## 连接与输入边界

旧句柄超时后，Computer Use 在 Finder 的 Applications 中对已发现的 PolyULife 执行“打开”，再从本次应用发现结果选择真实运行 Wrapper 路径，成功取得窗口。未执行退出或重启命令；进程是否连续没有验证。后续复用成功句柄。用户再次解锁后读取仍得到真实通知列表截图，当前可观察。

Payment 筛选的 AX 按钮及父容器点击均未显示弹层；截图定位的坐标点击返回 `noWindowsAvailable`。该动作记为 attempted_unverified，工具失败不归为 App 缺陷。通知页签、记录、网页菜单及图片等 AX 控件能产生已保存的反馈。索引在返回/动画后会变化，必须读取新状态。

## 公开证据边界

截图来自实际 750×1390 窗口字节，去掉 57px 标题栏后归一化为 576×1024。保留的是一般 ITS 工作坊公告和公共控件；公开 AX 只保留安全叶节点。隐藏父容器中的身份信息和网页完整跟踪地址不公开。网页底部只保留截图已有的截断域名，不保存或重构完整 URL。私人原始 AX 和窗口截图留在被 Git 忽略的 `evidence/raw/`。

## Figma 来源准备检查点

[来源清单](../../design/polyulife/notification-record-sources.json)登记 9 份 SVG：未读/已读列表、无图/有图详情、图片展开、网页加载/空白/菜单，以及已读后 Payment 返回上下文。文字、控件与几何可编辑；公告插图和静态加载标识是经检查的公开裁片。

当前状态为 `prepared_not_imported_not_replayed`，尚未导入、配置或回放，不增加正式 Figma 数量。现有 Figma 仍 187 个映射画板、402 个配置控件、129 次原型运行。

下一步从现有 Payment `823:21` 接通知样本，按原生证据建立读前/读后返回、图片和网页路径。若用延时展示无图→有图或网页加载→空白，延时仅为演示代理；不代表实测机制或速度。已读后 Payment 来源暂只计划接实测 Notification 返回，其它日期/模式/Home 不自动复制。搜索、抽屉、分享、复制、系统浏览器及其它未执行控件仍待查。

本地生成器 [build_notification_record.py](../../design/scripts/build_notification_record.py) 只生成素材；不能用生成成功代替 Figma 导入与实际回放。原生归档脚本已执行，不要重跑。
