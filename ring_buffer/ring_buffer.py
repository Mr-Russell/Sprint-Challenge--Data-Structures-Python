class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.insert(self.oldest, item)
            self.storage.pop(self.oldest + 1)
            if self.oldest < self.capacity - 1:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return self.storage