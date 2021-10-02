ch=input("enter your choice(1/2/3/4/5/6):")
if (ch=='1'or ch=='2' or ch=='3' or ch=='4' or ch=='5'):
    a= int(input("enter 1st number:"))
    b= int(input("enter 2nd number:"))
elif (ch=='6'):
    c=int(input("enter a number:"))
else:
    print("Invalid choice......")
if ch=='1':
    print("addition is:",a+b)
elif ch=='2':
    print("subtraction is:",a-b)
elif ch=='3':
    print("multiplication is:",a*b)
elif ch=='4':
    print("division is:",a/b)
elif ch=='5':
    print("a to the power b is:",a**b)
elif ch=='6':
    fact=1
    i=1
    while i<=c:
        fact=fact*i
        i=i+1
    print("factorial of",c,"is",fact)    
        
else:
    pass


