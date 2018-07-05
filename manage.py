from flask import session
# 导入扩展flask-script扩展
from flask_script import Manager
# 导入扩展flask_migrate
from flask_migrate import Migrate, MigrateCommand
#  导入create_app函数
from info import create_app, db
# 导入模型类,让模型类的文件被引用,用来迁移创建表
from info import models

app = create_app('development')


# 实例化管理对象
manage = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 添加迁移命令
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':

    manage.run()
