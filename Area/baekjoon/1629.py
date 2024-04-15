"""
# 분할정복을 이용한 거듭제곱
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

예제 입력 1 
10 11 12
예제 출력 1 
4
"""

"""
지수 법칙
A^m+n = A^m x A^n

나머지 분배 법칙
(AxB)%C = (A%C) *(B%C) % C

예제에 적용한다면 다음과 같다.
a = 10 , b = 11 , c = 12
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x 
    (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
"""

import sys
input = sys.stdin.readline
def power(a, b, c):
    if b == 1:
        return a%c
        
    x = power(a, b//2, c)

    if b % 2 == 0:
        return (x * x) % c
    else:
        return (x * x * a) % c
a,b,c = map(int, input().split())
print(int(power(a,b,c)))

"""
이전 오답들
import math
import sys

input = sys.stdin.readline

a,b,c = map(int, input().split())

print(int(math.pow(a,b))%c)
"""