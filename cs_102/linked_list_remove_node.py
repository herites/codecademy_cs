#%%
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        self.length = 1

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value, next_node=self.head_node)
        self.head_node = new_node
        self.length += 1

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_first_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                    self.length -= 1
                else:
                    current_node = next_node

    def remove_all_nodes(self, value_to_remove):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() == value_to_remove:
                self.head_node = current_node.get_next_node()
                current_node = self.head_node
                self.length -= 1
            else:
                next_node = current_node.get_next_node()
                if next_node != None:
                    if next_node.get_value() == value_to_remove:
                        current_node.set_next_node(next_node.get_next_node())
                        self.length -= 1
                    else:
                        current_node = next_node
                else:
                    current_node = next_node

    def get_length(self):
        return self.length


ll = LinkedList(8)
ll.insert_beginning(10)
ll.insert_beginning(10)
ll.insert_beginning(10)
ll.insert_beginning(21)
print(ll.stringify_list())
print(f"list is {ll.get_length()} items long")
# ll.remove_first_node(21)
ll.remove_all_nodes(8)
print(ll.stringify_list())
print(f"list is {ll.get_length()} items long")
