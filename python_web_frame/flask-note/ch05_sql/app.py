from flask import Flask
from core import db

app = Flask(__name__)

# config_path = os.path.join("ch05_sql/config/config.yaml")
# with open(config_path, 'r') as f:
#     conf = yaml.safe_load(f.read())
# database_url = f"mysql+pymysql//{conf['DB']['USERNAME']}:{conf['DB']['PASSWORD']}@{conf['DB']['HOST']}:{conf['DB']['PORT']}/{conf['DB']['DATABASE']}?charset=utf8"

USERNAME = 'root'  # 用户名
PASSWORD = '1qazxsw2'  # 密码
HOST = '127.0.0.1'  # 数据库地址
PORT = '3306'  # 端口
DATABASE = 'test'  # 数据库名
database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE)
# 添加数据库配置文件到flask App中
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# 注册数据库连接
db.app = app
db.init_app(app)

from service import ArticleAPI
article_view = ArticleAPI.as_view('article_api')
app.add_url_rule('/article/', defaults={'key': None},
                 view_func=article_view , methods=['GET',])
app.add_url_rule('/article/', view_func=article_view , methods=['POST',])
app.add_url_rule('/article/<string:key>', view_func=article_view ,
                 methods=['GET', 'PUT', 'DELETE'])
if __name__ =='__main__':
    app.run()

