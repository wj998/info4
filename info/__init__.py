

from flask import Flask, session
# 导入扩展flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# 导入扩展 flask_session
from flask_session import Session

# 实例化sqlalchemy对象
db = SQLAlchemy()

# 导入配置文件中的字典
from config import config

# 工厂函数: 可以让我们的函数根据传入的参数的不同,生产不同环境下的app
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置信息
    app.config.from_object(config[config_name])
    # 实例化Session对象
    Session(app)
    # 通过init_app方法,让db和app进行关联
    db.init_app(app)


    # 返回app
    return app