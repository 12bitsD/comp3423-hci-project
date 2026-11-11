# Figma 迁移与协作说明 / Fresh Campus v0.2

本页是独立 Food Studio 的原设计规格，保留原页面与连线设想供对照。21 帧已并入共享文件；当前画框、入口和返回约定见[Food 整合记录](../../../docs/food-figma.md)。

## 页面结构

- `00 · Foundations`：颜色、字体、间距与组件。
- `01 · Observed UI`：引用已有原应用复现，不覆盖旧证据。
- `02 · Food Redesign`：下列画框和连线。
- `03 · Report Figures`：1200 × 760 对比图。
- `04 · Presentation`：1280 × 720 幻灯片布局参考。

## Food 画框

390 × 844：F00 Home 占位入口，F01 默认列表，F02 时间表展开，F03 详情，F04 食品搜索，F05 无结果，F06 未知营业时间，F07 地点地图。页面高度可滚动，不把长内容压缩成一屏。

组件：FoodCard（状态、展开变体）、SearchField、CategoryFilter、StatusText、BackHeader、HoursTable、ExternalPrompt。颜色从 tokens.json 建立 Color Styles / Variables。

## 连接

Home → 列表 → 详情 → 地图；地图 Back → 详情；详情 Back → 来源列表。

标签 → 查询结果 → 新详情；新详情 Back → 查询结果；查询结果 Back → 来源详情。

不要将详情 Back 固定连到默认列表。使用多个来源画框、可用的变量/条件或适合的返回机制，以实际 Present 运行结果确认。原型中的筛选、滚动和空状态需显式配置，导入截图不等于完成交互。

## 与组员的接口

- A/B/C/E 保留各自功能所有权。D 提供通用组件，不改写其业务流程。
- C 统筹全局导航与返回；E 负责跨类别校园地图。Food 的地点查看不替代 Map。
- B 与 E 将任务接入 Maze，采用真实参与者。设计稿与测后迭代分版本保存。


## 新版视觉映射

以 tokens.json 的 Fresh Campus v0.2 颜色建立变量；亮绿按钮采用深蓝文字，链接/焦点为深绿，关闭与未知状态独立。将 assets/fresh-bowl.svg 与 fresh-cup.svg 作为矢量装饰导入，截图中的商户标志仍保留原素材。
