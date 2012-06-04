__author__ = 'ryan'

from django.conf.urls import patterns, include, url
from learn_app.models import Article,User,Comment
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(User)

urlpatterns = patterns('learn_app.views',
    url(r'^$','index'),
)

