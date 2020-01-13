import Singly_Linked_List


class DeleteNAfterM(Singly_Linked_List.LinkedList):

    def __init__(self):
        self.head = None

    def delete_seq(self, m, n):
        current = self.head
        skip = 1
        count = 1
        while current and current.next:
            if skip == m:
                prev = current
                while count <= n and current.next:
                    current = current.next
                    count += 1
                prev.next = current.next
                current = prev.next
                skip = 1
                count = 1
            else:
                skip += 1
                current = current.next

    def del_seq_recursion(self, current, m, n):
        pass


ll = DeleteNAfterM()
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(8)
ll.insert_at_beginning(10)
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(6)
ll.insert_at_end(7)

ll.print_linked_list()

ll.delete_seq(2, 3)

print("Deleted Linked List")
ll.print_linked_list()


