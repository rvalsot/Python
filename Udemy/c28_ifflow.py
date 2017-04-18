__autor__ = 'rvalsot'


# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18 - age))
# # This is a comment

print("Please, give a number between 1 and 10.")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())

    if guess == 5:
        print("You're right, it's 5")
    else:
        print("Sorry, you didn't make it")
elif guess > 5:
    print("Please, guss lower")
    guess = int(input())
    if guess == 5:
        print("You're ok, it's 5")
    else:
        print("Nope, not right")
else:
    print("You got it first time, it's 5")
