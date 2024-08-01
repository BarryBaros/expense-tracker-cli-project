import sys
import os

# Add the project's root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the models and Base after adjusting sys.path
from lib.models.base import Base
from lib.models.category import Category
from lib.models.expense import Expense

# Create the database engine
engine = create_engine('sqlite:///expense_tracker.db')

# Create tables
Base.metadata.create_all(engine)

print("Tables created successfully.")