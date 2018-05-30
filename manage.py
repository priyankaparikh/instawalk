from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import server

migrate = Migrate(server.app, server.db)

manager = Manager(server.app)
manager.add_command('server.db', MigrateCommand)


if __name__ == '__main__':
    manager.run()