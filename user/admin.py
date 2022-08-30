from django.contrib import admin
from .models import Teacher_Profile, Student_Profile, School


admin.site.register(Teacher_Profile)
admin.site.register(Student_Profile)
admin.site.register(School)