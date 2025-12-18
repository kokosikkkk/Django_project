from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):#когда выз с запр GET, создается логин форма 
    if request.method == 'POST': #пользователь отправляет форму с помощ POST
        form = LoginForm(request.POST) #создаем экземпляр формы с отпр данными
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password']) #ищем чела в дб
            if user is not None:
                if user.is_active:
                    login(request, user) #устан сессию 
                    return HttpResponse('Успешный вход..?')
                else:
                    return HttpResponse('Акк не сущ')
            else:
                return HttpResponse('ты инвалид')
    else:
            form = LoginForm()
    return render(request, 'rega/login.html', {'form': form})
    
