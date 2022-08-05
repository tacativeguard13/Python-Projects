main = input("Enter the number\n")

intOr = True

def validOrNot ():
    if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in main:
        return intOr == True
    else:
        return intOr == False

if intOr == True :
    print("The the given word is an int")
else:
    print("The given word is ann string")