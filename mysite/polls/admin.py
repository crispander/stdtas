from django.contrib import admin
from mysite.polls.models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
    
class PollAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)


admin.site.register(Choice)
admin.site.register(UserProfile)
admin.site.register(Contact)

