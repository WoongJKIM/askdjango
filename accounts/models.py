import re
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.validators import RegexValidator
# Create your models here.

def follow(self, to_user):
    kwargs={'from_user':self, 'to_user':to_user}
    if not Follow.objects.filter(from_user=self, to_user=to_user).exists():
        Follow.objects.create(**kwargs)
'''
    try:
        Follow.objects.create(from_user:self, to_user=to_user)
    except IntegrityError:
        pass
'''# 다른 방법
def unfollow(self, to_user):
    Follow.objects.filet(from_user=self, to_user=to_user).delete()

setattr(User,'follow',follow)
setattr(User,'follow',follow)

def phone_validator(value):
    number=''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message='휴대폰 번호를 입력해주세요.')(number)

class PhoneField(models.CharField):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('max_length',20)
        super(PhoneField, self).__init__(*args,**kwargs)
        self.validators.append(phone_validator)

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    #phone=models.CharField(max_length=20)
    phone=PhoneField()
    birth_year=models.PositiveIntegerField()
    def __str__(self):#python 3 만 허용, 파이썬 코드로 인해 오브젝트만 나오는 것을 오브젝트 안에 title 부분을 불러옴
        return self.user.username

class Follow(models.Model):
    is_blocked=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    from_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='following_set')
    to_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='follower_user')
    '''
    class Meta:
        unique_together=[
            ['from_user','to_user']
        ]
    '''#중복 가입 방지 기능
