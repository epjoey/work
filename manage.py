import app
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.inspection import inspect
import json

manager = Manager(app.app)
migrate = Migrate(app.app, app.db)
manager.add_command('db', MigrateCommand)

@manager.command
def clockin(project=''):
    app.clockin(project);

@manager.command
def clockout():
    app.clockout();

@manager.command
def history():
    for s in app.history():
        print s.id, s.time_in, s.time_out, s.project


if __name__ == '__main__':
    manager.run()