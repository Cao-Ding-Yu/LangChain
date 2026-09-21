
import base64
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage

model = ChatOllama(
    model="qwen3.8:27b",
    reasoning=True,
    # base_url="http://localhost:11434",
)

# 将图片转为编码
def encode_image(img_path="鹦鹉.png"):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

response = model.invoke(
    [
        # 传统写法
        # HumanMessage(
        #     content=[
        #         {'type': 'text', 'text': '这张图里有什么？'},
        #         {'type': 'image_url', "image_url": encode_image(),}
        #     ]
        # )

        # 统一写法
        HumanMessage(
            content_blocks=[
                {'type': 'text', 'text': '这张图里有什么？'},
                {'type': 'image', 'base64': encode_image(), 'mime_type': 'image/png',}
                # {"type": "image", "url": "https://example.com/image.jpg" }
            ]
        )
    ]
)
print(response.content_blocks)