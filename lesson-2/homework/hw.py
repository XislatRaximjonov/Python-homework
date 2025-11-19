# Ask for user's name
name = input("Enter your name: ")

# Ask for user's year of birth
year_of_birth = int(input("Enter your year of birth: "))

# Calculate age
current_year = 2025
age = current_year - year_of_birth

# Display result
print(f"Hello {name}, you are {age} years old.")


txt = "LMaasleitbtui"

# Even index letters → first hidden car name
car1 = txt[0::2]

# Odd index letters → second hidden car name
car2 = txt[1::2]

print(car1)  # Lasetti
print(car2)  # Malibu


txt = 'MsaatmiazD'

car1 = txt[0::2]       # Even indices → "Matiz"
car2 = txt[1::2][::-1] # Odd indices reversed → "Damas"

print(car1)  # Matiz
print(car2)  # Damas


txt = "I'am John. I am from London"

# Split the text into words
words = txt.split()

# Find the word after "from"
index = words.index("from")
residence = words[index + 1]

print(residence)   # London

# Ask for user input
text = input("Enter a string: ")

# Print reversed string
print("Reversed:", text[::-1])


text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)

print("Number of vowels:", count)


numbers = input("Enter numbers separated by space: ").split()

# Convert to integers
numbers = list(map(int, numbers))

print("Maximum value:", max(numbers))


word = input("Enter a word: ")

if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


email = input("Enter your email address: ")

domain = email.split("@")[1]

print("Domain:", domain)


import random
import string

length = 12  # You can change password length

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
