from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse


# Create your views here.
from polls.forms import SignUpForm


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def post(request):
    return render(request, 'post.html', {})


def contact(request):
    return render(request, 'sign_in.html', {})


def signup(request):
    # Returns the path, plus an appended query string, if applicable. Example: "/music/bands/the_beatles/?print=true"
    path = request.get_full_path()

    if request.method == 'POST':
        form = SignUpForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            UserModel = get_user_model()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserModel.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_user = authenticate(username=username, password=password)
            auth_login(request, auth_user)
            return redirect("index")
        else:
            print("666")
    else:
        form = SignUpForm(auto_id="%s")
    return render(request, 'sign_in.html', locals())


def logout_view(request):
    logout(request)
    return redirect('index')
