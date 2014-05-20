from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work.db'
db = SQLAlchemy(app)

class Shift(db.Model):
    __tablename__ = 'shift'
    id = db.Column(db.Integer, primary_key=True)
    time_in = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    time_out = db.Column(db.DateTime)
    project = db.Column(db.String(80))


def clockin(project):
    last_shift = Shift.query.order_by(Shift.id.desc()).first()
    if last_shift and not last_shift.time_out:
        last_shift.time_out = datetime.datetime.utcnow()
    if not project:
        project = last_shift.project
    new_shift = Shift(project=project)
    db.session.add(new_shift)
    db.session.commit()
    pass

def history():
    return Shift.query.all()

def clockout():
    last_shift = Shift.query.order_by(Shift.id.desc()).first()
    if not last_shift:
        print "You have not started a shift yet"
    if last_shift.time_out:
        print "You already clocked out or you forgot to clockin"
    last_shift.time_out = datetime.datetime.utcnow()
    db.session.commit()
    pass