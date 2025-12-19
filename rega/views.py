from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
                    return render(request, 'rega/account.html') #заменить на всплывающее уведомление
                else:
                    return HttpResponse('Акк не сущ')
            else:
                return HttpResponse('ты инвалид')
    else:
            form = LoginForm()
    return render(request, 'rega/registration/login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    #return redirect('index')
    return render(request, 'rega/registration/logout.html')

def acc(request):
    return render(request, 'rega/account.html')