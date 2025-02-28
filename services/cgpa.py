from fastapi import APIRouter, Depends
from auth import get_current_user
from models import User

# Initialize Router
router = APIRouter(prefix="/services", tags=["CGPA"])

# Mocked CGPA Data for Each User with 8 Semesters
cgpa_data = {
    "REG1001": {
        "semesters": {
            "Semester 1": 70,
            "Semester 2": 80,
            "Semester 3": 60,
            "Semester 4": 75,
            "Semester 5": 85,
            "Semester 6": 78,
            "Semester 7": 82,
            "Semester 8": 90
        },
        "overall_performance": sum([70, 80, 60, 75, 85, 78, 82, 90]) / 8  # Average of all semesters
    },
    "REG1002": {
        "semesters": {
            "Semester 1": 65,
            "Semester 2": 75,
            "Semester 3": 70,
            "Semester 4": 68,
            "Semester 5": 80,
            "Semester 6": 85,
            "Semester 7": 78,
            "Semester 8": 88
        },
        "overall_performance": sum([65, 75, 70, 68, 80, 85, 78, 88]) / 8
    }
}

@router.get("/cgpa")
def get_cgpa(user: User = Depends(get_current_user)):
    return cgpa_data.get(user.registration_number, {
        "semesters": {},
        "overall_performance": 0
    })
