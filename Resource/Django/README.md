# Jump to Django 실습입니다.

### 장고 프로젝트 생성 명령어
- 프로젝트를 시작할 폴더로 이동한 뒤 `django-admin startproject config .` 명령어 입력

### 하위 디렉토리를 생성하지 않고 프로젝트를 생성하는 방법
- `django-admin startproject {폴더명}`

### 개발 서버 구동하고 웹 사이트에 접속해 보기
- `python manage.py runserver`

### 맥 os에서 가상환경 진입하기
-`[파일명:/Users/pahkey/.zshrc]`
- 예시 코드 `alias mysite='cd /Users/pahkey/projects/mysite;source /Users/pahkey/venvs/mysite/bin/activate'`


### 앱(App) 생성하기
- `django-admin startapp {앱 이름}`
- 실습 예제 : `django-admin startapp pybo`

### 서버 구동하기
- `python manage.py runserver`


### 장고 앱 모델
1. migrate
    - `python manage.py migrate`
    - `python manage.py makemigrations`

### 장고 관리자 생성
- `python manage.py createsuperuser`
사용자 이름 (leave blank to use 'pahke'): admin
이메일 주소: admin@mysite.com
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
