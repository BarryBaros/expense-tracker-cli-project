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

def find_category_by_name():
    name = input("Enter category's name: ")
    category = session.query(Category).filter_by(name=name).first()
    print(category if category else "Cateogry not found.")

def create_category():
    name = input("Enter new category name: ")
    Category = Category(name=name)
    session.add(Category)
    session.commit()
    print("Category created succesfully!")

