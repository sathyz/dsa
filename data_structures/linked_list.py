"""Linked List."""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)


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
        for node in iter(self):
            print("{} -> ".format(node.value), end="")
        print(flush=True)

    def __delitem__(self, value):
        """delete node with value."""
        print("Deleting: {}".format(value))
        prev_node = None
        for node in iter(self):
            if node.value == value:
                if prev_node is None:
                    # delete head node
                    self.head = node.next
                else:
                    prev_node.next = node.next
                break
            prev_node = node

    def insert_after(self, value1, value2):
        """insert value2 after value1."""
        print("insert {} after {}".format(value2, value1))
        for node in iter(self):
            if node.value == value1:
                new_node = Node(value2, node.next)
                node.next = new_node
                break

    def insert_before(self, value1, value2):
        """insert value2 after value1."""
        print("inserting {} before {}".format(value2, value1))
        prev_node = None
        for node in iter(self):
            if node.value == value1:
                if prev_node is None:
                    new_node = Node(value2, node)
                    self.head = new_node
                else:
                    new_node = Node(value2, node)
                    prev_node.next = new_node
                break
            prev_node = node

    def is_circular(self):
        fast = self.head
        slow = self.head
        slow_step = False
        for node in iter(self):
            if slow_step:
                slow = slow.next
            fast = fast.next
            if fast is slow:
                return True
            slow_step = not slow_step
        return False

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        size = 0
        for node in iter(self):
            size += 1
        return size

    def __contains__(self, value):
        for node in iter(self):
            if node.value == value:
                return True
        return False

    def reverse(self):
        prev_node = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node


if __name__ == "__main__":
    li = LinkedList([3, 1, 5, ])
    li.reverse()
    li.pprint()
    # li.pprint()
    # li.delete(1)
    # li.pprint()
    # li.insert_after(3, 4)
    # li.pprint()
    # del li[4]
    # li.pprint()
    # li.insert_before(3, 4)
    # li.pprint()
    # del li[5]
    # li.pprint()
    # print(len(li))
    # print(4 in li)

    # li = LinkedList([4, 1, 3, 5, 2, ])
    # print(li.is_circular())
    # n1 = li.head.next
    # print(n1)
    # node = li.head
    # while node.next is not None:
    #     node = node.next
    # node.next = n1
    # print(li.is_circular())
