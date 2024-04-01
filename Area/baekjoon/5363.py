"""
문제
어린 제다이들은 요다와 대화하는 법을 배워야 한다. 요다는 모든 문장에서 가장 앞 단어 두 개를 제일 마지막에 말한다.

어떤 문장이 주어졌을 때, 요다의 말로 바꾸는 프로그램을 작성하시오.

입력
첫째 줄에 문장의 수 N이 주어진다. 둘째 줄부터 N개의 줄에는 각 문장이 주어진다. 문장의 길이는 100글자 이내이다. 단어의 개수는 3개 이상이다.

출력
각 문장을 요다의 말로 바꾼 뒤 출력한다.

예제 입력 1 
4
I will go now to find the Wookiee
Solo found the death star near planet Kessel
I'll fight Darth Maul here and now
Vader will find Luke before he can escape
예제 출력 1 
go now to find the Wookiee I will
the death star near planet Kessel Solo found
Darth Maul here and now I'll fight
find Luke before he can escape Vader will
"""
n = int(input())

for _ in range(n):
    tmp = input().split(" ")
    print(' '.join(tmp[2:]+tmp[:2]))