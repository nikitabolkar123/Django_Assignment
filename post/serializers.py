from rest_framework import serializers
from .models import Like, Post


#
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         like = Like.objects.all()
#         fields = ['id', 'user', 'title', 'description', 'content', 'visibility', 'like']
#         read_only_fields = ['like']
#
class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'content', 'visibility', 'like_count']
        # read_only_fields = ['like']

    # def get_like(self, obj):
    #     # Assuming that Like is a related_name in the Post model's ManyToManyField
    #     likes = obj.like.all()
    #     like_count = likes.count()
    #     return like_count

# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ['post', 'user']
#     # read_only_fields = ['like', 'visibility']
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']

    # def create(self, validated_data):
    # post = validated_data.get('post')
    # user = validated_data.get('user')
    # like = Like.objects.filter(post_id=post.id)
    # a_list = []
    # for i in like:
    #     a_list.append(i.id)
    # validated_data.update({'like': a_list})
    # return validated_data

    # post = validated_data['post']
    # print(post.id)
    # user = self.context['request'].user
    # print(user.id)
    # like = Like.objects.filter(post_id=post)
    # print(like)

    # Check if the user has already liked the post

    # if Like.objects.filter(post=post, user=user).exists():
    #     raise serializers.ValidationError('User has already liked this post.')
    #
    # # Increase the likes count of the post
    # post.likes_count += 1
    # post.save()
    # print(validated_data, 1213)
    # print(super().create(validated_data))
    # return super().create(validated_data)
