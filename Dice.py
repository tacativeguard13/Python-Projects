import random as rd

status = True

def genrateNumber():
    randomNumber = rd.randint(1,6)
    return randomNumber

while status == True:
    main = input("Press 'Enter' to roll the dice ")

    if main == '':
        print(genrateNumber())
    elif main == "Exit" or "exit":
        print("The input was invalid or you choosed to exit the program")
        print("Thanks for using Digital Dice by Tact")
        break