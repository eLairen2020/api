from pickle import TRUE
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.response import Response
from exam.models import Type_of_exam, Examination, Mcqestion, Student_Answer_record
from rest_framework import status, generics, permissions

#==============================================================================================================
#for course models

class Type_of_examSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_exam
        fields = '__all__'

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        depth = 1
        fields = '__all__'

class McqestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcqestion
        depth = 1
        fields = '__all__'

class Student_Answer_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Answer_record
        depth = 1
        fields = '__all__'





