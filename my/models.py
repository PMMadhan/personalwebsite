from django.db import models

# Create your models here.
class student(models.Model):
	f_name = models.CharField(max_length=30)
	l_name = models.CharField(max_length=30)

	def __str__(self):
		return self.f_name

class contact(models.Model):
	email = models.EmailField()
	subject = models.CharField(max_length=196)
	message = models.TextField()

	def __str__(self):
		return self.email