from airPollution import app,db
from airPollution.model import User
@app.route('/')
def index():
    admin = User('admin')
    db.session.add(admin)
    db.session.commit()
    return "hello"