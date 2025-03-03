# Python公式の軽量イメージをベースに使用
FROM python:3.13-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPython依存パッケージをrequirements.txtからインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .

# コンテナ起動時に実行するコマンド
CMD ["bash"]
