from django.db import models
from datetime import datetime
from houses.models import House


class GarbageDay(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	house = models.ForeignKey(House, on_delete=models.CASCADE)

	last_garbage_day = models.DateField()
	next_garbage_day = models.DateField()
	garbage_frequency = models.DurationField(null=True)

	def calculate_garbage_frequency(self):
		delta = datetime.strptime(self.next_garbage_day, '%Y-%m-%d') - datetime.strptime(self.last_garbage_day, '%Y-%m-%d')
		self.garbage_frequency = delta

	def save(self, **kwargs):
		self.calculate_garbage_frequency()
		super(GarbageDay, self).save()

