from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Base, Category, Expense, Budget

engine = create_engine('sqlite:///expsense.db') #engine that connectes to the SQLite database
Session = sessionmaker(bind=engine) #a configured Session class
session = Session() #session instance

