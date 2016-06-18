from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Event(models.Model):
	event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	event_date = models.DateField()
	event_start_time = models.TimeField()
	event_image = models.CharField(max_length=255)
	event_description = models.TextField()
	event_url = models.CharField(max_length=255, unique=True)
	pin_code = models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(9999)])

	def save():
		
