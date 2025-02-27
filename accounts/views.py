from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout


# Create your views here.

# Create your views here.
def account_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def account_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                print("[***?next=] ", request.POST.get("next"))
                return redirect(request.POST.get("next"))
            else:
                # print(request.read())
                return redirect("articles:list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def account_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("articles:list")
