from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category")

    def __repr__(self):
        return f"<Budget(id={self.id}, amount={self.amount})>"
