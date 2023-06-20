from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string

#drf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# models
from .models import User
from .serializers import UserSerializer, ChangePasswordSerializer

@api_view(['POST'])
def register(request):

    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if not password:
        return Response({'error': '비밀번호 입력 오류입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.is_active = False
        
        # 회원가입 인증메일 발송
        send_register_email()

        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def send_register_email():
    pass