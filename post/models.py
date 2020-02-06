from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s post {}...".format(str(self.author), self.content[:20])
