from Singly_Linked_List import Node
from Singly_Linked_List import LinkedList


class HeadTail(LinkedList):
    def __init__(self):
        self.head = None

    def remove_head_tail(self):
        current = self.head
        while current.next.next:
            current = current.next
        before_last = current
        new_head = current.next
        before_last.next = None

        new_head.next = self.head
        self.head = new_head
        return self.head


ll = HeadTail()
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(8)
ll.insert_at_beginning(10)

ll.print_linked_list()

ll.remove_head_tail()
ll.print_linked_list()