from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'accounts/index.html', {})

def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = authenticate(request, username=User.objects.get(email=username), password=password)
    except:
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        context = {'error': 'invlaid tradionals'}
        return render(request, 'accounts/login.html', context)

def logoutView(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def signupView( request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('index'))
        context = {
            'form' : form,

        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)

