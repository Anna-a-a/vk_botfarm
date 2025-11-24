import uuid

from sqlalchemy import Column, DateTime, String, UUID, text, Enum

from database import Base
from model.user_domain import UserDomain
from model.user_env import UserEnv


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=text('NOW()'))
    login = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    project_id = Column(UUID(as_uuid=True), nullable=False)
    env = Column(Enum(UserEnv), nullable=False)
    domain = Column(Enum(UserDomain), nullable=False)
    locktime = Column(DateTime(timezone=True), nullable=True)

    def repr(self):
        return f"<User(id={self.id}, created_at='{self.created_at}', login='{self.login}, " \
               f"password={self.password}, project_id='{self.project_id}', " \
               f"env='{self.env}, domain={self.domain}, locktime='{self.locktime}')>"
