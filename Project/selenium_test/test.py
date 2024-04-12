# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행
driver = webdriver.Chrome() 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.google.co.kr/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)

from selenium.webdriver.common.by import By

# 검색어 창을 찾아 search 변수에 저장 (By.CLASS_NAME 방식)
search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식)
# search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').click()

from selenium.webdriver.common.keys import Keys

search_box.send_keys('파이썬')
search_box.send_keys(Keys.RETURN)
time.sleep(10)