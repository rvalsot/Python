print("Extended For Loops")

number = "1,232,433,430"

cleanedNumber = ""

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

print("There were more than {} people in 1900!".format(newNumber))

print("---------------------------------------------------------")

for state in ["awe", "wer", "dfd", "qws"]:
    print("The tree characters: " + state)

for i in range (1, 25, 5):
    print("i is {}".format(i))

print("---------------------------------------------------------")

for i in range (1, 4):
    for j in range(3,6):
        print("{1} times {0} is {2}".format(i, j, i * j))

print("---------------------------------------------------------")
