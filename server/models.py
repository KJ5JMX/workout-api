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

    #relationship
    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise", cascade="all, delete-orphan")

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
    
    @property
    def workouts(self):
        return [we.workout for we in self.workout_exercises]
    


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
            "notes": self.notes,
            "exercises": [we.to_dict() for we in self.workout_exercises]
        }
    
    #relationship
    workout_exercises = db.relationship("WorkoutExercise", back_populates="workout", cascade="all, delete-orphan")

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value is None or value <= 0:
            raise ValueError("Duration must be more than 0.")
        return value
    
    @property
    def exercises(self):
        return [we.exercise for we in self.workout_exercises]
    

class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)
    duration_seconds = db.Column(db.Integer)

    def to_dict(self):
        return { 
            "id": self.id,
            "sets": self.sets,
            "reps": self.reps,
            "weight": self.weight,
            "duration_seconds": self.duration_seconds,
            "exercise": self.exercise.to_dict()
        
        }

    #adding relationships
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    @validates("sets", "reps")
    def validate_positive_ints(self, key, value):
        if value is None or value <= 0:
            raise ValueError(f"{key} must be more than 0.")
        return value
    
    @validates("weight", "duration_seconds")
    def validate_optional_positive(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be positive if provided.")
        return value