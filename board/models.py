from django.db import models
from django.contrib.auth.models import User
import os
# from markdownx.utils import markdown
# from markdownx.models import MarkdownxField
# from datetime import timedelta




class Board(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # admin으로 board에 들어갔을 때, 제목부분 어떻게 보일지 설정
    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'# {self.author.email}'

    class Meta:
        db_table = 'board_board'
        # managed = False  # 이걸 잠깐 추가해줍니다.
        # https://gmyankee.tistory.com/357