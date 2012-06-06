from django.conf.urls import patterns, include, url
#import spreadsheet.spreadsheet_app.views as views
from app_core import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^django1/', include('django1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#    url(r'^spreadsheet_app/','views.index',name='index'),
    url(r'^learn/',include('learn_app.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^rbac/$',include('rbac_app.urls')),
)

#
# Serve media with Django in DEBUG mode
#
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^resources/(?P<path>.*)$',
            'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,}),
    )