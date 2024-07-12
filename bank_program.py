

def show_balance(account_balance):
    print(f"Current balance: ${account_balance:.2f}")


def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("Enter a valid amount!")
        return 0
    else:
        return amount


def withdraw(account_balance):
    amount = float(input("Enter the amount to withdraw: "))
    
    if amount > account_balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount

def main():
    account_balance = 0
    is_running = True

    while is_running:
        print("*************************")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4.Exit")
        print("****************************")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                show_balance(account_balance)
            case "2":
                account_balance += deposit()
            case "3":
                account_balance -= withdraw(account_balance)
            case "4":
                is_running = False
            case _:
                print("****************************")
                print("Enter a valid choice!")
                print("****************************")


    print("Thank you. Have a nice day!")
if __name__ == "__main__":
    main()



