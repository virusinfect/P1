from django.shortcuts import render
from .models import MainCategory, SubCategory, Photo, ChildCategory, Comment
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def subcategories_list(request, main_category_id):
    main_category = MainCategory.objects.get(pk=main_category_id)
    subcategories = SubCategory.objects.filter(parent_category=main_category)
    return render(request, 'sports.html', {'main_category': main_category, 'subcategories': subcategories})

def child_category_images(request, child_category_id):
    child_category = ChildCategory.objects.get(pk=child_category_id)
    images = Photo.objects.filter(category=child_category)
    return render(request, 'album.html', {'child_category': child_category, 'images': images})

def get_comments(request):
    photo_id = request.GET.get('photo_id')
    comments = Comment.objects.filter(photo_id=photo_id, approved=True).values('text')
    return JsonResponse({'comments': list(comments)})

def get_comment_count(request):
    photo_id = request.GET.get('photo_id')
    photo = get_object_or_404(Photo, id=photo_id)
    comment_count = Comment.objects.filter(photo=photo, approved=True).count()
    return JsonResponse({'commentCount': comment_count})