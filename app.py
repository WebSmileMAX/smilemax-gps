import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Cloudtype Flask!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Cloudtype에서 주는 포트 환경변수 사용
    app.run(host="0.0.0.0", port=port)
