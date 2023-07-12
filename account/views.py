from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# drf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# auth, author
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
        user.is_active = True
        # user.is_active = False
        
        # 회원가입 인증메일 발송
        # send_register_email()

        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 회원가입 인증메일 발송 함수
def send_register_email():
    pass

@api_view(['POST'])
def activate(request, uid64, token):
    pass

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def check_password(request):

    email = request.user.username
    password = request.user.password

    user = get_object_or_404(get_user_model(), email=email)

    if password != user.password:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': '인증됐습니다.'})

@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):

    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if not password:
        return Response({'error': '비밀번호 입력 오류 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ChangePasswordSerializer(request.user, data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mypage(request):

    user = request.user
    user_serializer = UserSerializer(data=user)

    data = {
        'user': user_serializer.data,
    }

    return JsonResponse(data, status=status.HTTP_200_OK)