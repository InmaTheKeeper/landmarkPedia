from .base import Base
from sqlalchemy import Column, Integer, Text, VARCHAR, Float
from sqlalchemy.orm import relationship


class Landmark(Base):
    __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    address = Column(Text, nullable=True)
    name = Column(VARCHAR, nullable=False)
    descr = Column(Text, nullable=False)
    history = Column(Text, nullable=False)
    latitude = Column(Float, nullable=True)
    longtitude = Column(Float, nullable=True)

    # Relationships
    photos = relationship("Photo", backref="landmark")
    history_refs = relationship("HistoricalReference", backref="landmark")

    # Relationship to the LandmarkCategory junction table
    categories = relationship("Category", secondary="landmark_categories", back_populates="landmarks")

    def __repr__(self):
        return f"<Landmark(id={self.id}, name='{self.name}', descr='{self.descr}', history={self.history})>"
