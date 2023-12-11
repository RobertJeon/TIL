from django.db import models
from django.contrib.auth.models import User

# Question 모델 정의
class Question(models.Model):
    # 글쓴이(User 모델과의 연결, 삭제 시 해당 글쓴이의 질문도 함께 삭제, related_name으로 역참조 설정)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)                  # 제목 (최대 200자)
    content = models.TextField()                                # 내용 (텍스트 필드)
    create_date = models.DateTimeField()                        # 생성 일시 (날짜와 시간)
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정 일시 (선택적, 비어있을 수도 있음)
    # 추천인(User 모델과의 다대다 관계, related_name으로 역참조 설정)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject  # 모델을 문자열로 표현할 때 사용할 값을 제목으로 설정

# Answer 모델 정의
class Answer(models.Model):
    # 글쓴이(User 모델과의 연결, 삭제 시 해당 글쓴이의 답변도 함께 삭제, related_name으로 역참조 설정)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # 질문과의 연결 (외래키로 질문 모델과의 관계 설정, 삭제 시 해당 질문의 답변도 함께 삭제)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()                                # 내용 (텍스트 필드)
    create_date = models.DateTimeField()                        # 생성 일시 (날짜와 시간)
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정 일시 (선택적, 비어있을 수도 있음)
    # 추천인(User 모델과의 다대다 관계, related_name으로 역참조 설정)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content  # 모델을 문자열로 표현할 때 사용할 값을 내용으로 설정