"""
문제
solved.ac 사이트에는 문제를 며칠 연속으로 풀었는지 보여주는 지표가 있는데, 이를 스트릭이라고 한다. 총 
$x$일 동안 매일 
$1$문제 이상을 빠짐없이 풀었다면 스트릭 
$x$일이라고 한다.

최장 스트릭은 총 
$N$일 기간 내에 달성한 스트릭 중 가장 큰 값을 의미한다. 
$N$일 동안의 푼 문제 수를 입력받아 최장 스트릭을 구하시오.

입력
첫 번째 줄에 
$N$이 주어진다. 
$(1 \le N \le 1\,000)$ 

두 번째 줄에 
$s_1$, 
$s_2$, 
$\cdots$, 
$s_N$이 공백으로 구분되어 주어진다. 
$s_i$는 
$i$일차에 푼 문제 수를 의미한다. 
$(0 \le s_i \le 100)$ 

출력
최장 스트릭을 출력한다.

예제 입력 1 
4
1 4 0 1
예제 출력 1 
2
예제 입력 2 
5
1 6 3 8 3
예제 출력 2 
5
예제 입력 3 
3
0 100 0
예제 출력 3 
1
예제 입력 4 
1
0
예제 출력 4 
0
"""
n = int(input())
tmp = list(map(int, input().split()))

max_day = 0
s = 0

for i in tmp:
    if i != 0:
        s += 1
    else:
        if max_day < s:
            max_day = s
        s = 0
if max_day < s:
    max_day = s
print(max_day)