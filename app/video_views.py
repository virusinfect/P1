from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.prefetch_related('parts').all()  # Fetch all videos with their parts
    context = {'videos': videos}
    return render(request, 'video_list.html', context)
