from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

def create_all_tables():
    Base.metadata.create_all(engine)

DATABASE_URL = "sqlite:///lib/db/expense.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  

if __name__ == "__main__":
    create_all_tables()

print("Database tables created.")