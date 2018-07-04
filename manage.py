from flask import Flask
# 导入扩展flask-script扩展
from flask_script import Manager

# 导入配置文件中的字典
from config import config

app = Flask(__name__)
# 使用配置信息
app.config.from_object(config['development'])


# 实例化管理对象
manage = Manager(app)


@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manage.run()