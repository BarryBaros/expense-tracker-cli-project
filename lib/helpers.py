from lib.models import Session, Expense, Category
from datetime import datetime

def exit_program():
    print("Goodbye!")
    exit()

def list_expenses():
    session = Session()
    expenses = session.query(Expense).all()
    for expense in expenses:
        print(expense)
    session.close()

def find_expense_by_id():
    id = input("Enter expense ID: ")
    session = Session()
    expense = session.query(Expense).filter_by(id=id).first()
    if expense:
        print(expense)
    else:
        print(f"No expense found with ID {id}")
    session.close()

def create_expense():
    amount = float(input("Enter amount: "))
    category_name = input("Enter category name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        expense = Expense(amount=amount, category_id=category.id, date=datetime.strptime(date, '%Y-%m-%d').date())
        session.add(expense)
        session.commit()
        print(f"Expense of {amount} created in category {category_name}.")
    else:
        print(f"No category found with name {category_name}")
    session.close()

def update_expense():
    id = input("Enter expense ID to update: ")
    session = Session()
    expense = session.query(Expense).filter_by(id=id).first()
    if expense:
        new_amount = float(input("Enter new amount: "))
        expense.amount = new_amount
        session.commit()
        print(f"Expense ID {id} updated with new amount {new_amount}.")
    else:
        print(f"No expense found with ID {id}")
    session.close()

def delete_expense():
    id = input("Enter expense ID to delete: ")
    session = Session()
    expense = session.query(Expense).filter_by(id=id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print(f"Expense ID {id} deleted.")
    else:
        print(f"No expense found with ID {id}")
    session.close()

def list_categories():
    session = Session()
    categories = session.query(Category).all()
    for category in categories:
        print(category)
    session.close()

def find_category_by_name():
    name = input("Enter category name: ")
    session = Session()
    category = session.query(Category).filter_by(name=name).first()
    if category:
        print(category)
    else:
        print(f"No category found with name {name}")
    session.close()

def find_category_by_id():
    id = input("Enter category ID: ")
    session = Session()
    category = session.query(Category).filter_by(id=id).first()
    if category:
        print(category)
    else:
        print(f"No category found with ID {id}")
    session.close()

def create_category():
    name = input("Enter category name: ")
    session = Session()
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' created.")
    session.close()

def update_category():
    id = input("Enter category ID to update: ")
    session = Session()
    category = session.query(Category).filter_by(id=id).first()
    if category:
        new_name = input("Enter new category name: ")
        category.name = new_name
        session.commit()
        print(f"Category ID {id} updated to new name '{new_name}'.")
    else:
        print(f"No category found with ID {id}")
    session.close()

def delete_category():
    id = input("Enter category ID to delete: ")
    session = Session()
    category = session.query(Category).filter_by(id=id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category ID {id} deleted.")
    else:
        print(f"No category found with ID {id}")
    session.close()

def list_category_expenses():
    category_name = input("Enter category name: ")
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        expenses = session.query(Expense).filter_by(category_id=category.id).all()
        for expense in expenses:
            print(expense)
    else:
        print(f"No category found with name {category_name}")
    session.close()
