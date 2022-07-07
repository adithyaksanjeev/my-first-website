from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def a(request):
    return render(request,"about.html")
def b(requests):
    return HttpResponse("this is services session")
