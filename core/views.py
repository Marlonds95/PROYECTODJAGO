from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"core/index.html")

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")
def error(request):
    return render(request,"core/404.html")

def blog(request):
    return render(request,"core/blog.html")

def testimonial(request):
    return render(request,"core/testimonial.html")