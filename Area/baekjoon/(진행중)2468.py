"""
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 예를 들어, 다음은 N=5인 지역의 높이 정보이다.

-- 입력
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

-- 출력
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

-- 예제입력1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

-- 예제출력1
5
"""

# 틀린코드
# n = int(input())
# matrix_ = []

# for i in range(n):
#     input_li = list(map(int, input().split()))
#     matrix_.append(input_li)

# def dfs_(x_, y_, matrix,n):
#     if 0 <= x_ < len(matrix) and 0 <= y_ < len(matrix[0]) and matrix[x_][y_] > n:
#         matrix[x_][y_] = n
#         dfs_(x_+1, y_, matrix,n)
#         dfs_(x_, y_+1, matrix,n)
#         dfs_(x_-1, y_, matrix,n)
#         dfs_(x_, y_-1, matrix,n)
#     return matrix

# count_ = 0
# for m_x in range(len(matrix_)):
#     for m_y in range(len(matrix_[0])):
#         if matrix_[m_x][m_y] > n:
#             count_ += 1
#             dfs_(m_x, m_y, matrix_,n)
# print(count_)

# 아직 문제 이해를 못한거같다. 

# 참고 
# https://velog.io/@phw1996/%EB%B0%B1%EC%A4%80-2468%EB%B2%88-%EC%95%88%EC%A0%84-%EC%98%81%EC%97%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
sys.setrecursionlimit(100000)

# 좌 우 상 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# x, y 지점을 기준으로 주변을 탐색하는 재귀 함수
def dfs_(x,y,h):
    # x, y 좌표를 기준으로 좌 우 상 하 좌표를 nx 반복문으로 가져옴
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        # 자신이 건너갈 nx, ny 좌표에 대한 유효성 검증
        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            # 유효성이 검증된 좌표에 한해서 재귀함수를 호출
            sink_table[nx][ny] = True
            dfs_(nx,ny,h)
# 입력 받기
N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과를 저장할 변수 초기화
ans = 1

# 물의 높이에 따라 안전 영역의 개수를 탐색
for k in range(max(map(max, water_board))):
    # 각 물의 높이마다 섬을 판별하기 위한 테이블 초기화
    sink_table = [[False for i in range(N)]for j in range(N)]
    count = 0
    # 모든 좌표에 대해 물의 높이가 K 이상이고, 해당 좌표가 아직 방문되지 않았다면 섬으로 판별
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j]
                dfs_(i,j,k) # 해당 좌표에서 시작하여 물의 높이 K 이상인 지점을 재귀적으로 방문
    ans = max(ans, count)   # 물의 높이가 k 일 때의 섬의 개수를 저장

# 최종적으로 가장 많은 섬이 나오는 경우의 섬의 개수 출력
print(ans)