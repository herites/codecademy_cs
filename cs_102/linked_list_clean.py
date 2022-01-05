#%%
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.length = 1

    def __repr__(self):
        return self.list_nodes()

    def insert_at_front(self, value):
        new_head = Node(value, next=self.head)
        self.head = new_head
        self.length += 1

    def list_nodes(self):
        lst = ""
        current_node = self.head
        while current_node:  # is not None:
            lst += str(current_node.value) + "\n"
            current_node = current_node.next
        return lst

    def remove_first(self, value_to_remove):
        current_node = self.head
        if current_node.value == value_to_remove:
            self.head = current_node.next
        else:
            while current_node:  # is not None:
                next_node = current_node.next
                if next_node.value == value_to_remove:
                    current_node.next = next_node.next
                    current_node = None
                    self.length -= 1
                else:
                    # will eventually result in None, breaking the while loop
                    current_node = current_node.next

    def remove_all(self, value_to_remove):
        current_node = self.head
        while current_node:  # is not None:
            if current_node.value == value_to_remove:
                self.head = current_node.next
                current_node = self.head
                self.length -= 1
            else:
                next_node = current_node.next
                if next_node:
                    if next_node.value == value_to_remove:
                        current_node.next = next_node.next
                        self.length -= 1
                    else:
                        current_node = next_node
                else:
                    current_node = None  # equals to break

    def swap_nodes(self, val1, val2):
        if val1 == val2:
            print("Elements are the same, swap not necessary.")
            return

        node1_prev = None
        node2_prev = None
        node1 = self.head
        node2 = self.head
        while node1:  # is not None:
            if node1.value == val1:
                break
            else:
                node1_prev = node1
                node1 = node1.next
        while node2:  # is not None:
            if node2.value == val2:
                break
            else:
                node2_prev = node2
                node2 = node2.next

        if node1 is None or node2 is None:
            print("Swap not possible, element(s) not found in list. ")
            return

        if node1_prev == None:
            self.head = node2
        else:
            node1_prev.next = node2
        if node2_prev == None:
            self.head = node1
        else:
            node2_prev.next = node1
        temp_next = node1.next
        node1.next = node2.next
        node2.next = temp_next


ll = LinkedList(6)
ll.insert_at_front(5)
ll.insert_at_front(4)
ll.insert_at_front(3)
ll.insert_at_front(2)
ll.insert_at_front(1)
print(ll)
ll.swap_nodes(2, 5)
print(ll)
