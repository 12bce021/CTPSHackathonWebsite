# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return render(request, 'verif/index.html')

def login(request):
    return HttpResponse("Welcome to login page.")