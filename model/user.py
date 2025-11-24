import uuid

from sqlalchemy import Column, DateTime, String, UUID, text

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=text('NOW()'))
    login = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    project_id = Column(UUID(as_uuid=True), nullable=False)
    env = Column(String(50), nullable=False)
    domain = Column(String(50), nullable=False)
    locktime = Column(DateTime(timezone=True), nullable=True)

    def repr(self):
        return f"<User(id={self.id}, created_at='{self.created_at}', login='{self.login}, " \
               f"password={self.password}, project_id='{self.project_id}', " \
               f"env='{self.env}, domain={self.domain}, locktime='{self.locktime}')>"
