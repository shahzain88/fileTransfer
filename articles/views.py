from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import model_forms
# Create your views here.


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        #                                   files dont come with POST so ...
        form = model_forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:

        form = model_forms.CreateArticle()
    return render(request, "articles/article_creat.html", {"form": form})

@login_required(login_url="/accounts/login/")
def article_list(request):

    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {"articles": articles})

@login_required(login_url="/accounts/login/")
def article_detail(requeat, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(requeat, "articles/article_detail.html", {"article": article})

@login_required(login_url="/accounts/login/")
def delete_article(request,slug):
    article = Article.objects.get(slug=slug)
    article.thumb_delete()
    article.delete()

    return redirect("articles:list")