from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.gis.db import models as geomodels


class User(models.Model):

    name = models.CharField(max_length=100)
    when = models.DateTimeField(auto_now_add=True)
    # coords = geomodels.PointField()


def user_directory_path(instance, filename):
    uid = uuid.uuid4()
    return 'user_{0}/{1}'.format(instance.owner.id, str(uid), filename)


class ImageStory(models.Model):

    owner = models.ForeignKey(User, related_name='stories')
    document = models.FileField(upload_to='documents/')
    when = models.DateTimeField(auto_now_add=True)
    # coords = geomodels.PointField()
