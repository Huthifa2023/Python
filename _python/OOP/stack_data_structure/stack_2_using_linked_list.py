#in this file we built stack using linked_list, which is more practical than building it using list i think, 
#there is no stack like list in python, so the main idea is to make a stack using OOP

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            return self
        current = self.top
        self.top = new_node
        self.top.prev = current
        return self
    
    def pop(self):
        if self.top is None:
            print('Empty Stack!')
            return self
        current = self.top
        self.top = current.prev
        return self

    def peak(self):
        if self.top is None:
            print('Empty Stack!')
            return self
        print(f'\n{self.top.value} is the top of this stack')
        return self
    
    def display_elements(self):
        if self.top is None:
            print('Empty Stack!')
            return self
        runner = self.top
        while runner is not None:
            print(f'{runner.value}', end=' -> ')
            runner = runner.prev
        return self
#############################################################################

stack0 = Stack()
stack0.push(11).push(33).push(66).push(77).push(99).pop().display_elements()
stack0.peak()

    
