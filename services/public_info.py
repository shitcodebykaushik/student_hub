from fastapi import APIRouter, HTTPException
from models import User
from services.timetable import timetable_data
from services.exam import exams_data
from services.materials import study_materials
from database import SessionLocal

# Initialize Router
router = APIRouter(prefix="/public", tags=["Public Information"])

# Database session
db = SessionLocal()

@router.get("/{registration_number}")
def get_public_info(registration_number: str):
    # Fetch user details
    user = db.query(User).filter(User.registration_number == registration_number).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch relevant data
    timetable = timetable_data.get(user.course, "Timetable not available")
    exams = exams_data.get(user.course, "Exam details not available")
    materials = study_materials.get(user.course, "Study materials not available")

    return {
        "registration_number": registration_number,
        "course": user.course,
        "timetable": timetable,
        "exams": exams,
        "study_materials": materials
    }
