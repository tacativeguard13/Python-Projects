letter = '''\nHello <|name|>

You are won in a compitation 
plese register on the link bellow

Team, Alibaug cycle club

Date <|Date|>
'''
name = input("Enter Your name\n")
date = input('''Enter Date\n''')
letter = letter.replace("<|name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)