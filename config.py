class Config:
    SECRET_KEY = "CESARandres#321"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_DB = "tienda"


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
