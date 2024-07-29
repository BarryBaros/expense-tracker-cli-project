from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date
from lib.models import Base, Category, Expense, Budget

# Connect to the SQLite database
engine = create_engine('sqlite:///expense.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ensure the database schema is created
Base.metadata.create_all(engine)

# Function to add a category if it doesn't exist
def add_category_if_not_exists(session, category_name):
    existing_category = session.query(Category).filter_by(name=category_name).first()
    if not existing_category:
        new_category = Category(name=category_name)
        session.add(new_category)
        return new_category
    return existing_category

# Create categories
category_names = ["Food", "Transportation", "Utilities"]
categories = {name: add_category_if_not_exists(session, name) for name in category_names}

# Commit the categories only once
session.commit()

# Create expenses
expenses = [
    Expense(amount=10.5, category_id=categories["Food"].id, date=date(2024, 7, 1)),
    Expense(amount=15.75, category_id=categories["Transportation"].id, date=date(2024, 7, 5)),
    Expense(amount=20.0, category_id=categories["Utilities"].id, date=date(2024, 7, 8))
]
session.add_all(expenses)
session.commit()

# Create budgets
budgets = [
    Budget(amount=500.0, category_id=categories["Food"].id),
    Budget(amount=300.0, category_id=categories["Transportation"].id),
    Budget(amount=200.0, category_id=categories["Utilities"].id)
]
session.add_all(budgets)
session.commit()

# Close the session
session.close()
