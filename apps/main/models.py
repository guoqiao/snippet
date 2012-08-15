# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    code = models.TextField()
    desc = models.CharField(max_length=512)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
