import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
print(f"{str1} => ",result1.text)

str2 = "I am happy"
result2 = translator.translate(str2, dest='ja', src='auto')
print(f"{str2} => ",result2.text)

# 번역 가능한 언어 확인하기
lang = googletrans.LANGUAGES
print(lang)

# 오류 해결 참조 : https://velog.io/@kir315/googletrans-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0
# pip install googletrans==3.1.0a0 

"""
# 영어 문서를 한글로 번역하는 코드 만들기
from os import linesep

translator = googletrans.Translator()

read_file_path = r"경로 입력"
write_file_path = r"경로 입력"

with open(read_file_path, 'r') as f:
    readline = f.readlines()
for lines in readline:
    result3 = translator.translate(lines, dest='ko')
    print(result3.text)
    with open(write_file_path,'a',encoding='UTF8') as f:
        f.write(result3.text + '\n')
"""