from django.shortcuts import render
from .models import Feature

def feature(request):
    features = Feature.objects.all()
    return render(request,'feature/feature.html', {'features':features})
