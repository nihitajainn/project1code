# ATM Management System Using Functions

balance = 5000
pin = 1234


def check_balance():
    print("Your current balance is Rs.", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: Rs. "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated balance: Rs.", balance)
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: Rs. "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance: Rs.", balance)


def atm_menu():
    while True:
        print("\n===== ATM MANAGEMENT SYSTEM =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Please try again.")


def main():
    print("Welcome to the ATM")
    entered_pin = int(input("Enter your 4-digit PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        atm_menu()
    else:
        print("Incorrect PIN! Access denied.")


main()