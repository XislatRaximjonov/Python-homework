try:
    a = int(input("Son kiriting: "))
    b = int(input("Bo'luvchini kiriting: "))
    print(a / b)
except ZeroDivisionError:
    print("Xato: Nolga bo'lish mumkin emas!")

try:
    n = int(input("Butun son kiriting: "))
    print("Kiritilgan son:", n)
except ValueError:
    print("Xato: Butun son kiriting!")

try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Xato: Fayl topilmadi!")

try:
    a = input("1-son: ")
    b = input("2-son: ")
    
    a = float(a)
    b = float(b)
    
    print(a + b)

except ValueError:
    print("Xato: Faqat son kiriting!")


try:
    f = open("/root/secret.txt", "r")  # odatda ruxsat bo'lmaydi
    print(f.read())
except PermissionError:
    print("Xato: Faylni ochishga ruxsat yo'q!")

lst = [10, 20, 30]

try:
    print(lst[5])
except IndexError:
    print("Xato: Indeks ro'yxatdan tashqarida!")

try:
    x = input("Son kiriting: ")
    print("Kiritildi:", x)
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi!")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ArithmeticError:
    print("Arifmetik xato yuz berdi!")

try:
    f = open("file.txt", "r", encoding="ascii")
    print(f.read())
except UnicodeDecodeError:
    print("Xato: Kodlash muammosi (UnicodeDecodeError)!")

lst = [1, 2, 3]

try:
    lst.push(5)   # push metodi Python listlarda yo‘q
except AttributeError:
    print("Xato: Bunday metod mavjud emas!")


with open("file.txt", "r") as f:
    print(f.read())


n = int(input("Nechta qator o‘qilsin? "))

with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

text = input("Qo‘shimcha matn: ")

with open("file.txt", "a") as f:
    f.write(text + "\n")

with open("file.txt", "r") as f:
    print(f.read())

n = int(input("Oxirgi nechta qator? "))

with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line, end="")

with open("file.txt", "r") as f:
    lst = f.readlines()

print(lst)


text = ""

with open("file.txt", "r") as f:
    for line in f:
        text += line

print(text)

arr = []

with open("file.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

print(arr)

with open("file.txt", "r") as f:
    words = f.read().split()

longest = max(words, key=len)
print("Eng uzun so‘z:", longest)


with open("file.txt", "r") as f:
    print("Qatorlar soni:", len(f.readlines()))

from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().lower().replace(",", "").split()

print(Counter(words))


import os

print(os.path.getsize("file.txt"), "bayt")

lst = ["apple", "banana", "cherry"]

with open("file.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")

with open("file.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())


with open("file1.txt") as f1, open("file2.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip(), b.strip())

import random

with open("file.txt") as f:
    lines = f.readlines()

print(random.choice(lines))

f = open("file.txt", "r")
print(f.closed)  # False
f.close()
print(f.closed)  # True


with open("file.txt", "r") as f:
    cleaned = [line.strip() for line in f]

print(cleaned)


with open("file.txt", "r") as f:
    text = f.read().replace(",", " ")

words = text.split()
print("So‘zlar soni:", len(words))


import glob

chars = []

for filename in glob.glob("*.txt"):
    with open(filename, "r") as f:
        chars.extend(list(f.read()))

print(chars)

import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()

