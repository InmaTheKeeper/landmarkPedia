from .base import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)

    # Relationship to the LandmarkCategory junction table
    landmarks = relationship("LandmarkCategory", back_populates="category")

    # Access to the actual Landmark objects
    landmark_list = relationship("Landmark", secondary="landmark_categories", back_populates="categories")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
