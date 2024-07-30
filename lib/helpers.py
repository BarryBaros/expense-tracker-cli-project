# lib/helpers.py
from lib.models import Session, Expense, Category, Budget
from datetime import datetime

def helper_1():
    print("Performing useful function#1.")

def exit_program():
    print("Goodbye!")
    exit()

# Function to create a new expense
def create_expense(amount, category_name, date_str):
    session = Session()
    try:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Category '{category_name}' does not exist.")
            return
        
        expense = Expense(
            amount=amount, 
            category_id=category.id, 
            date=datetime.strptime(date_str, '%Y-%m-%d').date()
        )
        
        session.add(expense)
        session.commit()
        print(f"Expense of {amount} added to category {category_name} on {date_str}.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        session.close()


def list_expenses():
    session = Session()
    try:
        expenses = session.query(Expense).all()

        for expense in expenses:
            print(expense)
    
    # Catch any exceptions that occur during database operations
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()

# Function to create a new category
def create_category(name):
    session = Session()
    try:
        category = Category(name=name)
        
        session.add(category)
        session.commit()
        print(f"Category '{name}' created.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()

# Function to list all categories
def list_categories():
    session = Session()
    try:
        categories = session.query(Category).all()

        for category in categories:
            print(category)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()

def create_budget(amount, category_name):
    session = Session()
    try:
        category = session.query(Category).filter_by(name=category_name).first()
        
        if not category:
            print(f"Category '{category_name}' does not exist.")
            return

        budget = Budget(amount=amount, category_id=category.id)

        session.add(budget)
        session.commit()
        print(f"Budget of {amount} set for category {category_name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()

