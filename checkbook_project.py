import os

# Welcome message and numbered options 
def welcome():    
    print('Welcome to your terminal checkbook.')
    print('    What would you like to do?')
    print('1. View current balance')
    print('2. Add a Debit (Withdraw)')
    print('3. Add a Credit (Deposit)')
    print('4. Exit')

    
    

# Current Balance Function
def current_balance():
    # check if file exists and maintain running balance when module ends
    if os.path.exists("ledger.txt"):
        balance = 0
        # create a new file if one does not exist
        with open("ledger.txt", "r") as f:
            # add transactions to leddger balance 
            for line in f:
                # remove spaces and commas
                transaction = line.strip().split(",")
                # add each credit to balance
                if transaction[0] == "credit":
                    balance += float(transaction[1])
                #subtract each debit from balance
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
    # try and except statements ensure the module will not end when an errortype occurs
    try:
        amount = float(amount)
    except ValueError:
        # notify user of invalid input
        print('~~~~~ Invalid input. Please enter a numerical value for Debit ~~~~~~')
        return
    # append the ledger with a new line as a debit and print new balance
    with open("ledger.txt", "a") as f:
        f.write(f"debit,{amount}\n")
    print(f"Your new balance is: ${current_balance():.2f}") 
    

    
    
# Option 3 add a credit.
def add_credit():
    amount = input('enter credit amount')
    # try and except statements ensure the module will not close when an errortype occurs
    try:
        amount = float(amount)
    except ValueError:
        print('~~~~~ Invalid input. Please enter a numerical value for Credit ~~~~~~')
        return
    # append the ledger with a new line as a credit and print new balance
    with open("ledger.txt", "a") as f:
        f.write(f"credit,{amount}\n")
    print(f"Your new balance is: ${current_balance():.2f}")



    
    
# Main function
def main():
    while True:
        # show user the welcome message and available options while module is running
        welcome()
        option = input("Enter your option (1-4): ")
        # option 1 is view balance fucntion
        if option == "1":
            view_balance()
            # add_debit function
        elif option == "2":
            add_debit()
            # add credit function
        elif option == "3":
            add_credit()
            # exit the while loop when 4 is entered
        elif option == "4":
            print("Goodbye")
            break
            # notify user if input is invalid
        else:
            return print("Invalid input. Please enter a number between 1 and 4.")    
    # conditional statement executes module when user runs file name
if __name__ == "__main__":
    main()
else:
    pass
    
    
    