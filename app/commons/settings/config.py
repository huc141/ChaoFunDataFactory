# -*- coding: utf-8 -*-
# @Time : 2023-06-11 12:49
# @Author : yulong
# @File : config.py

import os


# fastapi 启动配置文件
class Config(object):
    """配置类"""
    # 数据库连接信息
    HOST = "127.0.0.1"
    PORT = "3306"
    PWD = "123456"
    USER = "ROOT"
    DBNAME = "datafactory"
    PRO = False

    # 数据库配置
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DBNAME}"


class Text(object):
    """描述配置"""
    TITLE = "Fun数据工厂"
    VERSION = "V1.0"
    DESCRIPTION = "欢迎来到WEB测试组的数据工厂"
    # 类属性，表示 Redoc 文档的路径。它使用了一个条件表达式，如果 Config.PRO 为真，则将属性值设为 None，否则将属性值设为字符串 "/redoc"。这样做的目的是在生产环境中隐藏 Redoc 文档路径。
    REDOC = None if Config.PRO else "/redoc"
    DOC = None if Config.PRO else "/docs"
    OPENAPI = None if Config.PRO else "/openapi.json"


class FilePath(object):
    SETS_PATH = os.path.dirname(os.path.abspath(__file__)) # settings目录
    COM_path = os.path.dirname(os.path.abspath(SETS_PATH)) # commons目录
    APP_PATH = os.path.dirname(os.path.abspath(COM_path)) # app 路径
    BASE_DIR = os.path.dirname(os.path.abspath(APP_PATH)) # 后端服务项目目录

    LOG_FILE_PATH = os.path.join(BASE_DIR, "logs") # 日志文件路径
    if not os.path.isdir(LOG_FILE_PATH): os.mkdir(LOG_FILE_PATH)

    FUN_SERVER = os.path.join(LOG_FILE_PATH, 'fun_server.log')
    FUN_ERROR = os.path.join(LOG_FILE_PATH, 'fun_error.log')

    CRUD_PATH = os.path.join(APP_PATH, "crud") # crud路径
    
    KEYS_FILE_PATH = os.path.join(SETS_PATH, "keys") # keys路径
    if not os.path.isdir(KEYS_FILE_PATH): os.mkdir(KEYS_FILE_PATH)

    RSA_PUB_KEY = os.path.join(KEYS_FILE_PATH, "rsa_pub_key")

    RSA_PRI_KEY = os.path.join(KEYS_FILE_PATH, "rsa_pri_key")

HTTP_MSG_MAP = {
    404 : '请求路径找不到',
    405 : '请求方法不支持',
    408 : '请求超时',
    500 : '服务器内部错误',
    302 : '请求方法不支持'
}

API_WHITE_LIST = [
    '/docs',
    '/static',
    '/favicon.ico',
    '/openapi.json',
    '/redoc',
    '/api/user/register',
    '/api/user/login',
    '/api/cases/out',
    '/api/cases/rpc/',
    '/api/project/gitSync'
]

API_ADMIN_LIST = [
    '/api/user/update'
]

# 项目日志滚动配置（日志文件超过10 MB就自动新建文件扩充）
LOGGING_ROTATION = "10 MB"

# 项目日志配置
# FilePath.FUN_SERVER: 通过使用类名来访问属性，可以明确地表示属性所属的类，提高代码的可读性
LOGGING_CONF = {
    'server_handler': {
        'file': FilePath.FUN_SERVER,
        'level': 'INFO',
        'rotation': LOGGING_ROTATION,
        'enqueue': True,
        'backtrace': False,
        'diagnose': False,
    },
    'error_handler': {
        'file': FilePath.FUN_ERROR,
        'level': 'ERROR',
        'rotation': LOGGING_ROTATION,
        'enqueue': True,
        'backtrace': True,
        'diagnose': True,
    },
}