# 2. Related Work

## 2.1 从功能堆叠到任务完成

Card、Moran 和 Newell 用目标、操作、方法和选择规则描述人机交互，说明用户带着目标使用系统，而不是来浏览功能清单。[1] Krug 进一步强调，好的界面应该让用户一看就知道下一步做什么。[2]

校园 App 也遵循同样的逻辑。学生打开 PolyULife，是为了查课、找教室、看地图、找服务或点餐。首页和导航应该直接支持这些任务，而不是让用户先理解整个系统的结构。

本项目把高频任务放到主要入口，并减少进入任务所需的层级。Apps 直接列出服务，Calendar 直接显示日期和当天事件，Room 直接显示房间和可用状态，Food 直接显示餐厅信息，Map 直接显示地点。

## 2.2 信息层级与认知负荷

Miller 指出，人的工作记忆容量有限。[3] Sweller 的认知负荷理论进一步说明，界面中的无关信息会消耗理解任务所需的资源。[4] Nielsen 提出的渐进式披露则给出了一种具体做法：先显示当前需要的信息，再按用户操作展开更多内容。[5]

这些研究都指向同一个结论：页面不应该一次展示所有信息和控件。

本项目采用三步信息结构：

- 先看当前状态：日期、建筑、餐厅或服务。
- 再看匹配结果：课程、房间、地点或服务详情。
- 最后看扩展内容：完整列表、路线、营业时间或操作说明。

Calendar 先显示日期，再显示当天事件，最后打开课程详情。Map 先显示建筑，再显示楼层和房间。Room 先显示查询条件，再显示可用结果。Food 先显示餐厅列表，再展开营业时间和位置。每一层都围绕当前任务展开。

## 2.3 状态、反馈与可逆操作

Nielsen 的可用性原则要求系统及时反馈当前状态，并允许用户撤销和恢复操作。[6] Norman 把反馈看作理解系统行为的关键，同时强调识别优于回忆。[7] Raskin 也主张让系统状态和控制方式保持清楚可见。[8]

这些原则直接决定了本项目的界面形式：

- 当前筛选、日期、类别和结果数量直接显示。
- 选中的类别同时使用文字、图标和颜色。
- Apply、Reset、Close 分开，明确各自作用。
- Clear 用来清除条件，Back 用来返回上一状态。
- 空结果说明具体原因，并提供恢复入口。

Calendar 的 `Class ✓`、结果数量和 Clear，让用户直接识别当前结果。Exam 空状态明确显示 `No exams on this date`，并提供 `Show all events`。Map 的空楼层直接指出没有目标设施，并给出最近可用楼层。Food 的无结果显示查询条件和重新查询入口。

## 2.4 触控目标与无障碍

Fitts’ Law 说明，目标越大、距离越近，指向操作越快。[9] W3C 的无障碍指南要求信息不能只依赖颜色表达，控件需要有可识别的名称和状态。[10]

本项目放大主要按钮和结果卡片，让整张卡片都能点击。筛选项使用大尺寸整行目标，当前类别同时显示图标和文字。选中、未选中和不可用状态采用不同文案，不只改变颜色。

这些做法同时服务于操作效率和可访问性：用户更容易点中，也更容易理解。

## 2.5 用真实任务检验设计

Tullis 和 Albert 将任务完成率、耗时和错误列为重要的可用性指标。[11] Sauro 和 Lewis 强调把行为数据与主观反馈结合，而不是只依赖满意度。[12] Bangor、Kortum 和 Miller 对 SUS 的研究说明，量表可以把主观体验转成可比较的数据。[13] Shneiderman 则强调在真实任务中观察用户，而不是只检查页面外观。[14]

本项目使用 Maze 记录任务成功、退出、误点和耗时，再用量表和开放问题补充原因。数据直接用于修改页面：找不到入口就强化入口，看不懂状态就补充反馈，误点集中就调整目标大小和布局，无法恢复就增加返回和清除路径。

## 2.6 对本项目的启示

上述研究形成了五个统一设计规则：

1. **任务优先**：首页直接支持查课、找房、找地点、找服务和找餐厅。
2. **分层展示**：先给当前信息，再展开详情，控制认知负荷。
3. **状态可见**：筛选、结果、加载和空状态都给出明确反馈。
4. **操作可逆**：Back、Clear、Reset、Close 各有固定含义。
5. **用测试推动修改**：用真实参与者的行为、数据和原话决定下一版设计。

这五个规则贯穿五个功能，保证各模块采用一致的信息结构和交互方式。

## References

[1] Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Lawrence Erlbaum Associates.

[2] Krug, S. (2014). *Don’t Make Me Think, Revisited: A Common Sense Approach to Web Usability* (3rd ed.). New Riders.

[3] Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97.

[4] Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.

[5] Nielsen, J. (2006). Progressive disclosure. Nielsen Norman Group. https://www.nngroup.com/articles/progressive-disclosure/

[6] Nielsen, J. (1994). Heuristic evaluation. In J. Nielsen & R. L. Mack (Eds.), *Usability Inspection Methods*. Wiley.

[7] Norman, D. A. (2013). *The Design of Everyday Things: Revised and Expanded*. Basic Books.

[8] Raskin, J. (2000). *The Humane Interface: New Directions for Designing Interactive Systems*. Addison-Wesley.

[9] Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology, 47*(6), 381–391.

[10] W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

[11] Tullis, T., & Albert, B. (2013). *Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics* (2nd ed.). Morgan Kaufmann.

[12] Sauro, J., & Lewis, J. R. (2016). *Quantifying the User Experience: Practical Statistics for User Research* (2nd ed.). Morgan Kaufmann.

[13] Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An empirical evaluation of the System Usability Scale. *International Journal of Human–Computer Interaction, 24*(6), 574–594.

[14] Shneiderman, B. (2016). *Designing the User Interface: Strategies for Effective Human-Computer Interaction* (6th ed.). Pearson.
