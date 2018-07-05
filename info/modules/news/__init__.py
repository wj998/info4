
from flask import Blueprint
# 创建蓝图函数
news_blue = Blueprint('news_blue', __name__)

# 把蓝图对象的文件导入到创建蓝图对象的下面
from . import views