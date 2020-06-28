from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from bluelog import db
from bluelog.models import Admin, Category, Post, Comment, Link
# 在进行迁移时,必须导入模型,不然数据库不会改变


from bluelog import create_app  # noqa
app = create_app('production')
db.init_app(app)

manager = Manager(app)
# init  migrate upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()

