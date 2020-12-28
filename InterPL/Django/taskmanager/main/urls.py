from django.urls import path
from . import views

urlpatterns = [
    # попали сюда из \main\urls.py
    path('', views.index, name='main'),
    path('about-us', views.about, name='about' ),
    path('create', views.create, name='create')
]
