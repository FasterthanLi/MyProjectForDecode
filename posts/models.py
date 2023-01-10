from django.conf import settings
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    @property
    def categories(self):
        return ', '.join([x.name for x in self.category.all()])

class Comment(models.Model): 
    article = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("post_list")

