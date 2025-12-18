# Flask SQLAlchemy Workout API

This project is a Flask backend application for tracking workouts and exercises.  
It uses Flask, Flask-SQLAlchemy, and Flask-Migrate to model workouts, exercises, and their relationships.

The API supports viewing exercises, workouts, and detailed workout data including sets, reps, and weights.

---

## Features

- Exercises with categories and equipment requirements
- Workouts with duration, date, and notes
- Many-to-many relationship between workouts and exercises via a join table
- Nested JSON serialization
- Database migrations
- Seed script to populate starter data

---

## Tech Stack

- Python 3.8
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Pipenv

---

## Project Structure

workout-api/
├── server/
│ ├── init.py
│ ├── app.py
│ ├── models.py
│ ├── seed.py
│ └── workout.db
├── migrations/
├── Pipfile
├── Pipfile.lock
└── README.md

---

## Setup Instructions

### 1. Install dependencies

```bash
pipenv install
pipenv shell
flask --app server.app db upgrade
python -m server.seed

flask --app server.app run


```
