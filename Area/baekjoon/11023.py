"""
문제
수 N개가 주어졌을 때, N개의 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)개의 수가 공백으로 구분되어서 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다. 또, 0으로 시작하는 수는 주어지지 않는다.

출력
입력받은 수 N개의 합을 출력한다.
"""
print(sum(list(map(int,input().split()))))