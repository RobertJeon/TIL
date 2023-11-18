# 연결리스트로 큐 구현하기

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue_linked:
    def __init__(self):
        self.front = None       # 가장 먼저 들어온 위치
        self.rear = None        # 가장 마지막에 들어온 위치
    
    def enqueue(self, value):
        current = Node(value)
        if self.front == None:
            self.front = current
            self.rear = current       
        else:
            self.rear.next = current
            self.rear = self.rear.next
    
    def dequeue(self):
        if self.front == None:
            print("비었습니다.")
            return
        temp = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp

queue_1 = Queue_linked()
queue_1.enqueue(5)
queue_1.enqueue(7)
print(queue_1.front.data, queue_1.rear.data)
queue_1.enqueue(6)
print(queue_1.front.next.data, queue_1.rear.data)
queue_1.enqueue(8)
print(queue_1.front.next.next.data, queue_1.rear.data)
queue_1.dequeue()
print(queue_1.front.data, queue_1.rear.data)


"""
list로 구현

# 리스트로 큐를 구현해보기

class Queue_list(list):
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("비었습니다.")
            return
        return self.queue.pop(0)


queue_2 = Queue_list()
queue_2.enqueue(5)
queue_2.enqueue(7)
queue_2.enqueue(8)
print(queue_2.queue)
queue_2.dequeue()
queue_2.dequeue()
print(queue_2.queue)
"""