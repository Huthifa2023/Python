#create linked list contains (5, 4, 2, 7, 8,11)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkeList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


