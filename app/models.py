from django.db import models

class Founder(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='founder_images/')
    bio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name

from django.db import models

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
    parent_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag) 

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag) 

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text

