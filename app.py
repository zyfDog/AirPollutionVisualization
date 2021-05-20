from flask import Flask
import json

from model import Grade
app = Flask(__name__)


@app.route('/')
def hello_world():
    grades = Grade.query.all()
    print(grades)
    return json.dumps("{a:112}")


if __name__ == '__main__':
    app.run(debug=True)
