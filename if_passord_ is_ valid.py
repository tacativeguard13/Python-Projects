password = input("Ente the password\n")

passLenght= len(password)

if passLenght < 10:
    print("The password is invalid")
else:
    print("The password is valid")

print(type(passLenght))