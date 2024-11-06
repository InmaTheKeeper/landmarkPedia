from .base import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(VARCHAR, nullable=False)
    street = Column(VARCHAR, nullable=True)
    house_num = Column(VARCHAR, nullable=True)

    landmark = relationship("Landmark", uselist=False, back_populates="address")

    def __repr__(self):
        return f"<Adress(id={self.id}, city='{self.city}', street='{self.street}', house={self.house_num})>"
