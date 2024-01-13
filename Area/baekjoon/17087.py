"""
수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.

수빈이는 걸어서 이동을 할 수 있다. 수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.

모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 105)과 S(1 ≤ S ≤ 109)가 주어진다. 둘째 줄에 동생의 위치 Ai(1 ≤ Ai ≤ 109)가 주어진다. 동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다.

출력
가능한 D값의 최댓값을 출력한다.

--- 예제 입력 1
3 3
1 7 11
--- 예제 출력 1
2
"""
n,s  = map(int,input().split())
arr = list(map(int,input().split()))

def gcd(x,y):
    if y>x:
        x,y=y,x
    while y > 0:
        x= x%y
        x,y = y,x
    return x

distance = []
for i in arr:
    x = s - i
    if x == 0:
        continue
    elif x < 0 :
        x *= -1
    distance.append(x)

ans=distance[0]
for i in range(1,n):
    ans=gcd(distance[i],ans)

print(ans)

# 유클리드 호제법을 활용하여 문제를 푸는 방식
# 유클리드 호제법을 몰라서 검색해보았지만, 최대 공약수를 구할 때 반복을 돌리면서 최대 공약수만 구하면 되는 문제였다.