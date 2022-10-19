from flask import Flask
from core import JSONEncoder

app = Flask(__name__)

# 返回json格式转换
app.json_encoder = JSONEncoder

if __name__ == "__main__":
    app.run()