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

from .views import (Type_of_examList, Examinationlist, Mcqestionlist, Student_Answer_recordlist, Type_of_examAllList, ExaminationAllList, McqestionAllList, Student_Answer_recordAllList, CreateType_of_exam, CreateExamination, CreateMcqestion,
 CreateStudent_Answer_record, UpdateStudent_Answer_record, UpdateMcqestion, UpdateExamination, UpdateType_of_exam, )


urlpatterns = [

    path('Type_of_examList/', Type_of_examList.as_view(), name='Type_of_examList'),
    path('ExaminationList/', Examinationlist.as_view(), name='ExaminationList'),
    path('McqestionList/', Mcqestionlist.as_view(), name='McqestionList'),
    path('Student_Answer_recordList/', Student_Answer_recordlist.as_view(), name='Student_Answer_recordList'),

    path('Type_of_exam/<str:id>', Type_of_examAllList.as_view(), name='Type_of_exam'),
    path('Examination/<str:id>', ExaminationAllList.as_view(), name='Examination'),
    path('Mcqestion/<str:id>', McqestionAllList.as_view(), name='Mcqestion'),
    path('Student_Answer_record/<str:id>', Student_Answer_recordAllList.as_view(), name='Student_Answer_record'),

    path('CreateType_of_exam/', CreateType_of_exam.as_view(), name='CreateType_of_exam'),
    path('CreateExamination/', CreateExamination.as_view(), name='CreateExamination'),
    path('CreateMcqestion/', CreateMcqestion.as_view(), name='CreateMcqestion'),
    path('CreateStudent_Answer_record/', CreateStudent_Answer_record.as_view(), name='CreateStudent_Answer_record'),

    path('UpdateType_of_exam/<str:id>', UpdateType_of_exam.as_view(), name='UpdateType_of_exam'),
    path('UpdateExamination/<str:id>', UpdateExamination.as_view(), name='UpdateExamination'),
    path('UpdateMcqestion/<str:id>', UpdateMcqestion.as_view(), name='UpdateMcqestion'),
    path('UpdateStudent_Answer_record/<str:id>', UpdateStudent_Answer_record.as_view(), name='UpdateStudent_Answer_record'),



]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)