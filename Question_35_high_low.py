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

    def create_high_lows(self):
        current = self.head.next
        prev = self.head

        while current.next:
            if current.data < prev.data:
                current.data, prev.data = prev.data, current.data

            if current.next.data > current.data:
                current.next.data, current.data = current.data, current.next.data

            prev = current.next
            current = current.next.next

        return self.head


ll = LinkedList()
ll.insert_node_at_end(1)
ll.insert_node_at_end(2)
ll.insert_node_at_end(3)
ll.insert_node_at_end(4)
ll.insert_node_at_end(5)
ll.insert_node_at_end(6)

#ll.print_linked_list()

ll.head = ll.create_high_lows()
ll.print_linked_list()





