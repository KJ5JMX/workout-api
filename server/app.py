from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from server.models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.get("/")
def home():
    return make_response({"status": "ok"}, 200)



if __name__ == "__main__":
    app.run(port=5555, debug=True)


