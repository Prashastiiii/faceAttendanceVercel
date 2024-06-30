import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Ensure this path is correct and the file exists
cred = credentials.Certificate("serviceAccountKey.json")

# Corrected key for database URL
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendancerealtime-38803-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12": {
        "name": "Prashasti Rai",
        "Major": "IT",
        "starting_year": 2022,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-11 00:54:34"
    },
    "23": {
        "name": "Pranshi Rai",
        "Major": "GEO",
        "starting_year": 2018,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-11 00:54:50"
    },
    "34": {
        "name": "Seema Rai",
        "Major": "HISTORY",
        "starting_year": 1990,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-11 00:57:37"
    },
    "45": {
        "name": "Elon Musk",
        "Major": "IT",
        "starting_year": 1990,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-05-11 00:40:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
