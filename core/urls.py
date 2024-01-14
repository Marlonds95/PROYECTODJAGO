
from django.urls import path
from core import views 

urlpatterns = [
    path("",views.index, name="index"),
    path("about/", views.about, name="about"),
    path("404/", views.error, name="404"),
    path("blog/", views.blog, name="blog"),
    path("contact/",views.contact, name="contact"),
    path("testimonial/", views.testimonial, name="testimonial"),
  
]
