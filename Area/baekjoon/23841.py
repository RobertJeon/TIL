"""
문제
시험과 과제에 지친 희권이는 취미로 그림을 그리기 시작했다.

하지만, 그림이 별로 마음에 들지 않아 데칼코마니로 바꾸려 한다.

위에 보이는 것처럼 그림을 좌우 방향으로 반으로 포개어 접으면, 맞닿는 면에 물감이 번지면서 데칼코마니가 완성된다.

접은 그림은 원래대로 되돌릴 수 없기 때문에 희권이는 결과를 미리 알고 싶어 한다.

희권이에게 그림을 데칼코마니 한 결과를 알려주자.

입력
첫 줄에 그림의 세로 길이 정수 N과 가로 길이 정수 M이 주어진다. (1 ≤ N, M ≤ 50, M은 짝수)

N개 줄에 M개씩 그림에 대한 정보가 주어진다.

물감은 26가지가 있고, 각각 알파벳 대문자 하나로 나타낸다.

그림에서 색칠한 곳은 물감에 해당하는 알파벳으로 빈 곳은 '.'으로 표현한다. 그림의 가로 길이는 짝수이고, 그림을 접었을 때 두 물감이 겹치는 경우는 없다.

출력
데칼코마니 한 그림을 N개의 줄에 걸쳐 출력한다.

예제 입력 1 
3 6
G..R..
..B...
Y.....
예제 출력 1 
G.RR.G
..BB..
Y....Y
본문에서 사용된 그림을 나타내는 예제이다.
"""
n, m = map(int,input().split())
li = []
for _ in range(n):
    tmp = list(map(str, input()))
    for i in range(m):
        if tmp[i] != ".":
            tmp[-(i+1)] = tmp[i]
    li.append(tmp)
for i in range(n):
    for j in range(m):
        if j == m-1:
            print(li[i][j],end='\n')
        else:
            print(li[i][j],end="")