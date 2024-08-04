import click
from datetime import datetime
from models import Category, Expense
# from base import engine
from lib.helpers import (
    list_categories as list_cats,
    find_category_by_name as find_cat_by_name,
    create_category as create_cat,
    update_category as update_cat,
    delete_category as delete_cat,
    list_expenses as list_exps,
    find_expense_by_id as find_exp_by_id,
    create_expense as create_exp,
    update_expense as update_exp,
    delete_expense as delete_exp,
)

@click.group()
def cli():
    """My Expense Tracker CLI"""
    pass

@cli.command()
def list_categories():
    """List all categories"""
    list_cats()

@cli.command()
@click.argument('name')
def find_category_by_name(name):
    """Find category by name"""
    find_cat_by_name(name)

@cli.command()
@click.argument('name')
def create_category(name):
    """Create a new category"""
    create_cat(name)

@cli.command()
@click.argument('id', type=int)
@click.argument('name')
def update_category(id, name):
    """Update category by ID"""
    update_cat(id, name)

@cli.command()
@click.argument('id', type=int)
def delete_category(id):
    """Delete category by ID"""
    delete_cat(id)

@cli.command()
def list_expenses():
    """List all expenses"""
    list_exps()

@cli.command()
@click.argument('id', type=int)
def find_expense_by_id(id):
    """Find expense by ID"""
    find_exp_by_id(id)

@cli.command()
@click.argument('amount', type=float)
@click.argument('category_id', type=int)
@click.argument('date')
def create_expense(amount, category_id, date):
    """Create a new expense"""
    create_exp(amount, category_id, date)

@cli.command()
@click.argument('id', type=int)
@click.argument('amount', type=float)
@click.argument('category_id', type=int)
@click.argument('date')
def update_expense(id, amount, category_id, date):
    """Update expense by ID"""
    update_exp(id, amount, category_id, date)

@cli.command()
@click.argument('id', type=int)
def delete_expense(id):
    """Delete expense by ID"""
    delete_exp(id)

@cli.command()
def exit():
    """Exit the CLI"""
    click.echo("Thank you, goodbye!")
    raise SystemExit(0)

if __name__ == "__main__":
    cli()
