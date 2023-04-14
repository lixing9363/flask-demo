import os
import logging
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

log_dir = os.path.join(basedir, '..', 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
# 创建日期日志文件
log_path = os.path.join(log_dir, f'{datetime.now().strftime("%Y-%m-%d")}.log')

def create_app(config_name):
    configer = config[config_name]
    # 创建Flask实例
    app = Flask(__name__)
    app.config['SECRET_KEY'] = configer.SECRET_KEY
    # 配置SQLAlchemy数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = configer.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configer.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

    # 配置日志
    app.logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app.logger.addHandler(handler)

    # 注册蓝图
    # from apps.app1 import app1_bp
    from apps.app1.views import app1_bp
    app.register_blueprint(app1_bp)
    return app
