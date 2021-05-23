from django.shortcuts import render
from .models import works
import datetime
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name","not given")
        date = request.POST.get("date","not given")
        x = works(Name=name,Done=False,Date=date)
        x.save()
    data = works.objects.all()
    context = {
        "works":data
    }
    return render(request,"home.html",context)