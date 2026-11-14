# 世林的 PPT 风格

把真实修改意见和参考作品整理成可读取、可追溯、可更新的个人技能。

**核心风格：组会模板下的高密度技术讲解。页面紧凑规整，图文对应，机制与证据充分展开，最后用一句话收住重点。**

## 使用

技能名称：`wsl-ppt-style`。可以直接说：

> 用 $wsl-ppt-style 做这篇论文的课堂分享，面对了解 LLM 推理、但不熟悉本文方法的同学。沿用组会模板，尽量少页，保留关键实验和不足。

也可以说“按我的 PPT 风格”，让支持自动选择技能的环境根据描述选择本技能。明确写出 `$wsl-ppt-style` 更容易定位。新安装后如当前聊天没有显示技能，请新开聊天或重新加载应用。

它负责视觉偏好、讲解组织和风格检查；具体导入、编辑、渲染与导出由当前环境的演示文稿工具负责。用户本次指定的模板、页数、字体和输出方式优先。

## 安装与更新

要求 Python 3，默认安装到 `${CODEX_HOME:-~/.codex}/skills`。

```sh
gh repo clone wangshilin-2004/wsl-ppt-style
cd wsl-ppt-style
python3 scripts/install.py
python3 scripts/install.py --check
```

安装器建立指向本仓库的链接，不覆盖已有技能。仓库目录需要保留；规则更新后，本地安装会读取同一份文件。在其他机器上可用 `git pull --ff-only` 接收已提交的更新。

## 持续学习

下次可以说：

> 把这次“实验图再大一点，解释移到右边”的要求更新进我的 PPT 风格技能；先区分这是这一页的调整，还是以后都适用。

如果还希望同步到 GitHub，可以明确补充“并提交、同步到 GitHub”。普通制稿或一次页面调整不会自动修改、提交风格规则。

更新时先修改最相关的规则，记录适用场景和来源，再写入 [CHANGELOG.md](CHANGELOG.md)。纠正已有规则优先于不断追加新禁令。详见 [更新方法](skills/wsl-ppt-style/references/update-style.md)。

## 文件

- [技能入口](skills/wsl-ppt-style/SKILL.md)：实际制作时首先读取。
- [布局与视觉](skills/wsl-ppt-style/references/layouts.md)：页面结构、图表、颜色与字体。
- [讲解与场景](skills/wsl-ppt-style/references/teaching.md)：课堂、答辩、教材配图的区别。
- [偏好依据](skills/wsl-ppt-style/references/evidence.md)：明确要求与作品观察分开记录。
- [更新方法](skills/wsl-ppt-style/references/update-style.md)：如何纳入下一轮反馈。

## 参考作品与范围

初版依据既有对话反馈，以及毕业设计目录中的组会稿、答辩稿和独立配图。仓库保存提炼后的风格，不包含论文内容、完整原始 PPT、字体文件或学校标识素材。

本机可通过技能目录下的 `.local/reference-paths.json` 定位原始参考文件；这个文件不提交 Git。换机器时可以重新指定参考路径；没有原文件时按文字规则制作，不声称精确复用了模板，也不伪造学校标识。

初始版本：`0.1.0`，2026-11-14。
