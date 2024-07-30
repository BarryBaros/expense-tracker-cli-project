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
    
    