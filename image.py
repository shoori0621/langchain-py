from dotenv import load_dotenv
from openai import OpenAI
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

image_url = "https://raw.githubusercontent.com/yoshidashingo/langchain-book/main/assets/cover.jpg"

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "画像を説明してください。"},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
        response_format={"type": "json_object"},
        timeout=10,
    )

    print(response.choices[0].message.content)
except requests.exceptions.Timeout:
    print("OpenAI API request timed out")
