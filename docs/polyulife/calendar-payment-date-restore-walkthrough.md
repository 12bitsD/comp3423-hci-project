# Payment October3 → October2 返回补齐

2026-10-03 在覆盖台账中核对到 `A-NATIVE-PAYNAV-RESTORE2` 已有真实原生动作依据，但尚未配置对应 Figma 日期连接。[原生采样06](../../evidence/2026-10-03-payment-day3-navigation-native/06-oct2-restored.png)及安全AX路径以 [coverage.json](coverage.json) 的 `E-NATIVE-PAYNAV-06` / `E-NATIVE-PAYNAV-06-AX` 为准：从 October3 / Payment 点击最新 AX 的 October2，返回 October2 / Payment。该事实只支持已观察的两日上下文，不支持任意日期的通用规则。

在现有 October3 根 `828:19` 内选择实际 `Day2` 组 `828:62`，配置 On click / Navigate to / Instant → October2 根 `823:21`。根节点及已有日期、Home、模式连接保留，没有新增原生状态或假设。配置读回见[连接台账](../../design/polyulife/calendar-payment-date-restore-connections.json)。

## 实际回放与结果

第一组从 October2 → October3 → October3 Home → Calendar 保留 October3 → October2 → October2 Home → Calendar 保留 October2。第二组从该 October2 再选 October3，并直接点击 October2 返回。两组共保存[9张Present截图、2张编辑器截图与联系表](../../evidence/2026-10-03-payment-date-restore/manifest.json)。Home个人内容全部是既有合成DEMO，不包含真实身份或课表。

五项重复日期视口比较全部相等：October2起点对三个返回样本，October3对Home返回与第二轮样本。这证明本批有限原型路径和采样状态，不能证明整App保真、其它日期或通用调用者持久性。URL读取仍可能滞后，以已保存并检查的像素判定画面。

原型参考流程说明更新为33个有限画板、49个控件；整份Figma共有180个映射画板、388个配置控件、126次运行。原生统计仍为170状态/327动作，完整应用继续为 `not_verified`。筛选重开、其它日期/记录和Calendar分支整合仍待完成。

## 本轮原生连接复查

复用已知仍运行的PolyULife句柄尝试截图，返回 LSOpen/AppleEvent 通信超时，未取得新的实际窗口画面。上轮从实时清单选择运行Wrapper后的读取也超时。不能把这些结果解释为仍锁屏或App业务故障；本轮没有重启、退出登录、改变设置或新增成功原生动作。已完成的Figma补齐使用此前实际原生证据，分别归档。
