"""
문제
GEC에는 여러 학교가 있다. 각 학교의 약칭과 정식 명칭은 다음과 같다.

NLCS: North London Collegiate School
BHA: Branksome Hall Asia
KIS: Korea International School
SJA: St. Johnsbury Academy
학교 이름을 좋아하는 규빈이는, 학교 이름을 짧게 부르는 것을 싫어하기 때문에, 각 학교의 약칭이 주어졌을 때 정식 명칭을 출력하는 프로그램을 만들기로 하였다.

각 학교의 약칭이 주어졌을 때, 정식 명칭을 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 학교의 약칭 중 하나가 주어진다.

출력
첫 번째 줄에 입력된 학교의 정식 명칭을 출력한다.

예제 입력 1 
NLCS
예제 출력 1 
North London Collegiate School
"""
tmp = input()

if tmp == "NLCS":
    print("North London Collegiate School")
elif tmp == "BHA":
    print("Branksome Hall Asia")
elif tmp == "KIS":
    print("Korea International School")
elif tmp == "SJA":
    print("St. Johnsbury Academy")