"""
이 세상에서 두 번째로 맛있는 과자 브실칩이 있다.

하나의 브실칩에는 A부터 Z 중 하나의 알파벳 띠부띠부씰이 들어있다.

모은 띠부띠부씰들로 BRONZESILVER 글자를 만들어 우편으로 보내면 이 세상에서 제일 맛있는 골드칩 한 봉지를 배송해 준다고 한다.

지금까지 모은 띠부띠부씰들로 골드칩을 최대 몇 봉지 배송받을 수 있을지 계산해 보자.

입력
첫 번째 줄에는 모은 알파벳 띠부띠부씰 개수 
$N$ 이 주어진다. 
$(1 \le N \le 1\,000)$ 

두 번째 줄에는 알파벳 대문자로 이루어진 
$N$개의 알파벳 띠부띠부씰이 나열된다.

출력
배송받을 수 있는 최대 골드칩 봉지 수를 출력한다.

예제 입력 1 
12
BRONZESILVER
예제 출력 1 
1
예제 입력 2 
26
ABCDEFGHIJKLMNOPQRSTUVWXYZ
예제 출력 2 
0
"""
num = int(input())
tmp = input()

b = 0
r = 0
o = 0
n = 0
z = 0
s = 0
i = 0
l = 0
v = 0
e = 0

for j in tmp:
    if j == "B":
        b += 1
    elif j == "R":
        r += 1
    elif j == "O":
        o += 1
    elif j == "N":
        n += 1
    elif j == "Z":
        z += 1
    elif j == "S":
        s += 1
    elif j == "I":
        i += 1
    elif j == "L":
        l += 1
    elif j == "V":
        v += 1
    elif j == "E":
        e += 1

e = e//2
r = r//2
print(min(b,r,o,n,z,s,i,l,v,e))