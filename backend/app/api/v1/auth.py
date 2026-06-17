from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.auth_service import register_user
from app.database.dependencies import get_db

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    created_user = register_user(db, user)
    return {"id": created_user.id, "email": created_user.email}