import datetime
import hashlib
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import func

from model.user import User
from model.user_domain import UserDomain
from model.user_env import UserEnv
from repository.user_repository import UserRepository


class UserService:
    def create(self) -> User:
        user_repository = UserRepository()
        password = str(uuid.uuid4()) # random str
        project_id = uuid.uuid4() # random str
        user = User(
            created_ad=datetime.now(timezone.utc),
            login="testLogin" + str(user_repository.count()),
            password=hashlib.sha256(password.encode('utf-8')).hexdigest(),
            project_id=project_id,
            env=UserEnv.STAGE,
            domain=UserDomain.CANARY
        )

        return user_repository.create(user)

    def get_users(self):
        user_repository = UserRepository()
        return user_repository.get_users()

    def lock_time(self, user_id):
        user_repository = UserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            raise HTTPException(
            status_code=404,
            detail=f"User with id '{user_id}' not found")

        if user.locktime is not None:
            raise HTTPException(
            status_code=409,
            detail=f"Lock for user with id '{user_id}' is already acquired"
                )

        user_repository.update_lock_time(user_id, func.now())

    def release_lock(self, user_id):
        user_repository = UserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail=f"User with id '{user_id}' not found")

        if user.locktime is None:
            raise HTTPException(
                status_code=409,
                detail=f"Lock for user with id '{user_id}' is already released"
            )

        user_repository.update_lock_time(user_id, None)

