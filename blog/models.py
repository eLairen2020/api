from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
# Create your models here.

class Blog(models.Model):
    title                   = models.CharField(max_length=100)
    hashtagg                = TaggableManager()
    author                  = models.CharField(max_length=100)
    author_picture          = models.FileField(upload_to='author_pic/', null=True)
    about_designation       = models.CharField(max_length=100)
    about_author            = models.TextField()
    blog_image              = models.FileField(upload_to='blog_pic/', null=True)
    article                 = models.TextField()
    date_of_publish         = models.DateTimeField(auto_now_add=True)
    updated                 = models.DateTimeField(auto_now=True)
    updated_by              = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Blog"
    def __str__(self):
        return str(self.title)

class BlogComment(models.Model):
    sno                     = models.AutoField(primary_key = True)
    comment                 = models.TextField()
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    blog                    = models.ForeignKey(Blog, on_delete = models.CASCADE)
    parent                  = models.ForeignKey('self', on_delete = models.CASCADE, null =True, blank=True)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)
        # return 'Comment {} by {}'.format(self.comment, self.user)



