from __future__ import unicode_literals
import uuid 
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint
from django.contrib.auth.models import User

class Event(models.Model):
	event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	event_date = models.DateField()
	event_start_time = models.TimeField()
	event_image = models.CharField(max_length=255, blank=True)
	event_description = models.TextField()
	event_url = models.CharField(max_length=255, unique=True)
	pin_code = models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(9999)], unique=True)
	created_by = models.OneToOneField(User)

	def save(self):
		#super(Event, self).save()
		date = datetime.datetime.today
		self.event_url = '%i/%i/%i/%i' % (date.year, date.month, date.day, self.event_id)
		pin_code = randint(1000,9999)

		super(Event, self).save()


class Announcements(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	profile_picture = models.CharField(max_length=255, blank=True)
	is_hackchat_admin = models.CharField(max_length=1, choices=(("Y","Yes"),("N","No"),), default="N")


