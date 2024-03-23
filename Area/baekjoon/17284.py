"""
문제
정웅이는 어머니께 5000원이라는 큰 용돈을 받아 자판기에 갔다.

자판기에는 세 개의 버튼이 있다.

1을 누르면 500원짜리 레쓰비를 먹을 수 있다.
2를 누르면 800원짜리 게토레이를 먹을 수 있다.
3을 누르면 1000원짜리 코카콜라를 먹을 수 있다.
누른 버튼값이 순서대로 주어질 때, 거스름돈이 얼마인지 구하시오. 단, 주어진 돈을 초과하도록 버튼을 누르는 일은 없다.

입력
첫째 줄에 정웅이가 누른 버튼의 번호가 공백으로 사이에 두고 주어진다. 정웅이는 버튼을 한 번 이상 눌렀다.

출력
첫째 줄에 자판기에서 나올 거스름돈을 출력한다.


"""
m = 5000
li = list(map(int, input().split()))

for i in range(len(li)):
    a = li[i]
    if a == 1:
        m -= 500
    elif a == 2:
        m -= 800
    else:
        m -= 1000
print(m)