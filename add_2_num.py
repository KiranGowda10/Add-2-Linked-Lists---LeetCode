
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        elements1 = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements1.append(current_node.data)


add1 = LinkedList()
add1.append(1)
add1.append(2)
add1.append(3)
print(add1.display())
add2 = LinkedList()
add2.append(4)
add2.append(5)
add2.append(6)
print(add2.display())






