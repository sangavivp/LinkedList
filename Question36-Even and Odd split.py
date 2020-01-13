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

    def separate_old_even_nodes(self):
        even_head = odd_head = None
        temp = self.head
        while temp:
            if even_head is None:
                even_head = Node(temp.data)
            else:
                even_head.next = Node(temp.data)

            if odd_head is None:
                odd_head = Node(temp.next.data)
            else:
                odd_head.next = Node(temp.next.data)
             
            temp = temp.next.next
        print("Even List")
        temp1 = even_head
        while temp1:
            print(temp1.data)
            temp1 = temp1.next

        print("Odd List")
        temp1 = odd_head
        while temp1:
            print(temp1.data)
            temp1 = temp1.next


ll = LinkedList()
ll.insert_node_at_end(0)
ll.insert_node_at_end(1)
ll.insert_node_at_end(2)
ll.insert_node_at_end(3)
ll.insert_node_at_end(4)
ll.insert_node_at_end(5)

#ll.print_linked_list()
ll.separate_old_even_nodes()






