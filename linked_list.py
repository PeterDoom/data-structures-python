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



#TODO Add insertion to Linked list


linked_list = LinkedList()
node_1 = Node("Monday")
node_2 = Node("Tuesday")
node_3 = Node("Wednesday")
linked_list.head_value = node_1
linked_list.head_value.next_value = node_2
node_2.next_value = node_3

linked_list.print_list()
