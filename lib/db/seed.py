# lib/db/seed.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Category, Expense

engine = create_engine('sqlite:///expense_tracker.db')
Base.metadata.create_all(engine)  

Session = sessionmaker(bind=engine)
session = Session()

# seeding the database
category1 = Category(name="Food")
category2 = Category(name="Transport")
category3 = Category(name="Utilities")

session.add_all([category1, category2, category3])
session.commit()

# Seed expenses
expense1 = Expense(amount=50.00, category_id=category1.id, date='2023-01-01')
expense2 = Expense(amount=30.00, category_id=category2.id, date='2023-01-02')
expense3 = Expense(amount=100.00, category_id=category3.id, date='2023-01-03')

session.add_all([expense1, expense2, expense3])
session.commit()
