from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.views import View
from django.utils.translation import activate

def timeline(request):
    return render(request, 'timeline.html')
def test(request):
    return render(request, 'test.html')
def members(request):
    return render(request, 'members.html')
def founders(request):
    return render(request, 'founders.html')
def index(request):
    return render(request, 'index.html')
def sports(request):
    return render(request, 'sports.html')
def video(request):
    return render(request, 'video.html')



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
