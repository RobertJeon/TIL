"""
문제
평소 맛살을 즐겨 먹는 혜선은 맛살을 구입하러 2-마트에 갔다. 식품코너에서 맛살을 고르면서 혜선은 고민이 되기 시작했다. 여러 업체에서 나온 맛살들이 들어있는 개수도 다르고 가격도 다르기 때문에 어떤 것을 사야 싼 가격에 많이 먹을 수 있을지 생각해야 했기 때문이다. 

혜선은 현명하게도 각 맛살에 써진 중량(g)과 가격(원)을 다 조사해서 같은 가격으로 최대한 많은 중량을 살 수 있는 맛살을 사기로 했다. 혜선의 고민을 해결해 줄 프로그램을 작성하시오.

입력
입력은 표준입력(standard input)을 통해 받아들인다. 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스는 첫째 줄에는 맛살의 종류 N이 주어지고 두 번째 줄부터는 각 맛살의 중량(g) W와 가격(원) C가 순서대로 공백 하나를 사이에 두고 한 줄에 하나씩 N개가 주어진다. (1 ≤ N ≤ 100, 1 ≤ W ≤ 5000, 1 ≤ C ≤ 100000, W와 C는 정수)

출력
출력은 표준출력(standard output)을 통하여 출력한다. 각 테스트 케이스에 대해서 혜선이 사야 하는 맛살의 가격을 한 줄에 하나씩 출력하시오. 같은 가격으로 살 수 있는 최대 중량이 같은 맛살이 두 개 이상인 경우는 낮은 가격의 것을 사기로 한다. 

예제 입력 1 
3
2
300 2000
200 1500
3
320 2139
700 3200
1400 6400
5
250 1920
500 2980
430 2700
380 2350
340 2310
예제 출력 1 
2000
3200
2980
"""

"""내 오답
n = int(input())

for _ in range(n):
    start = 10001
    max_c = 0
    for _ in range(int(input())):
        w, c = map(int, input().split())
        if start > c/w:
            start = c/w
            max_c = c
        elif start == c/w:
            if max_c > c:
                mac_c = c
    print(max_c)
"""

import sys
for i in range(int(sys.stdin.readline())):
    startC=100001
    exb = 0
    for j in range(int(sys.stdin.readline())):
        a,b=map(int,sys.stdin.readline().split())
 
        if startC> b/a :
            startC=b/a
            exb=b
        elif startC== b/a:
            if exb>b: exb=b
    print(exb)