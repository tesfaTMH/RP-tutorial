from views import db, app
from models import Task
from datetime import date

# create database and db table by setting up an application context
app.app_context().push()
db.create_all()

# insert data

db.session.add(Task("Finish this tutorial", date(2024, 12, 12), 10, 1))
db.session.add(Task("Finish Real Python Course 2", date(2024, 12, 2), 10, 1))

# commit changes
db.session.commit()