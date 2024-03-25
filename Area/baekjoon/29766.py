"""
학교의 로고인 DKSH는 Dankook University Software High School의 약자이다.

D, K, S, H로만 이루어진 문자열이 주어진다. 이 문자열에서 DKSH가 몇 번 나타나는지 구해보자.

입력
첫째 줄에 문자열이 입력된다. 문자열의 길이는 
$1\,000$을 넘지 않는다.

출력
첫째 줄에 입력된 문자열에서 DKSH가 몇 번 나타나는지 출력한다.
"""
s = input()
cnt = 0
for i in range(len(s)-3):
    if s[i] == "D":
        if s[i+1]=="K" and s[i+2] == "S" and s[i+3] == "H":
            cnt += 1
print(cnt)