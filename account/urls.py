from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('register/', views.register),
    path('check_password/', views.check_password),
    path('change_password/', views.change_password),
    path('api-token-auth/', obtain_jwt_token),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('mypage/', views.mypage),
]