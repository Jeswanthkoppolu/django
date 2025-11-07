from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
# Create your views here.

def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    # data={'name':'bobby','age':23,'city':'nellore'}
    # return JsonResponse(data)
    data=[4,5,6,7] 
    return JsonResponse(data,safe=False)  ## for list type of data we need to use 

def dynamicresponse(request):
    name=request.GET.get('name','bobby')
    city=request.GET.get('city','nellore')
    return HttpResponse(f'hello{name} from {city}')