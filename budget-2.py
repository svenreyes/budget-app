class Category:
    def __init__(self, name):
        self.name = name # Set the name of the category
        self.ledger = [] # Initialize an empty ledger list

    def __str__(self): 
        title = f"{self.name.center(30, '*')}\n" # Create the title
        items = "" # Initialize an empty string
        total = 0 # Initialize the total balance as 0
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23) #Get the description and left-justify it to 23 characters
            amount = format(entry['amount'], '.2f').rjust(7) # Format the amount with 2 decimal places and right-justify it to 7 characters
            items += f"{description}{amount}\n" # Concatenate the formatted description and amount as a ledger item
            total += entry['amount']  #Accumulate the entry amount to calculate the total balance
        output = title + items + f"Total: {format(total, '.2f')}" #Concatenate the title, ledger items, and total balance
        return output # Return the formatted output string

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) # Append a deposit entry to the ledger list

    def withdraw(self, amount, description=""): # Check if there are sufficient funds to withdraw
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self): 
        balance = 0  # Initialize the balance as 0
        for entry in self.ledger:
            balance += entry['amount'] # Accumulate the entry amount to calculate the balance
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount): # Check if there are sufficient funds to transfer
            self.withdraw(amount, f"Transfer to {category.name}") # Perform the withdrawal from the current category
            category.deposit(amount, f"Transfer from {self.name}") # Perform the deposit into the destination category
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance() # Check if the amount is less than or equal to the current balance


def create_spend_chart(categories):
    total_withdrawals = 0 # Initialize the total withdrawals as 0
    category_withdrawals = {} # Initialize an empty dictionary to store category withdrawals
    percentages = [] # Initialize an empty list to store percentages
  

    for category in categories: # Initialize the withdrawals for each category as 0
        withdrawals = 0
        for entry in category.ledger: 
            if entry['amount'] < 0:  # Consider only negative amounts (withdrawals)
                withdrawals -= entry['amount']
        total_withdrawals += withdrawals # Accumulate the withdrawals to calculate the total
        category_withdrawals[category.name] = withdrawals
      
  # Check if there are no withdrawals made in any category
    if total_withdrawals == 0:
        return "No withdrawals made. Spending chart cannot be generated."

    for category in categories: # Calculate the percentage spent by each category
        percentage = int((category_withdrawals[category.name] / total_withdrawals) * 10) * 10
        percentages.append(percentage) # Add the percentage to the list of percentages

    chart = "Percentage spent by category\n"  # Initialize the chart string with the title
    for percentage in range(100, -10, -10): # Iterate from 100 to 0 in steps of -10
        chart += str(percentage).rjust(3) + "| " # Add the percentage label to the chart
        for p in percentages:
            if p >= percentage:
                chart += "o  " # Add "o" if the category's percentage is greater than or equal to the current percentage
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories) # Find the maximum length of category names
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  " # Add each character of category names with two spaces in between
            else:
                chart += "   "  # Add empty spaces if the name is shorter
        if i != max_length - 1:
            chart += "\n" # Add a new line after each row except the last

    return chart
