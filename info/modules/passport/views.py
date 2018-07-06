# 导入蓝图
from . import passport_blue
# 导入flask内置的对象
from flask import request, jsonify, current_app, make_response
# 导入自定义状态码
from info.utils.response_code import RET
# 导入图片验证码工具
from info.utils.captcha.captcha import captcha
# 导入redis实例, 常量文件
from info import redis_store, constants



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

    # 获取前端传入的uuid,作为图片验证码的后缀名保存到redis数据库中
    image_code_id = request.args.get('image_code_id')
    # 判断获取结果
    if not image_code_id:
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    # 调用captcha工具生成图片验证码
    name, text, image = captcha.generate_captcha()
    # 在redis数据库中储存text
    try:
        redis_store.setex('ImageCode' + image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger(errno=RET.DBERR, errmsg='保存图片验证码失败')
    else:
        # 返回图片给前端,使用make_response
        response = make_response(image)
        # 修改响应的数据类型
        response.headers['Content-Type'] = 'image/jpg'
        # 返回响应
        return response





