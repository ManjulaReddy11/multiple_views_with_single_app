from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<marquee><h1>hi ra thinava</h1></marquee>')

def second(request):
    return HttpResponse('<marquee><h1>haa thinna nuvu thinava</h1></marquee>')

def third(request):
    return render(request,'home.html')
