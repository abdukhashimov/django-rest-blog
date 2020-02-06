from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', related_name='reply', null=True, blank=True,
        on_delete=models.CASCADE)

    def __str__(self):
        if self.parent is None:
            return "{}'s comment".format(str(self.author))
        return "{}'s reply".format(str(self.author))
