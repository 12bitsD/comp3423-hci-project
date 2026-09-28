# 协作说明

## 获取仓库与写入权限

仓库公开可读，任何人都可以直接浏览和克隆，无需协作者邀请。组员需要直接向仓库推送工作分支时，将 **GitHub 用户名或个人主页 URL** 提供给仓库 owner `12bitsD`，接受协作者邀请后获得写入权限。请通过私下渠道提供账号，不在公开仓库登记个人邮箱或账号名单，也不收集 Google 邮箱或密码。

```bash
git clone https://github.com/12bitsD/comp3423-hci-project.git
cd comp3423-hci-project
```

## 认领任务与提交改动

1. 在 [Issues](https://github.com/12bitsD/comp3423-hci-project/issues) 提出或认领任务，写清目标、计划交付和已知限制。首次接手先看 [项目简述](docs/project-brief.md) 与 [决策记录](docs/decisions.md)。
2. 从最新 `main` 创建 `feat/` 分支，例如 `feat/room-enquiry-analysis`。有写入权限的组员直接推送工作分支；尚无写入权限时先 fork，再从自己的 fork 发起 PR。一次 PR 聚焦一项可复查的研究或修改。
3. 按 [证据约定](evidence/README.md) 整理脱敏截图与步骤，区分实测、推断及未完成事项。普通文档改动检查链接、时间与事实是否一致即可，不额外要求形式化测试或强制 CI。
4. 提交并推送分支，创建 PR，说明解决的问题、材料位置、验证结果及待讨论项，关联相关 Issue。团队审阅后合并。
5. 讨论形成新的范围或路线决定时，同步更新 `docs/decisions.md`，注明日期、依据和被替代的旧决定。

操作 PolyULife 前遵循仓库嵌入的 [分析 skill](.agents/skills/polyulife-ui-analysis/SKILL.md)。提交前查看 diff 与新增文件，确认材料适合公开，且没有密码、令牌、个人原始截图、参与者身份映射或会议录音。
