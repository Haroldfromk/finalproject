from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Dogbreed, Enquiry, Choice, Imgs

admin.site.register(Dogbreed)
admin.site.register(Enquiry)
admin.site.register(Choice)
admin.site.register(Imgs)