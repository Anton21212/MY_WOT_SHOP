from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm
from .models import Profile


def main_page(request):
    return render(request, 'main/main_page.html')


def main_page2(request):
    return render(request, 'main/main_page2.html')




def register(request):
    """
    Регистрация
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            """
            Создаем новый пользовательский объект, но не сохраняем его
            """
            new_user = user_form.save(commit=False)
            """
            Устанавливаем выбранный пароль
            """
            new_user.set_password(user_form.cleaned_data['password'])
            """
            Сохраняем объект юзера
            """
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return redirect('autorization')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})




def user_login(request):
    """
    Авторизация
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/main_page2.html', {'form': form})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/autorization.html', {'form': form})


@login_required
def edit_profile(request):
    """
    Изменение профиля
    """
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'main/edit_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def profile(request):
    """
    Профиль
    """
    my_profile = Profile.objects.filter(user=request.user)
    return render(request, 'main/profile.html', {'my_profile': my_profile})
