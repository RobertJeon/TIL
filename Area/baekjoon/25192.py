"""
알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.

ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.

새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.

채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!

입력
첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 
$N$ 이 주어진다. (
$1 \le N \le 100\,000$)

두 번째 줄부터 
$N$ 개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다. (문자열길이
$1 \le \texttt{문자열 길이} \le 20$)

첫 번째 주어지는 문자열은 무조건 ENTER이다.

출력
채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.

--- 입력 예제 1
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402
--- 출력 예제 1
8
"""

from sys import stdin

input = stdin.readline

n = int(input())
gom = set()
cnt = 0

for _ in range(n):
    user = input().strip()
    if user == 'ENTER':
        cnt += len(gom)
        gom = set()
    else:
        gom.add(user)

cnt += len(gom)
print(cnt)

"""
# 시간초과 코드
import sys
n = int(sys.stdin.readline())
wait = set()
res = 0
for _ in range(n):
    tmp = sys.stdin.readline()
    if tmp == "ENTER":
        res += len(wait)
        wait = set()
    else:
        wait.add(tmp)
res += len(wait)
print(res)
"""