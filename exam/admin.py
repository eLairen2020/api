from django.contrib import admin

from .models import Examination, Mcqestion, Type_of_exam, Student_Answer_record
from django.contrib.sessions.models import Session

# Register your models here.


admin.site.register(Examination)
admin.site.register(Mcqestion)
admin.site.register(Type_of_exam)
admin.site.register(Student_Answer_record)
