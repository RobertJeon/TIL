"""
문제
 
$10 \times 10$ 격자의 각 칸에 가지가 한 개씩 들어 있습니다. 키위새는 가로로 연속한 
$10$개의 칸 혹은 세로로 연속한 
$10$개의 칸에 들어 있는 모든 가지를 단 한 번 줄줄이 연결할 수 있습니다. 가지 한 두름은 같은 색의 가지를 정확히 
$10$개 연결한 것입니다. 각 칸에 들어 있는 가지의 색이 주어질 때, 키위새가 가지 한 두름을 만들 수 있는지 판단해 봅시다.

가지 한 두름의 예
첫 행의 모든 가지로 가지 한 두름을 만든 모습

입력
첫 번째 줄부터 
$10$개 줄 각각에 각 행에 들어 있는 가지 
$10$개의 색을 나타내는 문자열이 공백으로 구분되어 주어집니다. 그중 
$r$번째 줄의 
$c$번째 문자열은 
$r$행 
$c$열에 위치한 가지의 색을 나타냅니다. 가지의 색은 영어 소문자로만 이루어진 길이 
$1$ 이상 
$8$ 이하의 문자열입니다.

출력
키위새가 가지 한 두름을 만들 수 있으면 1을, 만들 수 없으면 0을 출력합니다.

예제 입력 1 
r r r r r r r r r r
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
g b g b g b g b g b
예제 출력 1 
1
예제 입력 2 
r b g b g b g b g b
r g b g b g b g b g
r b g b g b g b g b
r g b g b g b g b g
r b g b g b g b g b
r g b g b g b g b g
r b g b g b g b g b
r g b g b g b g b g
r b g b g b g b g b
r g b g b g b g b g
예제 출력 2 
1
예제 입력 3 
chipi chapa chipi chapa chipi chapa chipi chapa chipi chapa
chapa chipi chapa chipi chapa chipi chapa chipi chapa chipi
chipi chapa chipi chapa chipi chapa chipi chapa chipi chapa
chapa chipi chapa chipi chapa chipi chapa chipi chapa chipi
chipi chapa chipi chapa chipi chapa chipi chapa chipi chapa
chapa chipi chapa chipi chapa chipi chapa chipi chapa chipi
chipi chapa chipi chapa chipi chapa chipi chapa chipi chapa
chapa chipi chapa chipi chapa chipi chapa chipi chapa chipi
chipi chapa chipi chapa chipi chapa chipi chapa chipi chapa
chapa chipi chapa chipi chapa chipi chapa chipi chapa chipi
예제 출력 3 
0
"""
li = []
for _ in range(10):
    li.append(list(map(str, input().split())))

ans = 0

for i in range(10):
    tmp = set(li[i])

    if len(tmp) == 1:
        ans = 1
        break

if ans == 0:
    for i in range(10):
        tmp_li = set()
        for j in range(10):
            tmp_li.add(li[j][i])
        if len(tmp_li) == 1:
            ans = 1
            break
print(ans)