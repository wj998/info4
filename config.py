from redis import StrictRedis


class Config:
    DEBUG = True
    # 设置秘钥
    SECRET_KEY = 'Uj1TCDDEnTbnkMeq7f6LhnMe1EkIejGI4Mvy0gQooRjOrehJ3m6TkQ=='
    # 配置数据库的链接和动态追踪修改
    SQLALCHEMY_DATABASE_URI = 'mysql://root:wangjian@localhost/info666'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置状态保持存储的session信息
    SESSION_TYPE = 'redis'
    # 配置session的签名
    SESSION_USE_SIGNER = True
    # 构造redis的实例
    SESSON_REDIS = StrictRedis(host='127.0.01', port=6379)
    # 配置session的过期时间
    PERMANENT_SESSION_LIFETIME = 86400



# 开发模式下的配置信息
class developmentConfig(Config):
    DEBUG = True



#  生产模式下的配置信息
class productionConfig(Config):
    DEBUG = False


config = {
    'development': developmentConfig,
    'production': productionConfig
}