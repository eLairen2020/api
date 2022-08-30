from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Standard, Subject, LiveClass,StudentAttendance, Notice

from django.contrib.sessions.models import Session


admin.site.site_header = "eMahei Admin"
admin.site.site_title = "eMahei Admin Dashboard"
admin.site.index_title = "eMahei Admin Dashboard"



admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(LiveClass)
admin.site.register(StudentAttendance)
admin.site.register(Notice)

