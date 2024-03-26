"""
문제
오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.

이 역사적인 순간을 맞이하기 위해 줄에서서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해 졌다.

두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.

줄에 서있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)

둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 231 나노미터 보다 작다.

사람들이 서 있는 순서대로 입력이 주어진다.

출력
서로 볼 수 있는 쌍의 수를 출력한다.

예제 입력 1 
7
2
4
1
2
2
5
1
예제 출력 1 
10
"""

"""
# 단순 구현 코드 - 시간복잡도 측면에서 문제가 큼.
import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
res = 0
for i in range(len(li)):
    max = 0
    for j in range(1,len(li[i:])):
        if li[i] >= max and li[i+j] >= max:
            max = li[i+j]
            res += 1
        else:
            break
print(res)
"""

# 정답코드
# 참고 : https://velog.io/@thguss/%EB%B0%B1%EC%A4%80-3015.-%EC%98%A4%EC%95%84%EC%8B%9C%EC%8A%A4-%EC%9E%AC%EA%B2%B0%ED%95%A9-with.-Python
oasis = [int(input()) for _ in range(int(input()))]

stack = [] # (키, cnt)로 append
result = 0

for o in oasis:

    # 스택 끝 값보다 키 크면 pop
    while stack and stack[-1][0]<o:
        result += stack.pop()[1]

    # 스택이 비어있으면 해당 키 append하고 continue
    if not stack:
        stack.append((o, 1))
        continue

    
    # 스택 끝 값의 키와 같을 때
    if stack[-1][0]==o:
        cnt = stack.pop()[1]
        result += cnt

        if stack: result += 1
        stack.append((o, cnt+1))

    # 스택 끝 값의 키보다 작을 때
    else:
        stack.append((o, 1))
        result += 1

# 결과값 출력
print(result)