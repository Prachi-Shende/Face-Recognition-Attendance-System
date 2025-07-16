import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceattendancerealtime-bae9f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1": {
        "name": "Prachi Shende",
        "major": "Computer Engineering",
        "starting_year": 2017,
        "total_attendance": 10,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2020-06-26 00:54:34"
    },
    "2": {
        "name": "Emily Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2020-06-26 00:54:34"
    },
    "3": {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2020-06-26 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
