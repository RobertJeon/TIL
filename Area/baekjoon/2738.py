"""
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

입력예시
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

출력예시
4 4 4
6 6 6
5 6 100
"""

n, m = map(int,input().split())
# 정답 행렬
sum_ans = [[0 for i in range(m)] for j in range(n)]
# 외부 반복문 - n 갯수 * 2배 input 받기
for i in range(n*2):
    temp = input().split()
    # 내부 반복문 - input 받은 값 정답행렬 위치에 맞게 더해주기
    if i < n:
        for j in range(len(temp)):
            sum_ans[i][j] += int(temp[j])
    else:
        for k in range(len(temp)):
            sum_ans[i-n][k] += int(temp[k])
for a in range(n):
    for b in range(m):
        print(sum_ans[a][b], end=" ")
    print("")