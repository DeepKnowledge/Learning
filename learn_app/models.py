from django.db import models
from django.contrib.auth.models import User

'''
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)

    GENDER_CHOICES = (
        (u'M',u'Male'),
        (u'F',u'Female'),
        )
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.nick_name
'''
class Article(models.Model):
    title = models.CharField(max_length=200)
    create_at = models.DateField(auto_now=True)
    introduction = models.CharField(max_length=200)
    body = models.TextField()
#    comments = models.ManyToManyField(Comment,null=True,blank=True)
    author = models.ManyToManyField(User,null=False,blank=False)
    audio = models.FileField(upload_to='audio/%Y/%m/%d',blank=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    create_at = models.DateField()
    star_count = models.IntegerField()
    reviewer = models.ManyToManyField(User,null=True,blank=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.content
