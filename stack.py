class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item of the stack
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item of the stack without removing it
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)  # Return the number of items in the stack

# Example usage:
stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.peek())  # Output: c
print(stack.pop())  # Output: c
print(stack.size())  # Output: 2
