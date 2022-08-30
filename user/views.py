from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .models import Student_Profile, School, Teacher_Profile
from .serializers import UserSerializer, StudentProfileSerializer, SchoolSerializer,TeacherProfileSerializer

from django.db import models

from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['POST',])

def api_User(request, id):
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

# genrics.UpdateRetrieveDestroyAPIView

class CreateUser(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
 
# get user details api

class GetUserDetail(generics.RetrieveAPIView):
    serializer_class = StudentProfileSerializer
    lookup_field = 'pk'
    queryset = Student_Profile.objects.all()

class GetSchoolDetail(generics.RetrieveAPIView):
    serializer_class = SchoolSerializer
    lookup_field = 'pk'
    queryset = School.objects.all()

class GetTeacherDetail(generics.RetrieveAPIView):
    serializer_class = TeacherProfileSerializer
    lookup_field = 'pk'
    queryset = Teacher_Profile.objects.all()


# updating user details for all the type of user

class UpdateStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentProfileSerializer
    lookup_field = 'pk'
    queryset = Student_Profile.objects.all()

class UpdateSchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    lookup_field = 'pk'
    queryset = School.objects.all()

class UpdateTeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherProfileSerializer
    lookup_field = 'pk'
    queryset = Teacher_Profile.objects.all()


class SchoolList(generics.RetrieveAPIView):
    serializer_class = SchoolSerializer
    queryset = Student_Profile.objects.all()

class StudentList(generics.RetrieveAPIView):
    serializer_class = StudentProfileSerializer
    queryset = Student_Profile.objects.all()