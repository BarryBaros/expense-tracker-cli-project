from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Category, Expense

engine = create_engine('sqlite:///expense_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Thank you, goodbye!")
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
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category created successfully!")

def update_category():
    category_id = int(input("Enter category's iD to update: "))
    name = input("Enter new category name: ")
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = name
        session.commit()
        print("Category updated.")
    else:
        print("Categpry not found.")

def delete_category():
    category_id = int(input("Enter Category's ID to delete: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted.")
    else:
        print("Category not found.")

def list_expenses():
    expenses = session.query(Expense).all()
    for expense in expenses:
        print(expense)

def find_expense_by_id():
    expense_id = int(input("Enter expense's ID: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    print(expense if expense else "Expense not found.")

from datetime import datetime

def create_expense():
    amount = float(input("Enter amount: "))
    category_id = int(input("Enter category's ID: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    
    # Convert the date string to a datetime.date object
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    expense = Expense(amount=amount, category_id=category_id, date=date)
    session.add(expense)
    session.commit()
    print("Expense created successfully!")

from datetime import datetime

def update_expense():
    expense_id = int(input("Enter expense ID to update: "))
    amount = float(input("Enter new amount: "))
    category_id = int(input("Enter new category ID: "))
    date_str = input("Enter new date (YYYY-MM-DD): ")
    
    #Convert the date string to a datetime.date object
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    #Fetch the expense record from the database
    expense = session.query(Expense).filter(Expense.id == expense_id).first()
    
    if expense:
        expense.amount = amount
        expense.category_id = category_id
        expense.date = date
        session.commit()
        print("Expense updated successfully!")
    else:
        print("Expense not found.")


def delete_expense():
    expense_id = int(input("Enter expense's ID to delete: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted successfully.")
    else:
        print("expense not found.")