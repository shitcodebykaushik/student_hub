from fastapi import APIRouter, Depends
from auth import get_current_user
from models import User

# Initialize Router
router = APIRouter(prefix="/services", tags=["Study Materials"])

# Mocked Study Materials Data with 8 Books per Course
study_materials = {
    "BCA": [
        {"title": "Introduction to Programming", "pdf_link": "https://example.com/programming.pdf"},
        {"title": "Data Structures", "pdf_link": "https://example.com/data-structures.pdf"},
        {"title": "Database Systems", "pdf_link": "https://example.com/database.pdf"},
        {"title": "Operating Systems", "pdf_link": "https://example.com/os.pdf"},
        {"title": "Computer Networks", "pdf_link": "https://example.com/networks.pdf"},
        {"title": "Software Engineering", "pdf_link": "https://example.com/software-engineering.pdf"},
        {"title": "Artificial Intelligence", "pdf_link": "https://example.com/ai.pdf"},
        {"title": "Cyber Security", "pdf_link": "https://example.com/cyber-security.pdf"}
    ],
    "BTech": [
        {"title": "Thermodynamics", "pdf_link": "https://example.com/thermodynamics.pdf"},
        {"title": "Fluid Mechanics", "pdf_link": "https://example.com/fluid-mechanics.pdf"},
        {"title": "Strength of Materials", "pdf_link": "https://example.com/strength.pdf"},
        {"title": "Machine Design", "pdf_link": "https://example.com/machine-design.pdf"},
        {"title": "Electrical Engineering", "pdf_link": "https://example.com/electrical.pdf"},
        {"title": "Electronics", "pdf_link": "https://example.com/electronics.pdf"},
        {"title": "Embedded Systems", "pdf_link": "https://example.com/embedded.pdf"},
        {"title": "Robotics", "pdf_link": "https://example.com/robotics.pdf"}
    ],
    "MBA": [
        {"title": "Business Strategy", "pdf_link": "https://example.com/business-strategy.pdf"},
        {"title": "Marketing Management", "pdf_link": "https://example.com/marketing.pdf"},
        {"title": "Financial Accounting", "pdf_link": "https://example.com/accounting.pdf"},
        {"title": "Human Resource Management", "pdf_link": "https://example.com/hr.pdf"},
        {"title": "Operations Management", "pdf_link": "https://example.com/operations.pdf"},
        {"title": "Entrepreneurship", "pdf_link": "https://example.com/entrepreneurship.pdf"},
        {"title": "Business Analytics", "pdf_link": "https://example.com/analytics.pdf"},
        {"title": "Corporate Law", "pdf_link": "https://example.com/corporate-law.pdf"}
    ],
    "Fashion": [
        {"title": "Fashion Design Basics", "pdf_link": "https://example.com/fashion-design.pdf"},
        {"title": "Textile Technology", "pdf_link": "https://example.com/textile.pdf"},
        {"title": "Fashion Illustration", "pdf_link": "https://example.com/illustration.pdf"},
        {"title": "Garment Manufacturing", "pdf_link": "https://example.com/garment.pdf"},
        {"title": "Pattern Making", "pdf_link": "https://example.com/pattern-making.pdf"},
        {"title": "Fashion Marketing", "pdf_link": "https://example.com/fashion-marketing.pdf"},
        {"title": "Textile Chemistry", "pdf_link": "https://example.com/textile-chemistry.pdf"},
        {"title": "Sustainable Fashion", "pdf_link": "https://example.com/sustainable-fashion.pdf"}
    ],
    "BioTech": [
        {"title": "Genetics Research", "pdf_link": "https://example.com/genetics.pdf"},
        {"title": "Biotechnology Basics", "pdf_link": "https://example.com/biotech.pdf"},
        {"title": "Microbiology", "pdf_link": "https://example.com/microbiology.pdf"},
        {"title": "Genetic Engineering", "pdf_link": "https://example.com/genetic-engineering.pdf"},
        {"title": "Biopharmaceuticals", "pdf_link": "https://example.com/biopharma.pdf"},
        {"title": "Bioinformatics", "pdf_link": "https://example.com/bioinformatics.pdf"},
        {"title": "Environmental Biotechnology", "pdf_link": "https://example.com/environmental.pdf"},
        {"title": "Biomedical Engineering", "pdf_link": "https://example.com/biomedical.pdf"}
    ]
}

@router.get("/materials")
def get_study_materials(user: User = Depends(get_current_user)):
    return study_materials.get(user.course, [{"title": "No materials available", "pdf_link": "#"}])
