validity = True

while validity == True :
    #These are the main thre inputs
    num1 = int(input())
    sign = input()
    num2 = int(input())

        #Let us use the logic
    if sign == '+':
        print(num1+num2)
    elif sign == '-':
        print(num1-num2)
    elif sign == '*':
        print(num1*num2)
    elif sign == '/':
        print(num1/num2)