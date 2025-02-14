import os
from datetime import datetime

def generate_navigation():
    # 获取blogs目录下所有.html文件
    blogs_dir = "blogs"
    html_files = [f for f in os.listdir(blogs_dir) if f.endswith(".html")]

    # 按文件修改时间排序
    html_files.sort(key=lambda x: os.path.getmtime(os.path.join(blogs_dir, x)), reverse=True)

    # 读取文件名并生成导航项
    nav_items = []
    for file in html_files:
        filename = os.path.splitext(file)[0]
        # 将文件名转换为标题格式（如"my_blog" -> "My Blog"）
        title = " ".join([word.capitalize() for word in filename.split('_')])
        # 获取文件修改时间
        modified_time = datetime.fromtimestamp(os.path.getmtime(os.path.join(blogs_dir, file))).strftime("%Y-%m-%d")
        nav_items.append({
            "title": title,
            "link": os.path.join(blogs_dir, file),
            "modified_time": modified_time
        })

    # 生成导航页HTML内容
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blogs Navigation</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}

        body {{
            background: #f0f2f5;
            padding: 2rem;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 3rem;
        }}

        h1 {{
            color: #2c3e50;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}

        .blog-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }}

        .blog-card {{
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            cursor: pointer;
        }}

        .blog-card:hover {{
            transform: translateY(-5px);
        }}

        .blog-card h2 {{
            color: #34495e;
            margin-bottom: 0.5rem;
        }}

        .blog-card .date {{
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }}

        .blog-card .preview {{
            color: #666;
            font-size: 0.95rem;
            line-height: 1.5;
            height: 60px;
            overflow: hidden;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}

            h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>我的博客导航</h1>
        </header>

        <div class="blog-cards">
""")

        # 添加博客卡片
        for item in nav_items:
            f.write(f"""
            <div class="blog-card">
                <h2>{item['title']}</h2>
                <div class="date">{item['modified_time']}</div>
                <div class="preview">预览：{item['title']}</div>
                <a href="{item['link']}" style="color: #3498db; text-decoration: none;">阅读更多 →</a>
            </div>
""")

        f.write(f"""
        </div>
    </div>
</body>
</html>
""")

if __name__ == "__main__":
    generate_navigation()
    print("导航页已成功生成为 index.html！")
