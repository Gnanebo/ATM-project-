# ATM Machine Simulator
atm_pin = '9949'
my_pin=(input())
if atm_pin != my_pin:
    print("incorect pin ")
    exit()
print("Welcome to atm ")
balance = 3000
while True:
    print("1 . check balance")
    print("2 . withdrawl")
    print("3 . deposit")
    print("4 .exit")

    choice = input("enter your choice ")
    if choice == '1':
        print("your account balance") 
    elif choice == '2':
        amount=float(input("enter the withdraw amount"))
        if amount > balance:
            print("insufficent balance")
        else:
            amount <= balance
            print("please collect your cash")
    elif choice == '3':
        amount = float(input("enter the deposit amount"))
        balnace += amount
        print(f"your amount deposit sucessfully {balance}") 
    elif choice == '4':
        print("thank you for choosing for ATM have a great day sir !")
        break
    else:
        print("your card is declined try again")
        continue


