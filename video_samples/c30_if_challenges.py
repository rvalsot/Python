# Write a program that asks for age and name,
# Check if person is bewteen 18-30 years
# Welcome with a holiday or refuse

print("Welcome to the 20s")
name = input("What's your name? ")
age  = int(input("Whats your age {}? ".format(name)))

if age >= 18 and age <= 30:
    print("Welcome to your 20's! Gotta to learn and work!")
else:
    print("You're not at your 20s, not overwelmingly crucial, enjoy!")
