from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date


db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "equipment_needed": self.equipment_needed,
        }

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("You must provide an exercise name.")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        if not value or not value.strip():
            raise ValueError("You must provide an exercise category.")
        return value.strip()
    


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "duration_minutes": self.duration_minutes,
            "exercise": self.exercise.to_dict() if self.exercise else None,
        }

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value is None or value <= 0:
            raise ValueError("Duration must be more than 0.")
        return value