# Create your views here.
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.data.update({'user': request.user.id})
            serializer = PostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"message": "Post Created Successfully", "status": 201, "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)





    def get(self, request):
        try:
            posts = Post.objects.annotate(like_count=Count('like')).filter(visibility='public')
            serialized_data = PostSerializer(posts, many=True).data

            for post in serialized_data:
                if post['user'] != request.user.id:
                    post['private'] = True if post['visibility'] == 'private' else False
                else:
                    post['private'] = False
                post.pop('visibility')  # Remove the 'visibility' field from the serialized data

            return Response({'message': ' data retrieved successfully', 'data': serialized_data, 'status': 200},
                            status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    # def get(self, request):
    #     posts = Post.objects.all()
    #     serialized_data = []
    #
    #     for post in posts:
    #         if post.user != request.user and not post.is_public:
    #             continue
    #         serialized_post = PostSerializer(post).data
    #         serialized_post['like_count'] = post.like_set.count()  # Count likes for the post
    #         serialized_data.append(serialized_post)
    #     return Response(serialized_data)
    # def get(self, request):
    #     posts = Post.objects.annotate(like_count=Count('like')).filter(
    #         models.Q(user=request.user) | models.Q(is_public=True)
    #     )
    #     serialized_data = PostSerializer(posts, many=True).data
    #     return Response(serialized_data)

    def put(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.user != request.user:
                raise PermissionDenied("You don't have permission to perform this action.")

            serializer = PostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # try:
            #     # request.data.update({'user': request.user.id})  #
            #     if post.user != request.user:
            #         raise PermissionDenied("You don't have permission to perform this action.")
            #     post = Post.objects.get(id=post_id)
            #     serializer = PostSerializer(post, data=request.data)
            #     serializer.is_valid(raise_exception=True)
            #     serializer.save()
            return Response({"message": "Updated Successfully", "status": 200, "data": serializer.data},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.user != request.user:
                raise PermissionDenied("You don't have permission to perform this action.")

            post.delete()
            # try:
            #     books = Post.objects.get(id=post_id)
            #     books.delete()
            return Response({"message": " deleted Successfully", "status": 200, "data": {}},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)


class LikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     try:
    #         request.data.update({'user': request.user.id})
    #         # post = Post.objects.get(id=request.data.get('post_id'))
    #         # post = Like.objects.get(id='post_id')
    #         serializer = LikeSerializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(
    #             {"message": "Post Created Successfully", "status": 201, "data": serializer.data},
    #             status=status.HTTP_201_CREATED
    #         )
    #     except Exception as e:
    #         # logger.exception(e)
    #         return Response(
    #             {"message": str(e), "status": 400, "data": {}},
    #             status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = LikeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Like Added successfully', 'data': serializer.data, 'status': 200},
                            status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def get(self, request):
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response({'message': 'data retrieved successfully', 'data': serializer.data, 'status': 200},
                            status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, like_id):
        try:
            # request.data.update({'user': request.user.id})  #
            like = Like.objects.get(id=like_id)
            serializer = LikeSerializer(like, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Updated Successfully", "status": 200, "data": serializer.data},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)

    def delete(self, request, like_id):
        try:
            like = Like.objects.get(id=like_id)
            like.delete()
            return Response({"message": " deleted Successfully", "status": 200, "data": {}},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)

    # def get(self, request):
    #     posts = Post.objects.annotate(likes_count=Count('likes')).prefetch_related(
    #         Prefetch('likes', queryset=Like.objects.all().select_related('user'))
    #     )
    #     serializer = PostSerializer(posts, many=True)
    #     return Response({'message': 'Post data retrieved successfully', 'data': serializer.data}, status=200)
