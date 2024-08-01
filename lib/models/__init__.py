from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Import all the models to register them with SQLAlchemy
from .expense import Expense
from .category import Category

DATABASE_URL = "sqlite:///lib/db/expense.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
