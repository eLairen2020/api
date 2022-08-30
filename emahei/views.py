from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from blog.models import Blog, BlogComment
from user.models import Teacher_Profile
from course.models import Courses, Categories

from .serializers import CourseSerializer, CourseListSerializer, CategoriesSerializer, TeacherProfileSerializer, TeacherProfileListSerializer, BlogSerializer, BlogListSerializer, TagSerializer, CommentSerializer
from django.db import models

#tag for blog
from taggit.models import Tag


# django filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




# SEARCH ENGINE ==== left to make ========================================================================




class CourseList(generics.ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Courses.objects.all()
    pagination_class = None
    # def get_queryset(self):
        # return Courses.objects.filter()[10]


class CategoryList(generics.ListAPIView):
    permission_class = [permissions.AllowAny]
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    pagination_class = None

class TeacherProfileList(generics.ListAPIView):
    serializer_class = TeacherProfileListSerializer
    queryset = Teacher_Profile.objects.all()

class BlogList(generics.ListAPIView):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    
class Tag(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

#--------------------------Specific GET-----------------------------------


class CourseDetail(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    queryset = Courses.objects.all()

class CategoriesDetail(generics.RetrieveAPIView):
    serializer_class = CategoriesSerializer
    lookup_field = 'pk'
    queryset = Categories.objects.all()

class TeacherProfileDetail(generics.RetrieveAPIView):
    serializer_class = TeacherProfileSerializer
    lookup_field = 'pk'
    queryset = Teacher_Profile.objects.all()

class BlogDetails(generics.RetrieveAPIView):
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    queryset = Blog.objects.all()



#=============================================================
class SearchList(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', '^requirments', '^What_you_will_learn']




class Comment(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset = Comment.objects.filter(blog=pk)
        return queryset



#-------------------------- Blog create-----------------

class CreateBlog(generics.CreateAPIView):
    serializer_class = BlogSerializer

class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer

# like create/ destroy fucntion-----------------------------


# Update coment -------------------------------------

class CommentUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    queryset = Categories.objects.all()

