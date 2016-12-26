for i in range (1,12):
    print("i is now {}".format(i))

print("-----------------------------------------\n")

a_number = "12,3,4kifi,3"

for i in range(0, len(a_number)):
    print(a_number[i])

print("-----------------------------------------\n")

a_string = "oiajfiew"
justVowels = ""

for i in range (0, len(a_string)):
    if a_string[i] in 'aeiou':
        print(a_string[i])
        justVowels = justVowels + a_string[i]

print("Just the vowels: {}".format(justVowels))
#
