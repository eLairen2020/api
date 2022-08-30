from typing import ChainMap

from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

#------------------------------------------------------------

from django.contrib.auth.models import User
from user.models import Teacher_Profile
from .models import Courses, Categories, Chapter, Reviews, Topics, QuestionBank, Ebooks, Enotes, FAQ, Course_enroll_details

from .serializers import ( CategorySerializer, ChapterSerializer, Course_enroll_detailsSerializer, CourseSerializer, TopicsSerializer, FAQSerializer,
 QuestionBankSerializer, EbooksSerializer, EnotesSerializer, ReviewsSerializer)
from django.db import models

#  API for viewing=============================================================================================== 

class ChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer
    # queryset = Chapter.objects.all()

    def get_queryset(self) :
        pk = self.kwargs.get("id")
        print(pk)
        # isinstance = get_object_or_404(Courses,pk=id)
        queryset = Chapter.objects.filter(course_name=pk).order_by('chapter_no')
        return queryset

class TopicsList(generics.ListAPIView):
    serializer_class = TopicsSerializer
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset = Topics.objects.filter(name=pk).order_by('-topic_no')
        return queryset

class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset = FAQ.objects.filter(course_name=pk)
        return queryset

class QuestionBankList(generics.ListAPIView):
    serializer_class = QuestionBankSerializer
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  QuestionBank.objects.filter(course_name=pk)
        return queryset

class EbooksList(generics.ListAPIView):
    serializer_class = EbooksSerializer
    queryset = Ebooks.objects.all()

class EnotesList(generics.ListAPIView):
    serializer_class = EnotesSerializer
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  Enotes.objects.filter(course_name=pk)
        return queryset


#---------------------need adjustment---------------------------------#


class Course_enroll_detailsList(generics.ListAPIView):
    serializer_class = Course_enroll_details
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset = Course_enroll_details.objects.filter(course_name=pk)
        return queryset

class ReviewsList(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset = Enotes.objects.filter(course_name=pk)
        return queryset  

#--------------------------------------API for creating-----------------------------------------

class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CreateCourse(generics.CreateAPIView):
    serializer_class = CourseSerializer

class CreateChapter(generics.CreateAPIView):
    serializer_class = ChapterSerializer

class CreateTopic(generics.CreateAPIView):
    serializer_class = TopicsSerializer

class CreateFAQ(generics.CreateAPIView):
    serializer_class = FAQSerializer

class CreateQuestionBank(generics.CreateAPIView):
    serializer_class = QuestionBankSerializer

class CreateEbook(generics.CreateAPIView):
    serializer_class = EbooksSerializer

class CreateEnotes(generics.CreateAPIView):
    serializer_class = EnotesSerializer

class CreateCourseEnroll(generics.CreateAPIView):
    serializer_class = Course_enroll_detailsSerializer

class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewsSerializer

# API for Updating ======================================================

class UpdateCourse(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    queryset = Courses.objects.all()

class UpdateChapter(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapterSerializer
    lookup_field = 'pk'
    queryset = Chapter.objects.all()

class UpdateTopic(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicsSerializer
    lookup_field = 'pk'
    queryset = Topics.objects.all()

class UpdateFAQ(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FAQSerializer
    lookup_field = 'pk'
    queryset = FAQ.objects.all()


class UpdateQuestionBank(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionBankSerializer
    lookup_field = 'pk'
    queryset = QuestionBank.objects.all()

    
class UpdateEbook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EbooksSerializer
    lookup_field = 'pk'
    queryset = Ebooks.objects.all()

class UpdateEnotes(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnotesSerializer
    lookup_field = 'pk'
    queryset = Enotes.objects.all()

class UpdateReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializer
    lookup_field = 'pk'
    queryset = Reviews.objects.all()

# from django.http import HttpResponse
# from django.contrib.auth.models import User, auth
# from django.forms import inlineformset_factory
# from django.views.generic import ListView
# from django.core.paginator import Paginator
# from user_accounts.models import User_profile

# from django.contrib import messages 
# from django.contrib.auth.forms import UserCreationForm
# from courses.models import Courses, Categories, Chapter, Topics, FAQ, Enotes, Ebooks, Course_enroll_details



# class CourseDetail(generics.RetrieveAPIView):
#     serializer_class = CourseSerializer
#     lookup_field = 'pk'
#     queryset = Courses.objects.all()
    

#     def coursedetails(request, id=None):
#     isinstance = get_object_or_404(Courses,pk=id)
#         if request.method == "POST":
#             user = request.user
            
#             pay_ = request.POST.get('pay')
#             Course_enroll_details.objects.create(
#                 student_name = user,
#                 course_name = isinstance,
#                 payment_details = pay_,
#             )

#         categories = Categories.objects.all()
#         chapter1 = Chapter.objects.filter(course_name=isinstance).order_by('chapter_no')
#         chapter2 = Chapter.objects.filter(course_name=isinstance).count()
#         faqs = FAQ.objects.filter(course_name=isinstance)
#         user_ = request.user.id
#         mycourse = Course_enroll_details.objects.filter(student_name=user_,course_name=isinstance)
#         user_= request.user
#         if user_.is_authenticated:
            
#             profile = User_profile.objects.filter(username=user_)
#         else :
#             profile = User_profile.objects.filter(username=1)
#         return


# class CategoriesDetail(generics.RetrieveAPIView):

#     serializer_class = CategoriesSerializer
#     lookup_field = 'pk'
#     queryset = Categories.objects.all()
    























# # Create your views here.

# def coursedetails(request, id=None):
   
#     if request.method == "POST":
#         user = request.user
        
#         pay_ = request.POST.get('pay')
#         Course_enroll_details.objects.create(
#             student_name = user,
#             course_name = isinstance,
#             payment_details = pay_,
#         )

#     categories = Categories.objects.all()
#     chapter1 = Chapter.objects.filter(course_name=isinstance).order_by('chapter_no')
#     chapter2 = Chapter.objects.filter(course_name=isinstance).count()
#     faqs = FAQ.objects.filter(course_name=isinstance)
#     user_ = request.user.id
#     mycourse = Course_enroll_details.objects.filter(student_name=user_,course_name=isinstance)
#     user_= request.user
#     if user_.is_authenticated:
        
#         profile = User_profile.objects.filter(username=user_)
#     else :
#         profile = User_profile.objects.filter(username=1)
#     return render(request, "coursedetails.html", {'Courses':isinstance,
#     'cat_nav':categories,
#     'chapt': chapter1,
#     'count': chapter2,
#     'faqs' : faqs,
#     'mycourse':mycourse,
#     'profile':profile

#     });

# def allcourses(request,id):

#     isinstance = get_object_or_404(Categories,pk=id)
#     category = Categories.objects.all()
#     courses = Courses.objects.filter(category_id=isinstance)
#     paginator = Paginator(courses, 3)
#     page = request.GET.get('page')
#     courses = paginator.get_page(page)
#     user_= request.user
#     if user_.is_authenticated:
        
#         profile = User_profile.objects.filter(username=user_)
#     else :
#         profile = User_profile.objects.filter(username=1)
#     return render(request, "allcourses.html",{'categories':isinstance, 'course':courses,'cat_nav': category ,'profile':profile});


# def video(request,id):
#     isinstance = get_object_or_404(Courses,pk=id)
#     user_= request.user
#     categories = Categories.objects.all()
#     chapter1 = Chapter.objects.filter(course_name=isinstance).order_by('chapter_no')
#     chapter2 = Chapter.objects.filter(course_name=isinstance).count()
#     faqs = FAQ.objects.filter(course_name=isinstance)
#     mycourse = Course_enroll_details.objects.filter(student_name=user_,course_name=isinstance)
#     if user_.is_authenticated:

#         profile = User_profile.objects.filter(username=user_)
#     else :
#         profile = User_profile.objects.filter(username=1)

    
#     enrolluser = Course_enroll_details.objects.filter(student_name=user_,course_name=isinstance)
#     if enrolluser: 
#         category = Categories.objects.all()

#         chapter1 = Chapter.objects.filter(course_name=isinstance).order_by('chapter_no')
#         chapter2 = Chapter.objects.filter(course_name=isinstance).count()
#         course = Courses.objects.filter(title=isinstance)
#         faqs = FAQ.objects.filter(course_name=isinstance)
#         notes = Enotes.objects.filter(course_name=isinstance)


#         user_= request.user
#         if user_.is_authenticated:

#             profile = User_profile.objects.filter(username=user_)
#         else :
#             profile = User_profile.objects.filter(username=1)
#     else:
#         return HttpResponse('<h1>page not found. Go back to previous page</h1>')
    

#     return render(request, "mainvideo.html",{'cat_nav':category, 'chapt': chapter1, 'count': chapter2, 'enotes': notes, 'faqs': faqs, 'course': course ,'profile':profile});



# def videoplay(request,id):
#     category = Categories.objects.all()
#     isinstance = get_object_or_404(Topics,pk=id)
#     top = Topics.objects.get(name=isinstance)
#     c_name = top.chapter.course_name.id
#     d_name = top.chapter.id
#     course_all = Courses.objects.get(id=c_name)
#     chapter = Chapter.objects.filter(course_name=course_all)
#     chapter2 = Chapter.objects.filter(course_name=course_all).count()
#     faqs = FAQ.objects.filter(course_name=course_all)
#     notes = Enotes.objects.filter(course_name=course_all).order_by('chapter_name')

#     user_= request.user
#     if user_.is_authenticated:
        
#         profile = User_profile.objects.filter(username=user_)
#     else :
#         profile = User_profile.objects.filter(username=1)
    
#     return render(request, "mainvideoplay.html",{'cat_nav':category, 'chap': chapter,'topic':top,'enotes': notes, 'count': chapter2,'faqs': faqs, 'cour': course_all,'profile':profile });


# def mycourses(request):
#     category = Categories.objects.all()
#     user_ = request.user
#     mycourse = Course_enroll_details.objects.filter(student_name=user_)
#     paginator = Paginator(mycourse, 3)
#     page = request.GET.get('page')
#     mycourse = paginator.get_page(page)

#     user_= request.user
#     if user_.is_authenticated:
        
#         profile = User_profile.objects.filter(username=user_)
#     else :
#         profile = User_profile.objects.filter(username=1)
    
#     return render(request, "mycourses.html" ,{'cat_nav':category, 'mycourse':mycourse,'profile':profile})



    
    











