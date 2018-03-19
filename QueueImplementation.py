from Queue import Queue

q = Queue()
print(q.isEmpty())
q.enqueue('Aman')
q.enqueue('Madan')
q.enqueue('xyz')
q.dequeue()
print(q.size())