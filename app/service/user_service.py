import hashlib

from app.model.user import User
import datetime
import uuid
from datetime import datetime, timezone
from app.repository.user_repository import UserRepository


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
            env="stage", ## todo enum (prod, predprod, stage)
            domain="canary" ## canary, regular
        )

        return user_repository.create(user)

    def get_users(self):
        user_repository = UserRepository()
        return user_repository.get_users()
