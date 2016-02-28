# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from myapp.forms import CommentForm, ArticleForm, SubCommentsForm, ChangeArticleForm
from myapp.models import Articles, Comments, CommentToComment

#------------------- Главная страница (Main page) --------------------
def home(request, page_num=1):
    args = {}
    articles = Articles.objects.all()
    comments = Comments.objects.all()
    subcomments = CommentToComment.objects.all()
    current_page = Paginator(articles, 3)               # Разбиение сообщений на страницы
    args = {
        'articles': current_page.page(page_num),
        'comments': comments,
        'subcomments': subcomments,
    }
    return render(request, "myapp/home.html", args)

#-- Отдельная страница с формой комментария (Page with comment for)----
def article(request, articles_id=1):
    args = {}
    args.update(csrf(request))
    args = {
        'form': CommentForm(),
        'article': Articles.objects.get(id=articles_id),
        'comments': Comments.objects.filter(article_id=articles_id),
        'subcomments': CommentToComment.objects.all(),
    }
    return render(request, "myapp/articl.html", args)

#------------ Добавление сообщения (Add message on the wall)------------
def addarticle(request, user_id=1):
    args = {}
    args.update(csrf(request))
    if request.POST:
        newart = ArticleForm(request.POST)
        if newart.is_valid():
            new = newart.save(commit=False)
            new.user = User.objects.get(id=user_id)
            new.save()
    return redirect('/', args)

#------------- Добавление комментария (Add comment)----------------------
def addcomment(request, articles_id=1, user_id=1):
    if request.POST:
        newcomm = CommentForm(request.POST)
        if newcomm.is_valid():
            comment = newcomm.save(commit=False)
            comment.article = Articles.objects.get(id=articles_id)
            comment.user = User.objects.get(id=user_id)
            newcomm.save()
    return redirect('/article/%s/' % articles_id)

#-- Добавление комментария на комментарий (Add comments to comment)------
def addsubcomment(request, articles_id, comment_id=1, user_id=1):
    if request.POST:
        newsubcomm = SubCommentsForm(request.POST)
        if newsubcomm.is_valid():
            subcomm = newsubcomm.save(commit=False)
            subcomm.comment = Comments.objects.get(id=comment_id)
            subcomm.user = User.objects.get(id=user_id)
            subcomm.save()
    return redirect('/article/%s' % articles_id)

#------------------- Удаление сообщений (Message remove) -----------------
def article_delete(request, articles_id=1):
    art = get_object_or_404(Articles, id=articles_id)
    if request.POST:
        art.delete()
    return redirect('/')

#-------------- Удаление комментариев (Comments remove)--------------------
def comment_delete(request, articles_id=1, comment_id=1):
    comm = get_object_or_404(Comments, id=comment_id)
    if request.POST:
        comm.delete()
    return redirect('/article/%s' % articles_id)

#------- Удаление ответов на коментарии (Remove answers to comments)-------
def subcomment_delete(request, articles_id=1, subcomment_id=1):
    sub = get_object_or_404(CommentToComment, id=subcomment_id)
    if request.POST:
        sub.delete()
    return redirect('/article/%s' % articles_id)

#----------------------------- Выход (Logout)------------------------------
def logout(request):
    auth.logout(request)
    return redirect('/')
