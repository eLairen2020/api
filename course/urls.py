"""emahei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (ChapterList, TopicsList, FAQList, QuestionBankList, EbooksList, EnotesList, Course_enroll_detailsList, ReviewsList,
 CreateCourse, CreateChapter, CreateTopic , CreateFAQ , CreateQuestionBank , CreateEbook , CreateEnotes, CreateCourseEnroll, CreateReview, CreateCategory,
 UpdateCourse, UpdateChapter, UpdateTopic, UpdateFAQ, UpdateEbook, UpdateQuestionBank, UpdateEnotes, UpdateReview)


urlpatterns = [
    # Get
    path('chapter/<int:id>', ChapterList.as_view(), name='ChapterList_for Specific_courses'),
    path('topics/<int:id>', TopicsList.as_view(), name='TopicsList_for specific_course'),
    path('FAQ/<int:id>', FAQList.as_view(), name='FAQList_for_specific_course'),
    path('questionbank/<int:id>', QuestionBankList.as_view(), name='QuestionBankList_for_specific_course'),
    path('ebooks/<int:id>', EbooksList.as_view(), name='EbooksList'),
    path('enotes/<int:id>', EnotesList.as_view(), name='EnotesList_for_specific_course'),
    path('course_enroll/<int:id>', Course_enroll_detailsList.as_view(), name='Course_enroll_detailsList'),
    path('review/<int:id>', ReviewsList.as_view(), name='ReviewsList_for_specific_course'),
    # Create
    path('CreateCourse/', CreateCourse.as_view(), name='CreateCourse'),
    path('CreateChapter/', CreateChapter.as_view(), name='CreateChapter'),
    path('CreateTopic/', CreateTopic.as_view(), name='CreateTopic'),
    path('CreateFAQ/', CreateFAQ.as_view(), name='CreateFAQ'),
    path('CreateQuestionBank/', CreateQuestionBank.as_view(), name='CreateQuestionBank'),
    path('CreateEbook/', CreateEbook.as_view(), name='CreateEbook'),
    path('CreateEnotes/', CreateEnotes.as_view(), name='CreateEnotes'),
    path('CreateCourseEnroll/', CreateCourseEnroll.as_view(), name='CreateCourseEnroll'),
    path('CreateReview/', CreateReview.as_view(), name='CreateReview'),
    path('CreateCategory/', CreateCategory.as_view(), name='CreateCategory'),
    # Update
    path('UpdateCourse/<int:pk>', UpdateCourse.as_view(), name='UpdateCourse'),
    path('UpdateChapter/<int:pk>', UpdateChapter.as_view(), name='UpdateChapter'),
    path('UpdateTopic/<int:pk>', UpdateTopic.as_view(), name='UpdateTopic'),
    path('UpdateFAQ/<int:pk>', UpdateFAQ.as_view(), name='UpdateFAQ'),
    path('UpdateQuestionBank/<int:pk>', UpdateQuestionBank.as_view(), name='UpdateQuestionBank'),
    path('UpdateEbook/<int:pk>', UpdateEbook.as_view(), name='UpdateEbook'),
    path('UpdateEnotes/<int:pk>', UpdateEnotes.as_view(), name='UpdateEnotes'),
    path('UpdateReview/<int:pk>', UpdateReview.as_view(), name='UpdateReview'),

#    path('BlogComment/<int:id>', Comment.as_view(), name='Comment'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)