def modify_string(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0  # count characters since last underscore
    
    i = 0
    while i < len(txt):
        ch = txt[i]
        result.append(ch)
        count += 1

        # When 3 characters are collected, we must insert "_"
        if count == 3:
            # Determine where to place underscore
            pos = len(result)  # default position (after current)
            
            # Shift forward until character is NOT vowel AND NOT '_'
            while pos < len(txt) and (txt[pos] in vowels or txt[pos] == "_"):
                pos += 1

            # Add underscore only if not at end
            if pos < len(txt):
                result.append("_")

            count = 0  # reset counter
        
        i += 1

    # Ensure string never ends with underscore
    if result and result[-1] == "_":
        result.pop()

    return "".join(result)


n = int(input())

for i in range(n):
    print(i * i)

i = 1
while i <= 10:
    print(i)
    i += 1


n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 50 < num <= 150:
        print(num)

num = 75869
count = len(str(num))
print(count)

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

for i in range(-10, 0):
    print(i)

for i in range(5):
    print(i)
else:
    print("Done!")

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

n = 10
a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(f"{num}! = {fact}")

def uncommon_elements(list1, list2):
    result = []

    # Add elements from list1 that are NOT in list2
    for x in list1:
        if x not in list2:
            result.append(x)

    # Add elements from list2 that are NOT in list1
    for x in list2:
        if x not in list1:
            result.append(x)

    return result
