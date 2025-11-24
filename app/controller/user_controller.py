from fastapi import APIRouter, HTTPException

from app.service.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get():
    user_service = UserService()
    return user_service.get_users()


@router.post("/")
def create():
    user_service = UserService()
    return user_service.create()


@router.put("/acquire/{user_id}")
def acquire_lock(user_id: str):
    user_service = UserService()
    user_service.lock_time(user_id)


@router.put("/release/{user_id}")
def release_lock(user_id: str):
    user_service = UserService()
    user_service.release_lock(user_id)
