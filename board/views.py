from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Board
from .forms import BoardForm

# 장고에서 제공하는 ListView 상속받기
# 파일 명을 "모델명_list"로 쓰면 알아서 동작
class BoardList(ListView):
    model = Board

    # 최신꺼 부터 보이도록
    ordering = '-pk'

    


# 하나만 보여주고 싶을 때, 장고에서 제공하는 DetailView상속 받기
# 파일 명을 "모델명_detail"로 쓰면 알아서 동작
# url에 설정한 path '<int:pk>/', views.BoardDetail.as_view
class BoardDetail(DetailView):
    model = Board


# 로그인 되어있는지 확인하고LoginRequiredMixin > 
class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(BoardCreate, self).form_valid(form)

            return response
        else:
            return redirect('/board/')
