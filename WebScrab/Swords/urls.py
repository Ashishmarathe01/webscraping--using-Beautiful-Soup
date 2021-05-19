
from django.urls import path
from . import  views

urlpatterns = [
    path('frequency/',views.frquent,name="frequent"),
    path('result/', views.result, name="result")
    
]
