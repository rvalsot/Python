# name = input("Please, enter your last name: ")
# age = int(input("How old are you, {}? ".format(name)))
#
# #print(age)
#
# legal_age = 16
#
# if age >= legal_age:
#     print("Cool, you can have some beer {}".format(name))
# else:
#     print("You cannot enter this bar, come in {} years.".format(legal_age - age))
#
# print("\n End of the program")

## ---------------- Second part -----------------

print("Please, enter a number bewteen 1 and 12, you got 2 chances")
guess = int(input())

if guess < 6:
    print("Please, guess higher")
    guess = int(input())
    if guess == 6:
        print("You guess it right")
    else:
        print("Nope, badd one")
elif guess > 6:
    print("Please, guess lower")
    guess = int(input())
    if guess == 6:
        print("You guess it right")
    else:
        print("Nope, badd one #2.")
else:
    print("Congrats, first time guess was right")
