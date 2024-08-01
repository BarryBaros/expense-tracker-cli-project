from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Use cascade="all, delete-orphan" to handle cascading deletes
    expenses = relationship("Expense", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

    @classmethod
    def create(cls, session, name):
        """Create and add a new category."""
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category

    @classmethod
    def delete(cls, session, category_id):
        """Delete a category by ID."""
        category = session.query(cls).filter_by(id=category_id).first()
        if category:
            session.delete(category)
            session.commit()
            print(f"Deleted category with ID {category_id}.")
        else:
            print(f"Category with ID {category_id} not found.")

    @classmethod
    def get_all(cls, session):
        """Return all categories."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, category_id):
        """Find a category by ID."""
        return session.query(cls).filter_by(id=category_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        """Find a category by name."""
        return session.query(cls).filter_by(name=name).first()
