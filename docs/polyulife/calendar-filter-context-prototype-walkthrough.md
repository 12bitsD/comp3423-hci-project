# Calendar 筛选上下文检查点 — 2026-09-30

后续[截图连接恢复与两个调用者](calendar-filter-resume-prototype-walkthrough.md)已完成当前Monday返回、Tuesday样例及Flow3清理；本页保留中断时事实。

新增三个可编辑筛选画板、八条控件，Monday调用者的选择循环、学术日历Apply及重开已实际回放。累计128映射画板、299配置控件、64次原型运行。完整应用仍 `not_verified`，本次为可接力检查点。

## 来源与连接

Acad画板604:19取自E-CALENDAR-FILTER-PERSIST完整公开截图；All604:208和None604:405仅有公开面板裁片，组合到学术日历Sep28背景，不是完整原生截图。勾选草稿不等于已经应用的筛选。[素材来源及哈希](../../design/polyulife/calendar-filter-context-assets.json)、[生成脚本](../../design/scripts/build_calendar_filter_context_svg.py)记录近似字体、图标与几何范围。

五条原生对应连接：Sep28 Filter→Acad（A-CALENDAR-FILTER-REOPEN）；Acad SelectAll→All（A-CALENDAR-RESTORE-ALL，原生恢复动作见AX trace）；All SelectAll→None（A-CALENDAR-DESELECT-ALL）；None AcadCalendar→Acad（A-CALENDAR-SELECT-ACAD）；Acad Apply→Sep28（A-CALENDAR-APPLY-ACAD）。三个CloseFilter→Sep28是 `action_id:null` 的原型恢复推广，原生X和取消语义未观察。全部On click/Swap overlay/Instant，仅描述Figma实现。[连接清单](../../design/polyulife/calendar-filter-context-connections.json)记录根/控件节点、来源与配置截图。

All Apply/None Apply、Class/Exam/Payment单项切换未配置。All Apply虽有原生动作，其默认结果包含私人日程，当前上下文未重建；None Apply原生仍not_attempted。本轮点击17、21仍停在原面板并出现Figma热点提示，只证明原型缺口。

## 实际保存结果与中断

01–03导入画板，04–11保存八个连接。选Sep28根时初次定位同时匹配右侧连接文字，严格匹配拒绝，没有发生修改；随后限定到已观察的左侧objects-panel并检查节点URL再连线。

12–30为一次Monday样例：Home经Week/选择器/月份循环进入Sep28；14→15→16为Acad→All→None，18、22、24分别验证三种X恢复；25→26→27→28→29为Acad→All→None→Acad→Apply，30重开仍Acad。三次X均为推断的原型出口，不更新原生A-CALENDAR-FILTER-X状态。十二项应用裁片比较有12项相等、0项差异，详见[公开清单](../../evidence/2026-09-30-calendar-filters/manifest.json)；比较只判断原型内部一致性。

保存30之后尝试X/读取状态时截图采集失败，同一Present句柄再次获取仍失败。没有31或Home返回截图，不能声称最后X或Home成功，也没有完成Tuesday或三个根的额外Flow检查。04号配置截图可见临时Flow 3；连入完成后的最终状态没有复核，清理仍待检查。保留已保存30张截图及[对照图](../../evidence/2026-09-30-calendar-filters/contact-sheet.png)，不新增原生成功动作。原生Wrapper连接先前超时、发现列表仍运行，不证明窗口可观察；本轮没有重启应用。

## 接力位置

恢复Computer Use文档后，读取现有Present真实状态；可能已执行X但不能假定位置。先核对页面并完成Monday Home返回，再测试Tuesday调用者、三个筛选根是否出现额外Flow。12号Home基线留存文件底部照片可见，未完成Home返回不能证明图片长期稳定。随后补原生X/None Apply/单项筛选及其它日期组合。所有历史失败、原生状态/动作数组保留，Agent回放不代替真人评估。
