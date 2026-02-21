from myqueue import Queue

longqueue = Queue(3)

longqueue.complain()

longqueue.enqueue("Meow")
longqueue.enqueue("hello")
print(longqueue.dequeue())
print(longqueue.peek())

longqueue.enqueue(2)
longqueue.enqueue(3)
longqueue.enqueue(4)

emptyqueue = Queue(2)
emptyqueue.peek()
emptyqueue.dequeue()