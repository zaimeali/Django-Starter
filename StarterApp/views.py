from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def hello_world(request):
    return JsonResponse({
        "message": "Hello World"
    }, status=200)

def more_message(request):
    return JsonResponse({
        "Message": "Hello Django"
    }, status=200)

def moreWord(request,message):
    return JsonResponse({
        "message": "Hello, " + message
    }, status=200)

