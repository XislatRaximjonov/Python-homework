fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[2])   # third fruit

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)

numbers = [10, 20, 30, 40, 50, 60, 70]

new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(new_list)

movies = ["Titanic", "Avatar", "Interstellar", "Inception", "Joker"]

movies_tuple = tuple(movies)
print(movies_tuple)

cities = ["London", "Paris", "Berlin", "Rome"]

print("Paris" in cities)

nums = [1, 2, 3]

duplicate = nums * 2
print(duplicate)

nums = [11, 22, 33, 44, 55]

nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

numbers = (1,2,3,4,5,6,7,8,9,10)

print(numbers[3:7])

colors = ["blue", "red", "green", "blue", "yellow", "blue"]

print(colors.count("blue"))

animals = ("dog", "cat", "lion", "tiger", "wolf")

print(animals.index("lion"))

t1 = (1,2,3)
t2 = (4,5,6)

merged = t1 + t2
print(merged)

lst = [1,2,3,4]
tup = (10,20,30)

print("List length:", len(lst))
print("Tuple length:", len(tup))

numbers = (10,20,30,40,50)

numbers_list = list(numbers)
print(numbers_list)

numbers = (4,2,8,6,1,9)

print("Max:", max(numbers))
print("Min:", min(numbers))

words = ("hello", "world", "python")

reversed_tuple = words[::-1]
print(reversed_tuple)



