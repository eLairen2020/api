from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Categories, Courses, Chapter, Topics, FAQ, QuestionBank, Ebooks, Enotes, Course_enroll_details, Reviews
from django.contrib.sessions.models import Session



admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Chapter)
admin.site.register(Topics)
admin.site.register(FAQ)
admin.site.register(QuestionBank)
admin.site.register(Ebooks)
admin.site.register(Enotes)
admin.site.register(Course_enroll_details)


admin.site.register(Reviews)
