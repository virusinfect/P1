from django.contrib import admin

admin.site.site_title = "JSC"
admin.site.site_header = "JSC"
admin.site.index_title = "Adminstration"

from .models import Founder, MainCategory, SubCategory, Photo, Comment, Tag, ChildCategory, Chairman, Video, VideoPart

admin.site.register(Founder)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(ChildCategory)
admin.site.register(Chairman)
admin.site.register(Video)
admin.site.register(VideoPart)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'approved')
    list_filter = ('category',)  # Add category as a filter option

admin.site.register(Photo, PhotoAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'approved')
    list_filter = ('approved',)  # Add category as a filter option

admin.site.register(Comment, CommentAdmin)


