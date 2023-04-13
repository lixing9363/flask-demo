# 创建和迁移数据库表
from apps import db
from main import app
from flask_migrate import Migrate, upgrade

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        import os
        from flask_migrate import init, migrate

        if not os.path.exists('./migrations'):
            init()
        migrate()
        # 创建表结构
        db.create_all()
        # 运行迁移
        upgrade()
