
# 노드
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

# 연결리스트
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    
    # 추가하기
    def add_node(self, value):
        # head가 없을 경우 현재 추가하는 노드를 head 노드로
        if self.head == None:
            self.head = Node(value)
        
        else:
            node = self.head
            # 가장 마지막 노드에 도달하면 next 값 추가
            while node.next:
                node = node.next
            node.next = Node(value)
    
    # 삭제하기
    def del_node(self, value):
        # head가 비었다면 None 값을 반환
        if self.head == None:
            return None
        
        elif self.head.value == value:
            temp_node = self.head
            self.head = self.head.next
            del temp_node
        
        else:
            node = self.head
            while node.next:
                if node.next.value == value:
                    temp_node = node.next
                    node.next = node.next.next
                    del temp_node
                    return
                else:
                    node = node.next
    # 연결리스트 확인용
    def ord_desc(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    
    # 찾는 노드가 있는지 탐색
    def serach_node(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node.value
            else:
                node = node.next

# 출력 테스트
if __name__ == "__main__":
    linked_1 = LinkedList(1)
    linked_1.add_node(5)
    linked_1.add_node(9)
    linked_1.add_node(10)
    linked_1.ord_desc()
    linked_1.del_node(5)
    print("--삭제 이후--")
    linked_1.ord_desc()


