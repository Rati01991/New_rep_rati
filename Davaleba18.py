#1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # ასე ჯობია:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2

print('Vector 1 =', v1)
print('Vector 2 =', v2)
print('Sum of vectors =', v3)

#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        # ასე ჯობია:
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author

# Example
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print("Book 1:", book1.title, "by", book1.author)
print("Book 2:", book2.title, "by", book2.author)
print("Book 3:", book3.title, "by", book3.author)

print("book1 == book2: are equal?", book1 == book2) 
print("book1 == book3: are equal?", book1 == book3) 