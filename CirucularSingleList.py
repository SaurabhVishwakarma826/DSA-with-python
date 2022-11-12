class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=None

class CircularSingleLinked:
    def __init__(self):
        self.head=None

    def insert_beginn(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            node.next = self.head
        else:
            ptr = self.head
            while ptr.next!=self.head:
                ptr = ptr.next
            node = Node(data)
            node.next=self.head
            ptr.next = node
            self.head = node

    def insert_last(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            node.next = self.head
        ptr = self.head
        while ptr.next!=self.head:
            ptr = ptr.next
        node = Node(data)
        ptr.next = node
        node.next = self.head

    def delete_begin(self):
        if self.head is None:
            print("List  is empty")
        elif self.head.next is self.head:
            self.head=None
        else:
            ptr = self.head
            while ptr.next!=self.head:
                ptr = ptr.next
            ptr.next = self.head.next
            self.head = ptr.next

    def delete_last(self):
        if self.head is None:
            print("lsit is empty")
        elif self.head.next is self.head:
            self.head=None
        else:
            ptr = self.head
            while ptr.next!=self.head:
                preptr = ptr
                ptr = ptr.next
            preptr.next = ptr.next

    def display(self):
        if self.head is None:
            print("List is empty")

        else:
            ptr = self.head
            while ptr.next!=self.head:
                print(" ", ptr.data)
                ptr = ptr.next
            print(" ",ptr.data)


cll = CircularSingleLinked()
cll.insert_beginn(10)
cll.insert_beginn(15)
cll.insert_last(20)
cll.insert_last(25)
cll.delete_begin()
cll.delete_last()
cll.display()