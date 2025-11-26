my_dict = {3: 40, 1: 10, 2: 20, 4: 30}

# Ascending order
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc)

# Descending order
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)


d = {0: 10, 1: 20}

d[2] = 30
print(d)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)

n = 5

squares = {x: x*x for x in range(1, n+1)}
print(squares)

squares = {x: x*x for x in range(1, 16)}

print(squares)

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)

my_set = {1, 2, 3}

my_set.add(4)             # add single item
my_set.update([5, 6, 7])  # add multiple items

print(my_set)

my_set = {1, 2, 3, 4, 5}

my_set.remove(3)    # removes 3 (error if not found)
print(my_set)

my_set = {1, 2, 3, 4, 5}

if 10 in my_set:
    my_set.remove(10)
else:
    print("Item not found")

print(my_set)
