from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

# Define the Expense class to map the to table in the database
class Expense(Base):
    __tablename__ = 'expenses' # Table name in the database