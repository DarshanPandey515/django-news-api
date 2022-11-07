from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.


class PostModel(models.Model):
    source = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    author = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    publishedAt = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    url = models.CharField(max_length=1000,null=True,blank=True)
    urlToImage = models.CharField(max_length=1000,null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.title