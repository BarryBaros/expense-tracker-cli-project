# Expense Tracker CLI

## Introduction

The Expense Tracker CLI is a command-line interface application built with Python and SQLAlchemy. It allows users to manage and track their expenses and categories through interactive prompts. This project provides a way to handle expenses, categorize them, and perform CRUD (Create, Read, Update, Delete) operations on both categories and expenses.

## Features

- List all categories
- Find category by name
- Create, update, and delete categories
- List all expenses
- Find expense by ID
- Create, update, and delete expenses

## Directory Structure

Here’s a quick overview of the project's directory structure:

```console
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
