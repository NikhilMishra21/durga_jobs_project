from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def hydjobs(request):
    s = 'Hyderabad jobs information'
    return HttpResponse(s)

def punejobs(request):
    s = 'Pune jobs information'
    return HttpResponse(s)

def mumjobs(request):
    s = 'mumbai jobs information'
    return HttpResponse(s)

def chenjobs(request):
    s = 'Chennai jobs information'
    return HttpResponse(s)
