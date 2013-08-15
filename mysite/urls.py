from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.polls.views import *
from tastypie.api import Api
from mysite.polls.api import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(EntryResource2())
v1_api.register(EntryResource3())

urlpatterns = patterns('',
    url(r'^$', ViewHome.as_view()),
    url(r'^senderlogin/$', ViewLogin.as_view()),
    url(r'^accounts/profile/$', ViewOneall.as_view()),
    url(r'^create/$', ViewForm.as_view()),
    url(r'^polls/$', ViewIndex.as_view()),
    url(r'^polls/(?P<pk>\d+)/$', ViewDetail.as_view()),
    url(r'^polls/(?P<pk>\d+)/results/$', ViewResults.as_view()),
    url(r'^polls/(?P<poll_id>\d+)/submit/$', submit),
    url(r'^create/submit/$', create_poll),
	url(r'^render/poll/(?P<pk>\d+)/$', render_poll),
	url(r'^contact/$', ViewContact.as_view()),
	url(r'^contact/submit$', submit_Contact),
	url(r'^sobreapp/$', ViewSobreApp.as_view()),
    #api
    url(r'^api/', include(v1_api.urls)),
	#oneall
    url(r'^oneall/', include('django_oneall.urls')),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
