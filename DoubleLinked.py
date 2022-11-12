# YouTube Video: https://www.youtube.com/watch?v=8kptHdreaTA
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def insert_at(self, index, data):
        if index == 0:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            while temp:
                if count == index - 1:
                    new_node = Node(data)
                    new_node.next = temp.next
                    new_node.prev = temp
                    temp.next = new_node
                    temp.next.prev = new_node
                    break
                temp = temp.next
                count +=1


    def delete_at(self,index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            temp = self.head
            while temp:
                if count == index - 1:
                    temp.next = temp.next.next
                    temp.next.prev = temp
                    break
                temp = temp.next
                count += 1




dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.insert_at(5, 10)
dllist.delete_at(5)
dllist.delete_at(1)
dllist.print_list()