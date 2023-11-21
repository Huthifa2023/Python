    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        self.list.pop()
        

    def top(self):
        top_value = self.list[-1]
        return top_value

    def getMin(self):
        return min(self.list)