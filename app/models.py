from django.db import models
from django.utils import timezone

class Founder(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='founder_images/')
    bio = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name
class MainCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory_images/',blank=True, null=True)
    parent_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) 

    def __str__(self):
        return self.name
    
class ChildCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) 

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True) 

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Chairman(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chairmans_images/')
    bio = models.TextField(blank=True)
    year_started = models.PositiveIntegerField(null=True, blank=True)
    year_ended = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Other fields you might want to include, such as upload date, tags, etc.

    def __str__(self):
        return self.title

class VideoPart(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='parts')
    part_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200, null=True, blank=True)
    video_file = models.FileField(upload_to='video_parts/')
    # Other fields you might want to include for each part

    class Meta:
        unique_together = ('video', 'part_number')  # Ensure each part has a unique part number within a video

    def __str__(self):
        return f"{self.video.title} - Part {self.part_number}: {self.title}"
    

class PDFBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

