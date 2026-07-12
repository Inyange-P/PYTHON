FirstNumber = int(input('Enter your First Number : '))
SecondNumber = int(input('Enter Your Second Number : '))
print ('The First Number Entered Is ', FirstNumber)
print ('The Second Number Entered Is ', SecondNumber)
if (FirstNumber > SecondNumber):
    X = FirstNumber - SecondNumber
    print ('The final answer is ', X )
    exit()
else :
    Answer = SecondNumber - FirstNumber
print('The Final answer is ', Answer)
