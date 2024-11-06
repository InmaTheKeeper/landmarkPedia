from .base import Base
from sqlalchemy import Column, Integer, Text, VARCHAR, ForeignKey


class HistoricalReference(Base):
    __tablename__ = 'hreferences'

    id = Column(Integer, primary_key=True)
    landmark_id = Column(Integer, ForeignKey("landmarks.id"), nullable=False)
    content = Column(Text, nullable=False)
    year = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return f"<Reference(id={self.id}, content='{self.content}', year='{self.year}')>"
