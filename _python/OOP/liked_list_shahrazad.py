class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None 

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self 
        runner = self.head
        while(runner.next != None):
            runner = runner.next

        runner.next = new_node
        #new_node.next = None
        return self
    
    def print_value(self):
       runner = self.head
       while(runner.next != None):
           print(runner.value, end=' ---> ')
           runner = runner.next

       print(runner.value)
       return self    


my_list = SList()
my_list.add_to_tail(141).add_to_tail(302).add_to_tail(164).add_to_tail(530).add_to_tail(474).print_value()               