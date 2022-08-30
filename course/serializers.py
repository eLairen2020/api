from pickle import TRUE
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.response import Response
from course.models import Courses, Categories, Chapter, Topics, FAQ, QuestionBank,Ebooks, Enotes, Course_enroll_details, Reviews
from rest_framework import status, generics, permissions

#==============================================================================================================
#for course models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class TopicsSerializer(serializers.ModelSerializer):
    chapter1 = serializers.CharField(source='chapter.id', read_only=TRUE)
    class Meta:
        model = Topics
        depth = 1
        fields = '__all__'
        extra_field = ['chapter1']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = '__all__'

class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields = '__all__'

class EnotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enotes
        fields = '__all__'

class Course_enroll_detailsSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(source='User.id', read_only=TRUE)
    class Meta:
        model = Course_enroll_details
        depth = 1
        fields = '__all__'
        extra_field = ['uid']
        
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        depth = 1
        fields = '__all__'





