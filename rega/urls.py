from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('account/', views.acc, name='account'),
    #path('login/', 'django.contrib.auth.views.login', name='login'),
]