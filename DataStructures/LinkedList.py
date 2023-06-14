class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            previousHead = self.head
            self.head = node
            node.next = previousHead


def build_ll():
    ll = LinkedList()
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    return ll


if __name__ == '__main__':
    ll = build_ll()
    pass




