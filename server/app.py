from flask import Flask, abort, make_response, jsonify
from flask_migrate import Migrate

from server.models import db, Exercise, Workout, WorkoutExercise

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.get("/")
def home():
    return make_response({"status": "ok"}, 200)


@app.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([e.to_dict() for e in exercises]), 200


@app.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([w.to_dict() for w in workouts]), 200



@app.get("/workouts/<int:id>")
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        abort(404, description="Workout not found")
    return jsonify(workout.to_dict()), 200
        



if __name__ == "__main__":
    app.run(port=5555, debug=True)


