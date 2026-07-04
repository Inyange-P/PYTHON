#Meet Yourself

print("Welcome to the Lost Treasure Game!")
UserName = input("Please enter your name: ")
print("Hello", UserName, "! Your adventure begins now.")

#The Pirate's Age

UserAge = int(input("Please enter your age: "))
print("Great! You are", UserAge, "years old.")
print("You find yourself in a mysterious forest. There are other questions I would Like to Ask you.")

#Pirate Name

FavColor = input("What is your favourite colour? ")
FavAnimal = input("What is your favourite animal? ")
print("Interesting! Your favourite colour is", FavColor, "and your favourite animal is", FavAnimal, ".")
print("Now Your Pirate Name is", FavColor, FavAnimal, "!")

#Treasure Coins

GoldCoins = int(input("How many gold coins were found? "))
print("You have found", GoldCoins, "gold coins!")

#Split The Treasure

PiratesNumber = int(input("How many pirates are in the crew? "))
print("The crew consists of", PiratesNumber, "pirates.")
PirateShare = GoldCoins / PiratesNumber
print("Each pirate will receive", PirateShare, "gold coins.")

#Happy Pirates?

if PirateShare >= 15:

#Guess The Number

    SecretNumber = 7
    GuessNumber = int(input("Guess the secret number: "))
    if GuessNumber == SecretNumber:
        print("Congratulations! You guessed the secret number and found the treasure!")
    else:
        print("Sorry, that's not the secret number. Better luck next time!")

#Talking Parrot

Aword = input("Enter any word: ")
for i in range(1,6):
    print(Aword)

#Treasure Inventory

Items = ["Sword", "Compass", "Map", "Key", "Lantern"]
for x in Items:
    print(x)

#Count The Treasure

print("The total number of inventory items is: ")
print(len(Items))

#secret Cave

Age = int(input("Enter your age to enter the secret cave: "))
if Age >= 18:
    print("You are old enough to enter the secret cave!")
else:
    print("Sorry, you are not old enough to enter the secret cave.")
 
#Treasure Calculator

GoldCoins = int(input("Enter the number of gold coins you have: "))
SilverCoins = int(input("Enter the number of silver coins you have: "))
TotalNumber = (GoldCoins) + (SilverCoins)
print("The total number of coins you have is: ", TotalNumber)
if GoldCoins > SilverCoins:
    print("You have more gold coins than silver coins.")
    DifferenceNumber = (GoldCoins) - (SilverCoins)
    print("The difference between gold and silver coins is: ", DifferenceNumber)
else:
    DifferenceNumber = (SilverCoins) - (GoldCoins)
    print("You have more silver coins than gold coins.")
    print("The difference between silver and gold coins is: ", DifferenceNumber)
ProductNumber = (GoldCoins) * (SilverCoins)
print("The product of gold and silver coins is: ", ProductNumber)
DivisionNumber = (GoldCoins) / (SilverCoins)
print("Gold coins divided by silver coins is: ", DivisionNumber)
