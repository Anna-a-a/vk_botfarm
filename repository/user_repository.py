
from sqlalchemy import func

from database import session
from model.user import User


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
            print(f"Error getting users count: {e}")
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
        finally:
            session.close()

    def update_lock_time(self, user_id: str, value) -> User:
        try:
            user = session.query(User).filter(User.id == user_id).first()
            user.locktime = value
            session.commit()
            session.refresh(user)

            return user
        except Exception as e:
            session.rollback()
            print(f"Error setting lock time: {e}")
        finally:
            session.close()

    def get_user_by_id(self, user_id: str) -> User:
        try:
            return session.query(User).filter(User.id == user_id).first()
        except Exception as e:
            print(f"Error getting user: {e}")
            return None
        finally:
            session.close()


