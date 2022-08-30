from pickle import TRUE
from rest_framework import serializers
from user.models import Teacher_Profile
from django.contrib.auth.models import User

from rest_framework.response import Response
from course.models import Courses, Categories
from blog.models import Blog, BlogComment
from user.models import Teacher_Profile
from rest_framework import status, generics, permissions

from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

#==============================================================================================================
#for index page 

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['title', 'subtitle','price','offerprice','picture','category','instructor','durations']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

# for category list its the same
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']

class TeacherProfileListSerializer(serializers.ModelSerializer):
    username1 = serializers.CharField(source='username.username', read_only=TRUE)
    class Meta:
        model = Teacher_Profile
        depth = 1
        fields = ['username1','first_name','last_name']

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Profile
        fields = '__all__'


class BlogListSerializer(TaggitSerializer,serializers.ModelSerializer):
    hashtagg = TagListSerializerField()
    class Meta:
        model = Blog
        depth = 1
        fields = ['title','author','about_designation', 'blog_image', 'date_of_publish', 'article','hashtagg']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


#================================================================================================================================
#for blog  page

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        depth = 1
        fields = '__all__'







# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     confirm_password = serializers.CharField()
#     usertype = serializers.CharField()

#     def validate_email(self, email):
#         existing = User.objects.filter(email=email).first()
#         if existing:
#             raise serializers.ValidationError("Someone with that email "
#                 "address has already registered. Was it you?")
#         return email

#     def validate(self, data):
#         if not data.get('password') or not data.get('confirm_password'):
#             raise serializers.ValidationError("Please enter a password and "
#                 "confirm it.")
#         if data.get('password') != data.get('confirm_password'):
#             raise serializers.ValidationError("Those passwords don't match.")
#         return data

#     def create(self, validated_data):
#         user = User.objects.create(
#         username=validated_data['username'],
#         email=validated_data['email'],
#         password=make_password(validated_data['password'])
#         )
#         if validated_data['usertype']=="School":
#             profile = School.objects.create(username=user)

#         elif validated_data['usertype']=="Teacher":
#             profile = Teacher_Profile.objects.create(username=user)

#         elif validated_data['usertype']=="Student":
#             profile = Student_Profile.objects.create(username=user)

#         return Response(profile, status=status.HTTP_201_CREATED)
    


