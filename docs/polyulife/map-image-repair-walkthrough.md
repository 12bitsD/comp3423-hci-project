# Map 底图重新上传与重复进入验证

2026-09-29。本批原生 Computer Use 仍报告 Mac locked，没有新增原生观察。完整应用保持 `not_verified`。

## 修改与实测结果

Figma 的 Toilets、Toilets+Water、Water、Water 列表后段、Clinics、Banks、AEDs、Bookstores 共 8 个页面，使用既有公开 PNG 通过 Image → Upload from computer 重新上传填充。保留图片的位置、尺寸、文字图层和交互控件，没有重新导入整页。图片内容 hash 保持相同；可读填充属性增加 thumbnail，imageShouldColorManage 从 false 变为 true。这是修改前后属性差异，尚不足以判定丢图根因。

先验证 Toilets 连续 3 次 Home→Map→Toilets 进入均显示底图，再处理其余 7 张。中途一次编辑器跨节点导航被浏览器中止；检查确认仍停留在上一图片后，下一次独立导航成功，未误改其它节点。

全部替换并重载 Present 后，从 Monday Home 连续执行两轮既有路径：Map→Toilets→Toilets+Water→Water→列表后段→清除→Clinics→清除→右侧分类→Banks→清除→AEDs→清除→Bookstores→Home。两轮 16 次被测页面底图均可见；两次 Home 返回与本批基线应用区域 `(581,60,938,661)` 像素完全一致。首轮结束后未重载，直接再次进入，覆盖了本次要复测的重复进入情况。

## 完成边界

本次仅证明两轮 Monday 样例路径中 8 张地图可见。没有重新验证 Tuesday/legacy 来源、独立 Map 起点、长时会话及全部地图操作。`D-MAINMAP-IMAGES` 从 open 改为 partially_resolved：Home 装饰图等同一问题记录的其它对象仍未修复，Food 图片也不在本次范围。独立 Map 外层 Back 仍未完成；原生 86 个未尝试动作、列表及其它交互继续保留。

[上次底图缺失及返回栈记录](map-return-prototype-walkthrough.md)保留作失败证据；不能把本次回放当作原生补测或 Maze 真人测试。Home/Map/legacy 三份流程说明已更新，Monday 说明在重载 Present 后读回。

## 可复现配置与证据

[图片节点、素材哈希、前后填充属性及像素比较](../../design/polyulife/map-image-repair.json)。24 张实际 Present 截图只遮盖 Figma 账号区；公开 PNG 与原始 JPEG 转码和遮盖结果逐像素核对。最初四张的时间来自原始文件保存时间，其余为截图保存后的 UTC 记录。

| 步骤 | 状态 | 证据 |
| --- | --- | --- |
| toilets-first | S-MAINMAP-TOILETS | [E-MAP-PNG-REENTRY-01](../../evidence/2026-09-28-full-audit/map-png-toilets-first.png) |
| home-after-first | S-HOME-SCHEDULE-MON | [E-MAP-PNG-REENTRY-02](../../evidence/2026-09-28-full-audit/map-png-home-after-first.png) |
| toilets-second | S-MAINMAP-TOILETS | [E-MAP-PNG-REENTRY-03](../../evidence/2026-09-28-full-audit/map-png-toilets-second.png) |
| toilets-third | S-MAINMAP-TOILETS | [E-MAP-PNG-REENTRY-04](../../evidence/2026-09-28-full-audit/map-png-toilets-third.png) |
| home-baseline | S-HOME-SCHEDULE-MON | [E-MAP-PNG-REENTRY-05](../../evidence/2026-09-28-full-audit/map-png-home-baseline.png) |
| pass1-toilets | S-MAINMAP-TOILETS | [E-MAP-PNG-REENTRY-06](../../evidence/2026-09-28-full-audit/map-png-pass1-toilets.png) |
| pass1-combined | S-MAINMAP-TOILETS-WATER | [E-MAP-PNG-REENTRY-07](../../evidence/2026-09-28-full-audit/map-png-pass1-combined.png) |
| pass1-water | S-MAINMAP-WATER | [E-MAP-PNG-REENTRY-08](../../evidence/2026-09-28-full-audit/map-png-pass1-water.png) |
| pass1-water-scrolled | S-MAINMAP-WATER-SCROLLED | [E-MAP-PNG-REENTRY-09](../../evidence/2026-09-28-full-audit/map-png-pass1-water-scrolled.png) |
| pass1-clinics | S-MAINMAP-CLINICS | [E-MAP-PNG-REENTRY-10](../../evidence/2026-09-28-full-audit/map-png-pass1-clinics.png) |
| pass1-banks | S-MAINMAP-BANKS | [E-MAP-PNG-REENTRY-11](../../evidence/2026-09-28-full-audit/map-png-pass1-banks.png) |
| pass1-aeds | S-MAINMAP-AEDS | [E-MAP-PNG-REENTRY-12](../../evidence/2026-09-28-full-audit/map-png-pass1-aeds.png) |
| pass1-bookstores | S-MAINMAP-BOOKSTORES | [E-MAP-PNG-REENTRY-13](../../evidence/2026-09-28-full-audit/map-png-pass1-bookstores.png) |
| pass1-return | S-HOME-SCHEDULE-MON | [E-MAP-PNG-REENTRY-14](../../evidence/2026-09-28-full-audit/map-png-pass1-return.png) |
| pass2-toilets | S-MAINMAP-TOILETS | [E-MAP-PNG-REENTRY-15](../../evidence/2026-09-28-full-audit/map-png-pass2-toilets.png) |
| pass2-combined | S-MAINMAP-TOILETS-WATER | [E-MAP-PNG-REENTRY-16](../../evidence/2026-09-28-full-audit/map-png-pass2-combined.png) |
| pass2-water | S-MAINMAP-WATER | [E-MAP-PNG-REENTRY-17](../../evidence/2026-09-28-full-audit/map-png-pass2-water.png) |
| pass2-water-scrolled | S-MAINMAP-WATER-SCROLLED | [E-MAP-PNG-REENTRY-18](../../evidence/2026-09-28-full-audit/map-png-pass2-water-scrolled.png) |
| pass2-clinics | S-MAINMAP-CLINICS | [E-MAP-PNG-REENTRY-19](../../evidence/2026-09-28-full-audit/map-png-pass2-clinics.png) |
| pass2-banks | S-MAINMAP-BANKS | [E-MAP-PNG-REENTRY-20](../../evidence/2026-09-28-full-audit/map-png-pass2-banks.png) |
| pass2-aeds | S-MAINMAP-AEDS | [E-MAP-PNG-REENTRY-21](../../evidence/2026-09-28-full-audit/map-png-pass2-aeds.png) |
| pass2-bookstores | S-MAINMAP-BOOKSTORES | [E-MAP-PNG-REENTRY-22](../../evidence/2026-09-28-full-audit/map-png-pass2-bookstores.png) |
| pass2-return | S-HOME-SCHEDULE-MON | [E-MAP-PNG-REENTRY-23](../../evidence/2026-09-28-full-audit/map-png-pass2-return.png) |
| home-description | S-HOME-SCHEDULE-MON | [E-MAP-PNG-REENTRY-24](../../evidence/2026-09-28-full-audit/map-png-home-description.png) |
