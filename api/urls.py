from django.urls import path
from .views import UserViewsApi, GetUserViewsApi



urlpatterns = [
    path('users/', UserViewsApi.as_view(), name='users'),
    path('users/<int:pk>/', GetUserViewsApi.as_view(), name='getusers'),
]
