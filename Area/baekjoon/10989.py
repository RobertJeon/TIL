"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
10
5
2
3
1
4
2
3
5
1
7
예제 출력 1 
1
1
2
2
3
3
4
5
5
7
"""

"""
1차시도 - 메모리초과
import sys

input = sys.stdin.readline

n = int(input())
tmp = []
for _ in range(n):
    tmp.append(int(input()))
tmp.sort()
for i in range(len(tmp)):
    print(tmp[i])
"""

"""
2차시도 - 시간초과
test = {k: 0 for k in range(1,10001)}
key = set()

n = int(input())
for _ in range(n):
    tmp = int(input())
    test[tmp] += 1
    key.add(tmp)
key = list(key)
key.sort()

for i in key:
    for _ in range(test[i]):
        print(i)
"""

import sys

input = sys.stdin.readline

test = {k: 0 for k in range(1,10001)}
key = set()

n = int(input())
for _ in range(n):
    tmp = int(input())
    test[tmp] += 1
    key.add(tmp)
key = list(key)
key.sort()

for i in key:
    for _ in range(test[i]):
        print(i)

# 메모리 - 32948 KB
# 시간 - 10728 ms