import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Test
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())


from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        return date.today().year - self.birth_year


# Test
p = Person("Ali", "Uzbekistan", 2000)
print("Age:", p.age())



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"


# Test
calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 0))


import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Test
t = Triangle(3, 4, 5)
print("Triangle area:", t.area())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur, value):
        if value < cur.value:
            if cur.left:
                self._insert(cur.left, value)
            else:
                cur.left = Node(value)
        else:
            if cur.right:
                self._insert(cur.right, value)
            else:
                cur.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, cur, value):
        if not cur:
            return False
        if value == cur.value:
            return True
        elif value < cur.value:
            return self._search(cur.left, value)
        else:
            return self._search(cur.right, value)


# Test
b = BST()
b.insert(10)
b.insert(5)
b.insert(20)
print(b.search(20))
print(b.search(15))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"


# Test
s = Stack()
s.push(10)
s.push(20)
print(s.pop())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new

    def delete(self, value):
        cur = self.head
        if cur and cur.value == value:
            self.head = cur.next
            return

        prev = None
        while cur and cur.value != value:
            prev = cur
            cur = cur.next

        if cur:
            prev.next = cur.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.value, end=" -> ")
            cur = cur.next
        print("None")


# Test
l = LinkedList()
l.insert(10)
l.insert(20)
l.display()
l.delete(10)
l.display()


class ShoppingCart:
    def __init__(self):
        self.items = {}  # item: price

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total(self):
        return sum(self.items.values())


# Test
cart = ShoppingCart()
cart.add_item("Bread", 5000)
cart.add_item("Milk", 7000)
print(cart.total())


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Empty!"

    def display(self):
        print(self.items)


# Test
s = Stack()
s.push(1)
s.push(2)
s.display()


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0) if self.q else "Queue empty"

    def display(self):
        print(self.q)


# Test
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
q.display()


class Bank:
    def __init__(self):
        self.accounts = {}  # name: balance

    def create_account(self, name):
        self.accounts[name] = 0

    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            print("Not enough balance")

    def show_balance(self, name):
        return self.accounts.get(name, "No such account")


# Test
b = Bank()
b.create_account("Ali")
b.deposit("Ali", 1000)
b.withdraw("Ali", 300)
print(b.show_balance("Ali"))
