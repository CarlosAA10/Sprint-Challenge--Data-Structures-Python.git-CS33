class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.cur] = item
            self.cur = self.cur + 1
            
            if self.cur == self.capacity:
                self.cur = 0
        else:
            self.data.append(item)

    def get(self):
        return self.data