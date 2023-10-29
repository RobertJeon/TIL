# 트리 노드 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # 생성자 함수
    def __init__(self, head):
        # 헤드 노드 삽입
        self.head = head

    # 노드 삽입 함수
    def insert_node(self, value):
        # 헤드를 시작 노드로 지정
        self.base_node = self.head
        # while 트리의 리프에 값이 없을때까지 반복:
        while True:
            # 1) if 넣는 값이 기존 노드보다 작은 경우:
            if value < self.base_node.value:
                # 1-1) if 기존 노드의 왼쪽(아래)에 값이 존재하는 경우:
                if self.base_node.left != None:
                    # 왼쪽(아래) 노드로 이동
                    self.base_node = self.base_node.left

                # 1-2) else 기존 노드의 왼쪽에 값이 존재하지 않는 경우:
                else:
                    # value를 값으로 가지는 새 노드를 왼쪽에 삽입
                    self.base_node.left = Node(value)
                    # print(value, '노드 생성')
                    break # 삽입 후 반복문 탈출

            # 2) else 넣는 값이 기존 노드보다 크거나 같은 경우:
            else:
                # 2-1) if 기존 노드의 오른쪽(아래)에 값이 존재하는 경우:
                if self.base_node.right != None:
                    # 왼쪽(아래) 노드로 이동
                    self.base_node = self.base_node.right
                # 2-2) else 기존 노드의 오른쪽(아래)에 값이 존재하지 않는 경우:
                else:
                    # value를 값으로 가지는 새 노드를 오른쪽에 삽입
                    self.base_node.right = Node(value)
                    # print(value, '노드 생성')
                    break # 삽입 후 반복문 탈출

    # 노드 탐색 함수
    def search_node(self, value):
        # 헤드를 시작 노드로 지정
        self.base_node = self.head
        # while 노드가 존재하는 동안 시작 노드부터 탐색:
        while self.base_node:
            # 1) if 입력값와 같은 값을 찾은 경우:
            if value == self.base_node.value:
                # print('찾았다.')
                # return True
                return True

            # 2) else 입력값과 다른 경우:
            else:
                # 2-1) if 입력값이 더 큰 경우
                if value > self.base_node.value:
                    # 노드의 오른쪽으로 이동
                    self.base_node = self.base_node.right
                    # print('오른쪽으로 이동')
                # 2-2) else 입력값이 더 작은 경우:
                else:
                    # 노드의 왼쪽으로 이동
                    self.base_node = self.base_node.left
                    # print('왼쪽으로 이동')
        # 찾는 값이 없는 경우 False 반환
        return False

if __name__ == "__main__":
    head = Node(16)
    bt = BinarySearchTree(head)

    bt.insert_node(12)
    bt.insert_node(19)
    bt.insert_node(11)
    bt.insert_node(13)
    bt.insert_node(18)
    bt.insert_node(20)
    bt.insert_node(9)
    bt.insert_node(8)
    bt.insert_node(10)

    print(bt.search_node(5))    #False
    print(bt.search_node(-2))   #False
    print(bt.search_node(18))   #True