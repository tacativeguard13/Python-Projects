poem = open('Poem.txt', 'r')
poemStr = poem.read()

if 'Twinkle' in poemStr:
    print("The word is present in th poem")
else:
    print("The word is not present")

print(poemStr)

poem.close()