import sys
import os
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base
from lib.models.category import Category
from lib.models.expense import Expense

# Debugging information
print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

# Add the project's root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Create the database engine
engine = create_engine('sqlite:///expense_tracker.db')

# Drop all tables if they exist
Base.metadata.drop_all(engine)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Seed categories
    categories = [
        "Food",
        "Transport",
        "House Bills"
    ]

    # Only add categories if they do not already exist
    existing_categories = session.query(Category).all()
    existing_category_names = {cat.name for cat in existing_categories}

    for cat_name in categories:
        if cat_name not in existing_category_names:
            session.add(Category(name=cat_name))
    session.commit()

    # Query categories to get their IDs
    categories = session.query(Category).all()
    category_map = {cat.name: cat.id for cat in categories}

    # Seed expenses
    expenses = [
        (50.00, category_map["Food"], date(2023, 1, 1)),
        (30.00, category_map["Transport"], date(2023, 1, 2)),
        (100.00, category_map["House Bills"], date(2023, 1, 3))
    ]

    # Only add expenses if they do not already exist
    existing_expenses = session.query(Expense).all()
    existing_expenses_data = {(exp.amount, exp.category_id, exp.date) for exp in existing_expenses}

    for amount, cat_id, exp_date in expenses:
        if (amount, cat_id, exp_date) not in existing_expenses_data:
            session.add(Expense(amount=amount, category_id=cat_id, date=exp_date))
    session.commit()

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    session.close()

# Verification functions
def print_all_categories():
    session = Session()
    try:
        categories = session.query(Category).all()
        print("Categories:")
        for cat in categories:
            print(cat)
    finally:
        session.close()

def print_all_expenses():
    session = Session()
    try:
        expenses = session.query(Expense).all()
        print("Expenses:")
        for exp in expenses:
            print(exp)
    finally:
        session.close()

# Print the contents to verify
print_all_categories()
print_all_expenses()
