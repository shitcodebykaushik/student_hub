from fastapi import APIRouter, Depends
from auth import get_current_user
from models import User

# Initialize Router
router = APIRouter(prefix="/services", tags=["Exams"])

# ✅ Ensure exams_data is defined
exams_data = {
    "REG1001": [{"subject": "Math", "date": "2024-06-10"}, {"subject": "Science", "date": "2024-06-15"},{"subject": "Math", "date": "2024-06-10"},{"subject": "Math", "date": "2024-06-10"}],
    "REG1002": [{"subject": "Physics", "date": "2024-06-12"}, {"subject": "Chemistry", "date": "2024-06-18"}],
}

@router.get("/exams")
def get_exams(user: User = Depends(get_current_user)):
    return {"exams": exams_data.get(user.registration_number, "No exams scheduled")}

# ✅ Explicitly export exams_data
__all__ = ["router", "exams_data"]
