from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import get_db
from models import User
from datetime import datetime, timedelta
from pydantic import BaseModel
import bcrypt

# Initialize Router
router = APIRouter()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Secret Key & Algorithm
SECRET_KEY = "your_secret_key_here"  # Change this to a secure key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Pydantic model for login request
class LoginRequest(BaseModel):
    registration_number: str
    password: str

# Function to verify password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

# Function to generate JWT token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Login endpoint
@router.post("/login")
def login(user_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.registration_number == user_data.registration_number).first()

    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid registration number or password")

    access_token = create_access_token(
        data={"sub": user.registration_number},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "token_type": "bearer"}

# Function to verify JWT token and get current user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        reg_number: str = payload.get("sub")
        if reg_number is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.registration_number == reg_number).first()
    if user is None:
        raise credentials_exception

    return user
