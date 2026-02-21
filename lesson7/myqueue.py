class Queue():
    def __init__(self, max):
        self.list = [None] * max
        self.max = max
        self.front = 0
        self.rear = 0
        self.avaliable = max

    def enqueue(self, item):
        if self.avaliable > 0:
            self.list[self.rear] = item
            self.rear = (self.rear + 1) % self.max
            self.avaliable -= 1
        else:
            print("Queue full, cannot enqueue")
        
    def complain(self):
        print("This queue is sooo long and boring")
        
    def dequeue(self):
        if self.avaliable < self.max:
            item = self.list[self.front]
            self.list[self.front] = None
            self.front = (self.front + 1) % self.max
            self.avaliable += 1
            return item
        else:
            print("Queue empty, cannot dequeue")
    
    def peek(self):
        if self.avaliable < self.max:
            return self.list[self.front]
        else:
            print("Queue empty, cannot peek")