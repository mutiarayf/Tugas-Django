from django.urls import path
from classdigitalapp import views 

urlpatterns = [
    path('', views.index, name='index'),
]
