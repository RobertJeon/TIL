# BFS 구현 - deque 사용
"""
1. 방문 리스트에 시작 노드를 기록
2. Queue에 시작노드의 인접 노드를 삽입(enqueue)
3. 큐에서 노드를 Dequeue하면서 방문처리(출력)한다.
4. 꺼내온 노드와 이웃한 노드를 큐에 넣는다.(enqueue)
방문했던 노드인지 아닌지 체크한다.
5. 큐에 아무 것도 남지 않을때까지 2-4 반복
6. 모든 노드를 방문할때까지 1-5를 반복
"""

# deque 라이브러리 불러오기
from collections import deque

# BFS 메서드 정의
def bfs(start_node, graph):
    # 방문 처리용 리스트 만들기
    visited = []
    # 시작 노드를 큐에 삽입
    queue = deque([start_node])

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에서 값을 뽑아낸다.
        cur_node = queue.popleft()  # 리스트의 queue.pop(0)과 같다. 그러나 시간복잡도 상수시간 보장
        # 해당 노드가 방문처리 된 노드라면
        if cur_node not in visited:
            # 방문처리용 큐에 노드 추가
            visited.append(cur_node)
            # 해당 노드의 인접한 노드를 큐에 추가
            queue.extend(graph[cur_node])
    return visited

# 테스트 해보기

graph_1 = {
    1: [2,5,3],
    2: [6,4],
    3: [4,7],
    4: [2,5,3],
    5: [1,5],
    6: [2],
    7: [3]
}

print(bfs(1, graph_1))   # [1, 2, 5, 3, 6, 4, 7]


"""
# deque 라이브러리를 활용한 queue 구현하기

# 우선 deque를 위해 자료구조의 큐에서 배웠던 내용을 복습한다.
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")             # append: 오른쪽끝 삽입   
queue.append("Graham")
# print(queue.pop())
print(queue.popleft())            # popleft: 왼쪽끝 빼오기 pop(0)와 같은 역할이지만 상수시간 보장
# print(queue.popleft())
print(queue)
"""