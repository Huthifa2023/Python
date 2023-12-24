#a. Write a function in any programming language to reverse a linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Slist:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self
#b. Implement a method to detect if a linked list has a cycle.
    def has_cycle(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            if prev.next == next:
                return 'yes it has a cycle'
        return 'no cycle detected'

        
