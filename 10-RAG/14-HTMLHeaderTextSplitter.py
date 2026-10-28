# HTML切分器

from langchain_text_splitters import HTMLHeaderTextSplitter

html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>欢迎来到尚硅谷！</h1>
        <p>尚硅谷是专门培训IT技术方向</p>
        <div>
            <h2>尚硅谷老师简介</h2>
            <p>尚硅谷老师拥有多年教学经验，都是从一线互联网下来</p>
            <h3>尚硅谷北京校区</h3>
            <p>北京校区位于宏福科技园区</p>
        </div>
    </div>
</body>
</html>
"""

# 
headers_to_split_on = [
    ("h1", "标题1"),
    ("h2", "标题2"),
    ("h3", "标题3"),
]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
print(html_header_splits)
