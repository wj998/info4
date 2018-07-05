# 导入蓝图
from . import passport_blue


@passport_blue.route('/image_code')
def generate_image_code():
    '''
    生成图片验证码:获取参数-校验参数-业务处理-返回结果
    1. 获取参数,查询字符串形式,args
    2. 校验参数uuid是否存在,如果不存在,直接return
    3. 调用captcha生成图片验证码:name text image
    4. 在服务器redis数据库中存储图片验证码
    5. 返回图片本身,使用相应对象
    reponse = make_response
    reture response
    6. 修改相应的数据类型 image/jpg
    :return:
    '''

    pass