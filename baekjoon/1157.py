"""
문제 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제입력 1
Mississipi

예제출력 1
?

예제입력 2
zZa

예제출력 2
Z

예제입력 3
z
예제출력 3
Z
"""

m = input()
n = m.upper()
ans_li = list(n)
ans_du = list(set(ans_li))
max_str = "?"
max_cnt = 0
same_nu = 0
for i in range(len(ans_du)):
    if max_cnt < ans_li.count(ans_du[i]):
        max_str = ans_du[i]
        max_cnt = ans_li.count(ans_du[i])
        same_nu = 0
    elif max_cnt == ans_li.count(ans_du[i]):
        same_nu += 1
if max_cnt != 0 and same_nu == 0:
    print(max_str)
else:
    print("?")


"""
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])
"""