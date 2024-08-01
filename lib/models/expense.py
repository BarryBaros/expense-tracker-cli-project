from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    date = Column(Date, nullable=False)

    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, category_id={self.category_id}, date={self.date})"

    @classmethod
    def create(cls, session, amount, category_id, date):
        """Create and add a new expense."""
        expense = cls(amount=amount, category_id=category_id, date=date)
        session.add(expense)
        session.commit()
        return expense

    @classmethod
    def delete(cls, session, expense_id):
        """Delete an expense by ID."""
        expense = session.query(cls).filter_by(id=expense_id).first()
        if expense:
            session.delete(expense)
            session.commit()
        else:
            print(f"Expense with ID {expense_id} not found.")

    @classmethod
    def get_all(cls, session):
        """Return all expenses."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, expense_id):
        """Find an expense by ID."""
        return session.query(cls).filter_by(id=expense_id).first()