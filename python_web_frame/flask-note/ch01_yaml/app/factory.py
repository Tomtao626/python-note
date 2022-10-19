import os

import yaml
from flask import Flask


def create_app(config_name=None, config_path=None):
    app = Flask(__name__)
    if not config_name:
        config_name = "PRODUCTION"
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'ch01_yaml/config/config.yaml')
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)
    return app


def read_yaml(config_name: str, config_path: str):
    if config_name and config_path:
        with open(config_path, 'rb') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            return KeyError("未找到对应的配置信息")
    else:
        return ValueError("请输入正确的配置名称或配置文件路径")
