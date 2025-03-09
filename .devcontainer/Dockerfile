# Microtsft公式のPythonイメージを利用する
FROM mcr.microsoft.com/vscode/devcontainers/python:3

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPython依存パッケージをrequirements.txtからインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .

# コンテナ起動時に実行するコマンド
CMD ["bash"]
