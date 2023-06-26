import budget
from budget import create_spend_chart

def run_budget_app():
    # Initialize categories
    food = budget.Category("Food")
    clothing = budget.Category("Clothing")
    auto = budget.Category("Auto")

    while True:
        # Display menu options
        print("************ Budget App ************")
        print("1. View Categories")
        print("2. Add Funds to a Category")
        print("3. Withdraw Funds from a Category")
        print("4. Transfer Funds between Categories")
        print("5. Create Spending Chart")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            # View categories and their balances
            print("************ Categories ************")
            print(food)
            print(clothing)
            print(auto)
            print("************************************")

        elif choice == "2":
            # Add funds to a category
            category = input("Enter the name of the category: ")
            amount = float(input("Enter the amount to add: "))
            if category.lower() == "food":
                food.deposit(amount)
            elif category.lower() == "clothing":
                clothing.deposit(amount)
            elif category.lower() == "auto":
                auto.deposit(amount)
            else:
                print("Invalid category name.")

        elif choice == "3":
            # Withdraw funds from a category
            category = input("Enter the name of the category: ")
            amount = float(input("Enter the amount to withdraw: "))
            if category.lower() == "food":
                food.withdraw(amount)
            elif category.lower() == "clothing":
                clothing.withdraw(amount)
            elif category.lower() == "auto":
                auto.withdraw(amount)
            else:
                print("Invalid category name.")

        elif choice == "4":
            # Transfer funds between categories
            from_category = input("Enter the name of the source category: ")
            to_category = input("Enter the name of the destination category: ")
            amount = float(input("Enter the amount to transfer: "))
            if from_category.lower() == "food":
                if to_category.lower() == "clothing":
                    food.transfer(amount, clothing)
                elif to_category.lower() == "auto":
                    food.transfer(amount, auto)
                else:
                    print("Invalid destination category name.")
            elif from_category.lower() == "clothing":
                if to_category.lower() == "food":
                    clothing.transfer(amount, food)
                elif to_category.lower() == "auto":
                    clothing.transfer(amount, auto)
                else:
                    print("Invalid destination category name.")
            elif from_category.lower() == "auto":
                if to_category.lower() == "food":
                    auto.transfer(amount, food)
                elif to_category.lower() == "clothing":
                    auto.transfer(amount, clothing)
                else:
                    print("Invalid destination category name.")
            else:
                print("Invalid source category name.")

        elif choice == "5":
            # Create spending chart
            chart = create_spend_chart([food, clothing, auto])
            print(chart)

        elif choice == "0":
            # Exit the app
            print("Exiting the Budget App.")
            break

        else:
            print("Invalid choice. Please try again.")

run_budget_app()
