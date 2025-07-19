atm_pin="9949"
my_pin=input("enter your card number")
if atm_pin != my_pin:
    print("incorrect pin")
    exit()
print("welcome to ATM")
account_balance = 5000000
while True:
    print("1 . check balance ")
    print("2 . deposit       ")
    print("3 . withdraw      ")
    print("4 . EXIT          ")
    choice = input("enter your choice")
    if choice == "1":
        print("your account balance is",account_balance)
    elif choice == "2":
        amount = float(input("enter the amount"))
        account_balance += amount
        print("your deposit succesfully",account_balance)
    elif choice == "3":
        amount = float(input("enter your withdraw amount"))
        if amount>account_balance:
            print("insufficent account balance")
        else:
            amount -= account_balance
            print("collect your cash ")
    elif choice == "4":
        print("thank you for choosing atm have a nice day")
        break
    else:
        print("declined your atm card try again ")
        continue                   
       