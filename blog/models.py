from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.
min_length_validator=MinLengthValidator(3)#글자의 길이를 검사해 길이가 지정한 값보다 작을 경우 저장이 안됨

class Tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


@python_2_unicode_compatible#python3 에만 적용되는 코드를 2에서도 사용하고 싶을때
class Post(models.Model):
    title=models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    post_author=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_author')
    content=models.TextField(null=False)
    tags=models.ManyToManyField(Tag,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):#python 3 만 허용, 파이썬 코드로 인해 오브젝트만 나오는 것을 오브젝트 안에 title 부분을 불러옴
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')#Post 클래스에 외래키로 저장, related_name은 외래키의 필드 네임을 지정
    message=models.TextField()
    image=models.ImageField(blank=False)
    def __str__(self):#python 3 만 허용
        return self.message[:50]
