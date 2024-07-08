"""
문제
브실이는 이제 막 체스에 입문한 체스 초보이다. 브실이는 아직 초보이기 때문에 체스판의 기물 점수 계산을 잘하지 못한다.

체스판의 기물 점수는 백의 기물 점수 합에서 흑의 기물 점수 합을 뺀 값이고, 기물에 해당하는 킹, 폰, 나이트, 비숍, 룩, 퀸의 기물 점수는 각각 
$0$, 
$1$, 
$3$, 
$3$, 
$5$, 
$9$점이다.

체스 초보 브실이를 위해 체스판의 기물 점수 계산을 도와주자!

입력
첫 번째 줄부터 
$8$개의 줄에 걸쳐 
$8\times8$ 크기의 체스판의 상태가 공백 없이 주어진다.

백의 기물은 영어 대문자, 흑의 기물은 영어 소문자로 주어진다.

입력으로 주어지는 문자열은 ., K, k, P, p, N, n, B, b, R, r, Q, q로만 이루어져 있고, 각각의 문자들은 다음을 뜻한다.

.: 빈칸
K 또는 k: 킹
P 또는 p: 폰
N 또는 n: 나이트
B 또는 b: 비숍
R 또는 r: 룩
Q 또는 q: 퀸
출력
주어진 체스판의 기물 점수를 출력한다.

예제 입력 1 
rnbqkbnk
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNK
예제 출력 1 
0
예제 입력 2 
RRRRRRRR
RRRRRRRR
RRRRRRRR
RRRRRRRR
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrk
예제 출력 2 
5
예제 입력 3 
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrr
rrrrrrrr
예제 출력 3 
-320
"""
chess = {
    "K": 0,
    "k": 0,
    "P": 1,
    "p": 1,
    "N": 3,
    "n": 3,
    "B": 3,
    "b": 3,
    "R": 5,
    "r": 5,
    "Q": 9,
    "q": 9,
}

white, black = 0, 0
for _ in range(8):
    pieces = input()
    for p in pieces:
        if p == ".":
            continue
        if p.isupper():
            white += chess[p]
        else:
            black += chess[p]

print(white - black)