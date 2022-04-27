"""AnimaRR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ------------------------------------
# import mainapp.views
from django.conf import settings
from django.conf.urls.static import static
# ------------------------------------

from main  import views

# URL설정 => 뷰 함수 정의 => templates정의

# [프로젝트 URL]/form/으로 요청이 오면 강아지 기질 선호도 문항 페이지 나오게
# views.form 는 main/views.py에 작성할 함수
# 이 설정은 [프로젝트 URL]/form/로 요청이 오면 main/views.py에 있는 form이라는 함수를 실행하겠다는 의미
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
	path('form/', views.form),
    path('redom/', views.recom),

    # #QnA게시판
    # path('community/', include('community.urls')),

    # 
    path('board/', include('board.urls')),

    #Map
    path('map/', include('map.urls')),


    # dogimg/로 접속하는 경우 > 
    # 모델링 연결
    path('dogimg/', include('dogimg.urls')),
    # path('dogimg/', include('dogimg.urls')),
        # path('predict',views.predict,name='predict',

    # blog/로 접속하는 경우 > blog 앱 폴더의 urls.py를 참고
    path('blog/', include('blog.urls')),


    #
    path('summernote/', include('django_summernote.urls')),


    # 구글, 카카오톡, 페이스북 로그인
    # $ pip install django-allauth 로 먼저 설치  ----------------------------------
    path('accounts/', include('allauth.urls')),

    # $ django-allauth 사용하려면, db에도 반영 해야함
    # $ pip python manage.py migrate 입력하면 알아서 처리
    # 구글 계정으로 웹 사이트에서 로그인할 수 있게 하려면 구글에 웹 사이트 등록해야 함

    #$ pip install django-markdownx  로 먼저 설치  ----------------------------------
    path('markdownx/', include('markdownx.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

