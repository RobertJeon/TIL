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
n = int(input())
matrix_ = []

for i in range(n):
    input_li = list(map(int, input().split()))
    matrix_.append(input_li)

def dfs_(x_, y_, matrix,n):
    if 0 <= x_ < len(matrix) and 0 <= y_ < len(matrix[0]) and matrix[x_][y_] > n:
        matrix[x_][y_] = n
        dfs_(x_+1, y_, matrix,n)
        dfs_(x_, y_+1, matrix,n)
        dfs_(x_-1, y_, matrix,n)
        dfs_(x_, y_-1, matrix,n)
    return matrix

count_ = 0
for m_x in range(len(matrix_)):
    for m_y in range(len(matrix_[0])):
        if matrix_[m_x][m_y] > n:
            count_ += 1
            dfs_(m_x, m_y, matrix_,n)
print(count_)

# 아직 문제 이해를 못한거같다. 