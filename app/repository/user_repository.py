
from sqlalchemy import func

from app.database import session
from app.model.user import User


class UserRepository:

    def count(self) -> int:
        try:
            count = session.query(func.count(User.id)).scalar()
            return count or 0
        except Exception as e:
            print(f"Error getting users count: {e}")
            return 0

    def create(self, user: User) -> User:

        try:

            session.add(user)
            session.commit()
            session.refresh(user)

            return user

        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

    def get_users(self):
        try:
            users = session.query(User).all()
            return users
        except Exception as e:
            print(f"Error getting users: {e}")
            return []


