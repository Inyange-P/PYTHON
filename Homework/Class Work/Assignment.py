#Write a Python program that:

#Asks the user to enter their name.
#Asks the user to enter marks for 3 subjects.
#Create a function called CalculateAverage() that calculates the average mark.
#Display the average.
#Use if, elif, and else to determine the grade:
#Average	Grade
#80–100	A
#70–79	B
#60–69	C
#50–59	D
#Below 50	F
#Print whether the student Passed or Failed.
#Pass = Average ≥ 50
#Fail = Average < 50

FirstName = input("Enter your First name: ")
SecondName = input("Enter your Second name: ")
Subject1 = float(input("Enter marks for Subject 1: "))
Subject2 = float(input("Enter marks for Subject 2: "))
Subject3 = float(input("Enter marks for Subject 3: "))
Average = (Subject1 + Subject2 + Subject3) / 3
def CalculateAverage():
    print("Your Full Name is : ", FirstName, SecondName)
    print("Your marks Average is: ", Average)
    if (Average >=80 and Average<=100):
        print("Your Grade is: A")
    elif (Average >=70 and Average<=79):
        print("Your Grade is: B")  
    elif (Average >=60 and Average<=69):
        print("Your Grade is: C")
    elif (Average >=50 and Average<=59):
        print("Your Grade is: D")
    else:
        print("Your Grade is: F")  
CalculateAverage() 
def CalculatePassFail():
    if (Average >= 50):
        print("Status is that You Passed")
    elif (Average < 50):
        print("Status is that You Failed") 
    else:
        print("You have entered wrong marks. Please enter a valid number between 0 and 100.")

CalculatePassFail()
        
        
