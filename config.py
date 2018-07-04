class Config:
    DEBUG = True

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