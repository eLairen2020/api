from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Student_Profile(models.Model):
    username                = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=100, blank=True, null=True,)
    last_name               = models.CharField(max_length=100, blank=True, null=True,)
    phone                   = models.CharField(max_length=13, blank=True, null=True,)
    Standard                = models.CharField(max_length=50, blank=True, null=True,)
    school                  = models.CharField(max_length=100, blank=True, null=True,)
    address                 = models.CharField(max_length=200, blank=True, null=True,)
    roll                    = models.IntegerField( blank=True, null=True,)
    image                   = models.ImageField(upload_to='user_pic', blank=True, null=True,)
    

    class Meta:
        verbose_name_plural = "Student_Profile"
    def __str__(self):
        return str(self.username)

class Teacher_Profile(models.Model):

    username                = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=100, blank=True, null=True,)
    last_name               = models.CharField(max_length=100, blank=True, null=True,)
    phone                   = models.CharField(max_length=13, blank=True, null=True,)
    subject                 = models.CharField(max_length=100, blank=True, null=True,)
    address                 = models.CharField(max_length=200, blank=True, null=True,)
    image                   = models.ImageField(upload_to='user_pic', blank=True, null=True,)
    

    class Meta:
        verbose_name_plural = "Teacher_Profile"
    def __str__(self):
        return str(self.username)

class School(models.Model):
    schoolname              = models.CharField(max_length=100, blank=True, null=True,)
    schoolusername          = models.OneToOneField(User, on_delete=models.CASCADE)
    phone                   = models.CharField(max_length=13, blank=True, null=True,)
    address                 = models.CharField(max_length=200, blank=True, null=True,)
   
    class Meta:
        verbose_name_plural = "School"
    def __str__(self):
        return str(self.schoolname)

