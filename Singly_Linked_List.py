class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        current = self.head
        new_node = Node(data)

        if current is None:
            current = new_node
        else:
            new_node.next = current
            current = new_node

        self.head = current

    def insert_at_end(self, data):
        current = self.head
        new_node = Node(data)

        if current is None:
            current = new_node
            return current
        else:
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after(self, data, node):
        new_node = Node(data)
        node_after = Node(node)

        current = self.head
        next_node = None

        if current is None:
            return "Empty"
        else:
            while current:
                if current.data == node_after.data:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

    def delete_a_node(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            current = None

        else:
            while current.next:
                if current.next.data == data:
                    prev = current
                    current = current.next  # Moving the current pointer ahead
                    prev.next = current.next

                    break
                current = current.next

    def reversal(self, current):

        if current.next is None:
            self.head = current
            return

        self.reversal(current.next)
        old = current.next
        old.next = current
        current.next = None

    def cycle_detection_ll_hash(self):
        current = self.head
        hash_set = set()
        while current:
            if current.next in hash_set:
                return "Loop"
            else:
                hash_set.add(current)
                current = current.next
        return "No Loop"

    def cycle_detection_floyd_method(self):
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.remove_loop_floyd_extension(slow_p)
                return "Loop by Floyd"
        return "No Loop by Floyd"

    def remove_loop_floyd_extension(self, loop_node):
        ptr_1 = self.head

        while 1:
            ptr_2 = loop_node
            while ptr_2.next != loop_node and ptr_2.next != ptr_1:
                ptr_2 = ptr_2.next

            if ptr_2.next == ptr_1:
                break

            ptr_1 = ptr_1.next

        ptr_2.next = None
        print(ptr_2.data)

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


"""ll = LinkedList()

# INSERT AT THE BEGINNING
print("INSERT AT THE BEGINNING:")
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(8)
ll.insert_at_beginning(10)

ll.print_linked_list()


# INSERT AT THE END
print("INSERT AT THE END:")
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.print_linked_list()

# INSERT AFTER
print("INSERT AFTER:")
ll.insert_after(9, 2)
ll.print_linked_list()


# DELETE A NODE
print("Delete a Node at beginning")
ll.delete_a_node(10)
ll.print_linked_list()
print("Delete a Node")
ll.delete_a_node(1)
ll.print_linked_list()

# REVERSAL OF NODE
print("Reversing a linked list")
ll.reversal(ll.head)
ll.print_linked_list()

# GENERIC LOOP DETECTION METHOD
print(ll.cycle_detection_ll_hash())
print(ll.cycle_detection_floyd_method())
# Creating Loop
print("Loop setup", ll.head.next.next.next.next.next.data)
print(ll.head.next.next.data)
ll.head.next.next.next.next.next = ll.head.next.next
print(ll.cycle_detection_ll_hash())
print(ll.cycle_detection_floyd_method())

# REMOVING LOOP

ll.print_linked_list()"""



