from flask import Flask, session
# 导入扩展flask-script扩展
from flask_script import Manager
# 导入扩展flask_migrate
from flask_migrate import Migrate, MigrateCommand
# 导入扩展flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# 导入扩展 flask_session
from flask_session import Session




# 导入配置文件中的字典
from config import config

app = Flask(__name__)
# 使用配置信息
app.config.from_object(config['development'])
# 实例化Session对象
Session(app)

# 实例化sqlalchemy对象
db = SQLAlchemy(app)

# 实例化管理对象
manage = Manager(app)
# 使用迁移框架
Migrate(db, app)
# 添加迁移命令
manage.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = '2018'
    return 'index'

if __name__ == '__main__':
    manage.run()
