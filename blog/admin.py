from django.contrib import admin
from .models import Blog, Comment
# 같은 폴더에 잇는 model에서 blog객체를 가져와라

# 모델에 만들어준 양식을 어드민에 넣어줘야댄다

admin.site.register(Blog)
# 어드민 사이트에 등록해라
admin.site.register(Comment)