"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

-- 입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

-- 출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.


-- 입력 예시 1
5
2 4 -10 4 -9

-- 출력 예시 1
2 3 0 3 1
"""

n = int(input())
a = list(map(int, input().split()))
unique_values = list(set(a))

count_dict = {value: index for index, value in enumerate(sorted(unique_values))}
result = [count_dict[value] for value in a]

print(" ".join(map(str, result)))

"""
# 시간초과 코드

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = list(set(a))
for i in range(n):
    count = 0
    for j in range(len(b)):
        if a[i] > b[j]:
            count += 1
    if i == n:
        print(count)
    else:
        print(count, end=" ")
"""