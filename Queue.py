import threading
import time
from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self, data):
        self.buffer.appendleft(data)

    def pops(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

q = Queue()

def place_orders(ord):
    for order in ord:
        print("placing order : ", order)
        q.push(order)
        time.sleep(0.5)

def serve_order():
    while True:
        time.sleep(1)
        orde = q.pops()
        print("Sevring Order : ",orde)
        time.sleep(2)

def binary(n):
    q.push("1")
    for i in range(n):
        front = q.front()
        print("  ", front)
        q.push(front+"0")
        q.push(front+"1")
        q.pops()
 

if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t = threading.Thread(target=place_orders, args=(orders,))
    t1 = threading.Thread(target=serve_order)
    binary(20)
    t.start()
    t1.start()

