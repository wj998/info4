from redis import StrictRedis


class Config:
    DEBUG = True
    # 设置秘钥
    SECRET_KEY = 'Uj1TCDDEnTbnkMeq7f6LhnMe1EkIejGI4Mvy0gQooRjOrehJ3m6TkQ=='
    # 配置数据库的链接和动态追踪修改
    SQLALCHEMY_DATABASE_URI = 'mysql://root:wangjian@localhost/info666'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # 定义redis的主机和port
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 配置状态保持存储的session信息
    SESSION_TYPE = 'redis'
    # 配置session的签名
    SESSION_USE_SIGNER = True
    # 构造redis的实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
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