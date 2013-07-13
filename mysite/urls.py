from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.polls.views import *
from tastypie.api import Api
from mysite.polls.api import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(EntryResource2())

urlpatterns = patterns('',
    url(r'^$', ViewHome.as_view()),
    url(r'^create/$', ViewForm.as_view()),
    url(r'^polls/$', ViewIndex.as_view()),
    url(r'^polls/(?P<pk>\d+)/$', ViewDetail.as_view()),
    url(r'^polls/(?P<pk>\d+)/results/$', ViewResults.as_view()),
    url(r'^polls/(?P<poll_id>\d+)/submit/$', 'polls.views.submit'),
    url(r'^create/submit/$', 'polls.views.create_poll'),
	url(r'^render/poll/(?P<pk>\d+)/$', 'polls.views.render_poll'),
    #api
    url(r'^api/', include(v1_api.urls)),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
