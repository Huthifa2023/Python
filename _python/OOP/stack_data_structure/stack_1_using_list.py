#in this file, we built a stack (LIFO: last in first out) where we have only one pointer that is top, 
#represent stack using list is easy, (but i think there is no point for this, cuz just use the list as it is, but ok for sake testing)



class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)
        return self

    def pop(self):
        self.list.pop()
        return self
        

    def top(self):
        top_value = self.list[-1]
        print(f"the top value fro this stack is:{top_value}")
        return self

    def getMin(self):
        print(f'minimum value in this stack is:{min(self.list)}')
        return self
    
    def display_stack(self):
        for i in self.list:
            print(f'{i}',end='->')

stack_1 = Stack()
stack_1.push(0).push(1).push(2).push(3)
stack_1.top()