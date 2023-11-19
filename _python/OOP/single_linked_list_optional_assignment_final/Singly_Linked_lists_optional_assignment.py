class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self):
        self.head = None

    def print_length(self):
        if self.head == None:
            print('\nthis list has 0 elements')
            return self
        current = self.head
        counter = 1
        while current.next is not None:
            current = current.next
            counter += 1
        print(f'\nthis list has {counter} elements')
        return self 

    def print_all_values(self):
        if self.head == None:
            print('\nthis list has 0 elements')
            return self
        current = self.head
        while current is not None:
            print(current.value,end='--->')
            current = current.next
        return self

# # #   add methods  #   #   #
    def add_to_end(self, value):
        if self.head == None:
            self.head = Node(value)
            return self
        current = self.head
        while current.next != None:
            current =current.next
        current.next = Node(value)
        return self

    def add_to_start(self, value):
        if self.head == None:
            self.head = Node(value)
            return self
        current = self.head
        new_node = Node(value)
        self.head = new_node
        new_node.next = current
        return self


    def add_at_index(self,value,index):
        if index == 0:
            self.add_to_start(value)
            return self
        if index < 0:
            print(f'cannot add value:({value}) at index=({index}), reason: out of range. Try "add_to_start method" instead!')
            return self
        new_node = Node(value)
        prev_val = self.head
        curr_val = prev_val.next
        for i in range(1,index):
            prev_val = prev_val.next
            if curr_val.next == None:
                print(f'cannot add value:({value}) at index=({index}), reason: out of range. Try "add_to_end method" instead!')
                return self
            curr_val = curr_val.next
        prev_val.next = new_node
        new_node.next = curr_val
        return self

# # #   Remove methods  #   #   #
    def remove_from_end(self):
        current_val = self.head
        if current_val.next is None:
            current_val.value = None
            return self
        while current_val.next.next is not None:
            current_val = current_val.next
        current_val.next = None
        return self

    def remove_from_start(self):
        self.head = self.head.next
        return self
    
    def remove_at_value(self,value):
        current = self.head
        if current.value == value:
            self.remove_from_start()
            return self
        next_value = current.next
        while next_value.value != value:
            next_value = next_value.next
            current = current.next
        current.next = next_value.next
        return self
            
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self


        
####################################################################
list0 = Slist()
list0.add_to_end('one').add_to_end('two').add_to_end('three').add_to_end('four').add_to_start('zero').add_at_index('random',3).add_to_end('hhhh').add_to_start('bbbb')

list0.add_at_index('huthifa',0).add_to_end('buckbcuk').add_to_end('sucksuck')
list0.add_at_index('alqasim',2)
list0.add_at_index('Ahmad',4)
list0.remove_from_end().remove_from_end().remove_from_end()
list0.remove_from_start().add_at_index('BABABA',10)
list0.remove_at_value('random').remove_at_value('two').add_at_index('duckduck',66)


list0.add_at_index('last',7).add_at_index('test',-4)
list0.print_all_values().print_length()


