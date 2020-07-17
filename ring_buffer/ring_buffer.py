class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0
    def append(self, item):


        # self.data.append(item)
        # if len(self.data) == self.capacity:
            
	    #     self.__class__ = RingBufferFull
        #     self.cur = 0


        if len(self.data) == self.capacity:
            self.data[self.cur] = item
            self.cur = self.cur + 1
            if self.cur == self.capacity:
                self.cur = 0
        else:
            self.data.append(item)

    def get(self):
        return self.data


# class RingBufferFull:
# 	def __init__(self,n):
# 		raise "you should use RingBuffer"
# 	def append(self,x):		
# 		self.data[self.cur] = x
# 		self.cur = (self.cur+1) % self.max
# 	def get(self):
# 		return self.data[self.cur:]+self.data[:self.cur]