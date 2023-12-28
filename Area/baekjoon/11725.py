"""
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

--- 입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

--- 출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

--- 예제 입력 1
7
1 6
6 3
3 5
4 1
2 4
4 7

--- 예제 출력 1
4
6
1
3
1
4
"""

"""
시간초과 코드
def dfs_recur(start, graph, pr, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            if pr[node-1] == 0:
                pr[node-1] = start
            dfs_recur(node, graph, pr,visited)
    return visited, pr
n = int(input())
tree_ = {k+1:[] for k in range(n)}
for _ in range(n-1):
    k, v = map(int, input().split())
    tree_[k].append(v)
    tree_[v].append(k)
pr = [0 for i in range(n)]
dfs_recur(1, tree_, pr,visited=[])
for i in range(1, len(pr)):
    print(pr[i])
"""

# GPT 도움을 받은 코드
import sys
sys.setrecursionlimit(10**6)

def dfs_recur(start, graph, pr, visited):
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            if pr[node-1] == 0:
                pr[node-1] = start
            dfs_recur(node, graph, pr, visited)
    return pr

n = int(sys.stdin.readline())
tree_ = {k+1: [] for k in range(n)}
for _ in range(n-1):
    k, v = map(int, sys.stdin.readline().split())
    tree_[k].append(v)
    tree_[v].append(k)

visited = set()
pr = [0] * n
result = dfs_recur(1, tree_, pr, visited)

for i in range(1, len(result)):
    print(result[i])

# 다른 사람 코드
# https://d-cron.tistory.com/22

"""
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

arr = []

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])
"""