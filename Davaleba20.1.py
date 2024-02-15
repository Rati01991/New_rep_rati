class Stack:
    def __init__(self):
        self.stack = []

    #Use list append method to add element
    def push(self, data):
       self.stack.append(data)

    #Use list pop method to remove element
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else: 
            print("It's empty, you can't delete anything")
            return None
        
# Test:
list = Stack()
list.push(0)
list.push(1)
list.push(2)

# Print Poped element is:
print("Poped element is:", list.pop())
print("Poped element is:", list.pop())
print("Poped element is:", list.pop())

# When list is ampty:
print(list.pop())