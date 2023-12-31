"""
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 종이에 0은 적혀있지 않다.

출력
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

-- 예제 입력 1
5
3 2 1 -3 -1

--- 예제 출력 1
1 4 5 3 2
"""

"""
# 정답은 나오지만 틀렸습니다가 나오는 코드 반례 확인 필요.
from collections import deque
import sys

de = deque()

n = int(input())
de = deque(map(int, input().split()))
idx = deque(i+1 for i in range(n))
result = []

for i in range(n):
    result.append(idx[0])
    tmp = de.popleft()
    if tmp > 0:
        tmp -= 1
    idx.popleft()
    de.rotate(tmp)
    idx.rotate(tmp)

for j in range(len(result)):
    if j == len(result):
        print(result[j])
    else:
        print(result[j], end=" ")
"""

"""
# 참고 : https://velog.io/@highcho/Algorithm-baekjoon-2346
import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
for i in range(n):
	p = deq.popleft() # pop(0)과 같은 결과를 가져오지만, pop(0)보다 더 빠르다
	print(p[0], end=' ')
	if p[1] > 0:
		deq.rotate(-(p[1] - 1)) # popleft된 1칸을 제외하고 시계 반대방향으로 회전
	else:
		deq.rotate(-p[1]) # 시계 방향으로 회전
"""

# from collections import deque
# import sys

# n = int(input())
# de = deque(map(int, input().split()))
# idx = deque(i+1 for i in range(n))

# print("de", de)
# print("idx", idx)


# for i in range(n):
#     tmp = de.popleft()
#     tmp_idx = idx.popleft()
#     print(tmp_idx, end = ' ')
#     if tmp > 0:
#         tmp -= 1
#     de.rotate(tmp)
#     idx.rotate(tmp)
#     print("for de", de)
#     print("for idx", idx)

"""
from collections import deque
import sys

n = int(sys.stdin.readline())
de = deque(map(int, sys.stdin.readline().split()))
idx = deque(i+1 for i in range(n))

for i in range(n):
    tmp = de.popleft()
    tmp_idx = idx.popleft()
    print(tmp_idx, end = ' ')
    if tmp > 0:
        tmp -= 1
    de.rotate(tmp)
    idx.rotate(tmp)
"""

import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for _ in range(n):
    p = deq.popleft()
    print(p[0], end = ' ')
    if len(deq) != 0:
        if p[1] > 0:
            for i in range(p[1]-1):
                tmp = deq.popleft()
                deq.append(tmp)
        else:
            for j in range(-(p[1])):
                tmp = deq.pop()
                deq.appendleft(tmp)