num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1 > num2):
    sf1 = num1
else:
    sf1 = num2

if (num3 > num4):
    sf2 = num3
else:
    sf2 = num4

if (sf1 > sf2):
    print(str(sf1) + " is the greatest")
else:
    print(str(sf2) + " is greatest")


