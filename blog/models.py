from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    # 타이틀이라는 변수에는 Charfidld 타이틀이라는 이름으로 정의 길이는 200
    pub_date = models.DateTimeField('date published')
    # 퍼블리시 데이트는 데이트 타임 필드를 날짜와 시간을 정한 시간으로 정의해주겠다
    body = models.TextField()
    # 긴 문장을 바디변수에 넣겠다

    def __str__(self):
        return self.title
    # 타이틀이 뜨길 원함
    
    def summary(self):
        return self.body[:100]
        # 100글자까지만 상환해줘라

        
class Comment(models.Model):
    post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    # ForeignKey viewcrud앱에 Blog 클래스를 연결해줘
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # default 기본값
    approved_comment = models.BooleanField(default=False)
    # BoolenanField 참 거짓을 담는 Field

    def approve(self):
        self.approved_comment = True
        # 자기자신 객체에 
        # 암튼 여러개에 넣어줄라고 있는거임 그런거임
        self.save()
    
    def __str__(self):
        # 매직
        return self.text