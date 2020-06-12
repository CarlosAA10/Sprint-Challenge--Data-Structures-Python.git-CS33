class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0
    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
		    
			self.__class__ = RingBufferFull
        # if len(self.data) == self.capacity:
        #     self.data.pop(0)
        #     self.data.append(item)
        # else:
        #     self.data.append(item)

    def get(self):
        return self.data