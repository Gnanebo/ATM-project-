"""x=5
y=5.0
print(x==y)
print(x is y)


a=5
b="6"
print(a+int(b))


# convert 5.6  into int,str,boolen
a=5.6
print(int(a))
print(str(a))
print(bool(a))

# day 1 project mini caluculator
a=int(input("enter the number :"))
b=int(input("enter the number :"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


# write a program check if number is even or odd
n=int(input("enter the number :"))
if n%2 == 0:
    print("it is even number")
elif n%2 != 0:
    print("it is odd number")
else:
    print("it is equal to zero")    \




# Skip multiples of 3 from 1 to 20 using continue
for i in range(1,21):
    if i % 3 == 0:
        continue
       
    print(i)           

# sum of even number from  1 to N
n=int(input())
count=0
for i in range(1,n+1):
    if i%2 == 0:
        count += i  
print(count)       """ 

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


