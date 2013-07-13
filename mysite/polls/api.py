from tastypie.resources import ModelResource
#from django.contrib.auth.models import User
#from tastypie import fields
from mysite.polls.models import Poll, Choice


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
#    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        allowed_methods = ['get']
#        fields = ['votes']

