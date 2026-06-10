#Personal Expense Tracker
import os
print("\n--- Personal Expense Tracker ---")


#Task 1: Load expense from file
def load_expense(filename):


    expenses = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                #Strip whitespace and skip empty lines
                line = line.strip()
                if not line:
                    continue

                #Split by comma and parse values
                category, amount_str = line.split(',')
                expenses.append((category.strip(), float(amount_str)))

    except FileNotFoundError:
        #Return an empty list if the file doesn't exist yet
        return[]
    
    return expenses

#Task 2: Add new expense

def add_expense(filename, category, amount):
    #Appends a new expense line to the file. Raises ValueError if the amount is not a positive number.

    if amount <=0:
        raise ValueError("Amount must be a positive number.")
    
    with open(filename, 'a') as file:
        file.write(f"{category}, {amount}\n")


#Task 3: Calculate and print category totals

def category_totals(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    totals={}
    grand_total= 0.0

    #Group and sum using the .get() hint
    for category, amount in expenses:
        totals[category] = totals.get(category, 0.0)+ amount
        grand_total += amount


    #Print formatting matches the expected output

    print(f"{'Category':<16} Total")
    print("________________")
    for category, total in totals.items():
        print(f"{category:<15} : ${total:.2f}")

    print("________________")
    print(f"{'Grand Total': <15} : ${grand_total:.2f}\n")


#Task 4: Filter Expenses above threshold

def above_threshold(expenses, limit):

    return[(c, a) for c, a in expenses if a > limit]

#Demonstration / Main Execution- Interactive User Interface
def main():

    FILENAME = "expenses.txt"
    print("== Personal Expense Tracker ===")
    
    while True:
        print("1. Add New Expense: ")
        print("2. View Expense Summary & Totals: ")
        print("3. View Expenses Above a Threshold: ")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            category = input("Enter expense category (e.g., Food, Transport): ").strip()
            if not category:
                print("Error: Category cannot be empty.\n")
                continue

            try:
                amount = float(input("Enter expense amount: "))
                #This calls Task 2 and validates if amount > 0
                add_expense(FILENAME, category, amount)
                print(f"Successfully added: {category} -> ${amount:.2f}\n")

            except ValueError as e:
                #Catches bout non-numeric inputed and our custom negative number error
                if "cound not convert string to float" in str(e):
                    print("Error: Please enter a valid numeric amount.\n")

                else:
                    print(f"Error:{e}\n")


        elif choice == '2':
#Reloads the file dynamically to get the latest inputs

            expenses  = load_expense(FILENAME)
            category_totals(expenses)

        elif choice =="3":
            expenses = load_expense(FILENAME)
            if not expenses:
                print("\nNo expenses recorded yet.\n")
                continue

            try:
                limit = float(input("Enter the threshold limit amount: "))
                expensive_items = above_threshold(expenses, limit)

                print(f"\nExpenses about ${limit:.2f}: ")
                if not expensive_items:
                    print(" None Found.")
                for cat, amt in expensive_items:
                    print(f" {cat:<13}  ${amt:.2f}")
                print()

            except ValueError:
                print("Error: Please enter a valid NUmber for the limit.\n")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please pick a number from 1 to 4.\n")

if __name__ == "__main__":
    main()