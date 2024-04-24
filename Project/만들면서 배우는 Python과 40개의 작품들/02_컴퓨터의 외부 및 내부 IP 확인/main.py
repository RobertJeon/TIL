# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러옵니다.
import socket

# 1-1. 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩합니다.
in_addr_1 = socket.gethostbyname(socket.gethostname())

# 1-2. 내부 IP를 확인합니다.
print("1. 내부 IP : ",in_addr_1)

# 2-1. 소켓을 연겷
in_addr_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2-2. 구글에 접속합니다. https의 기본 접속포트는 443
in_addr_2.connect(("www.google.com", 443))
# 2-3. 연결된 소켓을 출력합니다.
print("2. 연결된 소켓 : ", in_addr_2.getsockname()[0])

# 3-1. 사이트에 접속하기 위해 requests 모듈을 불러옵니다.
import requests
# 3-2. IP주소를 찾기 위한 정규식을 사용하기 위해 re 모듈을 불러옵니다.
import re

# 3-3. ipconfig 사이트에 접속합니다. 
req = requests.get("http://ipconfig.kr")
# 3-4. 정규식 표현을 사용하여 IP주소를 가져와 out_addr 변수와 바인딩 합니다.
out_addr_3 = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 3-5. 외부 IP주소를 출력합니다.
print("3. 외부 IP : ", out_addr_3)