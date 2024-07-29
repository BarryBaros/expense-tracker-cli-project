from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from . import Base

class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category = relationship("Category")

    def __repr__(self):
        return f"<Budget(id={self.id}, amount={self.amount})>"