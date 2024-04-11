"""
문제
상근이와 선영이는 동시에 가지고 있는 CD를 팔려고 한다. CD를 몇 개나 팔 수 있을까?

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 상근이가 가지고 있는 CD의 수 N, 선영이가 가지고 있는 CD의 수 M이 주어진다. N과 M은 최대 백만이다. 다음 줄부터 N개 줄에는 상근이가 가지고 있는 CD의 번호가 오름차순으로 주어진다. 다음 M개 줄에는 선영이가 가지고 있는 CD의 번호가 오름차순으로 주어진다. CD의 번호는 십억을 넘지 않는 양의 정수이다. 입력의 마지막 줄에는 0 0이 주어진다.

상근이와 선영이가 같은 CD를 여러장 가지고 있는 경우는 없다.

출력
두 사람이 동시에 가지고 있는 CD의 개수를 출력한다.

예제 입력 1 
3 3
1
2
3
1
2
4
0 0

예제 출력 1 
2
"""
import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    set_n = set()
    set_m = set()
    for _ in range(n):
        set_n.add(int(input()))
    for _ in range(m):
        set_m.add(int(input()))
    print(len(set_n & set_m))