from django.urls import path
from . import views

urlpatterns = [
    # Other URLs
    path('posts/', views.PostCreateView.as_view(), name='create_post'),
    # path('posts/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:post_id>/', views.PostCreateView.as_view(), name='create_post'),
    path('like/<int:like_id>/', views.LikeView.as_view(), name='create_post'),
    path('like/', views.LikeView.as_view(), name='create_like'),

]
