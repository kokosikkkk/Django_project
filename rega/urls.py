from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    #path('login/', 'django.contrib.auth.views.login', name='login'),
]