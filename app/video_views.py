from django.shortcuts import render
from .models import Video
from django.shortcuts import render, get_object_or_404

def video_list(request):
    videos = Video.objects.prefetch_related('parts').all()  # Fetch all videos with their parts
    context = {'videos': videos}
    return render(request, 'video_list.html', context)

def video_player(request, video_id):
    video = Video.objects.get(id=video_id)
    parts = video.parts.all()
    context = {
        'video': video,
        'parts': parts,
    }
    return render(request, 'video_player.html', context)

def celebration_video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        video = None

    return render(request, '75years.html', {'video': video})
