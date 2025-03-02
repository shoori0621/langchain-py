from dotenv import load_dotenv
from openai import OpenAI
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "こんにちは！私はジョンと言います！"},
        ],
        timeout=10,
        stream=True
    )

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end="", flush=True)

except requests.exceptions.Timeout:
    print("OpenAI API request timed out")

