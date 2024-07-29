from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base


DATABASE_URL = "sqlite:///lib/db/expense.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  

print("Database tables created.")