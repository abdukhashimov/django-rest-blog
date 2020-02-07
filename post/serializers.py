from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)
    author = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'author',
                  'content', 'tag', 'category', 'comment')

    def get_author(self, obj):
        return [str(obj.author), obj.author.profile_picture.url]

    def get_comment(self, obj):
        return {
            'comment': obj.comment.comment,
            'replies': obj.comment.objects.get_child_comment()
        }
