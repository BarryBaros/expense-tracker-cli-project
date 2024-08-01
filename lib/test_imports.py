import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from lib.models.base import Base
    from lib.models.category import Category
    from lib.models.expense import Expense
    print("Imports successful!")
except ImportError as e:
    print(f"Import failed: {e}")
