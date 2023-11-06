"""
대구과학고등학교 학생들은 내기를 좋아한다. 이번에는 이안이와 예환이가 서로의 공부를 위해 시험 성적으로 내기를 하려고 한다. 어떤 과목에서 점수를 비교해서 점수가 높은 사람은 공부를 아주 열심히 했으니 100원을 받고, 점수가 낮은 사람은 공부를 안한 벌금으로 50원을 낸다. 만약 점수가 같다면 둘다 공부를 열심히 했다고 치고 20원씩 받기로 했다.

그런데 여기서 맹점이 하나 있다. 이안이는 예환이와 학교가 다르기 때문에 예환이는 이안이가 어떤 과목 시험을 쳤는지 잘 모른다. 그래서 이안이는 공부를 열심히 한 척을 하기 위해 최대한 많은 과목에서 예환이를 이길 수 있도록 과목 간 점수를 바꾸고자 한다. 예를 들어 시험을 친 과목이 3과목이고 이안이가 받은 점수가 10점, 100점, 50점이고 예환이가 받은 점수가 50점, 80점, 40점이라면 이안이는 내기를 두 번 이기고 한 번 질 수 있다.

이안이가 얻는 돈이 최대가 되도록 도와주자.

-- 입력
첫 번째 줄에 시험을 본 과목의 수 
$N$이 주어진다.

두 번째 줄에는 
$N$ 과목에 대한 이안이의 점수들이 공백으로 구분되어 주어지고, 세 번째 줄에는 예환이의 점수들이 공백으로 구분되어 주어진다.

-- 출력
이안이가 받을 수 있는 돈의 최댓값을 출력한다. 이안이가 공부를 너무 안 했을 경우 벌금만 낼 수 있어 답이 음수인 경우가 존재함을 유의하라.

-- 예제 입력 1
3
10 20 30
40 50 60

-- 예제 출력 1
-150
"""
n = int(input())

ian = list(map(int, input().split()))
yeh = list(map(int, input().split()))

ian.sort(reverse=True)
yeh.sort(reverse=True)
res = 0
max = 0 
for i in range(len(ian)):
    res = 0
    for j in range(len(ian)):
        if ian[j] > yeh[(j+i)%n]:
            res += 100
        elif ian[j] == yeh[(j+i)%n]:
            res += 20
        else:
            res -= 50
    if res > max:
        max = res
    elif max == 0:
        max = res
print(max)

"""
틀렸던 코드들

n = int(input())
total_list = [[]for i in range(n)]
ian = list(map(int, input().split()))
yeh = list(map(int, input().split()))
total = 0
for i in range(len(ian)):
    for j in range(len(ian)):
        if ian[i] > yeh[j]:
            total_list[i].append(100)
        elif ian[i] == yeh[j]:
            total_list[i].append(20)
        else:
            total_list[i].append(-50)
    total += max(total_list[i])
print(total)

python3로 하면 시간초과 및 예제 2번 틀림.
이번엔 pypy로 제출했더니 성공함.
"""

"""
다른 사람 코드
N = int(input()) ; A = sorted(map(int,input().split())) ; B = sorted(map(int,input().split()))

A.reverse() ; B.reverse() ; Ans = 0 ; a = 1

for i in range(N) :
    if A[i] > B[i] : Ans += 100
    elif A[i] == B[i] : Ans += 20
    else : Ans -= 50

while A :
    A.pop() ; cnt = -50*(N-len(A))

    for i in range(len(A)) :
        if A[i] > B[i+a] : cnt += 100
        elif A[i] == B[i+a] : cnt += 20
        else : cnt -= 50

    Ans = max(Ans, cnt) ; a += 1

print(Ans)
"""