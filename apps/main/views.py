# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import Snippet
from .forms import SnippetForm

def index(request):
    objs = Snippet.objects.all()
    ctx = {'objs': objs}
    return render(request, 'main/index.html', ctx)

def detail(request, pk):
    obj = Snippet.objects.get(pk=pk)
    ctx = {'obj': obj}
    return render(request, 'main/detail.html', ctx)

@login_required
def new(request):
    obj = Snippet(user=request.user)
    if request.method == 'GET':
        form = SnippetForm(instance=obj)
    else:
        form = SnippetForm(request.POST,instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('main:detail',pk=obj.pk)
    ctx = {'form': form}
    return render(request, 'main/new.html', ctx)

def tags(request):
    ctx = {}
    return render(request, 'main/tags.html', ctx)

def tag(request, tag_slug):
    objs = Snippet.objects.filter(tags__slug=tag_slug)
    ctx = {'objs': objs}
    return render(request, 'main/index.html', ctx)
