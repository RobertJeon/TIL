"""
문제
가위 바위 보는 두 명이서 하는 게임이다. 보통 미리 정해놓은 수 만큼 게임을 하고, 많은 게임을 이긴 사람이 최종 승자가 된다.

가위 바위 보를 한 횟수와 매번 두 명이 무엇을 냈는지가 주어졌을 때, 최종 승자를 출력하는 프로그램을 작성하시오.

바위는 가위를 이긴다.
가위는 보를 이긴다.
보는 바위를 이긴다.
입력
첫째 줄에는 테스트 케이스의 개수 t(0 < t < 1000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 가위 바위 보를 한 횟수 n(0 < n < 100)이 주어진다. 다음 n개의 줄에는 R, P, S가 공백으로 구분되어 주어진다. R, P, S는 순서대로 바위, 보, 가위이고 첫 번째 문자는 Player 1의 선택, 두 번째 문자는 Player 2의 선택이다.

출력
각 테스트 케이스에 대해서 승자를 출력한다. (Player 1 또는 Player 2) 만약, 비겼을 경우에는 TIE를 출력한다.
"""
n = int(input())

def RSP(a, b):
    if a == b:
        return "TIE"
    elif a == "R":
        if b == "P":
            return "Player 2"
        else:
            return "Player 1"
    elif a == "P":
        if b == "S":
            return "Player 2"
        else:
            return "Player 1"
    else:
        if b == "R":
            return "Player 2"
        else:
            return "Player 1"

for i in range(n):
    m = int(input())
    tmp_a = 0
    tmp_b = 0
    for j in range(m):
        a, b = map(str, input().split())
        tmp = RSP(a, b)
        if tmp == "Player 1":
            tmp_a += 1
        elif tmp == "Player 2":
            tmp_b += 1
    if tmp_a > tmp_b:
        print("Player 1")
    elif tmp_b > tmp_a:
        print("Player 2")
    else:
        print("TIE")