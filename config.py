class Config:
    DEBUG = True

    # 配置数据库的链接和动态追踪修改
    SQLALCHEMY_DATABASE_URI = 'mysql://root:wangjian@localhost/info666'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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