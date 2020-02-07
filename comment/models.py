from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.admin.utils import NestedObjects


class CommentManager(models.Manager):
    def get_parent_comment(self):
        return super(
            CommentManager, self).get_queryset().filter(parent__isnull=True)

    def get_child_comment(self):
        collector = NestedObjects(using='default')
        collector.collect(Comment.objects.get(id=1))
        print(collector.data[parents[0].__class__])


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', related_name='reply', null=True, blank=True,
        on_delete=models.CASCADE)

    objects = CommentManager()

    def __str__(self):
        if self.parent is None:
            return "{}'s comment".format(str(self.author))
        return "{}'s reply".format(str(self.author))

    # def get_child_comments(self, id):
        # return Comment.objects.filter(Q(parent_id=id))
