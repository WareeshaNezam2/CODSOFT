print ("SIMPLE ARTTHMETIC CALCULATOR")
a = float(input("input enter your first number:"))
b = float(input("input enter your second number:"))
print ("press 1 for add\npress 2 for add\npress 3 for subract\npress 4 for divide")
choice = int(input("Enter your choice between 1-4:"))
if choice ==1:
    print("The addition of two number is:",a+b)
elif choice ==2:
    print("The subraction of two number is:",a-b)  
elif choice ==3:
    print("The multiplication of two number is:",a*b)     
elif choice ==4:
    print("The division of two number is:",a/b) 
else:
    print("Select a valid option")

