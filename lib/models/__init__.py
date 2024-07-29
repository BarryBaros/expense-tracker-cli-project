from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///expenses.db')
Session = sessionmaker(bind=engine)

# Import models to ensure they are registered with Base
from .category import Category
from .expense import Expense
from .budget import Budget
from .base import Base
