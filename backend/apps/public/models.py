
from django.db import models


class User(models.Model):
	name = models.CharField(max_Length=25)
	street = models.CharField(max_Length=50)
	city = models.CharField(max_Length=50)
	state = models.CharField(max_Length=50)
	group = models.ManyToManyField(group)

	def __str__(self):
		return self.name

class Event(models.Model):
	notes = models.TextField(blank=True, null=True, help_text="This is a quick description of your dinner")
	street = models.CharField(max_Length=50)
	city = models.CharField(max_Length=25)
	state = models.CharField(max_Length=20)
	time = models.CharField(max_Length=10)
	date = models.CharField(max_Length=10)


	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_Length=25)
	user = models.ManyToManyField(user)
