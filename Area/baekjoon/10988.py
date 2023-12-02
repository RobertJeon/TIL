"""
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

-- 입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

-- 출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.
"""

"""
내가 틀린 코드
str_1 = list(input())

def palindrome(li):
    for i in range(int(len(li)/2)):
        if li[i] != li[i-1] and i != int(len(li)/2):
            return print(0)
    return print(1)

palindrome(str_1)

이렇게 작성하면 반례로 aabcaa가 들어오면 틀린다..
"""

str_1 = input()

if str_1==str_1[::-1]:
    print(1)
else:
    print(0)