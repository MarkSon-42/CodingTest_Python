# Like stack, queue is a linear data structure...

# Queue :FIFO , Stack LIFO
queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

print(queue.pop())
print(queue.pop())
print(queue.pop())

print(queue.pop()) # error : pop from empty list

