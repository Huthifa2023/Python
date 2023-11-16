# define a function that takes one input that is a function
# def invoker(callback):
#     # invoke the input pass the argument 2
#     print(callback(2))
# invoker(lambda x: 2 * x)
# invoker(lambda y: 5 + y)




class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None


    def addATHead(self,value):
        if self.head is None:
            self.head = Node(value)
            return self
        new_node = Node(value)
        current = self.head
        self.head = new_node
        self.head.next = current
        return self
    
    def addAtTail(self,value):
        if self.head is None:
            self.addATHead(value)
            return self
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        return self

    def addATIndex(self, index, value):
        if index < 0:
            return -1
        if index == 0:
            self.addATHead(value)
            return self
        new_node = Node(value)
        prev_node = self.head
        current_node = prev_node.next
        for i in range(index-1):   
            current_node = current_node.next
            if current_node is None:
                print('\nout of index try addAtTail method')
            prev_node = prev_node.next
        prev_node.next = new_node
        new_node.next = current_node
        return self

    def print_all_values(self):
        if self.head is None:
            print('\nthe list is empty')
        current = self.head
        while current is not None:
            print(f'{current.value}',end='-->')
            current = current.next
        return self

    def deleteATIndex(self,index):
        current = self.head
        if index < 0:
            print('\nindex out of range')
            return self
        if index == 0:
            self.head = current.next
            return self
        for i in range(index-1):
            current = current.next
            if current.next is None:
                print('\nindex out of range')
                return self
        current.next = current.next.next
        return self

    def get_val_at_index(self,index):
        if index < 0:
            print('\nindex out of range')
            return self
        if index == 0:
            print(f'\nthe value at index({index}) is {self.head.value}')
            return self
        current = self.head
        for i in range(index-1):
            current = current.next
            if current.next is None:
                print('\nindex out of range')
                return self
        print(f'\nthe value at index({index}) is {current.next.value}')
        return self
    


list0 = MyLinkedList()
list0.addAtTail(1).addAtTail(2).addAtTail(3).addATHead(0).addATIndex(3,'here')
list0.deleteATIndex(3).print_all_values()

list0.get_val_at_index(4)



