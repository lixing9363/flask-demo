import os
import logging
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


def init_logger():
    log_dir = os.path.join(basedir, '..', 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    # 创建日期日志文件
    log_path = os.path.join(log_dir, f'{datetime.now().strftime("%Y-%m-%d")}.log')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    # 日志同时在控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console.setFormatter(formatter)
    logger.addHandler(console)
    # 日志同时保存到文件
    logger.addHandler(handler)
    return logger


logger = init_logger()


def create_app(config_name):
    configer = config[config_name]
    # 创建Flask实例
    app = Flask(__name__)
    app.config['SECRET_KEY'] = configer.SECRET_KEY
    # 配置SQLAlchemy数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = configer.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configer.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

    logger.info(f"configer: {configer}")

    # 日志
    app.logger = logger

    # 注册蓝图
    # from apps.app1 import app1_bp
    from apps.app1.views import app1_bp
    app.register_blueprint(app1_bp)
    return app
