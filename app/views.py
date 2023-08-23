from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.views import View
from django.utils.translation import activate
from .models import Video, PDFBook
from django.http import HttpResponse, FileResponse
import os
from django.contrib.staticfiles import finders

def timeline(request):
    return render(request, 'timeline.html')
def test(request):
    return render(request, 'test.html')
def pdf(request, pdf_id):    
    try:
        pdf_book = PDFBook.objects.get(pk=pdf_id)
        pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_book.pdf_file.name)
        print(pdf_path)
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    except PDFBook.DoesNotExist:
        return render(request, 'pdf_not_found.html')
    
def book_list(request):
    books = PDFBook.objects.all()
    return render(request, 'book_list.html', {'books': books})
def members(request):
    return render(request, 'members.html')
def founders(request):
    return render(request, 'founders.html')
def index(request):
    return render(request, 'index.html')
def sports(request):
    return render(request, 'sports.html')

def album(request):
    return render(request, 'album.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Corrected line
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


class SetLanguageView(View):
    def get(self, request, *args, **kwargs):
        lang_code = kwargs.get('lang_code')
        activate(lang_code)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang_code
        return redirect(request.META.get('HTTP_REFERER'))
