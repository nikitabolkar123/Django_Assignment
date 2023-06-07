from django.urls import path
from . import views

urlpatterns = [
    path('userregistration/<int:user_id>/', views.UserRegistration.as_view(), name='user_registration'),
    path('userregistration/', views.UserRegistration.as_view(), name='user_registration'),
    path('login/', views.Login.as_view(), name='logout'),
]
