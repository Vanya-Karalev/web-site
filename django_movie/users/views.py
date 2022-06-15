from django.shortcuts import render, redirect
from django.contrib import messages
from movies.models import Ticket
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    """Registration function"""
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('index')
    context = {'form': form}
    return render(request, 'registration.html', context)


def loginPage(request):
    """Login function"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'login or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    """Logout function"""
    logout(request)
    return redirect('index')


def profile(request):
    """Update profile function"""
    all_ticket = Ticket.objects.filter(user_login=request.user.username)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'all_ticket': all_ticket,
    }
    return render(request, 'profile.html', context)
