from flask import Flask, jsonify
import yaml
from code import ResponseCode
from response import ResMsg

app = Flask(__name__)

with open("msg.yaml", encoding="utf-8") as f:
    msg_conf = yaml.safe_load(f)
app.config.update(msg_conf)


@app.route("/", methods=["GET"])
def test():
    res = ResMsg()
    test_dict = dict(name="zhang", age=18)
    # 此处只需要填入响应状态码,即可获取到对应的响应消息
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    return jsonify(res.data)


if __name__ == "__main__":
    app.run()
