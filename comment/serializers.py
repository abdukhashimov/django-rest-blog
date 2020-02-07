from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('author', 'comment', 'replies')

    def get_replies(self, obj):
        return Comment.objects.get_child_comment()
