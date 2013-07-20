from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
#from django.contrib.auth.models import User
from tastypie import fields
from mysite.polls.models import Poll, Choice, Vote


#class UserResource(ModelResource):
#    class Meta:
#        queryset = User.objects.all()
#        resource_name = 'user'
        
class EntryResource(ModelResource):
#    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'
        excludes = ['pub_date']
        allowed_methods = ['get']


class EntryResource2(ModelResource):
    poll = fields.ForeignKey(EntryResource, 'poll')
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        allowed_methods = ['get', 'post']
        authorization = Authorization()

class EntryResource3(ModelResource):
    choice = fields.ForeignKey(EntryResource2, 'choice')
    class Meta:
        queryset = Vote.objects.all()
        resource_name = 'vote'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
		