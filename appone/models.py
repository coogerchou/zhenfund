from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email
		#or return str(self.timestamp) to get the time stamp when the user signed up


#----------------my try-------------------

class Transfer(models.Model):
	email = models.EmailField(blank=False)
	original_txt = models.TextField(max_length=100000,blank=False,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return str(self.timestamp)