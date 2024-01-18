from django.urls import path
from . import views


urlpatterns = [
    
    path('<int:page_id>/', views.polcies, name="policies"),
    
]