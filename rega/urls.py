from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='rega/registration/login.html'), name='login'), #workaet
    path('logout/', views.user_logout, name = 'logout'),
    path('account/', views.acc, name='account'),
    path('register/', views.register_view, name='register'),

    #path('pass-change/', views.passw, name='changepass'),
    #path('pass-change/', auth_views.PasswordChangeView.as_view(template_name='rega/registration/changepass.html'))
]