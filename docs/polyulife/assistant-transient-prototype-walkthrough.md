# Assistant 中间状态接入与实际回放 — 2026-09-30

三份[准备素材](assistant-transient-source-preparation.md)已导入Figma，576×970/Clip content逐一检查：BeforeHero613:600、WebLoading613:627、WebBlank613:662，位置0/700/1400,57000。两个现有入口改目标，新增三个控件；累计131映射画板、302配置控件、68次运行，全应用 `not_verified`。

## 最终连接与实际范围

More卡片12:446从直接到详情42:6改为先到BeforeHero；BeforeHero After delay800ms→42:6（A-ASSISTANT-HERO-LOAD）。正文here42:26从直接到Disclaimer改为先到WebLoading；WebLoading After delay800ms→42:43（action_id:null，观察序列的原型推进）。两个800ms仅为演示代理，原生两次截图间隔不是测得加载时长。两个旧连接作为superseded保留，旧失败/回放记录不改。

Blank CloseWeb613:671→42:6对应A-ASSISTANT-WEB-CLOSE原生AX结果；独立参考起点613:662实际X返回详情后Back→More。没有输入框或输入→Blank连线，也没有宣称原生输入造成空白。Welcome X仍是以前推广的源状态，不能用Blank样例消除该差异。

10–17实际More→BeforeHero→Detail→WebLoading→Disclaimer→Welcome→Detail→More，11和13均保存到实际短暂状态；22–24为独立Blank参考关闭。四项裁片比较3项相等、1项差异，结果见[清单](../../evidence/2026-09-30-assistant-transients/manifest.json)和[对照图](../../evidence/2026-09-30-assistant-transients/contact-sheet.png)，仅证明原型内部样例一致。12→16的差异范围为应用裁片内(0,51,374,213)，头图仍可见；原因未明，不能据此称完整视觉通过。加载前/后正文位置变化已保存，不是静态缺图帧冒充加载。加载校徽在导入和Present中可见，未需要重传。两个自动过渡根及Blank根均无额外起点。

## 工具尝试与未完成项

整行点击BeforeHero时误触visibility，URL守卫发现没有切到预期根，停止连线；04保存隐藏状态，05通过已观察checkbox恢复。后续根选择使用左侧精确名称gridcell。第一次Destination查询在Action None时无匹配，随后按实际菜单选Navigate to；解析差量AX时漏掉After delay，改用该菜单完整AX后配置成功，没有重复添加连接。

尝试接管已有tab3时焦点设置超时；没有以此重建浏览器或重启App，改在已确认可用的tab2回放More。原生Wrapper连接仍超时，未新增原生观察。新状态的提前Back/X、加载前here、浏览器菜单/地址/刷新/连续滚动、聊天/发送和问号仍未配置或验证。最终源码与连线见[连接清单](../../design/polyulife/virtual-assistant-transient-connections.json)，原生动作数组保持不变。Agent回放不替代真人评估。
