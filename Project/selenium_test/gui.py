import tkinter as tk
from tkinter import messagebox

def run_scraping():
    search_query = entry_search.get()
    # 사용자가 입력한 검색어를 이용하여 웹 스크래핑 실행하는 코드 추가하기
    messagebox.showinfo("알림", "검색 및 스크래핑이 완료되었습니다.")

# 메인 윈도우 생성
window = tk.Tk()
window.title("웹 스크래핑 프로그램")

# 레이블과 입력 상자 생성
label_search = tk.Label(window, text="검색어를 입력하세요:")
label_search.pack()

entry_search = tk.Entry(window)
entry_search.pack()

# 실행 버튼 생성
btn_run = tk.Button(window, text="실행", command=run_scraping)
btn_run.pack()

# 프로그램 실행
window.mainloop()
