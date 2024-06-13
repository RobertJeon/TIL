"""
문제
Write a program that prints a chessboard with N rows and M columns with the following rules:

The top left cell must be an asterisk (*)
Any cell touching (left, right, up or down) a cell with an asterisk must be a dot (.)
Any cell touching (left, right, up or down) a cell with a dot must be an asterisk.
A chessboard of 8 rows and 8 columns printed using these rules would be:

*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
입력
A single line with two integers N and M separated by spaces. The number N will represent the number of rows and M the number of columns. N and M will be between 1 and 10.

출력
Print N lines each containing M characters with the chessboard pattern.

예제 입력 1 
1 1
예제 출력 1 
*
예제 입력 2 
8 8
예제 출력 2 
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
예제 입력 3 
1 5
예제 출력 3 
*.*.*
예제 입력 4 
6 1
예제 출력 4 
*
.
*
.
*
.
예제 입력 5 
2 5
예제 출력 5 
*.*.*
.*.*.
"""
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if (i+j)%2 == 0:
            print('*', end='')
        else:
            print('.', end='')
    print()        