from django.shortcuts import render, redirect
from . import model_forms
from .models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/accounts/login/")
def contact_create_list(request):
    chats = Contact.objects.all().order_by("date")
    if request.method == "POST":
        form = model_forms.CreateContact(request.POST)
        if form.is_valid(): 
            
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            form.author = request.user
            print( form.author,request.user)
            form.save()
            return render(request, "contact/contact_create_list.html", {"form": form,"chats": chats})
    else:
        form = model_forms.CreateContact()
        form.author = request.user
        print( form.author,request.user)

        form = model_forms.CreateContact()
    return render(request, "contact/contact_create_list.html", {"form": form,"chats": chats})
