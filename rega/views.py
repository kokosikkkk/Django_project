from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required


def user_login(request):#когда выз с запр GET, создается логин форма 
    if request.method == 'POST': #пользователь отправляет форму с помощ POST
        form = LoginForm(request.POST) #создаем экземпляр формы с отпр данными
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) #ищем чела в дб
            if user is not None:
                if user.is_active:
                    login(request, user) #устан сессию 
                    return render(request, 'rega/account.html') #заменить на всплывающее уведомление
            else:
                return HttpResponse('акк не сущ')
    else:
        form = LoginForm()
    return render(request, 'rega/registration/login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('index')
    #return render(request, 'rega/registration/logout.html')

def passw(request):
    return render(request, 'rega/registration/changepass.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save() #польз сохр в базе данных
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'rega/registration/register.html', {'form': form})


@login_required
def acc(request):
    return render(request, 'rega/account.html')