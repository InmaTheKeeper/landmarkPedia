from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LandmarkCategory(Base):
    __tablename__ = 'landmark_categories'

    landmark_id = Column(Integer, ForeignKey("landmarks.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)

    def __repr__(self):
        return f"<LandmarkCategory(landmark_id={self.landmark_id}, category_id={self.category_id})>"
