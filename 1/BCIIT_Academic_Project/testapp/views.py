from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def staf(request):
    return render(request,'staf_info.html')
def student(request):
    return render(request,'student_info.html')
def event(request):
    return render(request,'event_info.html')