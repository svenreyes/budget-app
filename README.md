Budget App

The Budget App is a simple command-line application that allows you to manage your budget by creating and managing different spending categories. You can track your expenses, add funds, withdraw funds, transfer funds between categories, and generate spending charts.

Features

View Categories: Display the list of categories and their current balances.
Add Funds to a Category: Add funds to a specific category.
Withdraw Funds from a Category: Withdraw funds from a specific category.
Transfer Funds between Categories: Transfer funds from one category to another.
Create Spending Chart: Generate a chart showing the percentage of spending in each category.
Exit: Quit the application.
Getting Started

Clone the repository or download the source code.
Make sure you have Python 3 installed on your system.
Install the required dependencies by running the following command:
Copy code
pip install -r requirements.txt
Run the budget app by executing the following command:
css
Copy code
python main.py
Follow the on-screen instructions to interact with the budget app and manage your categories and funds.
Usage

Upon running the budget app, you will be presented with a menu of options to choose from. Simply enter the number corresponding to the desired option and follow the prompts to perform the corresponding action.

Note: The budget app supports both integer and decimal values for adding, withdrawing, and transferring funds.

Example

Here's an example usage scenario of the budget app:

markdown
Copy code
************ Budget App ************
1. View Categories
2. Add Funds to a Category
3. Withdraw Funds from a Category
4. Transfer Funds between Categories
5. Create Spending Chart
0. Exit
Select an option: 1

************ Categories ************
Category: Food
  Food Balance: $200.00

Category: Clothing
  Clothing Balance: $150.00

Category: Entertainment
  Entertainment Balance: $50.00
************************************

Select an option: 2
Enter the name of the category: Food
Enter the amount to add: 100.50

Select an option: 1

************ Categories ************
Category: Food
  Food Balance: $300.50

Category: Clothing
  Clothing Balance: $150.00

Category: Entertainment
  Entertainment Balance: $50.00
************************************

Select an option: 3
Enter the name of the category: Clothing
Enter the amount to withdraw: 75.25

Select an option: 1

************ Categories ************
Category: Food
  Food Balance: $300.50

Category: Clothing
  Clothing Balance: $74.75

Category: Entertainment
  Entertainment Balance: $50.00
************************************

Select an option: 5

Percentage spent by category
100|
 90|
 80|
 70|
 60|
 50|
 40|
 30|
 20|
 10|          o
  0|          o
    ----------
     F  C  E
     o  l  n
     o  o  t
     d  t  e
        h  r
        i  t
        n  a
        g  i
           n
           g

Select an option: 0

Exiting the Budget App.
Testing

The budget app includes a separate unit testing module (test_module.py) to ensure the correctness of its functionality. You can run the tests by executing the following command:

Copy code
python test_module.py
Running the tests will validate various aspects of the budget app, such as depositing funds, withdrawing funds, transferring
