from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User
from emahei.models import Subject, Standard
from user.models import School
from course.models import Courses

# Create your models here.
# to select the types of exam like semester, unit test, final etc
class Type_of_exam(models.Model):
    type_of_examination     = models.CharField(max_length=100, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "Type_of_exam"
    def __str__(self):
        return str(self.type_of_examination)

#to insert the detials of examination to be conducted
class Examination(models.Model):
    
    name_of_examination     = models.CharField(max_length=100, blank=True, null=True,)
    type_of_examination     = models.ForeignKey(Type_of_exam, blank=True, null=True, on_delete=models.CASCADE)
    subject                 = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Teacher                 = models.ForeignKey(User, on_delete=models.CASCADE)
    school                  = models.ForeignKey(School, on_delete=models.CASCADE)
    Standard                = models.ForeignKey(Standard, on_delete=models.CASCADE)
    date                    = models.DateField(auto_now=True)
    duration                = models.CharField(max_length=50, blank=True, null=True,)
    passmark                = models.IntegerField()
    fullmark                = models.IntegerField()
    Rules                   = models.TextField()
    
    class Meta:
        verbose_name_plural = "Examination"
    def __str__(self):
        return str(self.name_of_examination)

# to insert the questions of the examination
class Mcqestion(models.Model):
    name_of_examination        = models.ForeignKey(Examination, on_delete=models.CASCADE)
    Question_no                = models.IntegerField()
    Question                   = models.CharField(max_length=500, blank=True, null=True,)
    Option_A                   = models.CharField(max_length=500, blank=True, null=True,)
    Option_B                   = models.CharField(max_length=500, blank=True, null=True,)
    Option_C                   = models.CharField(max_length=500, blank=True, null=True,)
    Option_D                   = models.CharField(max_length=500, blank=True, null=True,)

    RATING_CHOICES = ( 
    ("A", "A"), 
    ("B", "B"), 
    ("C", "C"), 
    ("D", "D"), 
    ) 

    Answer                     = models.CharField(max_length = 20, choices = RATING_CHOICES )
    
    class Meta:
        verbose_name_plural = "Mcqestion"
    def __str__(self):
        return str(self.name_of_examination)


# to records the student answer to the database if we want to check thoroughly
class Student_Answer_record(models.Model):
    name_of_examination         = models.ForeignKey(Examination, on_delete=models.CASCADE)
    name_of_student             = models.ForeignKey(User, on_delete=models.CASCADE)
    Question_no                 = models.ForeignKey(Mcqestion, on_delete=models.CASCADE)
    Student_answer              = models.CharField(max_length=500, blank=True, null=True,)

    
    class Meta:
        verbose_name_plural = "Student_Answer_record"
    def __str__(self):
        return str(self.name_of_examination)



#to record and views the student result of a test. (report card)-------------------------------------------------------------


# like post or blog records--------------------------------------------------------------

class Like(models.Model):
    name_of_course              = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name_of_User                = models.ForeignKey(User, on_delete=models.CASCADE)
    likes                       = models.BooleanField()

    
    class Meta:
        verbose_name_plural = "Like"
    def __str__(self):
        return str(self.name_of_course)
