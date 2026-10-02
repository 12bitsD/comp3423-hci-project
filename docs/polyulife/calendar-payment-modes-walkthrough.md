# Payment 的 Month / Events / Week 与历史开关（2026-10-03）

通过实际 Computer Use，已观察 **Month → Events → Week5 → Month**，并打开/隐藏 Payment 历史。Figma 参考分支新增3个可编辑模式画板和6条连接，实际 Present 走通两种路径及既有 Home 回归。完整应用仍 `not_verified`。

## 原生结果

起点为 October2 / Payment / No event，结束恢复该起点。根据本次运行清单与 bundle 歧义结果选择实际 Wrapper，再 Raise 窗口；坐标输入仍返回 noWindowsAvailable。没有退出/重启应用、修改配置、输入凭证或执行任何支付。版本依据仍为前一会话的3.0.0，本批未重新核对。

| 实际动作 | 确认的反馈 | 脱敏证据 |
| --- | --- | --- |
| 月份模式图标 AX element53 | Events / Show History，Payment / No event | [02](../../evidence/2026-10-03-payment-modes-native/02-view-element-attempt.png) / [AX](../../evidence/2026-10-03-payment-modes-native/02-view-element-attempt.safe-ax.txt) |
| Events 标题 AX element16 | Show History 直接切成 Hide History，显示历史条目；没有独立菜单 | [03](../../evidence/2026-10-03-payment-modes-native/03-events-header-menu.png) / [AX](../../evidence/2026-10-03-payment-modes-native/03-events-header-menu.safe-ax.txt) |
| Events 图标 AX element17 | Week5 / Sep-Oct / Semester1，显示课程网格 | [05](../../evidence/2026-10-03-payment-modes-native/05-month-after-history.png) / [AX](../../evidence/2026-10-03-payment-modes-native/05-month-after-history.safe-ax.txt) |
| Week 图标 AX element17 | 回到 October2 Payment 空态 | [06](../../evidence/2026-10-03-payment-modes-native/06-month-after-week-history.png) |
| 再进 Events | Show History / No event，历史开启状态未保留 | [07](../../evidence/2026-10-03-payment-modes-native/07-events-history-retained-after-mode-cycle.png) |
| 再显示历史、点击 Hide History | 回到 Show History / No event | [09](../../evidence/2026-10-03-payment-modes-native/09-history-hidden-by-toggle.png) |
| 空 Events → Week → Month | 同样走通，恢复原生起点 | [10](../../evidence/2026-10-03-payment-modes-native/10-week-after-hidden-events.png) / [11](../../evidence/2026-10-03-payment-modes-native/11-month-restored-after-mode-cycle.png) |

03的menu、05的month、07的retained等文件名是动作时的尝试标签，不是结果断言；清单与状态ID按实际反馈登记。AX索引只对本次最新状态有效，不能跨页面复用。

[原生清单](../../evidence/2026-10-03-payment-modes-native/manifest.json)有12张实际截图、安全AX子集和6项比较。History的全部条目/日期区域及Week课程值/块位置已遮盖，身份和私人聚合AX不公开。被遮盖区域相等不能证明私人内容相同。原生起点恢复、Events复位等未遮盖公共状态的像素比较相等。

Month与Events显示Payment分类；Week显示课程网格，没有同样的分类标题。该事实不足以建立全局筛选规则或认定数据错误。是否符合用户的模式切换预期、历史状态复位是否影响任务，需要真实参与者验证；本批不新增重复或推测性HCI缺陷。

筛选入口仍未打开：新Wrapper Raise后的坐标输入报错，Events历史下的AX筛选容器点击没有建立弹层。失败归为输入/定位边界，不当作App缺陷。模式切换已通过AX得到真实反馈，不能把坐标失败泛化成整应用不可观察。

## 可编辑 Figma 与实际回放

| 状态 | 根画板 | 实现范围 |
| --- | --- | --- |
| Events空态 | [833:145](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=833-145) | Payment / No event，可切历史与Week |
| History DEMO | [835:209](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=835-209) | 月份带、日期列与粉色条目；字段全为虚构DEMO，可隐藏历史与进Week |
| Week DEMO | [835:312](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=835-312) | Week5网格；课程数量/值/位置均为合成样例，可回Month |

均为576×1024原生可编辑Frame/Text/Vector/分组，位于Y77400、X0/700/1400。[生成脚本](../../design/scripts/build_calendar_payment_modes.py)、[来源与哈希](../../design/polyulife/calendar-payment-modes-sources.json)、[六条连接及属性读回](../../design/polyulife/calendar-payment-modes-connections.json)。连接为On click / Navigate to / Instant，入口是既有Month823:21的ViewMode823:30。有限循环表达观察到的历史复位，不模拟任意日期/筛选持久化。

Week导入旧模板后，底部导航曾超出1024边界；已替换该子层，保留835:312根节点。长History根名称的选中检查曾拒绝实际已选状态，改为独立新读回与配置；没有为失败步骤登记连接。参考根画板暂不在虚拟图层列表，定位到真实行后才编辑Flow。这些编辑器事件与原生输入失败分别记录。

[Present清单](../../evidence/2026-10-03-payment-modes-prototype/manifest.json)有12张实际回放截图、编辑器范围截图和拼图，3组运行：带历史的模式循环并重入确认隐藏、显示/隐藏历史后从空态完成循环、既有October2 Home回归。7项重复状态裁片比较全部相等，目标均在保存像素中可见；不证明原生视觉保真、任意状态规则或真人可用性。

## 继续接力

参考Flow现为28个有限画板、39个控件。全台账19次原生会话、165状态、319动作（234 observed /81 not_attempted /4 attempted_unverified）；Figma175映射画板、378控件、121次回放。历史列表滚动/条目菜单、Week选择器/课程详情、其它日期/分类/调用者、筛选重开和完整状态模型仍未完成。字体、图形和几何近似，私人信息合成替换；手机设备能力与真人课程评估另行验证。
