from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Base, Category, Expense, Budget

engine = create_engine('sqlite:///expsense.db') #engine that connectes to the SQLite database
Session = sessionmaker(bind=engine) #a configured Session class
session = Session() #session instance

# Create categories
categories = [
    Category(name="Food"), 
    Category(name="Transporatation"), 
    Category(name="Utilities")
    ]
session.add_all(categories)
session.commit()

# Create expenses
expenses = [
    Expense(amount=10.5, category_id=1, date = '2024-07-01'),
    Expense(amount=15.75, category_id=2, date = '2024-07-05'),
    Expense(amount=20.0, category_id=3, date = '2024-07-08')
]
session.add_all(expenses)
session.commit

# Create budgets
budgets = [
    Budget(amount=500.0, category_id = 1),
    Budget(amount=300.0, category_id = 2),
    Budget(amount=200.0, category_id = 3)
]
session.add_all(budgets)
session.commit

session.close()