# lib/cli.py
import click
from lib.helpers import create_expense, list_expenses, create_category, list_categories, create_budget, list_budgets, generate_report

@click.group()
def cli():
    pass

@cli.command()
@click.option('--amount', prompt='Expense amount',  type=float)
@click.option('--category', prompt='Expense category')
@click.option('--date', prompt='Expense date (YYYY, MM, DD)')
def add_expense(amount, category, date):
    create_expense(amount, category, date)

@cli.command()
def show_expenses():
    list_expenses()

@cli.command()
@click.option('--name', prompt='Category name')
def add_category(name):
    create_category(name)

@cli.command()
def show_categories():
    list_categories()

@cli.command()
@click.option('--amount', prompt='Budget amount', type=float)
@click.option('--category', prompt='Budget category')
def add_budget(amount, category):
    create_budget(amount, category)

@cli.command()
def show_budgets():
    list_budgets()

@cli.command()
@click.option('--report_type', prompt='Report type (monthly/yearly)')
def report(report_type):
    generate_report(report_type)
    
if __name__ == "__main__":
    cli()
