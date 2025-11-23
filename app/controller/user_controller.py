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
    # todo 1) lock update lock_time
    raise HTTPException(
        status_code=409,
        detail=f"Lock for user with id:'{user_id}' is already acquired"
    )


@router.put("/release/{user_id}")
def release_lock(user_id: str):
    # todo 2) (remove lock date)
    print("her")