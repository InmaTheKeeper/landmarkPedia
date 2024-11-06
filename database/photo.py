from .base import Base
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    landmark_id = Column(Integer, ForeignKey("landmarks.id"), nullable=False)
    url = Column(VARCHAR, nullable=False)
    descr = Column(VARCHAR, nullable=True)

    def __repr__(self):
        return f"<Photo(id={self.id}, url='{self.url}', descr='{self.descr}')>"
