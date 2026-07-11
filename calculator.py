print("=====python calculator=====")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("choose an operation:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=input("enter your choice(1-4):")
if choice== "1":
    print("the answer is:", num1 + num2)
elif choice=="2":
    print("the answer is:", num1 - num2)
elif choice=="3":
    print("the answer is:", num1 * num2)
elif choice=="4":
     print("the answer is:",num1 / num2)
else:
    print("invalid choice")
