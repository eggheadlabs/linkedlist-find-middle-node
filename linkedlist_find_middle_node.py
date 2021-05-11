# How do you find the middle element of a singly linked list in one pass?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def middle(self):
        ptr_f = self.head   # fast pointer advances in two nodes
        ptr_s = self.head   # slow pointer finds the middle while the fast one reaches to the end
        while (ptr_f is not None and ptr_f.next is not None):
            ptr_f = ptr_f.next.next
            ptr_s = ptr_s.next
        return ptr_s.data

# Preparation: create the SinglyLinkedList according to a given data
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s.reverse()
sll = SinglyLinkedList()
for x in s: sll.push(x)

# find the middle in one pass 
if sll.head is not None:
    m = sll.middle()
    print('Found the middle element: ', m)
