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

from .views import (CourseDetail, CategoriesDetail, TeacherProfileDetail, BlogDetails, SearchList, Tag, Comment, CourseList, CategoryList,
 TeacherProfileList, BlogList, CreateComment , CreateBlog, CommentUpdateDestroy )


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('course/', include('course.urls')),
    path('exam/', include('exam.urls')),
    # Get Specific -------------------------------------------------
    path('CourseDetail/<str:pk>', CourseDetail.as_view(), name='CourseDetail'),
    path('CategoriesDetail/<str:pk>', CategoriesDetail.as_view(), name='CategoriesDetail'),
    path('BlogDetails/<str:pk>', BlogDetails.as_view(), name='BlogDetails'),
    path('searchresult/', SearchList.as_view(), name='SearchList'),
    path('TeacherProfileDetail/<str:pk>', TeacherProfileDetail.as_view(), name='TeacherProfileDetail'),
    path('BlogComment/<str:id>', Comment.as_view(), name='Comment'),
    # Get List ------------------------------------
    path('Courses/', CourseList.as_view(), name='CourseList'),
    path('Categories/', CategoryList.as_view(), name='CategoryList'),
    path('Teachers/', TeacherProfileList.as_view(), name='TeacherProfileList'),
    path('Blogs/', BlogList.as_view(), name='BlogList'),
    path('Tag/', Tag.as_view(), name='Tags'),

    # Create -------------------------------------------
    path('CreateComment/', CreateComment.as_view(), name='TeacherProfileList'),
    path('CreateBlog/', CreateBlog.as_view(), name='CreateBlog'),
    # Coment Update/Destroy--------------------------
    path('Update blog/<str:id>', CommentUpdateDestroy.as_view(), name='CommentUpdateDestroy'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)