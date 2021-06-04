from django.db import models

# Create your models here.
class Hire_me(models.Model):
	h_id = models.AutoField(primary_key=True)
	h_name = models.CharField(max_length=50, default="")
	h_email = models.CharField(max_length=50, default="")
	h_msg = models.CharField(max_length=255, default="")

	def __str__(self):
		return self.h_name