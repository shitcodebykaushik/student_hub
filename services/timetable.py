from fastapi import APIRouter, Depends
from auth import get_current_user
from models import User

# Initialize Router
router = APIRouter(prefix="/services", tags=["Timetable"])

# Mocked Timetable Data (Monday - Saturday, 9 AM to 5 PM)
timetable_data = {
    "BCA": {
        "Monday": [
            {"time": "9:00 AM - 10:00 AM", "lecture": "Dr. Smith", "subject": "Data Structures", "room": "CAP 512"},
            {"time": "10:00 AM - 11:00 AM", "lecture": "Prof. Johnson", "subject": "Algorithms", "room": "CAP 512"},
            {"time": "11:00 AM - 12:00 PM", "lecture": "Dr. Brown", "subject": "Database Systems", "room": "CAP 512"},
            {"time": "1:00 PM - 2:00 PM", "lecture": "Prof. Green", "subject": "Operating Systems", "room": "CAP 512"},
            {"time": "2:00 PM - 3:00 PM", "lecture": "Dr. White", "subject": "Computer Networks", "room": "CAP 512"},
            {"time": "3:00 PM - 4:00 PM", "lecture": "Prof. Black", "subject": "Software Engineering", "room": "CAP 512"},
            {"time": "4:00 PM - 5:00 PM", "lecture": "Dr. Gray", "subject": "Artificial Intelligence", "room": "CAP 512"}
        ],
        "Tuesday": [
            {"time": "9:00 AM - 10:00 AM", "lecture": "Prof. Adams", "subject": "Cyber Security", "room": "CAP 512"},
            {"time": "10:00 AM - 11:00 AM", "lecture": "Dr. James", "subject": "Data Structures", "room": "CAP 512"},
            {"time": "11:00 AM - 12:00 PM", "lecture": "Prof. Green", "subject": "Algorithms", "room": "CAP 512"},
            {"time": "1:00 PM - 2:00 PM", "lecture": "Dr. Smith", "subject": "Operating Systems", "room": "CAP 512"},
            {"time": "2:00 PM - 3:00 PM", "lecture": "Prof. Johnson", "subject": "Computer Networks", "room": "CAP 512"},
            {"time": "3:00 PM - 4:00 PM", "lecture": "Dr. Brown", "subject": "Software Engineering", "room": "CAP 512"},
            {"time": "4:00 PM - 5:00 PM", "lecture": "Prof. White", "subject": "Artificial Intelligence", "room": "CAP 512"}
        ],
        "Wednesday": [
            {"time": "9:00 AM - 10:00 AM", "lecture": "Dr. Gray", "subject": "Database Systems", "room": "CAP 512"},
            {"time": "10:00 AM - 11:00 AM", "lecture": "Prof. Black", "subject": "Cyber Security", "room": "CAP 512"},
            {"time": "11:00 AM - 12:00 PM", "lecture": "Dr. Adams", "subject": "Data Structures", "room": "CAP 512"},
            {"time": "1:00 PM - 2:00 PM", "lecture": "Prof. James", "subject": "Algorithms", "room": "CAP 512"},
            {"time": "2:00 PM - 3:00 PM", "lecture": "Dr. Green", "subject": "Operating Systems", "room": "CAP 512"},
            {"time": "3:00 PM - 4:00 PM", "lecture": "Prof. Smith", "subject": "Computer Networks", "room": "CAP 512"},
            {"time": "4:00 PM - 5:00 PM", "lecture": "Dr. Brown", "subject": "Software Engineering", "room": "CAP 512"}
        ],
        "Thursday": [
            {"time": "9:00 AM - 10:00 AM", "lecture": "Prof. White", "subject": "Artificial Intelligence", "room": "CAP 512"},
            {"time": "10:00 AM - 11:00 AM", "lecture": "Dr. Black", "subject": "Cyber Security", "room": "CAP 512"},
            {"time": "11:00 AM - 12:00 PM", "lecture": "Prof. Adams", "subject": "Database Systems", "room": "CAP 512"},
            {"time": "1:00 PM - 2:00 PM", "lecture": "Dr. James", "subject": "Algorithms", "room": "CAP 512"},
            {"time": "2:00 PM - 3:00 PM", "lecture": "Prof. Green", "subject": "Operating Systems", "room": "CAP 512"},
            {"time": "3:00 PM - 4:00 PM", "lecture": "Dr. Smith", "subject": "Computer Networks", "room": "CAP 512"},
            {"time": "4:00 PM - 5:00 PM", "lecture": "Prof. Brown", "subject": "Software Engineering", "room": "CAP 512"}
        ],
        "Friday": [
            {"time": "9:00 AM - 10:00 AM", "lecture": "Dr. Adams", "subject": "Cyber Security", "room": "CAP 512"},
            {"time": "10:00 AM - 11:00 AM", "lecture": "Prof. Smith", "subject": "Data Structures", "room": "CAP 512"},
            {"time": "11:00 AM - 12:00 PM", "lecture": "Dr. Johnson", "subject": "Algorithms", "room": "CAP 512"},
            {"time": "1:00 PM - 2:00 PM", "lecture": "Prof. Brown", "subject": "Operating Systems", "room": "CAP 512"},
            {"time": "2:00 PM - 3:00 PM", "lecture": "Dr. Green", "subject": "Computer Networks", "room": "CAP 512"},
            {"time": "3:00 PM - 4:00 PM", "lecture": "Prof. White", "subject": "Software Engineering", "room": "CAP 512"},
            {"time": "4:00 PM - 5:00 PM", "lecture": "Dr. Gray", "subject": "Artificial Intelligence", "room": "CAP 512"}
        ],
        "Saturday": [
            {"time": "9:00 AM - 12:00 PM", "lecture": "Workshop", "subject": "Project Work", "room": "Lab 101"},
            {"time": "1:00 PM - 3:00 PM", "lecture": "Seminar", "subject": "Industry Trends", "room": "Auditorium"},
            {"time": "3:00 PM - 5:00 PM", "lecture": "Dr. Smith", "subject": "Research Topics", "room": "CAP 512"}
        ]
    }
}

@router.get("/timetable")
def get_timetable(user: User = Depends(get_current_user)):
    return timetable_data.get(user.course, {"message": "Timetable not available for your course"})
