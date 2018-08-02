class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)

    def __del__(self):
        pass
        # print("deleting {}".format(self))
        # FIXME
        # if self.prev is not None:
        #     self.prev.next = self.next
        # if self.next is not None:
        #     self.next.prev = self.prev

    def insert_after(self, prev_node):
        assert prev_node is not None

        next_node = prev_node.next
        prev_node.next = self
        self.next = next_node

        if next_node is not None:
            next_node.prev = self
        self.prev = prev_node


class LinkedList2:
    def __init__(self, values):
        self.head = None
        self.tail = None

        prev_node = None
        node = None
        for value in values:
            node = Node(value)
            node.prev = prev_node
            if prev_node is None:
                self.head = node
            else:
                prev_node.next = node
            prev_node = node
        self.tail = node

    def reverse(self):
        node = self.head
        while node is not None:
            next_node = node.next
            node.prev, node.next = node.next, node.prev
            node = next_node
        self.head, self.tail = self.tail, self.head

    def pprint(self):
        node = self.head
        while node is not None:
            print("{} -> ".format(node.value), end="")
            node = node.next
        print(flush=True)

    def pprint_reverse(self):
        node = self.tail
        while node is not None:
            print("{} -> ".format(node.value), end="")
            node = node.prev
        print(flush=True)

    def remove(self, item):
        node = self.head
        while node is not None:
            if node.value == item:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev

                break
            node = node.next

    def insert_after(self, value1, value2):
        """insert value2 after value1."""
        new_node = Node(value2)
        node = self.head
        while node is not None:
            if node.value == value1:
                new_node.insert_after(node)
                break
            node = node.next


if __name__ == '__main__':
    li = LinkedList2([5, 1, 3, 2])
    # li.pprint()
    # li.remove(5)
    # li.pprint()
    # li.pprint_reverse()
    li.reverse()
    li.pprint()
    # li.pprint()
    # li.remove(5)
    # li.pprint()
    # li.insert_after(5, 4)
    # li.pprint()
    # li.pprint_reverse()

# 5, 1, 3, 2
# => + 4
# 5.next = 4
# 4.prev = 5
# 4.next = 3
# 3.prev = 4
