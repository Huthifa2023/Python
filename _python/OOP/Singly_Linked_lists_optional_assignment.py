class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self):
        self.head = None
    
    def add_to_end(self, value):
        if self.head == None:	
            self.head = Node(value)
            return self	
        new_node = Node(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	
        return self

    def delete_at_index(self,position):
        if position == 0:
            self.head = self.head.next
            return self
        current_node = self.head
        i = 0
        while i < position:
            prev_node = current_node
            current_node = current_node.next
            i += 1
        if i == 0:
            self.head = self.head.next
        else:
            prev_node.next = current_node.next
            current_node.value = None
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value,end='-->')
            runner = runner.next
        return self
    

list0 = Slist()
list0.add_to_end('huthifa').add_to_end('Ahmad').add_to_end('Ismael').add_to_end("Alqasim")
list0.delete_at_index(0).print_values()




























# def add_to_front(self,val):
#         new_node = Node(val)
#         Current_head = self.head
#         new_node.next = Current_head
#         self.head = new_node
#         return self