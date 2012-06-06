from django.conf.urls.defaults import *

urlpatterns = patterns('rbac_app.views',
#    url(
#        regex=r'^$',
#        view='my_view',
#        name='my_view',
#    ),
    url(r'^$','my_view'),

)
