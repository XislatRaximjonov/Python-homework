n = int(input("Son kiriting: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

def even_numbers_if(a, b):
    # Find first even
    if a % 2 == 0:
        start = a
    else:
        start = a + 1

    # Find last even
    if b % 2 == 0:
        end = b
    else:
        end = b - 1

    # If the range is valid, generate even numbers
    if start <= end:
        return list(range(start, end + 1, 2))
    else:
        return []


print(even_numbers_if(3, 15))   # [4, 6, 8, 10, 12, 14]
