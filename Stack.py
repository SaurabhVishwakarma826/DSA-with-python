# # Queue implementation in Python
#
# class Queue:
#
#     def __init__(self):
#         self.queue = []
#
#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)
#
#     # Display  the queue
#     def display(self):
#         print(self.queue)
#
#     def size(self):
#         return len(self.queue)
#
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
#
# q.display()
#
# q.dequeue()
#
# print("After removing an element")
# q.display()
#
# ### Exersize
#
# # For all exercises use Queue class implemented in main tutorial.
# #
# # Design a food ordering system where your python program will run two threads,
# #
# # Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# # Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# # Use this video to get yourself familiar with multithreading in python
# #
# # Pass following list as an argument to place order thread,
# #
# # orders = ['pizza','samosa','pasta','biryani','burger']



# import threading
# import time
from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, data):
#         self.buffer.append(data)
#
#     def dequeue(self):
#         if self.buffer == 0:
#             print("Stack is empty")
#         else:
#             return self.buffer.pop()
#
#     def isEmpty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
# food_order_queue = Queue()
#
# def place_order(orders):
#     for order in orders:
#         print("placing order : ",order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
#
# def serve_order():
#     time.sleep(1)
#     while True:
#         order = food_order_queue.dequeue()
#         print("Serving order : ",order)
#         time.sleep(2)
#
# if __name__ == '__main__':
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     t1 = threading.Thread(target=place_order, args=(orders,))
#     t2 = threading.Thread(target=serve_order)
#
#     t1.start()
#     t2.start()


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def reversPrint(self):
        length = self.stack
        rev = ''
        for i in range(len(length)):
            rev += self.stack.pop()
        return rev


ss = Stack()
ss.push(19)
ss.push(23)
ss.push(43)
ss.reversPrint()

