from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,HttpResponse,redirect


def homepage(request):
    return render(request,'home.html')
    # print("home page requested")
    # list=[
    #     'ankit',
    #     'ravi',
    #     'uttam'
    # ]
    # return JsonResponse(list,safe=False)