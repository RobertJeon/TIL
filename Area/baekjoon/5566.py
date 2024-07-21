"""
문제
상근이는 혼자 보드 게임을 하고 있다. 이 보드 게임의 보드는 N칸으로 이루어져 있고, 출발점은 1칸, 도착점은 N칸이다. 각 칸에는 지시 사항이 적혀있다. 지시 사항은 말을 얼만큼 이동해야 하는지가 쓰여 있다. 

상근이는 도착점에 도착할 때까지 주사위를 굴려 나온 눈의 수만큼 그 칸으로 이동한다. 이때, 도착한 칸에 쓰여 있는 지시만큼 말을 다시 이동시킨다. 지시 사항으로 이동해서 도착한 칸에 쓰여 있는 지시는 따르지 않는다.

N칸에 도착했을 때와 그 칸을 넘는 경우도 도착한 것이다.

상근이가 던졌을 때 나온 주사위의 눈과 보드판의 지시사항이 주어졌을 때, 몇 번 만에 도착하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. M은 상근이가 주사위를 던진 횟수이다. (2 ≤ N ≤ 1000, 1 ≤ M ≤ 1000)

다음 N개 줄에는 -999이상 999이하의 정수가 하나씩 적혀있다. i번째 정수는 i번 칸에 쓰여 있는 지시사항 X이다. 이때, X가 0이면 아무것도 하지 않고 그 자리에 멈춰 있는다. X가 양수인 경우에는 X칸 더 앞으로 진행하는 것을, 음수인 경우에는 |X|칸 뒤로 진행하는 것을 나타낸다.

다음 M개 줄에는 1이상 6이하의 정수가 주어진다. j번째 정수는 상근이가 주사위를 j번째로 던졌을 때, 나온 눈이다.

1번 칸과 N번 칸에 쓰여 있는 지시사항은 항상 0이다. 또, 항상 주사위를 M번 이하로 던져서 도착할 수 있다.  또, 1보다 작은 칸으로 이동하라는 지시가 있는 경우도 없다.

출력
주사위를 몇 번 던져서 도착할 수 있는지 출력한다.

예제 입력 1 
10 5
0
0
5
6
-3
8
1
8
-4
0
1
3
5
1
5
예제 출력 1 
5
예제 입력 2 
10 10
0
-1
-1
4
4
-5
0
1
-6
0
1
5
2
4
6
5
5
4
1
6
예제 출력 2 
6
"""
n, m = map(int, input().split())

board = []
dice = []
corr = 0
move = 0

for _ in range(n):
    board.append(int(input()))

for _ in range(m):
    dice.append(int(input()))

for i in range(1, m+1):
    corr += dice[i-1]

    if corr+1 >= n:
        print(i)
        break

    move = board[corr]
    corr += move

    if corr+1 >= n:
        print(i)
        break