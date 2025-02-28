from fastapi import APIRouter, Depends
from auth import get_current_user
from models import User

# Initialize Router
router = APIRouter(prefix="/services", tags=["Attendance"])

# Mocked Attendance Data for Each User with 7 Subjects
attendance_data = {
    "REG1001": {
        "faculty_name": "Dr. John Doe",
        "section": "A",
        "roll_number": "BCA101",
        "overall_percentage": 90,
        "subjects": [
            {"subject": "Data Structures", "last_class_attended": "2024-06-15", "duty_leaves": 2, "attendance_percentage": 92},
            {"subject": "Algorithms", "last_class_attended": "2024-06-14", "duty_leaves": 1, "attendance_percentage": 88},
            {"subject": "Database Systems", "last_class_attended": "2024-06-13", "duty_leaves": 0, "attendance_percentage": 95},
            {"subject": "Operating Systems", "last_class_attended": "2024-06-12", "duty_leaves": 1, "attendance_percentage": 89},
            {"subject": "Computer Networks", "last_class_attended": "2024-06-11", "duty_leaves": 2, "attendance_percentage": 90},
            {"subject": "Software Engineering", "last_class_attended": "2024-06-10", "duty_leaves": 0, "attendance_percentage": 94},
            {"subject": "Artificial Intelligence", "last_class_attended": "2024-06-09", "duty_leaves": 1, "attendance_percentage": 85}
        ]
    },
    "REG1002": {
        "faculty_name": "Prof. Alice Smith",
        "section": "B",
        "roll_number": "BCA102",
        "overall_percentage": 85,
        "subjects": [
            {"subject": "Data Structures", "last_class_attended": "2024-06-14", "duty_leaves": 1, "attendance_percentage": 87},
            {"subject": "Algorithms", "last_class_attended": "2024-06-13", "duty_leaves": 2, "attendance_percentage": 80},
            {"subject": "Database Systems", "last_class_attended": "2024-06-12", "duty_leaves": 0, "attendance_percentage": 90},
            {"subject": "Operating Systems", "last_class_attended": "2024-06-11", "duty_leaves": 1, "attendance_percentage": 83},
            {"subject": "Computer Networks", "last_class_attended": "2024-06-10", "duty_leaves": 2, "attendance_percentage": 86},
            {"subject": "Software Engineering", "last_class_attended": "2024-06-09", "duty_leaves": 1, "attendance_percentage": 89},
            {"subject": "Artificial Intelligence", "last_class_attended": "2024-06-08", "duty_leaves": 0, "attendance_percentage": 82}
        ]
    }
}

@router.get("/attendance")
def get_attendance(user: User = Depends(get_current_user)):
    return attendance_data.get(user.registration_number, {
        "faculty_name": "N/A",
        "section": "N/A",
        "roll_number": "N/A",
        "overall_percentage": 0,
        "subjects": []
    })
