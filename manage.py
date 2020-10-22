from flask_migrate import MigrateCommand
import os;os.environ['FLASK_ENV'] = "develop"  # 指定环境变量
from flask_script import Manager
from App import create_app


env = os.environ.get("FLASK_ENV", "develop")
app = create_app(env)
manage = Manager(app=app)


manage.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manage.run()
