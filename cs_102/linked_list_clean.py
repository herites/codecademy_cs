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
        while current_node:
            lst += str(current_node.value) + "\n"
            current_node = current_node.next
        return lst

    def remove_first(self, value_to_remove):
        current_node = self.head
        if current_node.value == value_to_remove:
            self.head = current_node.next
        else:
            while current_node:
                next_node = current_node.next
                if next_node.value == value_to_remove:
                    current_node.next = next_node.next
                    current_node = None
                    self.length -= 1
                else:
                    current_node = current_node.next

    def remove_all(self, value_to_remove):
        current_node = self.head
        while current_node:
            if current_node.value == value_to_remove:
                self.head = current_node.next
                current_node = self.head
                self.length -= 1
            else:
                next_node = current_node.next
                if next_node:
                    if next_node.value == value_to_remove:
                        current_node.next = next_node.next
                    else:
                        current_node = next_node
                else:
                    current_node = next_node


ll = LinkedList(5)
ll.insert_at_front(10)
ll.insert_at_front(9)
ll.insert_at_front(10)
ll.insert_at_front(9)
print(ll)
# ll.remove_first(9)
ll.remove_all(5)
print(ll)
