from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get():
    return {"users": ["user1", "user2"]}


@router.post("/")
def create():
    return "1"


@router.put("/acquire/{user_id}")
def acquire_lock(user_id: str):
    raise HTTPException(
        status_code=409,
        detail=f"Lock for user with id:'{user_id}' is already acquired"
    )


@router.put("/release/{user_id}")
def release_lock(user_id: str):
    print("her")