from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Category, Expense

engine = create_engine('sqlite:///expense_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Thank you for visiting!")
    exit()

def list_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(category)
