from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise
from datetime import date


def seed():
    print("Seeding database...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=True
    )

    bench = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    pullup = Exercise(
        name="Pull-up",
        category="Bodyweight",
        equipment_needed=False
    )

    db.session.add_all([squat, bench, pullup])
    db.session.commit()

    workout = Workout(
        date=date.today(),
        duration_minutes=60,
        notes="Push day"
    )

    db.session.add(workout)
    db.session.commit()

    we1 = WorkoutExercise(
        workout=workout,
        exercise=bench,
        sets=4,
        reps=8,
        weight=185
    )

    we2 = WorkoutExercise(
        workout=workout,
        exercise=pullup,
        sets=3,
        reps=10
    )

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Seed complete.")


if __name__ == "__main__":
    with app.app_context():
        seed()