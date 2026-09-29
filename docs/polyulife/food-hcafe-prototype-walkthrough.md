# Food 展开列表、H Café 和订餐外链提示

2026-09-29。本批仅编辑和回放 Figma，原生 Computer Use 仍报告 Mac 锁定，没有新增原生记录。完整应用仍 `not_verified`。

## 源证据与实现

根据 [Food 原生走查](food-walkthrough.md)的四个已观察视口，新增四个576×970可编辑画板：展开列表297:12、H Café列表299:287、营业时间299:425、外链提示306:12，位于Y=30000。文本、形状和控件可编辑；仅六份公开logo/地图条素材为栅格。源码由 [生成器](../../design/scripts/build_food_additional_svg.py)维护。Closed和营业时间是拍摄时标签，不是实时营业数据。

从Home进入Food，再展开VA210营业时间、上拖手柄到展开列表、拖动列表到H Café、展开营业时间、Online Order提示、点遮罩关闭、Back回Home。原生滚动在本版用On drag交换两个视口近似，未重建中间餐厅或连续列表；拖动的Smart animate 300ms是Figma默认值，不是测量所得。两个未展开营业时间的列表Back为推断，action_id为空；H Café hours Back引用E-APPS-TRACE中实际执行来源。

营业时间按证据保留Mon–Fri 08:00–22:00、Sat 08:00–18:00、Sun/public holiday 10:00–18:00。提示只显示证据中的截断URL；Open按钮未连接外站。

## 失败与修复

第一轮点击对话框正文也触发关闭（第08张），这是整屏遮罩作为点击热点造成的原型问题。将提示画板299:562替换为306:12，把关闭区域拆成上、下、左、右四块并重接OnlineOrder。最终11个控件，累计204个；旧节点/连接保留于修改历史，不作为当前映射。H Café列表早期箭头源码的纵线错误也在导入前修正，旧299:149不作为当前映射。

修复后正文点击和原型Open点击均保留提示；四侧点击都回到H Café营业时间。正文静止后的画面与提示初始画面逐像素一致。下、左、右关闭返回与hours基线逐像素一致；上侧关闭即时截图含Figma热点提示，目视回到hours，不宣称该张像素一致。Open的无动作是明确实现边界，不是原生Open观察。

从H Café营业时间返回、展开列表推断返回、H Café列表推断返回，共三次Home返回与进入前应用区域(461,60,818,661)逐像素一致，保留Tuesday内容和滚动位置。共28张截图，包含失败、热点高亮和修复结果。素材在所测路径可见；完整视觉验收未完成。

## 剩余范围

完整连续列表、中间餐厅、边界、反向滚动、sheet/hours收起、其它餐厅详情/标签、外站Open未实现。新链路只测Tuesday来源；Monday/legacy和独立入口未复测。独立Food返回缺口仍在。四侧关闭是对一次原生遮罩关闭的原型推广；对话框内部点击测试也不增加原生动作。Agent回放不等于真人Maze评价。

[节点、连接读回、历史与像素比较](../../design/polyulife/food-hcafe-connections.json)

| 步骤 | 结果 | 证据 |
| --- | --- | --- |
| 01-home-before | recorded | [E-FOOD-HCAFE-P-01](../../evidence/2026-09-28-full-audit/figma-food-extra-01-home-before.png) |
| 02-list | recorded | [E-FOOD-HCAFE-P-02](../../evidence/2026-09-28-full-audit/figma-food-extra-02-list.png) |
| 03-hours | recorded | [E-FOOD-HCAFE-P-03](../../evidence/2026-09-28-full-audit/figma-food-extra-03-hours.png) |
| 04-expanded | recorded | [E-FOOD-HCAFE-P-04](../../evidence/2026-09-28-full-audit/figma-food-extra-04-expanded.png) |
| 05-hcafe | recorded | [E-FOOD-HCAFE-P-05](../../evidence/2026-09-28-full-audit/figma-food-extra-05-hcafe.png) |
| 06-hcafe-hours | recorded | [E-FOOD-HCAFE-P-06](../../evidence/2026-09-28-full-audit/figma-food-extra-06-hcafe-hours.png) |
| 07-order-prompt | recorded | [E-FOOD-HCAFE-P-07](../../evidence/2026-09-28-full-audit/figma-food-extra-07-order-prompt.png) |
| 08-dialog-body-stays | failed_dialog_body_dismissed_before_fix | [E-FOOD-HCAFE-P-08](../../evidence/2026-09-28-full-audit/figma-food-extra-08-dialog-body-stays.png) |
| 09-dismissed | recorded | [E-FOOD-HCAFE-P-09](../../evidence/2026-09-28-full-audit/figma-food-extra-09-dismissed.png) |
| 10-home-return | recorded | [E-FOOD-HCAFE-P-10](../../evidence/2026-09-28-full-audit/figma-food-extra-10-home-return.png) |
| 11-home-settled | recorded | [E-FOOD-HCAFE-P-11](../../evidence/2026-09-28-full-audit/figma-food-extra-11-home-settled.png) |
| 12-fixed-hours-baseline | recorded | [E-FOOD-HCAFE-P-12](../../evidence/2026-09-28-full-audit/figma-food-extra-12-fixed-hours-baseline.png) |
| 13-fixed-prompt | recorded | [E-FOOD-HCAFE-P-13](../../evidence/2026-09-28-full-audit/figma-food-extra-13-fixed-prompt.png) |
| 14-fixed-dialog-body | dialog_remains_after_fix | [E-FOOD-HCAFE-P-14](../../evidence/2026-09-28-full-audit/figma-food-extra-14-fixed-dialog-body.png) |
| 15-fixed-dialog-settled | dialog_remains_after_fix | [E-FOOD-HCAFE-P-15](../../evidence/2026-09-28-full-audit/figma-food-extra-15-fixed-dialog-settled.png) |
| 16-open-unwired | dialog_remains_after_fix | [E-FOOD-HCAFE-P-16](../../evidence/2026-09-28-full-audit/figma-food-extra-16-open-unwired.png) |
| 17-top-dismiss | outside_region_dismissed_to_hours | [E-FOOD-HCAFE-P-17](../../evidence/2026-09-28-full-audit/figma-food-extra-17-top-dismiss.png) |
| 18-reopen-bottom | recorded | [E-FOOD-HCAFE-P-18](../../evidence/2026-09-28-full-audit/figma-food-extra-18-reopen-bottom.png) |
| 19-bottom-dismiss | outside_region_dismissed_to_hours | [E-FOOD-HCAFE-P-19](../../evidence/2026-09-28-full-audit/figma-food-extra-19-bottom-dismiss.png) |
| 20-reopen-left | recorded | [E-FOOD-HCAFE-P-20](../../evidence/2026-09-28-full-audit/figma-food-extra-20-reopen-left.png) |
| 21-left-dismiss | outside_region_dismissed_to_hours | [E-FOOD-HCAFE-P-21](../../evidence/2026-09-28-full-audit/figma-food-extra-21-left-dismiss.png) |
| 22-reopen-right | recorded | [E-FOOD-HCAFE-P-22](../../evidence/2026-09-28-full-audit/figma-food-extra-22-reopen-right.png) |
| 23-right-dismiss | outside_region_dismissed_to_hours | [E-FOOD-HCAFE-P-23](../../evidence/2026-09-28-full-audit/figma-food-extra-23-right-dismiss.png) |
| 24-home-return-fixed | home_return_pixel_equal | [E-FOOD-HCAFE-P-24](../../evidence/2026-09-28-full-audit/figma-food-extra-24-home-return-fixed.png) |
| 25-expanded-inferred-exit | recorded | [E-FOOD-HCAFE-P-25](../../evidence/2026-09-28-full-audit/figma-food-extra-25-expanded-inferred-exit.png) |
| 26-expanded-home-return | home_return_pixel_equal | [E-FOOD-HCAFE-P-26](../../evidence/2026-09-28-full-audit/figma-food-extra-26-expanded-home-return.png) |
| 27-list-inferred-exit | recorded | [E-FOOD-HCAFE-P-27](../../evidence/2026-09-28-full-audit/figma-food-extra-27-list-inferred-exit.png) |
| 28-list-home-return | home_return_pixel_equal | [E-FOOD-HCAFE-P-28](../../evidence/2026-09-28-full-audit/figma-food-extra-28-list-home-return.png) |
