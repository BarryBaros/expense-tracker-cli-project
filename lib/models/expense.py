from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from lib.models.base import Base
from datetime import date

# Define the Expense class to map the to table in the database
class Expense(Base):
    __tablename__ = 'expenses' # Table name in the database

# Class attirbutes
    id = Column(Integer, primary_key=True)  #Primary Key
    amount = Column(Float, nullable=False)  #Amount of expenses, cannot be null
    category_id = Column(Integer, ForeignKey('categories.id'))  #Foreign Key
    date = Column(Date, nullable=False) #Date of the expense, cannot be null

    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return (f"<Expense(id={self.id}, amount={self.amount}, "
                f"category_id={self.category_id}, date={self.date})>")