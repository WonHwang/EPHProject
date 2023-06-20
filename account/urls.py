from django.urls import path
from rest_framework import obtain_jwt_token
from . import views

urlpatterns = [
    path('register/'),
    path('check_password/'),
    path('change_password/'),
    path('api-token-auth/'),
    path('activate/<str:uid64>/<str:token>/'),
    path('mypage/'),
]