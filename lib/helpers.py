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

def creat_expense():
    amount = float(input("Enter amount: "))
    Category_id = int(input("Enter category's ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    expense = Expense(amount=amount, Category_id=Category_id, date=date)
    session.add(expense)
    session.commit()
    print("Expense created succesfully")

