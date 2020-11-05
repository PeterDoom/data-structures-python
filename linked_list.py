class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None


class LinkedList:
    def __init__(self):
        self.head_value = None

    def print_list(self):
        print_value = self.head_value
        while print_value is not None:
            print(print_value.value)
            print_value = print_value.next_value

    def reverse_list(self):
        prev = None
        current = None
        while current is not None:
            next = current.next_value
            current.next_value = prev
            prev = current
            current = next
        self.head_value = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head_value
        self.head_value = new_node


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist.reverse_list()

llist.print_list()