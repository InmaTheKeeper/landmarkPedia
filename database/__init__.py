from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .base import Base

from .category import Category
from .historical_reference import HistoricalReference
from .landmark import Landmark
from .landmark_category import LandmarkCategory
from .photo import Photo

engine = create_engine("postgresql+psycopg2://postgres@localhost:5432/postgres")
Session = sessionmaker(engine)
Base.metadata.create_all(engine)
