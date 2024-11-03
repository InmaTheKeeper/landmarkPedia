from sqlalchemy import create_engine, Column, Integer, String, Text, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, foreign, relationship

# Define a base class for our classes
Base = declarative_base()


class Landmark(Base):
    __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    address_id = Column(Integer, ForeignKey("adresses.id"), unique=True, nullable=True)
    name = Column(VARCHAR, nullable=False)
    descr = Column(Text, nullable=False)
    history = Column(Text, nullable=False)

    # Relationships
    address = relationship("Address", back_populates="landmark")
    photos = relationship("Photo", backref="landmark")
    history_refs = relationship("HistoricalReference", backref="landmark")

    # Relationship to the LandmarkCategory junction table
    categories = relationship("LandmarkCategory", back_populates="landmark")

    # Access to the actual Category objects
    category_list = relationship("Category", secondary="landmark_categories", back_populates="landmarks")

    def __repr__(self):
        return f"<Landmark(id={self.id}, name='{self.name}', descr='{self.descr}', history={self.history})>"


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


class LandmarkCategory(Base):
    __tablename__ = 'landmark_categories'

    landmark_id = Column(Integer, ForeignKey("landmarks.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)

    def __repr__(self):
        return f"<LandmarkCategory(landmark_id={self.landmark_id}, category_id={self.category_id})>"


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(VARCHAR, nullable=False)
    street = Column(VARCHAR, nullable=True)
    house_num = Column(VARCHAR, nullable=True)

    landmark = relationship("Landmark", uselist=False, back_populates="address")

    def __repr__(self):
        return f"<Adress(id={self.id}, city='{self.city}', street='{self.street}', house={self.house_num})>"


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    landmark_id = Column(Integer, ForeignKey("landmarks.id"), nullable=False)
    url = Column(VARCHAR, nullable=False)
    descr = Column(VARCHAR, nullable=True)

    def __repr__(self):
        return f"<Photo(id={self.id}, url='{self.url}', descr='{self.descr}')>"


class HistoricalReference(Base):
    __tablename__ = 'hreferences'

    id = Column(Integer, primary_key=True)
    landmark_id = Column(Integer, ForeignKey("landmarks.id"), nullable=False)
    content = Column(Text, nullable=False)
    year = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return f"<Reference(id={self.id}, content='{self.content}', year='{self.year}')>"
