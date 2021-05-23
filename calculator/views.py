from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def result(request):
    n1 = request.POST.get("number1")
    n2 = request.POST.get("number2")
    return render(request,"result.html")