from django.db import models
from inventory.models import Product
from user.models import User

class Consecutive(models.Model):
	code = models.IntegerField()

class Order(models.Model):
	code = models.ForeignKey(Consecutive, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	price = models.FloatField()
	quanty = models.FloatField()
	shipping = models.FloatField()
	date_generated = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	





