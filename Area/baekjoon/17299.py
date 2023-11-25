"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.

Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 
F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오등큰수는 -1이다.

예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. 
A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. 
A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. 
NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.

-- 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

-- 출력
총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.

-- 입력 예제 1
7
1 1 2 3 4 2 1

-- 출력 예제 1
-1 -1 1 2 2 1 -1
"""
""" 시간초과 코드
# 첫 번쨰 줄 입력받기
n = int(input())
# 두 번째 줄 입력받기 (오큰수에서는 숫자였으나 오등큰수는 출현횟수가 우선이므로 str으로 처리함.)
li = list(map(str, input().split()))

# 딕셔너리
key_dict = {}
key_set = set(li)
for i in key_set:
    key_dict[i] = li.count(i)
# 길이만큼 리스트 만들기 -1로 생성
result = [-1] * n
stack_li = []

for i in range(n):
    while stack_li and key_dict[li[i]] > key_dict[li[stack_li[-1]]]:
        idx = stack_li.pop()
        result[idx] = li[i]
    stack_li.append(i)

# 결과 출력
print(" ".join(map(str, result)))

"""

n = int(input())
li = list(map(int, input().split()))

# get을 사용하여 count하는 것을 줄이기..
count_dict = {}
for num in li:
    # 가져온 값을 1 증가시켜 다시 해당 키의 값으로 설정합니다. 만약 키가 존재하지 않았다면 새로운 키를 만들고 값을 1로 설정합니다.
    count_dict[num] = count_dict.get(num, 0) + 1

result = [-1] * n
stack_li = []

for i in range(n):
    while stack_li and count_dict[li[i]] > count_dict[li[stack_li[-1]]]:
        idx = stack_li.pop()
        result[idx] = li[i]
    stack_li.append(i)

print(" ".join(map(str, result)))