from django.shortcuts import render
from . import models
# Create your views here.
def homepage(request):
    phones = models.Phone.objects.all()
    return render(request,'home.html',{'phones':phones})