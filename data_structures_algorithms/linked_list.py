"""Linked List."""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, values):
        prev_node = None
        head = None
        for value in values:
            node = Node(value)
            if head is None:
                head = node
            if prev_node is not None:
                prev_node.next = node
            prev_node = node
        self.head = head

    def pprint(self):
        node = self.head
        while node is not None:
            print("{} -> ".format(node.value), end="")
            node = node.next
        print()


if __name__ == "__main__":
    li = LinkedList([4, 3, 1, 5, ])
    li.pprint()
