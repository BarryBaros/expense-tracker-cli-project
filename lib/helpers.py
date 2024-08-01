from sqlalchemy.orm import sessionmaker
from lib.db.create_tables import engine
from .models.category import Category
from .models.expense import Expense
from datetime import datetime

# Create a new session
Session = sessionmaker(bind=engine)

def list_categories():
    with Session() as session:
        categories = session.query(Category).all()
        for category in categories:
            print(category)

def find_category_by_name(name):
    with Session() as session:
        category = session.query(Category).filter_by(name=name).first()
        if category:
            print(category)
        else:
            print(f"No category found with name: {name}")

def create_category(name):
    with Session() as session:
        new_category = Category(name=name)
        session.add(new_category)
        session.commit()
        print(f"Category '{name}' created successfully.")

def update_category(id, name):
    with Session() as session:
        category = session.query(Category).filter_by(id=id).first()
        if category:
            category.name = name
            session.commit()
            print(f"Category ID '{id}' updated to '{name}'.")
        else:
            print(f"No category found with ID: {id}")

def delete_category(id):
    with Session() as session:
        category = session.query(Category).filter_by(id=id).first()
        if category:
            session.delete(category)
            session.commit()
            print(f"Category ID '{id}' deleted.")
        else:
            print(f"No category found with ID: {id}")

def list_expenses():
    with Session() as session:
        expenses = session.query(Expense).all()
        for expense in expenses:
            print(expense)

def find_expense_by_id(id):
    with Session() as session:
        expense = session.query(Expense).filter_by(id=id).first()
        if expense:
            print(expense)
        else:
            print(f"No expense found with ID: {id}")

def create_expense(amount, category_id, date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    with Session() as session:
        new_expense = Expense(amount=amount, category_id=category_id, date=date)
        session.add(new_expense)
        session.commit()
        print(f"Expense of '{amount}' created successfully.")

def update_expense(id, amount, category_id, date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    with Session() as session:
        expense = session.query(Expense).filter_by(id=id).first()
        if expense:
            expense.amount = amount
            expense.category_id = category_id
            expense.date = date
            session.commit()
            print(f"Expense ID '{id}' updated.")
        else:
            print(f"No expense found with ID: {id}")

def delete_expense(id):
    with Session() as session:
        expense = session.query(Expense).filter_by(id=id).first()
        if expense:
            session.delete(expense)
            session.commit()
            print(f"Expense ID '{id}' deleted.")
        else:
            print(f"No expense found with ID: {id}")

def exit_program():
    print("Thank you. Goodbye!")
    exit()
