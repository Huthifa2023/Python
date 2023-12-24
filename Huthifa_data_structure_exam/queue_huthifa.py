#a. Implement a circular queue in a programming language of your choice(Python or Js). 
class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = []
        self.length = k

    def enQueue(self, value):
        if len(self.queue) >= self.length:
            return False
        self.queue.append(value)
        return True

    def deQueue(self):
        if len(self.queue) < 1:
            return False
        self.queue.pop(0)
        return True
