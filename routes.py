from fastapi import APIRouter
from app.database import db
from app.schemas import UserSchema

router = APIRouter()

@router.post("/users")
async def create_user(user: UserSchema):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id)}
