inputed_string = input("Enter a string: ")

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "Y", "y"]
vowel_counter = 0


for char in inputed_string:
    if char in vowels:
        vowel_counter += 1

print(vowel_counter)
