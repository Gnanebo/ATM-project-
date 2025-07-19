# Step 1: PIN check
correct_pin = "9949"
my_pin = input("Enter your ATM PIN: ")

if my_pin != correct_pin:
    print("Incorrect PIN. Try again later.")
    exit()

print("Welcome to the ATM!")
balance = 5000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Please collect your cash.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        continue



