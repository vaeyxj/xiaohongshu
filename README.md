# xiaohongshu
小红书笔记生成


🌐 博客导航系统
这是一个基于 GitHub Pages 的博客导航系统，通过 Python 脚本自动生成导航页。用户只需要在 blogs 目录下添加新的 HTML 文件，运行脚本即可自动更新导航页，实现快速部署和管理。

网站说明
主要功能
自动化导航生成：扫描 blogs 目录下的所有 HTML 文件，自动生成导航卡片。
创意设计：导航页采用卡片式布局，结合动态悬停效果、阴影和渐变，视觉效果美观。
响应式布局：适应不同屏幕尺寸，PC 和移动端都能良好显示。
动态效果：卡片带有悬停动画，提升用户体验。
时间排序：按文件修改时间排序，最新博客显示在最前面。
文件结构
.
├── blogs/                  # 存放所有博客 HTML 文件
│   ├── my_first_blog.html
│   ├── my_second_blog.html
│   └── ...
├── index.html              # 生成的导航页
├── generate_nav.py         # 自动化生成导航页的脚本
└── README.md               # 项目说明文档
环境要求
Python 3.x
基础的 HTML/CSS 知识（可选）


GitHub 账号（用于部署）
快速开始
1. 准备博客内容
将所有博客文件放入 blogs 目录，文件名请使用清晰的命名规则（如 my_blog.html）。

2. 生成导航页
python generate_nav.py
成功提示：导航页已成功生成为 index.html！
3.提交代码访问：https://vaeyxj.github.io/xiaohongshu/

贡献指南
如果你有好的创意或建议，可以通过以下方式参与：

提交 Issues：描述你的问题或建议。
提交 Pull Request：直接修改代码或文档。
联系方式
邮箱：yxjworking@163.com
GitHub：https://github.com/vaeyxj
