from fastapi import FastAPI, Depends
from auth import router as auth_router, get_current_user
from models import User
from services.attendance import router as attendance_router
from services.cgpa import router as cgpa_router
from services.exam import router as exams_router  # ✅ Fixed import (was `exam.py`, now `exams.py`)
from services.materials import router as materials_router
from services.timetable import router as timetable_router
from services.announcements import router as announcements_router
from services.security import router as security_router  # ✅ Added Security Service
from services.public_info import router as public_info_router
# Initialize FastAPI app
app = FastAPI()

# Include authentication and services routes
app.include_router(auth_router)
app.include_router(attendance_router)
app.include_router(cgpa_router)
app.include_router(exams_router)  # ✅ Ensure Exams is included
app.include_router(materials_router)
app.include_router(timetable_router)  # ✅ Ensure Timetable is included
app.include_router(announcements_router)
app.include_router(security_router)  # ✅ Ensure Security Service is included
app.include_router(public_info_router) 
# ✅ Ensure `/user/details` is defined
@app.get("/user/details", tags=["User"])
def get_user_details(user: User = Depends(get_current_user)):
    return {
        "name": user.name,
        "registration_number": user.registration_number,
        "course": user.course,
        "phone": user.phone,
        "residence": user.residence
    }

@app.get("/")
def home():
    return {"message": "StudentHub API is running!"}
