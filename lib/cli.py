# lib/cli.py
import click
from lib.helpers import (
    exit_program,
    list_categories,
    find_category_by_name,
    create_category,
    update_category,
    delete_category,
    list_expenses,
    find_expense_by_id,
    create_expense,
    update_expense,
    delete_expense,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            create_category()
        elif choice == "4":
            update_category()
        elif choice == "5":
            delete_category()
        elif choice == "6":
            list_expenses()
        elif choice == "7":
            find_expense_by_id()
        elif choice == "8":
            create_expense()
        elif choice == "9":
            update_expense()
        elif choice == "10":
            delete_expense()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Create category")
    print("4. Update category")
    print("5. Delete category")
    print("6. List all expenses")
    print("7. Find expense by ID")
    print("8. Create expense")
    print("9. Update expense")
    print("10. Delete expense")

if __name__ == "__main__":
    main()