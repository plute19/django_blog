from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import *
from datetime import datetime


# Create your views here.
def index2(request):
    return HttpResponse("<h1>한글...</h1>")


def index(request):
    msg = "흰둥아 안녕"
    return render(request, 'index.html', {'message': msg})


def save(request):
    fb = Feedback(name='insect', email='plute19@gmail.com', comment='zzick', createDate=datetime.now())
    fb.save()
    return render(request, 'index.html', {'result': 'true'})

