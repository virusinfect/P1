from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.views import View
from django.utils.translation import activate


def backend(request):
    return render(request, 'backend\index.html')