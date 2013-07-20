from django.db import models
import datetime
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
        
    class Meta:
        verbose_name_plural = "user profile"

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, null=True, blank=True)
    width = models.CharField(max_length=200, null=True, blank=True)
    height = models.CharField(max_length=200, null=True, blank=True)
    width_subblock = models.CharField(max_length=200, null=True, blank=True)
    height_subblock = models.CharField(max_length=200, null=True, blank=True)
    width_blocktitle = models.CharField(max_length=200, null=True, blank=True)
    height_blocktitle = models.CharField(max_length=200, null=True, blank=True)
    border_visible = models.CharField(max_length=200, null=True, blank=True)
    border_width = models.CharField(max_length=200, null=True, blank=True)
    border_color = models.CharField(max_length=200, null=True, blank=True)
    background = models.CharField(max_length=200, null=True, blank=True)
    border_radius = models.CharField(max_length=200, null=True, blank=True)
    sub_background = models.CharField(max_length=200, null=True, blank=True)
    color_title = models.CharField(max_length=200, null=True, blank=True)
    size_title = models.CharField(max_length=200, null=True, blank=True)
    size_block = models.CharField(max_length=200, null=True, blank=True)
    font_family = models.CharField(max_length=200, null=True, blank=True)
    font_color = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    number_votes = models.CharField(max_length=200, null=True, blank=True)
    show_results = models.CharField(max_length=200, null=True, blank=True)
    padding = models.CharField(max_length=200, null=True, blank=True)
    padding_std_options = models.CharField(max_length=200, null=True, blank=True)
    gradient1 = models.CharField(max_length=200, null=True, blank=True)
    gradient2 = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.question
    
    class Meta:
        ordering = ["-pub_date"]
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def votes_ultimate(self):
        votes = 0
        choices = self.choice_set.all()
        for choice in choices:
            votes += choice.count_votes()
            
        return votes

    def get_choices(self):
        obj = Choice.objects.filter(poll=self)
        
        return obj

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    name = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["-votes"]
        
    def count_votes(self):
        """esta funcion es para obtener los resultadps de la elecion actual."""
        
        try:
            number = Vote.objects.filter(choice=self)[0].number_votes
        except IndexError:
           number = 0
        
        return number

class Vote(models.Model):
    choice = models.ForeignKey(Choice)
    ip = models.CharField(max_length=20, blank=True, null=True)
    number_votes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.choice.name
    
    class Meta:
        ordering = ["-date"]
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["-date"]


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    

