Expense Tracker CLI
Introduction
The Expense Tracker CLI is a command-line interface application built with Python and SQLAlchemy. It allows users to manage and track their expenses and categories through interactive prompts. This project provides functionality to handle expenses, categorize them, and perform CRUD (Create, Read, Update, Delete) operations on both categories and expenses.

Features
List all categories: Displays all categories stored in the database.
Find category by name: Retrieves a category by its name.
Create, update, and delete categories: Allows for CRUD operations on categories.
List all expenses: Displays all expenses recorded in the database.
Find expense by ID: Retrieves an expense by its ID.
Create, update, and delete expenses: Allows for CRUD operations on expenses.
Directory Structure

Overview of the project's directory structure:
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── expense_tracker.db
├── lib
│   ├── __init__.py
│   ├── cli.py
│   ├── db
│   │   ├── create_tables.py
│   │   ├── seed.py
│   ├── helpers.py
│   └── models
│       ├── __init__.py
│       ├── category.py
│       ├── expense.py
│       └── budget.py
└── migrations
    ├── README
    ├── env.py
    ├── script.py.mako
    └── versions
Install Dependencies

1. Ensure you have Pipenv installed, then run:

pipenv install

2. Create Database and Tables

To create the database and tables, run:
python lib/db/create_tables.py

3. Seed the Database

To populate the database with initial categories and expenses, run:
python lib/db/seed.py

CLI Commands
Categories
Create a new category:
python lib/cli.py create-category <name>

List all categories:
python lib/cli.py list-categories

Find a category by name:
python lib/cli.py find-category <name>


Update a category:
python lib/cli.py update-category <id> <new_name>

Delete a category:
python lib/cli.py delete-category <id>

Expenses
Create a new expense:
python lib/cli.py create-expense <amount> <category_id> <date>

List all expenses:
python lib/cli.py list-expenses

Find an expense by ID:
python lib/cli.py find-expense <id>

Update an expense:
python lib/cli.py update-expense <id> <amount> <category_id> <date>

Delete an expense:
python lib/cli.py delete-expense <id>
