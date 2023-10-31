
import os



# Welcome message and options 
def welcome():    
    print('Welcome to your terminal checkbook.')
    print('    What would you like to do?')
    print('1. View current balance')
    print('2. Add a Debit (Withdraw)')
    print('3. Add a Credit (Deposit)')
    print('4. Exit')





# Current Balance Function
def current_balance():
    balance = 0
    if os.path.exists("ledger.txt"):
        with open("ledger.txt", "r") as f:
            for line in f:
                transaction = line.strip().split(",")
                if transaction[0] == "credit":
                    balance += float(transaction[1])
                elif transaction[0] == "debit":
                    balance -= float(transaction[1])
                else:
                    pass
    return balance






# Option 1 view current balance.
def view_balance():
    balance = current_balance()
    return print(f"Your current balance is: ${balance:.2f}")




# Option 2 add a debit.
def add_debit():
    amount = input('Enter debit amount')
    try:
        amount = float(amount)
    except ValueError:
        print('~~~~~ Invalid input. Please enter a numerical value for Debit ~~~~~~')
        return
    with open("ledger.txt", "a") as f:
        f.write("debit,{}\n".format(amount))
    print(f"Your new balance is: ${current_balance():.2f}")



# Option 3 add a credit.
def add_credit():
    amount = input('enter credit amount')
    try:
        amount = float(amount)
    except ValueError:
        print('~~~~~ Invalid input. Please enter a numerical value for Credit ~~~~~~')
        return
    with open("ledger.txt", "a") as f:
            f.write(f"credit,{amount}\n")
    print(f"Your new balance is: ${current_balance():.2f}")




# Main function that holds other functions
def main():
    while True:
        welcome()
        option = input("Enter your option (1-4): ")
        if option == "1":
            view_balance()
        elif option == "2":
            add_debit()
        elif option == "3":
            add_credit()
        elif option == "4":
            print("Goodbye")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")





if __name__ == "__main__":
    main()
else:
    pass

