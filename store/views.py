from django.shortcuts import render, get_object_or_404
from .models import Store

def store(request):
    products = Store.objects.all()

    return render(request,'store/store.html', {'products':products})
# Create your views here.

