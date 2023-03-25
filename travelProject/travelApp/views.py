from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,People


# Create your views here.
def demo(request):
    # name = 'India'
    places = Place.objects.all
    people = People.objects.all
    return render(request, "index.html", {'result': places,'people':people})


def about(request):
    return  render(request, 'about.html')


def contact(reques):
    return HttpResponse("This is contact page")


# def add(request):
#     num1 = int(request.GET['num1'])
#     num2 = int(request.GET['num2'])
#     res = num2+num1
#     return render(request,'add.html',{'result': res})
