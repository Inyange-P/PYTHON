#Classwork
FirstInput = int(input("Enter the first number: "))
SecondInput = int(input("Enter the second number: "))   

if FirstInput > SecondInput : 
    print("The first number is greater than the second number.")
    Substraction = FirstInput - SecondInput
    print ("The substraction of the two numbers is: ", Substraction)
elif FirstInput < SecondInput :
    print("The first number is less than the second number.")
    Substraction = SecondInput - FirstInput
    print ("The substraction of the two numbers is: ", Substraction)
else:
    print("Both numbers are equal.")
    print("The substraction is zero")