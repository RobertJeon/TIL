"""
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

--- 입력 예제 1
5 3
5 4 3 2 1
1 3
2 4
5 5

--- 출력 예제 1
12
9
1
"""
"""
# 시간초과 코드
import sys

n, m = map(int,sys.stdin.readline().split())
target_li = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(sum(target_li[start-1:end]))

시간초과가 발생한 이유는 구간합을 구할 때 인덱싱하여 sum을 하면 이경우엔 수많은 값을 진행할때 시간복잡도가 O(n)이 되어 값이 많으면 처리 시간도 그만큼 오래 걸리게 된다.

구간합을 구해놓고 해당 인덱스의 빼기를 진행하면 원하는 값이 구해지게 된다.
"""

import sys

n, m = map(int, sys.stdin.readline().split())
n_li = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]

tmp = 0
for i in n_li:
    tmp += i
    prefix_sum.append(tmp)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b]-prefix_sum[a-1])