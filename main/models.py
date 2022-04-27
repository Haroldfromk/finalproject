from django.db import models

from django.contrib.auth.models import User
import os
from markdownx.utils import markdown
from markdownx.models import MarkdownxField
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


# 구글로 로그인 하게 할려고---------------------------------------------
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from sympy import content

# Create your models here.
# 강아지 유형, 결과값으로 보여 줄 모델
# name 강아지 종 이름(말티즈, 푸들)
# count 추천 결과에 대한 카운트 값
class Dogbreed(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField(default=0)

    # 매직문자열 : 클래스를 대표하는 문자열을 뭘로 할지 
    def __str__(self):
        return self.name

# ---------------------------------------------


# 강아지 선호 temp 문항
# number 열, 문항번호
# content 질문내용
class Enquiry(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=150)

    # 매직문자열 : 클래스를 대표하는 문자열을 뭘로 할지 / 몇번 질문인지, 문항
    def __str__(self):
        return f'{self.number}. {self.content}'
# ---------------------------------------------



# 선택항목
# content 선택지 내용
# question 선택지가 속한 문항
# dogbreed 해당 선택지가 어느 개발 유형의 선택지인지 담은
# on_delete=models.CASCADE 옵션 => ex, 게시물이 지워지면 댓글까지 같이 지워줄꺼다!
# [null=True] => db가 비어있어도 된다. 
class Choice(models.Model):
    content = models.CharField(max_length=150)
    question = models.ForeignKey(to='main.Enquiry', on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(to='main.Dogbreed', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content
# ---------------------------------------------


# 업로드한 이미지
# ImageField.height_field => 모델 인스턴스가 저장될 때마다 이미지 높이가 자동으로 채워질 모델 필드의 이름
# ImageField.width_field => 모델 인스턴스가 저장될 때마다 이미지 너비로 자동 채워지는 모델 필드의 이름
# img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=150)
class Imgs(models.Model):
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=150)
    

    # def __str__(self):
    #     return self.img
# ---------------------------------------------



# 게시판 이지만 블로그같은
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField()

# ---------------------------------------------