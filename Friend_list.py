main = input(">>> ")
friends = []
if main == "add friend":
    friend = input("What Is Your Friends Name ? \n")
    print("your friends name is added succesfully")
    frnd = friends.append(friend)

    ask = input("Do you want to add anoter friend ?(y/n)")
if ask == "y":
    friend2 = input("What Is Your Friends Name ? \n")
    print("your friends name is added succesfully")
    frnd = friends.append(friend2)
if ask == "n":
    print("its okey")

printName = input("do you want to Show your friends name ? (y/n)\n")
if printName == "y":
    print(friends)
else :
    print("thanks for using this code :)")


# ask = input("Do you want to add anoter friend ?(y/n)")
# if ask == "y":
#     friend2 = input("What Is Your Friends Name ? \n")
#     print("your friends name is added succesfully")
#     frnd = friends.append(friend2)
# if ask == "n":
#     print("its okey")

# printName = input("do you want to Show your friends name ? (y/n)\n")
# if printName == "y":
#     print(friends)
# else :
#     print("thanks for using this code :)")

