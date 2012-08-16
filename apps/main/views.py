# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect

from .models import Snippet

def index(request):
    objs = Snippet.objects.all()
    ctx = {'objs': objs}
    return render(request, 'main/index.html', ctx)

def detail(request, pk):
    obj = Snippet.objects.get(pk=pk)
    ctx = {'obj': obj}
    return render(request, 'main/detail.html', ctx)
