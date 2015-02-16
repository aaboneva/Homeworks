inputed_string = input("Enter a string: ")

counter = 0
sum_upper_vowels = []
sum_lower_vowels = []

upper_vowels = ["A", "E", "I", "O", "U", "Y"]
lower_vowels = ["a", "e", "i", "o", "u", "y"]

for char in inputed_string:
    if char in upper_vowels:
        counter += 1
        print(char)
        sum_upper_vowels.append(char)
        
    if char in lower_vowels:
        counter += 1
        print(char)
        sum_lower_vowels.append(char)

print(sum_upper_vowels)
print(sum_lower_vowels)


