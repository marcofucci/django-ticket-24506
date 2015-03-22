from django.db import models


class FKUserModel(models.Model):
    user = models.ForeignKey('core.User')

    def __unicode__(self):
        return u'%s' % self.user


class OneToOneUserModel(models.Model):
    user = models.OneToOneField('core.User')

    def __unicode__(self):
        return u'%s' % self.user
