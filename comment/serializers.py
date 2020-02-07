from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('author', 'comment', 'replies')

    # def get_replies(self, obj):
        # comment = obj.get_child_comments(obj.id)
        # print(comment)
        # return 'None'
