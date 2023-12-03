"""
ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.

예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다. ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다. 앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.

ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다. 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.

문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

-- 입력
첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

-- 출력
첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.

-- 입력 예제1
Baekjoon Online Judge

-- 출력 예제1
Onrxwbba Bayvar Whqtr
"""
str_1 = input()

alpha1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = "abcdefghijklmnopqrstuvwxyz"

res = ""

for i in range(len(str_1)):
    if str_1[i] in alpha1:
        if alpha1.index(str_1[i]) < 13:
            res += alpha1[alpha1.index(str_1[i])+13]
        else:
            res += alpha1[13-(26 - alpha1.index(str_1[i]))]
    elif str_1[i] in alpha2:
        if alpha2.index(str_1[i]) < 13:
            res += alpha2[alpha2.index(str_1[i])+13]
        else:
            res += alpha2[13-(26 - alpha2.index(str_1[i]))]
    else:
        res += str_1[i]
print(res)