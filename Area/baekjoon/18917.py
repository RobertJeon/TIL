"""
처음에 0이 하나 포함되어있는 배열 A가 있다. 이때, 다음 쿼리를 수행해야 한다.

1 x: A의 가장 뒤에 x를 추가한다.
2 x: A에서 x를 제거한다. A에 x가 두 개 이상 있는 경우에는 가장 앞에 있는 하나만 제거한다. 항상 A에 x가 있는 쿼리만 주어진다.
3: A에 포함된 모든 원소를 더한 값을 출력한다.
4: A에 포함된 모든 원소를 XOR한 값을 출력한다.

--입력
첫째 줄에는 쿼리의 개수 M이 주어진다. 둘째 줄부터 다음 M 개의 줄에 쿼리가 주어진다.

--출력
3번 혹은 4번 쿼리가 등장할 때마다, 답을 한 줄에 하나씩 출력한다.

1 ≤ M ≤ 500 000
1 ≤ x ≤ 1 000 000 000
3번 혹은 4번 쿼리가 적어도 하나 주어진다.

--입력 예제 1
12
1 3
1 1
1 4
3
4
1 1
3
4
2 1
2 4
3
4

--출력 예제 1
8
6
9
7
4
2
"""

"""이 전에 틀린 코드 1
n = int(input())
total = []
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        total.append(a[1])
    elif a[0] == 2:
        total.remove(a[1])
    elif a[0] == 3:
        print(sum(total))
    elif a[0] == 4:
        res = 0
        for i in range(len(total)):
            res = res ^ total[i]
        print(res)
"""

"""이 전에 틀린 코드 2
n = int(input())
total_sum = 0
total_xor = 0

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        total_sum += a[1]
        total_xor ^= a[1]
    elif a[0] == 2:
        total_sum -= a[1]
        total_xor ^= a[1]
    elif a[0] == 3:
        print(total_sum)
    else:
        print(total_xor)
"""


import sys

total_sum = 0
total_xor = 0
for _ in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1:
        total_sum += a[1]
        total_xor ^= a[1]
    elif a[0] == 2:
        total_sum -= a[1]
        total_xor ^= a[1]
    elif a[0] == 3:
        print(total_sum)
    else:
        print(total_xor)
