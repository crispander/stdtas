# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'polls_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('width_subblock', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('height_subblock', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('width_blocktitle', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('height_blocktitle', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('border_visible', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('border_width', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('border_color', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('background', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('border_radius', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sub_background', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('color_title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('size_title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('size_block', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('font_family', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('font_color', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('number_votes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('show_results', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('padding', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('padding_std_options', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('gradient1', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('gradient2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('etiquetas', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'polls', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'polls_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'polls', ['Choice'])

        # Adding model 'Vote'
        db.create_table(u'polls_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Choice'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('number_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'polls', ['Vote'])

        # Adding model 'Contact'
        db.create_table(u'polls_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'polls', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'polls_poll')

        # Deleting model 'Choice'
        db.delete_table(u'polls_choice')

        # Deleting model 'Vote'
        db.delete_table(u'polls_vote')

        # Deleting model 'Contact'
        db.delete_table(u'polls_contact')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polls.choice': {
            'Meta': {'ordering': "['-votes']", 'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'polls.contact': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Contact'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'polls.poll': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Poll'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'border_color': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'border_radius': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'border_visible': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'border_width': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'color_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'etiquetas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'font_color': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'font_family': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gradient1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gradient2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height_blocktitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height_subblock': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_votes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'padding': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'padding_std_options': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'show_results': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size_block': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sub_background': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'width_blocktitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'width_subblock': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'polls.vote': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Vote'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Choice']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'number_votes': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['polls']