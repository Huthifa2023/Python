#question from leetcode 
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

    def Front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def Rear(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
        

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else: return False

    def isFull(self):
        if len(self.queue) >= self.length:
            return True
        else: return False

       
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()