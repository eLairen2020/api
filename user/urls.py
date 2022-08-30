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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User


from .views import (api_User, SchoolList, StudentList, GetUserDetail, GetTeacherDetail, GetSchoolDetail, UpdateSchoolDetail, UpdateTeacherDetail, UpdateStudentDetail, CreateUser)

urlpatterns = [
    path('user/<str:id>', api_User, name='User'),
    path('GetStudentDetail/<str:pk>', GetUserDetail.as_view(), name='getUserDetail'),
    path('GetTeacherDetail/<str:pk>', GetTeacherDetail.as_view(), name='GetTeacherDetail'),
    path('GetSchoolDetail/<str:pk>', GetSchoolDetail.as_view(), name='getSchoolDetail'),
    path('UpdateSchoolDetail/<str:pk>', UpdateSchoolDetail.as_view(), name='UpdateSchoolDetail'),
    path('UpdateTeacherDetail/<str:pk>', UpdateTeacherDetail.as_view(), name='UpdateTeacherDetail'),
    path('UpdateStudentDetail/<str:pk>', UpdateStudentDetail.as_view(), name='UpdateStudentDetail'),
    
    path('CreateUser', CreateUser.as_view(), name='CreateUser'),

    path('GetSchoolList/<str:pk>', SchoolList.as_view(), name='SchoolList'),
    path('GetStudentList/<str:pk>', StudentList.as_view(), name='StudentList'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# email verification djoser jwt token left