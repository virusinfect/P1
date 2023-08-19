from django.shortcuts import render
from .models import MainCategory, SubCategory, Photo, ChildCategory

def subcategories_list(request, main_category_id):
    main_category = MainCategory.objects.get(pk=main_category_id)
    subcategories = SubCategory.objects.filter(parent_category=main_category)
    return render(request, 'sports.html', {'main_category': main_category, 'subcategories': subcategories})

def child_category_images(request, child_category_id):
    child_category = ChildCategory.objects.get(pk=child_category_id)
    images = Photo.objects.filter(category=child_category)
    return render(request, 'album.html', {'child_category': child_category, 'images': images})