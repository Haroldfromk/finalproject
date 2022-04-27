from django.shortcuts import render
from .models import Enquiry,  Dogbreed, Choice, Imgs

# Create your views here.
# URL설정 => 뷰 함수 정의 => templates정의

from .models import Enquiry, Dogbreed, Choice

#-------------------------------------


#-------------------------------------

def main(request):
    dogbreed = Dogbreed.objects.all()
    
    context = {
        'dogbreeds': dogbreed,
    }
    
    return render(request, 'main.html', context=context)

#-------------------------------------

# form 함수의 역할은 form.html 을 페이지로 보여주는 역할
# Questions.objects.all() : 모든 Question 요소를 불러옴
def form(request):
     # Enquiry에 입력된 모든 oject를 가지고 오겠다 => 질문지
    enquirys = Enquiry.objects.all()

    context = {
        # 키와 벨류(앞enquirysl=>이름으로 불러옴, enquirys=> 여기에 데이터 있다! 맵핑된거다)
        # 앞의 키인 enquirys로 html에서 불러올 수 있다.
        'enquirys': enquirys,
    }
    
    return render(request, 'form.html', context)

#--------------------------------------

def recom(request):
    
    # 전체 문항 갯 수 가지고옴
    N = Enquiry.objects.count()

    # 견종 기질 유형  갯 수
    K = Dogbreed.objects.count()
    
    # 선호하는 견종 기질 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)
    
    for n in range(1, N+1):
        dogbreed_id = int(request.POST[f'enquiry-{n}'][0])
        counter[dogbreed_id] += 1
    
    # 최고점 기질 유형
    best_dogbreed_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_dogbreed = Dogbreed.objects.get(pk=best_dogbreed_id)
    best_dogbreed.count += 1
    best_dogbreed.save()
    
    context = {
        'dogbreed': best_dogbreed,
        'counter': counter
    }
    
    return render(request, 'recom.html', context)


    #-------------------------------------

