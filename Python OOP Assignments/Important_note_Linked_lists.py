# linked lists are more filxible (size wize), from normal lists, in breif its a group of nodes (each node has value and pointer)
#pointer always toward next node"in this type" ,,(starting with head , ending with tail where pionter = none)
#we can implement linked lists using objects in python
#as follows:

#create linked list contains (5, 4, 2, 7, 8,11)

class linked_list:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node

node1 = linked_list(5)
node2 = linked_list(4)
node3 = linked_list(2)
node4 = linked_list(7)
node5 = linked_list(8)
node6 = linked_list(11)

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5

#now we have nodes that each point to next one, only tail node points at None
#create a fucntion to connect them!
cuurent_node = node1.next_node
while cuurent_node is not None:
    print(cuurent_node.value, end=' --> ')
    cuurent_node = cuurent_node.next_node