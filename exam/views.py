from django.shortcuts import render
from django.db import models
from rest_framework import status, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

#------------------------------------------------------------

from django.contrib.auth.models import User

from .models import Type_of_exam, Examination, Mcqestion, Student_Answer_record

from .serializers import (Type_of_examSerializer, ExaminationSerializer, McqestionSerializer, Student_Answer_recordSerializer )

#---------------List All-----------------------------

class Type_of_examAllList(generics.ListAPIView):
    serializer_class = Type_of_examSerializer
    queryset = Type_of_exam.objects.all()

class ExaminationAllList(generics.ListAPIView):
    serializer_class = ExaminationSerializer
    queryset = Examination.objects.all()

class McqestionAllList(generics.ListAPIView):
    serializer_class = McqestionSerializer
    queryset = Mcqestion.objects.all()

class Student_Answer_recordAllList(generics.ListAPIView):
    serializer_class = Student_Answer_recordSerializer
    queryset = Student_Answer_record.objects.all()

# showing for specific id  -----------------------------------------

class Type_of_examList(generics.ListAPIView):
    serializer_class = Type_of_examSerializer
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  Type_of_exam.objects.filter(school=pk)
        return queryset

class Examinationlist(generics.ListAPIView):
    serializer_class = ExaminationSerializer
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  Examination.objects.filter(school=pk)
        return queryset

class Mcqestionlist(generics.ListAPIView):
    serializer_class = McqestionSerializer
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  Mcqestion.objects.filter(name_of_examination=pk)
        return queryset

class Student_Answer_recordlist(generics.ListAPIView):
    serializer_class = Student_Answer_recordSerializer
    def get_queryset(self) :
        pk = self.kwargs.get("id")
        queryset =  Student_Answer_record.objects.filter(course_name=pk)
        return queryset


# Create API------------------------------------------
class CreateType_of_exam(generics.CreateAPIView):
    serializer_class = Type_of_examSerializer


class CreateExamination(generics.CreateAPIView):
    serializer_class = ExaminationSerializer


class CreateMcqestion(generics.CreateAPIView):
    serializer_class = McqestionSerializer
  

class CreateStudent_Answer_record(generics.CreateAPIView):
    serializer_class = Student_Answer_recordSerializer
    

# Update -----------------------------------

class UpdateType_of_exam(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Type_of_examSerializer
    lookup_field = 'pk'
    queryset = Type_of_exam.objects.all()

class UpdateExamination(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExaminationSerializer
    lookup_field = 'pk'
    queryset = Examination.objects.all()

class UpdateMcqestion(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = McqestionSerializer
    lookup_field = 'pk'
    queryset = Mcqestion.objects.all()

class UpdateStudent_Answer_record(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Student_Answer_recordSerializer
    lookup_field = 'pk'
    queryset = Student_Answer_record.objects.all()


    # def get_queryset(self) :
    #     pk = self.kwargs.get("id")
    #     print(pk)
    #     # isinstance = get_object_or_404(Courses,pk=id)
    #     queryset = Chapter.objects.filter(course_name=pk).order_by('chapter_no')
    #     return queryset
