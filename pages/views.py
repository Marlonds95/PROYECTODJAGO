from django.shortcuts import render, get_object_or_404
from .models import Page
# Create your views here.

def polcies(request, page_id):
    page=get_object_or_404(Page, id=page_id)
    return render(request,'pages/policies.html', {'page':page})
# Create your views here.
