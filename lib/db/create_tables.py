import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models.base import Base
from lib.models.category import Category
from lib.models.expense import Expense

# Create the database engine
engine = create_engine('sqlite:///expense_tracker.db')

# Create tables
Base.metadata.create_all(engine)

print("Tables created successfully.")