# lib/cli.py
import click

from helpers import (
    exit_program,
    list_expenses,
    find_expense_by_id,
    create_expense,
    update_expense,
    delete_expense,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_category_expenses
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_expenses()
        elif choice == "2":
            find_expense_by_id()
        elif choice == "3":
            create_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            list_categories()
        elif choice == "7":
            find_category_by_name()
        elif choice == "8":
            find_category_by_id()
        elif choice == "9":
            create_category()
        elif choice == "10":
            update_category()
        elif choice == "11":
            delete_category()
        elif choice == "12":
            list_category_expenses()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all expenses")
    print("2. Find expense by ID")
    print("3. Create expense")
    print("4. Update expense")
    print("5. Delete expense")
    print("6. List all categories")
    print("7. Find category by name")
    print("8. Find category by ID")
    print("9. Create category")
    print("10. Update category")
    print("11. Delete category")
    print("12. List all expenses in a category")

if __name__ == "__main__":
    main()
