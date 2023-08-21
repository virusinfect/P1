from django.shortcuts import render, get_object_or_404
from .models import Founder, Chairman

def founders_list(request):
    founders = Founder.objects.all()
    return render(request, 'founders.html', {'founders': founders})

def founderbio(request, founder_id):
    founder = get_object_or_404(Founder, id=founder_id)
    return render(request, 'founder_bio.html', {'founder': founder})

def chairmans_list(request):
    chairmans = Chairman.objects.all()
    return render(request, 'chairmans.html', {'chairmans': chairmans})

def chairmanbio(request, chairman_id):
    chairman = get_object_or_404(Chairman, id=chairman_id)
    return render(request, 'chairman_bio.html', {'chairman': chairman})