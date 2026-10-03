# 天气官方网页入口与回放 — 2026-09-30

本批通过 Computer Use 将既有原生天气网页状态接入Figma：新增一张画板、两条连接及三组运行记录。当前116个映射画板、270个配置控件、51次原型运行；全应用仍为 `not_verified`。

## 原生来源及明确边界

原生A-WEATHER-LINK记录了文章链接打开官方Academic Registry网页；E-WEATHER-WEB是2026-09-28 14:18:02取得的576×970公共截图，页面有Cookie提示。不是本批新观察。当前应用清单仍显示运行，但按本次发现的Wrapper路径连接超时；未重启，也未新增原生动作。

[源文件](../../design/polyulife/weather-web.svg)及[生成脚本](../../design/scripts/build_weather_web_svg.py)只复现已观察视口。画板[551:20](https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/?node-id=551-20)位置0,49000、576×970、Clip content均从实际编辑器读取。浏览器栏、站点标题、Cookie正文、适用范围文字和图标是可编辑Text/Vector；校徽与横幅来自[公共素材及哈希清单](../../design/polyulife/weather-web-assets.json)。横幅中的标题和白色指针痕迹仍在栅格图片里，未伪装成完整可编辑网页。

Cookie背景暂用不透明颜色，未复现透出下方内容；字体/图标近似，网站标题间距与Cookie尺寸仍有差异。未补造截图之外的网页正文、加载态或滚动边界；可见滚动条只是参考图形，未启用滚动。站点菜单、搜索、分享、Cookie关闭/隐私链接、浏览器更多/后退/前进/重载都保持未配置。

## 连接与返回来源

文章WeatherWebLink实际节点12:500设置On click → Open overlay → 551:20，代表已观察A-WEATHER-LINK。网页CloseWeatherWeb实际节点551:31设置On click → Close overlay，回到12:480；**它是原型恢复路径，action_id为null**。原生A-WEATHER-WEB-CLOSE仍为not_attempted，原生返回结果尚未确认。原型关闭通过不能补写原生成功。连接及修复见[清单](../../design/polyulife/weather-web-connections.json)。

## 实际回放、失败与修复

从[More Present](https://www.figma.com/proto/ulBuuteCRdzdBsHAaiqyUr/?node-id=12-435&starting-point-node-id=12%3A435&scaling=scale-down&content-scaling=fixed)点击天气卡片、文章下划线链接，查看网页后点击左上网页X，再点文章Back返回More。04–08首次路线通过导航，06保留Cookie首行在右侧裁切。

实际导入首行使用Inter字体替换，23px文字超出边界；在文本节点551:68把第一行改为22px并更新源文件，其余Cookie文字保持23px。09保存编辑器读回。这是适配原型文字的修正，未声称原生字体测量一致。

再次进入时立即工具画面显示校徽和横幅缺失，但保存10时两图已经恢复；保留文件名，不把10虚称为缺图画面。工具瞬时缺图没有对应的本地留存截图，不证明持续失败或根因。随后通过Figma图片填充对话框重传两个原PNG：校徽551:42、横幅551:58，11/12保存配置。13–18两轮修复回放中两图都可见，文章与More逐层返回可继续操作；只证明这两轮样例，长期与其它调用者图片稳定性未验证。工具瞬时表现与保存图的区别明确保留，未证明重传与恢复之间的因果关系。

[截图清单与七项像素比较](../../evidence/2026-09-30-weather-web/manifest.json)保存首次、瞬时输出后已恢复的画面与重传后回放。比较对象是同一原型的返回/重入状态，不是原生像素保真、原生时序或真人可用性数据。

## 后续

继续恢复原生连接，观察网页关闭、Cookie、站点及浏览器控制与完整滚动；再替换横幅中的栅格文字，校验整个网页和其它来源。当前仅接入已观察入口与有限视口，未达到全应用复现或课程真人Maze评估。
