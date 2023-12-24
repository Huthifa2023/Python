#a. Write a function in any programming language to reverse a linked list.
class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)
        return self

    def pop(self):
        self.list.pop()
        return self

    def length_stack(self):
        return len(self.list)

stack0 = Stack()

# b. Write a program to check if a given expression with parentheses is balanced using a stack.
def is_balanced(exp):
    for i in exp:
        if i == '(':
            stack0.push(')')
        elif i == '[':
            stack0.push(']')
        elif i == '{':
            stack0.push('}')
        else:
            if stack0.length_stack == 0 or i != stack0.pop():
                return "not balanced"
    return "is balanced"