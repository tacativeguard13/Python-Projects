import random

def gameWin():
    if computer == player:
        return None
    
    elif computer == "r":
        if player == "p":
            return True
        else:
            return False
    
    elif computer == "p":
        if player == "s":
            return True
        else:
            return False
        
    elif computer == "s":
        if player == "r":
            return True
        else:
            return False

randComputer = random.randint(1,3)

computer = "r"
player = input("Choose one option : Rock(r) , Paper(p) , Sisors(s) \n")

if randComputer == 1:
    computer = "r"
elif randComputer ==2:
    computer = "p"
else:
    computer = "s"

if computer == "r":
    print("The computer chose rock")
elif computer == "p":
    print("The computer chose papaer")
else:
    print("The computer chose sisors")

if player == "r":
    print("You chose rock")
elif player == "p":
    print("You chose papaer")
else:
    print("You chose sisors")

if gameWin() == True:
    print("You Won !")
elif gameWin() == False:
    print("You Loose !")
else:
    print("The game was tie !")