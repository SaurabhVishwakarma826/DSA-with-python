class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print(" list is empty")
            return
        itr = self.head
        llist =''
        while itr:
            llist += str(itr.data)+'-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llist)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr :
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid index")
        if index == 0:
            self.head= self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_value(self, new_data):
        self.head = None
        for data in new_data:
            self.insert_at_last(data)

ll = LinkedList()
ll.insert_value([10,20,30,40,50])
ll.insert_at_beginning(5)
ll.insert_at_last(60)
ll.insert_at(5, 45)
ll.remove_at(5)
ll.print()
ll.getLength()