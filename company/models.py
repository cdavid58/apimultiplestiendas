from django.db import models

class Company(models.Model):
	documentI = models.CharField(max_length = 25, unique = True)
	name = models.CharField(max_length = 70)
	phone = models.CharField(max_length = 15)
	email = models.EmailField(unique = True)
	block = models.BooleanField(default = False)
	category = models.CharField(max_length = 70, null= True, blank=True)
	logo = models.ImageField(upload_to = "Logo_Company", null = True, blank = True)

	def __str__(self):
		return self.name

