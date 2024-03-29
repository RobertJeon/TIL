"""
문제
경래는 닭을 기르는데 올 겨울 달걀 풍년으로 함박 웃음을 짓고 있다. 그리고 이 달걀을 영양란으로 둔갑하여 옥션에 판매하려한다.

경래는 총 N개의 달걀이 있고, 그의 잠재적인 고객은 총 M명이다. 그리고 각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 살 수 있다고 밝혔다.

경래는 영양란이라 속인 죄책감에 한 고객에게 두 개 이상의 달걀은 팔지 않기로 하였다. 하지만 위의 규칙 하에 수익은 최대로 올리고 싶기에 얼마로 팔지 고민하고 있다. 즉, A가격에 달걀을 판다고 하면 Pi가 A가격보다 크거나 같은 모든 고객은 달걀을 산다는 뜻이다. (물론 달걀 총 수량을 초과하여 팔 수 는 없다)

문제는 이러한 경래를 도와 최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격을 책정하는 것이다.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 1,000)과 M(1 ≤ M ≤ 1,000)이 입력된다. 둘째 줄부터 M+1번째 줄까지 i+1번째 줄에는 Pi(1 ≤ Pi ≤ 1,000,000)가 입력된다.

출력
첫째 줄에 경래가 책정한 가격과 이 가격으로 올릴 수 있는 수익을 출력한다.

---예제 입력
5 4
2
8
10
7

---예제 출력
7 21
"""
n, m = map(int, input().split())
tmp = []
for i in range(m):
    tmp.append(int(input()))
tmp.sort(reverse=True)
p = 0
max_sum = 0
idx = 0
while True:
    if idx == m:
        break
    if n >= m:
        tmp_sum = 0
        for i in range(m):
            if tmp[idx] <= tmp[i]:
                tmp_sum += tmp[idx]
        if max_sum < tmp_sum:
            max_sum = tmp_sum
            p = tmp[idx]
        idx += 1
    else:
        tmp_sum = 0
        for i in range(n):
            if tmp[idx] <= tmp[i]:
                tmp_sum += tmp[idx]
        if max_sum < tmp_sum:
            max_sum = tmp_sum
            p = tmp[idx]
        idx += 1
print(p, end=" ")
print(max_sum)