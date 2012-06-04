from django.db import models

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

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    create_at = models.DateField()
    star_count = models.IntegerField()
    reviewer = models.OneToOneField(User,null=True,blank=True)

    def __unicode__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=200)
    create_at = models.DateField(auto_now=True)
    introduction = models.CharField(max_length=200)
    body = models.TextField()
    comments = models.ManyToManyField(Comment,null=True,blank=True)

    def __unicode__(self):
        return self.title