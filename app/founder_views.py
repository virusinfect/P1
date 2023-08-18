from django.shortcuts import render, get_object_or_404
from .models import Founder

def founders_list(request):
    founders = Founder.objects.all()
    return render(request, 'founders.html', {'founders': founders})

def founderbio(request, founder_id):
    founder = get_object_or_404(Founder, id=founder_id)
    return render(request, 'founder_bio.html', {'founder': founder})

