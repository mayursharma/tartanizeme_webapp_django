from django.db import models
from django.contrib.auth.models import User


class Labels(models.Model):
    label = models.CharField(max_length=20)

    def __unicode__(self):
        return self.label


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    location = models.CharField(max_length=160)
    endTime = models.CharField(max_length=160)
    startTime = models.CharField(max_length=160)
    label = models.ManyToManyField(Labels)
    first_photo = models.ImageField(upload_to="pm-photos", blank=True)
    like = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name


class Photos(models.Model):
    event = models.ForeignKey(Event)
    photo = models.ImageField(upload_to="pm-photos", blank=True)

    def __unicode__(self):
        return self.event.name + " photos"


# class Comments(models.Model):
#     event = models.ForeignKey(Event)
#     user = models.ForeignKey(User)
#     comment = models.CharField(max_length=160)
#     def __unicode__(self):
#         return self.event.name+self.comment


class UserLabels (models.Model):
    user = models.ForeignKey(User)
    label = models.ManyToManyField(Labels)

    def __unicode__(self):
        return self.user.first_name + self.label
