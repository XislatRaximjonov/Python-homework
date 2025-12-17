# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# string_utils.py

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50
print(divide(10, 2))     # 5.0

print(reverse_string("Python"))  # nohtyP
print(count_vowels("Python"))    # 1


# geometry/circle.py

import math

def area(radius):
    return math.pi * radius * radius

def circumference(radius):
    return 2 * math.pi * radius

from geometry import circle

print(circle.area(5))
print(circle.circumference(5))


# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


from .circle import calculate_area, calculate_circumference


# file_operations/file_reader.py

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# file_operations/file_writer.py

def write_file(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

from .file_reader import read_file
from .file_writer import write_file

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry
r = 5
print("Area:", calculate_area(r))
print("Circumference:", calculate_circumference(r))

# File operations
write_file("test.txt", "Hello Python")
content = read_file("test.txt")
print("File content:", content)
