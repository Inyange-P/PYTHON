#Quest 1

#number = int(input("Enter a number to check if it's even or odd: "))
#def check_even_odd(number):
#   if number % 2 == 0:
#        print("Number you entered is an even number.")
#    else:
#        print("Number you entered is an odd number.")
#check_even_odd(number)


# Quest 2

#Mark = int(input("Enter your marks between 0 and 100  to check your grade: "))
#def check_result(Marks):
#    if Marks >= 50:
#        print("You passed! Congratulation!")
#    elif Marks < 50:
#        print("You failed the exam.")
#   else:
#     print("You have entered wrong marks. Please enter a valid number between 0 and 100.")
#check_result(Mark)

#quest 3

#Marks = int(input("Enter your marks between 0 and 100 to check your grade: "))
#def calculate_grade(Marks):
#    if Marks <= 100 and Marks >= 80:
#        print("You got an A grade!")
#    elif Marks < 80 and Marks >= 70:
#        print("You got a B grade!")
#    elif Marks < 70 and Marks >= 60:
#        print("You got a C grade!")
#    elif Marks < 60 and Marks >= 50:
#        print("You got a D grade!")
#    elif Marks < 50:
#        print("You failed the exam.")
#    else:
#        print("You have entered wrong marks. Please enter a valid number between 0 and 100.")
#calculate_grade(Marks)

#Quest 4

#Age = int(input("Enter your age to check your category: "))
#def Age_category(Age):
#    if Age >= 0 and Age <= 12:
#        print("You are a child.")
#    elif Age > 12 and Age < 20:
#        print("You are a teenager.")
#    elif Age >= 20 and Age < 60:
#        print("You are an adult.")
#    elif Age >= 60:
#        print("You are a senior citizen.")

#Age_category(Age)


#quest 5

FirstNumber = int(input("Enter the first number: "))
SecondNumber = int(input("Enter the second number: "))
print(" Choose The Operation you want to perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
Operation = int(input("Enter your choice ( From 1 to 4): "))
if Operation == 1:
    def Addition():
        Result = FirstNumber + SecondNumber
        print("The result of addition is: ", Result)
    Addition()
elif Operation == 2:
    def Subtraction():
        if FirstNumber > SecondNumber:
            print("The first number is Larger than the second number. Please enter a valid number.")
            Result = FirstNumber - SecondNumber
            print("The result of subtraction is: ", Result)
        elif SecondNumber > FirstNumber:
            Result = SecondNumber - FirstNumber
            print("The second number is Larger than the first number. Please enter a valid number.")
            print("The result of subtraction is: ", Result)
    Subtraction()
elif Operation == 3:
    def Multiplication():
        Result = FirstNumber * SecondNumber
        print("The result of multiplication is: ", Result)
    Multiplication()
elif Operation == 4:
    def Division():
        if SecondNumber != 0:
            Result = FirstNumber / SecondNumber
            print("The second number is not zero. You can perform division.")
            print("First Number divide by Second Number.")
            print("The result of division is: ", Result)
        else:
            print("Error: Division by zero is not allowed.")
        if FirstNumber != 0:
            Result = SecondNumber / FirstNumber
            print("The first number is not zero. You can perform division.")
            print("Second Number divide by First Number.")
            print("The result of division is: ", Result) 
    Division()