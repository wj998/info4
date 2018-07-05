# 导入蓝图函数
from flask import session, render_template

from . import news_blue


@news_blue.route('/')
def index():
    session['name'] = '2018'
    return render_template('news/index.html')
