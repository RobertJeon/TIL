# 연결리스트로 구현하기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack_linked:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        current = Node(value)
        current.next = self.head
        self.head = current

    def pop(self):
        if self.head == None:
            print("비었습니다.")
            return
        current = self.head.data
        self.head = self.head.next
        return current

stack_1 = Stack_linked()
stack_1.push(5)
stack_1.push(7)
stack_1.push(9)
print(stack_1.head.data)
stack_1.pop()
print(stack_1.head.data)
stack_1.pop()
stack_1.pop()
stack_1.pop()


# 리스트로 구현하기
"""
# 리스트로 스택 구현하기

class Stack_list(list):
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            print("비었습니다.")
            return
        else:
            self.stack.pop()

stack_2 = Stack_list()
stack_2.push(5)
stack_2.push(6)
stack_2.push(7)
print(stack_2.stack)
stack_2.pop()
stack_2.pop()
stack_2.pop()
stack_2.pop()
print(stack_2.stack)
"""