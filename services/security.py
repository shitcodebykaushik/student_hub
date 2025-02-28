from fastapi import APIRouter


router = APIRouter(prefix="/services", tags=["Security"])


security_officers = [
    {"name": "Officer John Doe", "uid_number": "SEC1001", "emergency_contact": "+91 9876543210", "image_url": "https://example.com/images/officer1.jpg", "position": "Security Guard"},
    {"name": "Officer Jane Smith", "uid_number": "SEC1002", "emergency_contact": "+91 8765432109", "image_url": "https://example.com/images/officer2.jpg", "position": "Female Security Guard"},
    {"name": "Officer Mark Brown", "uid_number": "SEC1003", "emergency_contact": "+91 7654321098", "image_url": "https://example.com/images/officer3.jpg", "position": "Security Supervisor"},
    {"name": "Officer Emma White", "uid_number": "SEC1004", "emergency_contact": "+91 8543210987", "image_url": "https://example.com/images/officer4.jpg", "position": "Female Security Guard"},
    {"name": "Officer Robert Black", "uid_number": "SEC1005", "emergency_contact": "+91 9123456780", "image_url": "https://example.com/images/officer5.jpg", "position": "Security Guard"},
    {"name": "Officer Olivia Green", "uid_number": "SEC1006", "emergency_contact": "+91 9234567891", "image_url": "https://example.com/images/officer6.jpg", "position": "Female Security Guard"},
    {"name": "Officer William Adams", "uid_number": "SEC1007", "emergency_contact": "+91 9345678902", "image_url": "https://example.com/images/officer7.jpg", "position": "Security Guard"},
    {"name": "Officer Sophia Brown", "uid_number": "SEC1008", "emergency_contact": "+91 9456789013", "image_url": "https://example.com/images/officer8.jpg", "position": "Female Security Guard"},
    {"name": "Officer Daniel Gray", "uid_number": "SEC1009", "emergency_contact": "+91 9567890124", "image_url": "https://example.com/images/officer9.jpg", "position": "Security Guard"},
    {"name": "Officer Isabella Blue", "uid_number": "SEC1010", "emergency_contact": "+91 9678901235", "image_url": "https://example.com/images/officer10.jpg", "position": "Female Security Guard"}
]

@router.get("/security")
def get_security_details():
    return {"security_officers": security_officers}
