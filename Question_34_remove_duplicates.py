class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def remove_duplicates(self):
        prev = self.head
        temp = self.head
        element_set = set()

        while temp:
            if temp.data in element_set:
                prev = temp.next
                temp = prev
            else:
                element_set.add(temp.data)
                print(element_set)
                prev = prev.next
                temp = temp.next
        self.print_linked_list()


ll = LinkedList()
ll.insert_node_at_end(1)
ll.insert_node_at_end(2)
ll.insert_node_at_end(3)
ll.insert_node_at_end(4)
ll.insert_node_at_end(4)
ll.insert_node_at_end(3)
ll.insert_node_at_end(2)
ll.insert_node_at_end(6)

ll.remove_duplicates()
