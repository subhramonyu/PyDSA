class Node:
    def __init__(self,data = None,next = None):
        self.next = next
        self.data = data


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

    def delete(self,key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            current = None

        previous = None
        while current is not None and current.data!= key:
            previous = current
            current = current.next

        if current is not None:
            previous.next = current.next
            current = None



    


    def show(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current= current.next
        print("None")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.delete(20)
    ll.show()




