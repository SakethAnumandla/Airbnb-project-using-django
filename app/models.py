from django.db import models

# Create your models here.
class Registration(models.Model):
	name=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	mobile=models.IntegerField()
	message=models.TextField()
