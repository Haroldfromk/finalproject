from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .models import hospitalinfo, pharmacyinfo


# f=open("static/data/test/pharmacy.csv",'r',encoding='cp949')
# lines = f.readlines()

# p = []
# for line in lines:
#     p.append(line.split(','))

# f.close()
# data = p

    

def index(request):
    pharmacies=pharmacyinfo.objects.all()
    hospitals=hospitalinfo.objects.all()
    return render(request, 'mapmain.html', {'pharmacies':pharmacies,'hospitals':hospitals})