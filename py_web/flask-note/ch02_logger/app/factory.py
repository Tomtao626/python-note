import logging
import logging.config
from flask import Flask
import yaml
import os


def create_app(config_name=None, config_path=None):
    app = Flask(__name__)
    if not config_name:
        config_name = "PRODUCTION"
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'ch01_yam2/config/config.yaml')
    conf = read_yaml(config_name, config_path)
    app.conf.update(conf)
    if not app.config['LOGGING_PATH']:
        os.mkdir(app.config['LOGGING_PATH'])
    with open(app.config["LOGGING_CONFIG"], "r", encoding='utf-8') as f:
        dict_conf = yaml.safe_load(f.read())
    logging.config.dictConfig(dict_conf)
    return app


def read_yaml(config_name, config_path):
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError("no find conf")
    else:
        raise ValueError("请输入正确的配置名称或配置文件路径")
