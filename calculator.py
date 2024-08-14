a=float(input("Enter number 1: "))
b=float(input("Enter number 2: "))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
ch=input("Enter your operation: ")
if ch=="1":
    print("Sum is",a+b)
elif ch=="2":
    print("Difference is",a-b)
elif ch=="3":
    print("Product is",a*b)
elif ch=="4":
    if b!=0:
        print("Quotient is",a/b)
    else:
        print("can't divide by zero")
else:
    print("Invalid operation")