from django.contrib import admin
from django.forms.models import inlineformset_factory

admin.site.site_title = "JSC"
admin.site.site_header = "JSC"
admin.site.index_title = "Adminstration"

from .models import Founder, MainCategory, SubCategory, Photo, Comment, Tag, ChildCategory, Chairman, Video, VideoPart,PDFBook

admin.site.register(Founder)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(PDFBook)
admin.site.register(Chairman)
admin.site.register(Video)
admin.site.register(VideoPart)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'approved')
    list_filter = ('category',)  # Add category as a filter option


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'approved')
    list_filter = ('approved',)  # Add category as a filter option

admin.site.register(Comment, CommentAdmin)

PhotoFormSet = inlineformset_factory(ChildCategory, Photo, fields=('title', 'image'), extra=1)

class PhotoInline(admin.TabularInline):  # Use TabularInline or StackedInline
    model = Photo
    formset = PhotoFormSet
    extra = 5  # Number of empty photo upload fields to display

@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Photo, PhotoAdmin)


