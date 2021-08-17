from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages;
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"profiles":Profile.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            profile = Profile()
            profile.username = username
            profile.content = "a brand new user :)"
            profile.save() 
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def profile(request, username):
    return render(request = request,
                  template_name='main/profile.html',
                  context = {"profile":Profile.objects.get(username=username)})

def myprofile(request):
    username = request.user.get_username()
    return render(request = request,    
                  template_name='main/profile.html',
                  context = {"profile":Profile.objects.get(username=username)})

def profile_edit(request, username):
    r_username = request.user.get_username()
    if (r_username == username):
        return render(request = request,
                template_name='main/profile.html',
                context = {"profile":Profile.objects.get(username=username),"edit":True})
    else:     
        return redirect("main:homepage")
   
def profile_update(request, username, changes):
    r_username = request.user.get_username()
    if (r_username == username):
        profile = Profile.objects.get(username=username)
        changes = changes.split(",")
        for change in changes:
            change = change.split("\":\"")
            key = change[0].strip("\"")
            value = change[1].strip("\"")
            test = getattr(profile, key)
            setattr(profile, key, value)
            profile.save()
        return redirect("main:myprofile")
    else:     
        return redirect("main:homepage")   