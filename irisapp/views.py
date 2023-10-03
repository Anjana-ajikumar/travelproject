from django.shortcuts import render
from . models import Place
from . models import Human
# Create your views here.
def myfun(request):
    obj=Place.objects.all()
    obj1=Human.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
#def addition(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   res=x+y
 #   return render(request,"result.html",{'result':res})
