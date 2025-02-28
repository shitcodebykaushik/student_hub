from fastapi import APIRouter

# Initialize Router
router = APIRouter(prefix="/services", tags=["Announcements"])

# Mocked Announcements Data
announcements = [
    {"date": "2024-06-01", "message": "Semester exams start on June 10"},
    {"date": "2024-06-05", "message": "Project submission deadline extended"},
]

@router.get("/announcements")
def get_announcements():
    return {"announcements": announcements}
