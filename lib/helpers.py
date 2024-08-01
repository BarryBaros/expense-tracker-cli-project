# lib/helpers.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Category, Expense

engine = create_engine('sqlite:///expense_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Thank you. Goodbye!")
    exit()

def list_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(category)

def find_category_by_name(name):
    category = session.query(Category).filter_by(name=name).first()
    print(category if category else "Category not found")

def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category created")

def update_category(category_id, new_name):
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = new_name
        session.commit()
        print("Category updated")
    else:
        print("Category not found")

def delete_category(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted")
    else:
        print("Category not found")

def list_expenses():
    expenses = session.query(Expense).all()
    for expense in expenses:
        print(expense)

def find_expense_by_id(expense_id):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    print(expense if expense else "Expense not found")

def create_expense(amount, category_id, date):
    expense = Expense(amount=amount, category_id=category_id, date=date)
    session.add(expense)
    session.commit()
    print("Expense created")

def update_expense(expense_id, new_amount, new_category_id, new_date):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        expense.amount = new_amount
        expense.category_id = new_category_id
        expense.date = new_date
        session.commit()
        print("Expense updated")
    else:
        print("Expense not found")

def delete_expense(expense_id):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted")
    else:
        print("Expense not found")
