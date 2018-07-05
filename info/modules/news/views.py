# 导入蓝图函数
from flask import session, render_template, current_app

from . import news_blue


# 项目首页
@news_blue.route('/')
def index():
    session['name'] = '2018'
    return render_template('news/index.html')


# 项目logo图片展示
@news_blue.route('/favicon.ico')
def favicon():
    # 把项目logo文件发送给浏览器
    return current_app.send_static_file('news/favicon.ico')