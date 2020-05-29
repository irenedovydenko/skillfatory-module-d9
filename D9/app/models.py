from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User,
                               null=True,
                               default=None,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 null=True,
                                 blank=True,
                                 default=None,
                                 on_delete=models.SET_NULL)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


