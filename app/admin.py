from django.contrib import admin

admin.site.site_title = "JSC"
admin.site.site_header = "JSC"
admin.site.index_title = "Adminstration"

from .models import Founder, MainCategory, SubCategory, Photo, Comment, Tag, ChildCategory

admin.site.register(Founder)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(ChildCategory)
