from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user.models import School



        
class Standard(models.Model):
    name                    = models.CharField(max_length=60)
    updated_by              = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Standard"
    def __str__(self):
        return self.name

class Subject(models.Model):
    name                    = models.CharField(max_length=60)
    updated_by              = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subject"
    def __str__(self):
        return self.name

class LiveClass(models.Model):
    created_by              = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    Standard                = models.ForeignKey(Standard,blank=True, null=True, on_delete=models.CASCADE)
    Subject                 = models.ForeignKey(Subject,blank=True, null=True, on_delete=models.CASCADE)
    School                  = models.ForeignKey(School,blank=True, null=True, on_delete=models.CASCADE)
    
    # Student attendance record left
    # how to record ttendance 
    
    class Meta:
        verbose_name_plural = "LiveClass"
    def __str__(self):
        return str(self.created_by)


class StudentAttendance(models.Model):
    liveclass                  = models.OneToOneField(LiveClass, blank=True, null=True, on_delete=models.CASCADE)
    teacher                    = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    student_name               = models.ManyToManyField(User, related_name='classtakingteacher', blank=True)
    
    class Meta:
        verbose_name_plural = "StudentAttendance"
    def __str__(self):
        return str(self.liveclass)

class Notice(models.Model):
    notice                    = models.TextField()
    teacher_school_subject  = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Notice"
    def __str__(self):
        return self.teacher_school_subject