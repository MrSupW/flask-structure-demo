import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def getDbURI(db_info):
    engine = db_info.get("ENGINE") or "sqlite"
    driver = db_info.get("DRIVER") or "sqlite"
    host = db_info.get("HOST") or "localhost"
    port = db_info.get("PORT") or "3306"
    user = db_info.get("USER") or ""
    password = db_info.get("PASSWORD") or ""
    name = db_info.get("NAME") or ""
    return '{}+{}://{}:{}@{}:{}/{}'.format(
        engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "mrsupw"
    SESSION_TYPE = "redis"
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 7 * 24 * 3600  # 7 天


class DevelopConfig(Config):
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Wanghe1351387884?",
        "NAME": "hello_flask"
    }
    SQLALCHEMY_DATABASE_URI = getDbURI(db_info)


class TestConfig(Config):
    TESTING = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Wanghe1351387884?",
        "NAME": "hello_flask"
    }
    SQLALCHEMY_DATABASE_URI = getDbURI(db_info)


# 演示环境
class StagingConfig(Config):
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Wanghe1351387884?",
        "NAME": "hello_flask"
    }
    SQLALCHEMY_DATABASE_URI = getDbURI(db_info)


class ProductionConfig(Config):
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Wanghe1351387884?",
        "NAME": "hello_flask"
    }
    SQLALCHEMY_DATABASE_URI = getDbURI(db_info)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
    "default": DevelopConfig
}
