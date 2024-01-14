from django.shortcuts import render
from .models import Store

def store(request):
    products = Store.objects.all()
    return render(request,'store/store.html', {'products':products})
# Create your views here.
