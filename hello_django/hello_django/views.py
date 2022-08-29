#файл представления
from django.http import HttpResponse
from django.shortcuts import render

def about (request):
    a =5+6
    return render(request,'about.html',{'gretting':a})

def home(request):#request - это ответ,котоорый придет с нашей страницы
    return HttpResponse('This is my home')


