# Git & Collaboration
> 📝 **Git 与协作** —— 这是第 0 阶段第 2 课，约 30 分钟。

> Version control is not optional. Every experiment, every model, every lesson you build here gets tracked.
> 📝 版本控制不是可选项。你在这里做的每一个实验、每一个模型、每一节课的成果，都会被追踪记录。就像律所的案件归档系统——每一步操作都有迹可查。

**Type:** Learn
**Languages:** --
**Prerequisites:** Phase 0, Lesson 01
**Time:** ~30 minutes
> 📝 课程类型：学习型 | 无需编程语言基础 | 前置：第 01 课（开发环境）| 预计用时：30 分钟

---

## Learning Objectives
> 📝 **学习目标** —— 本节课结束后你应该能做到以下四件事：

- Configure git identity and use the daily workflow of add, commit, and push
  > 📝 配置 Git 用户身份（署名），掌握 add → commit → push 这套日常三步流程

- Create and merge branches for isolated experiments without breaking main
  > 📝 创建分支做实验，实验完成后合并回主分支，全程不影响主线代码

- Write a `.gitignore` that excludes model checkpoints and large binary files
  > 📝 写一份 .gitignore 文件，告诉 Git 哪些文件不需要追踪（比如几 GB 的 AI 模型文件）

- Navigate the commit history with `git log` to understand project evolution
  > 📝 用 git log 翻看提交历史，了解项目是怎么一步步演变过来的

---

## The Problem
> 📝 **为什么需要版本控制？**

You're about to write hundreds of code files across 20 phases. Without version control you will lose work, break things you can't undo, and have no way to collaborate with others.
> 📝 你即将在 20 个阶段里写数百个代码文件。没有版本控制：会丢失工作成果、犯下无法撤销的错误、无法与他人协作。类比：在没有修订记录的情况下多人同时编辑同一份合同。

Git is the tool. GitHub is where the code lives. This lesson covers what you need for this course and nothing more.
> 📝 Git 是工具本身（装在你电脑上）；GitHub 是代码存放的云端平台。本课只教这门课真正用得上的，不做多余延伸。

---

## The Concept
> 📝 **核心概念：Git 的四个"地点"**
> 📝 工作目录（办公桌）→ 暂存区（待提交托盘）→ 本地仓库（本地档案柜）→ 远端 GitHub（云端备份）

\`\`\`mermaid
sequenceDiagram
    participant WD as Working Directory
    participant SA as Staging Area
    participant LR as Local Repo
    participant R as Remote (GitHub)
    WD->>SA: git add
    SA->>LR: git commit
    LR->>R: git push
    R->>LR: git fetch
    LR->>WD: git pull
\`\`\`
> 📝 流程图说明：文件从左到右流动是"保存备份"，从右到左流动是"获取更新"

Three things to remember:
> 📝 **只需记住三件事：**

1. Save often (`git commit`)
   > 📝 勤保存 —— 每完成一个小功能就 commit 一次，就像写合同时随时按 Ctrl+S

2. Push to remote (`git push`)
   > 📝 推送到远端 —— 把本地存档同步到 GitHub，做异地备份

3. Branch for experiments (`git checkout -b experiment`)
   > 📝 用分支做实验 —— 想试新想法时先开分支，不影响主线

---

## Build It
> 📝 **动手操作** —— 以下四个步骤按顺序执行

### Step 1: Configure git
> 📝 **第一步：配置身份** —— 告诉 Git 你是谁，每次提交都会自动署名

\`\`\`bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
\`\`\`
> 📝 把引号里的内容换成你自己的姓名和邮箱。`--global` 表示对这台电脑上所有项目生效，只需配置一次。

### Step 2: The daily workflow
> 📝 **第二步：日常工作流** —— 这四个命令是你以后每天都会用的核心操作

\`\`\`bash
git status                                     # 查看哪些文件有改动
git add file.py                                # 把 file.py 放进暂存区
git commit -m "Add perceptron implementation"  # 正式存档并写备注
git push origin main                           # 推送到 GitHub 的 main 分支
\`\`\`
> 📝 类比律所：写完合同（status 检查）→ 圈出要归档的页面（add）→ 盖章存档写备注（commit）→ 上传云端系统（push）

### Step 3: Branching for experiments
> 📝 **第三步：用分支做实验** —— 想试新方案时，先开"复印件"分支，不动主稿

\`\`\`bash
git checkout -b experiment/new-optimizer   # 新建并切换到实验分支
# ... make changes, commit ...            # 在实验分支上改代码、提交
git checkout main                          # 切换回主分支
git merge experiment/new-optimizer         # 把实验结果合并进主分支
\`\`\`
> 📝 实验成功 → merge 合并进主线；实验失败 → 直接删掉分支，主线毫发无损。

### Step 4: Working with this course repo
> 📝 **第四步：获取课程仓库并建立个人进度分支**

\`\`\`bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
git checkout -b my-progress
# work through lessons, commit your code
git push origin my-progress
\`\`\`
> 📝 你已经完成了这一步：克隆仓库 → 进入文件夹 → 建 my-progress 分支 → 提交练习 → 推送到你的 Fork

---

## Use It
> 📝 **命令速查** —— 这门课只需要掌握这五个命令

| Command | When |
|---------|------|
| `git clone` | Get the course repo |
| `git add` + `git commit` | Save your work |
| `git push` | Back it up to GitHub |
| `git checkout -b` | Try something without breaking main |
| `git log --oneline` | See what you've done |

> 📝 中文对照：clone 下载仓库 / add+commit 保存进度 / push 云端备份 / checkout -b 开分支实验 / log 查历史

That's it. You don't need rebase, cherry-pick, or submodules for this course.
> 📝 就这五个。rebase、cherry-pick、submodules 这些高级功能本课程用不到，暂时不必学。

---

## Exercises
> 📝 **课后练习** —— 三道实操题，你已经全部完成 ✅

1. Clone this repo, create a branch called `my-progress`, make a file, commit it, push it
   > 📝 ✅ 已完成：克隆仓库 → 建 my-progress → 新建 my_progress.md → commit → push

2. Create a `.gitignore` that excludes model checkpoint files (`.pt`, `.pth`, `.safetensors`)
   > 📝 ✅ 已完成：.gitignore 排除了 .pt / .pth / .safetensors 及 .DS_Store / .env

3. Look at the commit history of this repo with `git log --oneline` and read how lessons were added
   > 📝 ✅ 已完成：git log 看到自己的两条提交在最顶部，其余是课程作者的历史记录

---

## Key Terms
> 📝 **关键术语** —— 记住"实际含义"那列，不要被"常见说法"误导

| Term | What people say | What it actually means |
|------|----------------|----------------------|
| Commit | "Saving" | A snapshot of your entire project at a point in time |
| Branch | "A copy" | A pointer to a commit that moves forward as you work |
| Merge | "Combining code" | Taking changes from one branch and applying them to another |
| Remote | "The cloud" | A copy of your repo hosted somewhere else (GitHub, GitLab) |

> 📝 Commit = 整个项目的时间点快照（不只是保存）
> 📝 Branch = 指向提交的指针（不是真正的副本，不占双倍空间）
> 📝 Merge = 把一个分支的改动应用到另一个分支（不是简单粘贴）
> 📝 Remote = 托管在其他地方的仓库副本（GitHub / GitLab 都是远端平台）
