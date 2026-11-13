import math

n=int(input("Enter How many numbers you want:"))
result= float(input("enter number:"))

for i in range(2,n+1):
    
    a=float(input("enter number:"))
    op=input("enter operator(+,-,*,/):")

    if op == '+':
        result += a
    elif op == '-':
        result -= a
    elif op  == '*':
        result *= a
    elif op =='/':
        if result !=0:
            result /= a
        else:
            print("cannnot divide by zero")
            break
print("The Answer is :" , result)



