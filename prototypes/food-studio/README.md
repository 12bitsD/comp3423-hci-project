# PolyULife Food Design Studio / Fresh Campus v0.2

本地交互原型与视觉规范样包。负责人 D / FengTaiYang。当前状态：v0.2，2026-10-23 用户已通过完整包本地验收，并明确授权上传 GitHub 工作分支供团队审阅。

## 打开方式

最简单：双击 `index.html`。所有素材均在本目录，无需账号、网络、安装依赖或构建。

需要分享本机预览链接时：在本目录运行 `node tools/serve.mjs`，然后打开 `http://127.0.0.1:4186`。服务器仅绑定本机地址，按 Ctrl+C 关闭。Windows 可运行 `start-local.ps1`；它会查找系统或 Codex 自带的 Node。

## v0.2 更新

- 界面、报告图、六页PPT统一为米白底、深蓝文字与明亮绿点缀。
- 保留完整 Food 流程与数据边界；首页与 Food 标题采用获认可的线条插图。
- PPT 文字、编号与色块可编辑；界面截图和插画是嵌入图片，SVG 源在 assets/。
- 网页 PPT 页直接显示导出预览，避免网页与 PPT 文件不同步。

## 包含什么

- **交互原型**：首页入口、餐饮列表、搜索、类型筛选、营业中筛选、时间表展开、详情、地点、无结果恢复及营业时间未知。
- **报告插图**：两组旧界面/改版对比，附历史来源与提案标签，PNG 位于 `exports/`。
- **PPT 样例**：`exports/PolyULife-Food-Fresh-Campus-v02.pptx`，6 页；标题与正文可编辑，界面证据以图片嵌入。
- **共用规范**：`tokens.json` 是颜色、字体、间距和画幅的源数据；`tokens.css` / `tokens.js` 与插图 SVG 配色由同步脚本更新。
- **工作约定**：`AGENTS.md`、`docs/STYLE-GUIDE.md`、`docs/FIGMA-HANDOFF.md`、`docs/EVIDENCE.md`、`docs/ACCEPTANCE.md`。

## 推荐体验顺序

1. 首页入口 → Food；确认清晰的卡片与详情入口。
2. 查看 H Café 营业时间，进入详情，再返回列表。
3. 搜索 Chinese Soup → 详情 → 地图 → 返回两次，确认搜索词和结果保留。
4. 输入 Sushi，体验无结果与恢复；切换类型及 Open now 查看组合筛选。
5. 右侧切换“营业时间未知”，检查与 Closed 的区别。
6. 查看报告插图、6 页 PPT 样例和视觉规范，确认是否采用该方向。

## 演示数据

时间固定为周二 00:54 香港时间。H Café 与售卖机时间来自历史观察；分类有演示性补充；部分商户设为未知时间以演示边界。地图来自历史 VA210 画面，列表地图标记仅表示交互选中，不是真实坐标；其他地点不能把该图当作实际导航。完整来源见 `docs/EVIDENCE.md`。

浏览器原型用于本地风格与交互验收，不替代课程要求的 Figma 可点击原型和至少 5 位真实参与者的 Maze 测试。此包没有测试结果或性能提升结论。

## 修改与导出

- 图片资产：`assets/fresh-bowl.svg`、`assets/fresh-cup.svg`；对应 PNG 在 `exports/`。
- 幻灯片预览：`exports/slide-1.png` 至 `slide-6.png`，全部来自同一次 PPT 构建。
- 修改视觉变量：编辑 `tokens.json`，运行 `node tools/sync-tokens.mjs`。
- 修改商户、交互、页面和插图：编辑 `app.js`、`index.html`、`styles.css`、`fresh.css`。
- `?capture=1&state=default`、`?capture=1&state=detail` 显示无工作室边栏的 390 × 844 画面；供浏览器截图。
- `?capture=1&page=figures&figure=0` / `figure=1` 显示 1200 × 760 插图版式。
- `?capture=1&page=slides&slide=0` 到 `slide=5` 显示 1280 × 720 幻灯片。
- `tools/build-deck.mjs` 使用 Codex 提供的 `@oai/artifact-tool` 构建本地可编辑 PPTX；运行需设置 `CODEX_RUNTIME_MODULES` 指向该运行时的 node_modules。已导出的 PPTX 无此依赖，可直接用 PowerPoint/WPS 打开。
- 截图更新后需重新构建 PPT。`exports/` 是用于报告和展示的资产；`work/` 是忽略的中间文件。
- 再次构建时，用 `PPTX_OUTPUT_NAME` 指定新的版本文件名，避免覆盖已验收文件；相应更新页面中的下载入口。

## Figma 与演示

[共享 Food 入口、迁移前原件与走查记录](../../docs/food-figma.md)。
