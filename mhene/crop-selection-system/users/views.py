from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            region = form.cleaned_data.get('region')
            UserProfile.objects.create(user=user, region=region)
            login(request, user)
            return redirect('dashboard_by_region', region=region)
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user_profile = UserProfile.objects.get(user=user)
            return redirect('dashboard_by_region', region=user_profile.region)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})