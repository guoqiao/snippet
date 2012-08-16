# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('title','code','desc','tags',)
